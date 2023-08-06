import ast
import json
import logging
from typing import AsyncGenerator, List, Literal, Optional, Tuple

import httpx
import pandas as pd

from async_data_api import (
    Aggregation,
    Backends,
    ChannelName,
    ConfigFields,
    EventFields,
    RangeByDate,
    RangeByPulseId,
    RangeByTime,
    ResponseFormat,
    ValueMapping,
    ValueTransformations,
)


class DataApi:
    """Asynchronous Client for the PSI Rest DataAPI.

    A class object, that represents a client connection to the Restfull api.

    Parameters:
        client (Optional[httpx.AsyncClient]): The client to be used to make the requests. If using the class in a compound statement (async with) this gets set on initialize.
                                              Otherwise you can either provide a client or a client gets created and destroyed for each call (not recommended, expensive!).
                                              Default: None.
        base_url (str): The base of the url the calls get send to. To this the endpoints, e.g.: /proscan/channels will be attached. Default: "https://data-api.psi.ch"
        check_backends (bool): Whether or not to check backends when initializing with compound.
    Usage:
        ```python
        >>> async with DataApi(base_url="https://data-api.psi.ch/") as api:
        >>> async for result in api.get_data(
                                    channels=ChannelName(name="MMAC3:STR:2", backend=Backends.proscan),
                                    range=RangeByDate(
                                        start_date=datetime.now() - timedelta(days=3),
                                        endDate=datetime.now(),
                                        start_expansion=False,
                                    ),
                                    event_fields=[EventFields.global_millis, EventFields.raw_value],
                                    aggregation=Aggregation(
                                        aggregations=[
                                            Aggregation.Aggregations.min,
                                            Aggregation.Aggregations.mean,
                                            Aggregation.Aggregations.max,
                                        ],
                                        nr_of_bins=500,
                                    ),
        ):
        >>>    df = api.json_to_dataframe(result)
        >>>    print(df)
        ```
    """

    def __init__(
        self,
        client: Optional[httpx.AsyncClient] = None,
        base_url: str = "https://data-api.psi.ch",
        precheck_backends: bool = True,
    ) -> None:
        self.base_url = base_url
        self._logger = logging.getLogger(self.__class__.__module__)
        self._logger.debug("Initialized SFApi")
        self.client = client
        self.backends = []
        self.precheck_backends = precheck_backends
        if self.client and self.base_url:
            self.client.base_url = self.base_url

    async def __aenter__(self):
        """Async enter method for compound statement.

        Also initiates the self.backends property by running check_backends. Only adds backends that answered with OK.

        Returns:
            DataApi: Returns the class object.
        """
        if not self.client:
            self.client = httpx.AsyncClient(base_url=self.base_url)
        if self.precheck_backends:
            self.backends = await self.check_backends()
        return self

    async def __aexit__(self, *kwargs) -> None:
        """Async exit method for compound statement.

        Makes sure the client gets closed after the compound statement.

        Returns:
            None: Nothing
        """
        _ = await self.close()
        return None

    async def close(self) -> None:
        """Close the client.

        Closes the client and adds an entry into the log.

        Returns:
            None: Nothing
        """
        if self.client:
            if not self.client.is_closed:
                self._logger.debug("Closed httpx client.")
                await self.client.aclose()

    def _create_local_client(
        self, client: Optional[httpx.AsyncClient], follow_redirects: bool = False
    ) -> Tuple[bool, httpx.AsyncClient]:
        """Checks whether client exists, creates one if not.

        Checks passed in client and self.client, if neither exists creates a new client.

        Args:
            client (Optional[httpx.AsyncClient]): Client can be passed in if one already exists.
            follow_redirects (bool, optional): Whether or not to follow redirects, gets passed to client if a new one is created. Defaults to False.

        Returns:
            Tuple[bool, httpx.AsyncClient]: a boolean to signalize if a new client was created, the clients object.
        """
        _local_client = False
        if self.client:
            _client = self.client
        elif client:
            _client = client
        else:
            self._logger.info(
                "No client was passed. Creating client for call. This has a performance penalty and should be avoided."
            )
            _client = httpx.AsyncClient(
                base_url=self.base_url, follow_redirects=follow_redirects
            )
            _local_client = True
            _client.follow_redirects = True
        return (_local_client, _client)

    async def get_backends(
        self, backend: Backends, client: Optional[httpx.AsyncClient] = None
    ) -> Optional[List[str]]:
        _local_client, _client = self._create_local_client(client=client)
        try:
            resp = await _client.get(url=f"/{backend.value.path}/params/backends/")
            if resp.is_success:
                self._logger.debug(
                    f"Got response from {self.base_url}/{backend.value.path}/params/backends/: {resp.content.decode('utf-8')}"
                )
                return ast.literal_eval(resp.content.decode("utf-8"))
            else:
                resp.raise_for_status()
        except httpx.HTTPStatusError as http_error:
            http_error.add_note(http_error.response.content.decode("utf-8"))
            self._logger.error(str(http_error))
            raise http_error
        finally:
            if _local_client:
                self._logger.info("Closed local client!")
                await _client.aclose()

    async def check_backends(
        self,
        client: Optional[httpx.AsyncClient] = None,
        backends: Optional[List[Backends]] = None,
    ):
        _local_client, _client = self._create_local_client(client=client)
        try:
            if not backends:
                backends = [backend for backend in Backends]
            results: List = []
            for backend in backends:
                backend_list = await self.get_backends(backend=backend, client=_client)
                if backend_list:
                    results = results + [backend]
            self.backends = results
            return results
        except httpx.HTTPStatusError as http_error:
            http_error.add_note(http_error.response.content.decode("utf-8"))
            self._logger.error(str(http_error))
            pass
        finally:
            if _local_client:
                self._logger.info("Closed local client!")
                await _client.aclose()

    async def find_channels(
        self,
        regex: str,
        return_config: bool = False,
        backends: Optional[List[Backends]] | Optional[Backends] = None,
        ordering: Optional[Literal["asc", "desc"]] = None,
        source_regex: Optional[str] = None,
        client: Optional[httpx.AsyncClient] = None,
    ) -> Optional[List[str]]:
        """Find all channels that match the regex.

        Searches all or the provided backends to find a channel matching the regex.

        Args:
            regex (str): Reqular expression used to filter channel names. In case this value is undefined, no filter will be applied.
                         Filtering is done using JAVA's Pattern, more precisely Matcher.find()).
            return_config (bool, optional): Whether or not to return the config of the found channel(s). Defaults to False.
            backends (Optional[List[Backends]] | Optional[Backends], optional): Backend(s) to search. Defaults to None.
            ordering (Optional[Literal["asc", "desc"]], optional): The ordering of the channel names , if none channels are returned as found. Defaults to None.
            source_regex (Optional[str], optional): . Defaults to None.
            client (Optional[httpx.AsyncClient], optional): Reqular expression used to filter source names (like e.g. tcp://SINEG01-CVME-LLRF1:20000).
                                                            In case this value is undefined, no filter will be applied.
                                                            Filtering is done using JAVA's Pattern, more precisely Matcher.find()).. Defaults to None.

        Returns:
            Optional[List[str]]: _description_
        """
        _local_client, _client = self._create_local_client(client=client)
        result = []
        try:
            payload = {"regex": regex}

            if backends:
                if not isinstance(backends, List):
                    _backends = [backends]
                else:
                    _backends = backends
            # if no backends are specified use either the backends found with check backends or try and search all known backends.
            else:
                if self.backends:
                    _backends = self.backends
                else:
                    _backends = [backend for backend in Backends]

            if ordering:
                payload["ordering"] = ordering

            if source_regex:
                payload["source_regex"] = source_regex

            for backend in _backends:
                payload["backends"] = [backend.value.name]
                if return_config:
                    response = await _client.post(
                        url=f"/{backend.value.path}/channels/config/",
                        headers={"Content-Type": "application/json"},
                        json=payload,
                    )

                else:
                    response = await _client.post(
                        url=f"/{backend.value.path}/channels/",
                        headers={"Content-Type": "application/json"},
                        json=payload,
                    )
                if response.is_success:
                    self._logger.debug(
                        f"successfully returned channels for regex {regex}!"
                    )
                    # return ast.literal_eval(response.content.decode(encoding="utf-8"))
                    json_content = json.loads(response.content)
                    if json_content and json_content[0]["channels"]:
                        result = result + json_content
                else:
                    response.raise_for_status()

            return result
        except httpx.HTTPStatusError as http_error:
            http_error.add_note(http_error.response.content.decode("utf-8"))
            self._logger.error(str(http_error))
            pass
        finally:
            if _local_client:
                self._logger.info("Closed local client!")
                await _client.aclose()

    def _build_query(
        self,
        channels: ChannelName | List[ChannelName],
        range: RangeByDate | RangeByPulseId | RangeByTime,
        limit: Optional[int] = None,
        ordering: Optional[Literal["asc", "desc"]] = None,
        config_fields: Optional[List[ConfigFields]] = None,
        event_fields: Optional[List[EventFields]] = None,
        aggregation: Optional[Aggregation] = None,
        response: Optional[ResponseFormat] = None,
        mapping: Optional[ValueMapping] = None,
        value_transformations: Optional[ValueTransformations] = None,
    ) -> dict:
        # We need to bin the querys by backend since the querying multiple channels from multiple backends in one query is funky at best
        querys = {}

        if not isinstance(channels, List):
            _channels = [channels]
        else:
            _channels = channels

        _backends = list(set([channel.backend.value for channel in _channels]))
        for backend in _backends:
            payload = {}
            payload["range"] = range.to_dict()
            if limit:
                if aggregation:
                    raise Exception(
                        "Limit and aggregation at the same time doesn't make sense and is not supported!"
                    )
                else:
                    payload["limit"] = limit
            if ordering:
                payload["ordering"] = ordering
            if config_fields:
                payload["configFields"] = [
                    config_field.value for config_field in config_fields
                ]
            if event_fields:
                payload["eventFields"] = [
                    event_field.value for event_field in event_fields
                ]
            if aggregation:
                payload["aggregation"] = aggregation.to_dict()
            if response:
                payload["response"] = response.to_dict()
            if mapping:
                payload["mapping"] = mapping.to_dict()
            if value_transformations:
                payload["value_transformations"] = value_transformations.to_dict()
            for channel in _channels:
                if channel.backend.value.name == backend.name:
                    if "channels" in payload:
                        payload["channels"].append(channel.to_dict())
                    else:
                        payload["channels"] = [channel.to_dict()]
            querys[backend.path] = payload
        return querys

    async def get_data(
        self,
        channels: ChannelName | List[ChannelName],
        range: RangeByDate | RangeByPulseId | RangeByTime,
        limit: Optional[int] = None,
        ordering: Optional[Literal["asc", "desc"]] = None,
        config_fields: Optional[List[ConfigFields]] = None,
        event_fields: Optional[List[EventFields]] = None,
        aggregation: Optional[Aggregation] = None,
        response: Optional[ResponseFormat] = None,
        mapping: Optional[ValueMapping] = None,
        value_transformations: Optional[ValueTransformations] = None,
        client: Optional[httpx.AsyncClient] = None,
    ) -> AsyncGenerator[None, dict]:
        """Get the data of one or a list of channels from the specified backend.

        To get a list of available channels and their corresponding backends run get_channels().

        Args:
            channels (ChannelName | List[ChannelName]): Array of channels to be queried.
            range (RangeByDate | RangeByPulseId | RangeByTime): The range of the query.
            limit (int | None): An optional limit for the number of elements to retrieve. Limit together with aggregation does not make sense and thus is not supported.
            ordering (Literal["asc","desc"] | None): The ordering of the data. Defaults to None.
            config_fields (Optional[List[ConfigFields]], optional): Array of requested config fields. Omitting this field disables the config query. Defaults to None.
            event_fields (Optional[List[EventFields]], optional): Array of requested event fields. Omitting this field results in a default set of event fields. Defaults to None.
            aggregation (Optional[Aggregation], optional): Setting this attribute activates data aggregation. Defaults to None.
            response (Optional[ResponeFormat], optional): Specifies the format of the response of the requested data. If this value is not set it defaults to JSON. Defaults to None.
            mapping (Optional[ValueMapping], optional): Activates a table like alignment of the response which allows a mapping of values belonging to the same pulse-id/global time. Defaults to None.
            value_transformations (Optional[ValueTransformations], optional): Provides the option to apply transformations to channel values. Defaults to None.
            client (Optional[httpx.AsyncClient], optional): Client to use, if none self.client or a newly created client will be used.
        """
        querys = self._build_query(
            channels=channels,
            range=range,
            limit=limit,
            ordering=ordering,
            config_fields=config_fields,
            event_fields=event_fields,
            aggregation=aggregation,
            response=response,
            mapping=mapping,
            value_transformations=value_transformations,
        )

        _follow_redirects = False
        if response:
            if response.allow_redirect:
                _follow_redirects = True

        _local_client, _client = self._create_local_client(
            client=client, follow_redirects=_follow_redirects
        )
        result = []
        try:
            for backend in querys.keys():
                result = await _client.post(
                    url=f"/{backend}/query/", json=querys[backend]
                )
                if result.is_success:
                    data = json.loads(result.content)
                    yield data
                else:
                    result.raise_for_status()

        except httpx.HTTPStatusError as http_error:
            http_error.add_note(http_error.response.content.decode("utf-8"))
            self._logger.error(str(http_error))
            raise http_error
        finally:
            if _local_client:
                self._logger.info("Closed local client!")
                await _client.aclose()

    def json_to_dataframe(self, data):
        """Converts the JSON result to a dataframe.

        Args:
            data (dict): The JSON style dict that will be converted to a dataframe. Must contain key data.

        Returns:
            DataFrame: A DataFrame build from the value of the data record path.
        """
        return pd.json_normalize(data, record_path="data")
