from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from typing import List, Literal, Optional, Union

from isodate import duration_isoformat


def _to_dict(obj: object) -> dict:
    """This function converts a class into a dict conforming to the requirements of the PSI data-api.

    Args:
        obj (object): The object that is to be converted

    Returns:
        dict: A dictionary containing keys and values conforming to PSI data-api requirements
    """
    result = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, List):
            if isinstance(value, Enum):
                result[_to_camel_case(key)] = [element.value for element in value]
            else:
                result[_to_camel_case(key)] = value
        elif isinstance(value, Enum):
            result[_to_camel_case(key)] = value.value
        elif isinstance(value, datetime):
            result[_to_camel_case(key)] = value.isoformat()
        else:
            result[_to_camel_case(key)] = str(value).lower()
    return result


def _to_camel_case(snake_str: str) -> str:
    """Converts a snake_case string to a camelCase one.

    Args:
        snake_str (str): A string in snake_case format.

    Returns:
        str: A string in camelCase format.
    """
    components = snake_str.split("_")
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + "".join(x.title() for x in components[1:])


@dataclass
class Backend:
    path: str
    name: str

    def __key(self):
        return (self.path, self.name)

    def __hash__(self) -> int:
        return hash(self.__key())

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Backend):
            return self.__key() == __o.__key()
        return NotImplemented


class Backends(Enum):
    cryo = Backend(path="cryo", name="cryo-archive")
    esi = Backend(path="esi", name="esi-archive")
    gls = Backend(path="gls", name="gls-archive")
    hipa = Backend(path="hipa", name="hipa-archive")
    proscan = Backend(path="proscan", name="proscan-archive")
    sf_archiverappliance = Backend(
        path="sf-archiverappliance", name="sf-archiverappliance"
    )
    sf_imagebuffer = Backend(path="sf-imagebuffer", name="sf-imagebuffer")
    sf_rf_databuffer = Backend(path="sf-rf-databuffer", name="sf-rf-databuffer")
    twlha_archive = Backend(path="twlha-archive", name="twlha-archive")
    twlha_databuffer = Backend(path="twlha-databuffer", name="twlha-databuffer")


@dataclass
class ChannelName:
    """Channel Name Object.

    Holds a channel name and a backend. Used when specifying a backend per channel.
    """

    name: str
    backend: Backends

    def to_dict(self):
        return {"name": self.name, "backend": self.backend.value.name}


class Aggregation:
    """It is possible (and recommended) to aggregate queried data.

    Parameters:
        aggregation_type (AggregationType): Specifies the type of aggregation. The default type is value aggregation. (see class AggregationType(Enum) for details and values)
        aggregations (List[Aggregations]): List of requested aggregations (see class Aggregations(Enum) for details and values).
                                           These values will be added to the data array response.
        extrema (Optional[List[Extrema]]): Array of requested extrema. These values will be added to the data array response.
        nr_of_bins (Optional[int]):  Activates data binning. Specifies the number of bins the pulse/time range should be divided into (e.g., "nrOfBins":2).
        duration_per_bin (Optional[str]): Activates data binning. Specifies the duration per bin for time-range queries (using duration makes this binning strategy consistent between channel with different update frequencies).
                                          The duration can be defined as a ISO-8601 duration string or a Datetime.timedelta. The resolution is in milliseconds and thus the minimal duration is 1 millisecond.
        pulses_per_bin (Optional[int]): Activates data binning.
                                        Specifies the number of pulses per bin for pulse-range queries.
                                        Using number of pulses makes this binning strategy consistent between channel with different update frequencies.
    """

    class AggregationType(Enum):
        """Specifies the type of aggregation.

        Values:
            by_value: The default type is value aggregation (e.g., sum([1,2,3])=6)
            by_index: Index aggregation for multiple arrays in combination with binning (e.g., sum([1,2,3], [3,2,1]) = [4,4,4]).
            by_extrema: Global min/max of any Aggregation over a series of events (e.g., extrema of Aggregations.sum) ([1,2,3], [3,2,3], [1,1,1]) = [3,2,3])

        """

        by_value = "value"
        by_index = "index"
        by_extrema = "extrema"

    class Aggregations(Enum):
        """Array of requested aggregations. These values will be added to the data array response.

        Values:
            mean: The arithmetic mean value of an array. (see https://en.wikipedia.org/wiki/Arithmetic_mean)
            min: The minimum</a> value of an array. (see https://en.wikipedia.org/wiki/Sample_maximum_and_minimum)
            max: The maximum value of an array. (see https://en.wikipedia.org/wiki/Sample_maximum_and_minimum)
            sum: The sum of all value of an array.(see https://de.wikipedia.org/wiki/Summe)
            count: The number of values in an array. (see https://en.wikipedia.org/wiki/Count_data)
            variance: The sample variance of the values in an array. (see https://en.wikipedia.org/wiki/Variance#Sample_variance)
            stddev: The sample standard deviation of the values in an array. (see https://en.wikipedia.org/wiki/Standard_deviation#Corrected_sample_standard_deviation)
            skewness: The skewness of the values in an array. (see https://en.wikipedia.org/wiki/Skewness)
            kurtosis: The kurtosis of the values in an array. (see https://en.wikipedia.org/wiki/Kurtosis)
            typed: Provides a typed version of the statistics which can be recreated without information loss. **This does not work for CSV (Object cannot be represented as a double - use String?).**

        """

        mean = "mean"
        min = "min"
        max = "max"
        sum = "sum"
        count = "count"
        variance = "variance"
        stddev = "stddev"
        skewness = "skewness"
        kurtosis = "kurtosis"
        typed = "typed"

    class Extrema(Enum):
        """Array of requested extrema. These values will be added to the data array response.

        Values:
            minValue: The global minimal value (e.g., of a bin).
            maxValue: The global mxaimal value (e.g., of a bin).

        Raises:
            Exception: Gets raised when more than one of the binning types is specified
        """

        minValue = "minValue"
        maxValue = "maxValue"

    def __init__(
        self,
        aggregations: List[Aggregations],
        aggregation_type: AggregationType = AggregationType.by_value,
        extrema: Optional[List[Extrema]] = None,
        nr_of_bins: Optional[int] = None,
        duration_per_bin: Optional[Union[str, timedelta]] = None,
        pulses_per_bin: Optional[int] = None,
    ) -> None:
        if (nr_of_bins is not None) + (duration_per_bin is not None) + (
            pulses_per_bin is not None
        ) > 1:
            raise Exception(
                "Can specify only one of nr_of_bins, duration_per_bin or pulse_per_bin"
            )
        self.aggregation_type = aggregation_type
        self.aggregations = aggregations
        self.extrema = extrema
        self.nr_of_bins = nr_of_bins
        self.pulses_per_bin = pulses_per_bin

        if isinstance(duration_per_bin, timedelta):
            self.duration_per_bin = duration_isoformat(duration_per_bin)
        else:
            self.duration_per_bin = duration_per_bin

    def to_dict(self) -> dict:
        """Converts the class to a dictionary with keys and values conforming to the expected form of the data-api of PSI.

        Returns:
            dict: Dictionary representing the information encoded in the class.
        """
        result = {}
        result["aggregationType"] = self.aggregation_type.value
        result["aggregations"] = [
            aggregation.value for aggregation in self.aggregations
        ]
        if self.extrema:
            result["extrema"] = [extrema.value for extrema in self.extrema]

        if self.nr_of_bins:
            result["nrOfBins"] = self.nr_of_bins
        elif self.duration_per_bin:
            result["durationPerBin"] = self.duration_per_bin
        elif self.pulses_per_bin:
            result["pulsesPerBin"] = self.pulses_per_bin

        return result


@dataclass
class ResponseFormat(object):
    """How the response should be formatted.

    Parameters:
        format (Format): The format of the response (values: json|csv). Please note that csv does not support index and extrema aggregations.
        compression (Literal["gzip"] | None): Responses can be compressed when transferred from the server (values: none|gzip).
        allowRedirect (bool): Defines it the central query rest server is allowed to redirect queries to the query rest server of the actual backend given that the query allows for it (values: true|false).
    """

    class Format(Enum):
        json = "json"
        csv = "csv"

    format: Format = Format.json
    compression: Optional[Literal["gzip"]] = None
    allow_redirect: bool = True

    def to_dict(self) -> dict:
        """Converts the class to a dictionary with keys and values conforming to the expected form of the data-api of PSI.

        Returns:
            dict: Dictionary representing the information encoded in the class.
        """
        result = {"format": self.format.value}
        if self.compression:
            result["compression"] = self.compression
        if not self.allow_redirect:
            result["allowRedirect"] = "true"
        return result


@dataclass
class ValueMapping:
    """It is possible to map values based on their pulse-id/global time.

    Setting this option activates a table like alignment of the response which differs from the standard response format.

    Parameters:
        incomplete (Literal["provide-as-is", "drop", "fill-null"): Defines how incomplete mappings should be handled.
                    (e.g., when the values of two channels should be mapped but these channels have different frequencies or one was not available at the specified query range.)
                    provide-as-is: provides the data as recorded
                    drop: discards incomplete mappings
                    fill-null: fills incomplete mappings with a null string (simplifies parsing).

        alignment (Literal["by-pulse", "by-time"] | None): Defines how the events should be aligned to each other.
                   values: (by-pulse|by-time|none).
                   In case alignment is undefined it will be selected based on the query type (query by pulse-id or by time).
                   none will simply add one event of a channel after the other (independent of other channels).

        aggregations (List[Aggregation.Aggregations] | None): In case several events are mapped into the same bin
                      (e.g. due to activated binning or duplicated pulse-ids)
                      the values will be aggregated based on this parameter
                      (in case it is undefined it will use the global/default aggregations).

    """

    incomplete: Literal["provide-as-is", "drop", "fill-null"]
    alignment: Optional[Literal["by-pulse", "by-time"]] = None
    aggregations: Optional[List[Aggregation.Aggregations]] = None

    def to_dict(self) -> dict:
        """Converts the class to a dictionary with keys and values conforming to the expected form of the data-api of PSI.

        Returns:
            dict: Dictionary representing the information encoded in the class.
        """
        result = {"incomplete": self.incomplete}
        if self.alignment:
            result["alignment"] = self.alignment
        if self.aggregations:
            result["aggregations"] = [
                aggregation.value for aggregation in self.aggregations
            ]
        return result


@dataclass
class ValueTransformations:
    """A alue transformations.

    Assigning transformations to queried channels is done using regular expressions applied to channel names
    whereas a longer match sequence is considered superior to a shorter match sequence.

    Parameters:
        pattern (str): The regular expression applied to channel names.
        sequence (dict): A sequence of transformation operations
                 (see https://git.psi.ch/sf_daq/ch.psi.daq.databuffer/-/blob/master/ch.psi.daq.queryrest/Readme.md#value_transformation_operations for examples).
        backend (Backends | None): The backend (usually left undefined).
    """

    pattern: str
    sequence: dict
    backend: Optional[Backends] = None

    def to_dict(self) -> dict:
        """Converts the class to a dictionary with keys and values conforming to the expected form of the data-api of PSI.

        Returns:
            dict: Dictionary representing the information encoded in the class.
        """
        result = {"pattern": self.pattern, "sequence": [self.sequence]}
        if self.backend:
            result["backend"] = self.backend.value.name
        return result


class ConfigFields(Enum):
    """Array of requested config fields.

    Values:
        channel: The channel name (this is suppressed in the data array since it is already provided as the identifier of the data array)
        channel_name: Alias for channel.
        backend: The origin backend of the event.
        pulse_id: The pulse-id.
        global_seconds: The second of the global timing system as a decimal value including fractional seconds.
        global_date: The date of the global timing system. ISO8601 formatted String up do nano second resolution (e.g. 1970-01-01T02:00:59.123456789+01:00).
        global_millis: The millis of the global timing system as a long value.
        split_count: The split count (for internal storage setup)
        bin_size: The bin size (for internal storage setup)
        keyspace: The key space (for internal storage setup)
        data_type: The shape of the data point (e.g. [2048] for waveforms or [2560,1920] for images).
        shape: The shape of the data point.
        source: The source (e.g. server address) of the channel.
        precision: The precision of the channel values
        unit: The unit of the channel values.
        description: The description of the channel.
        modulo: The modulo of the channel (only applicable for bsread channels)
        offset: The offset, missing documentation on source, so your guess is as good as mine.
    """

    channel = "channel"
    channel_name = "name"
    backend = "backend"
    pulse_id = "pulseId"
    global_seconds = "globalSeconds"
    global_date = "globalDate"
    global_millis = "globalMillis"
    split_count = "splitCount"
    bin_size = "binSize"
    keyspace = "keyspace"
    data_type = "type"
    shape = "shape"
    source = "source"
    precision = "precision"
    unit = "unit"
    description = "desciroption"
    modulo = "modulo"
    offset = "offset"


class EventFields(Enum):
    """Array of requested event fields.

    Values:
        channel: The channel name.

        backend: The origin backend of the event.
        pulse_id: The pulse-id.
        global_time: The time of the global timing system (UNIX epoch) as unscaled seconds with an implicit scale of 9.
        global_seconds: The second of the global timing system (UNIX epoch) as a decimal value including fractional seconds.
        global_date: The date of the global timing system. ISO8601 formatted String up do nano second resolution (e.g. 1970-01-01T02:00:59.123456789+01:00).
        global_millis: The millis of the global timing system as a long value.
        ioc_time: The time of the IOC local timing system (UNIX epoch) as unscaled seconds with an implicit scale of 9.
        ioc_seconds: The second of the IOC local timing system (UNIX epoch) as a decimal value including fractional seconds.
        ioc_date: The date of the IOC local timing system. ISO8601 formatted String up do nano second resolution (e.g. 1970-01-01T02:00:59.123456789+01:00).
        ioc_millis: The millis of the IOC local timing system (JAVA epoch) as a long value.
        shape: The shape of the data point.
        data_type: The type of the data point (e.g. int32).
        event_count: Event count defines the number of events, i.e. distinct data points (**not** to be confused with 'count' aggregation), a data event consists of)
        raw_value: The raw value (e.g., when no aggregation was requested)
        transformed_value: The transformed value (value calculated from value).
        status: The status of the Event.
        severity: The severity of the Event.
    """

    channel = "channel"
    backend = "backend"
    pulse_id = "pulseId"
    global_time = "globalTime"
    global_seconds = "globalSeconds"
    global_date = "globalDate"
    global_millis = "globalMillis"
    ioc_time = "iocTime"
    ioc_seconds = "iocSeconds"
    ioc_date = "iocDate"
    ioc_millis = "iocMillis"
    shape = "shape"
    data_type = "type"
    event_count = "eventCount"
    raw_value = "value"
    transformed_value = "transformedValue"
    status = "status"
    severity = "severity"


@dataclass
class RangeByPulseId:
    """Applies Range by Pulse ID.

    Parameters:
        start_pulse_id (int): The start pulse-id of the range request.
        end_pulse_id (int): The end pulse-id of the range request.
        start_inclusive (bool): Defines if the start should be considered inclusive.
        start_expansion (bool): Expands the query start until the first entry before the defined start.
                                Binning aggregations are expanded until the start of the bin of that entry.
        end_inclusive (bool): Defines if the end should be considered inclusive.
        end_expansion (bool): Expands the query end until the first entry after the defined end.
                              Binning aggregations are expanded until the end of the bin of that entry.
    """

    start_pulse_id: int
    end_pulse_id: int
    start_inclusive: bool = True
    start_expansion: bool = False
    end_inclusive: bool = True
    end_expansion: bool = False

    def to_dict(self):
        """Converts the class to a dictionary with keys and values conforming to the expected form of the data-api of PSI.

        Returns:
            dict: Dictionary representing the information encoded in the class.
        """
        return _to_dict(self)


@dataclass
class RangeByDate:
    """Applies Range by Date.

    Parameters:
        start_date (datetime): The start datetime of the range request.
        endDate (datetime): The end datetime of the range request.
        start_inclusive (bool): Defines if the start should be considered inclusive.
        start_expansion (bool): Expands the query start until the first entry before the defined start.
                                Binning aggregations are expanded until the start of the bin of that entry.
        end_inclusive (bool): Defines if the end should be considered inclusive.
        end_expansion (bool): Expands the query end until the first entry after the defined end.
                              Binning aggregations are expanded until the end of the bin of that entry.
    """

    start_date: datetime
    end_date: datetime
    start_inclusive: bool = True
    start_expansion: bool = False
    end_inclusive: bool = True
    end_expansion: bool = False

    def to_dict(self):
        """Converts the class to a dictionary with keys and values conforming to the expected form of the data-api of PSI.

        Returns:
            dict: Dictionary representing the information encoded in the class.
        """
        return _to_dict(self)


@dataclass
class RangeByTime:
    """Applies Range by Time.

    Parameters:
        start_seconds (float): The start second as timestamp (UNIX epoch) of the range request.
        end_seconds (float): The end second as timestamp (UNIX epoch) of the range request.
        start_inclusive (bool): Defines if the start should be considered inclusive.
        start_expansion (bool): Expands the query start until the first entry before the defined start.
                                Binning aggregations are expanded until the start of the bin of that entry.
        end_inclusive (bool): Defines if the end should be considered inclusive.
        end_expansion (bool): Expands the query end until the first entry after the defined end.
                              Binning aggregations are expanded until the end of the bin of that entry.
    """

    start_seconds: float
    end_seconds: float
    start_inclusive: bool = True
    start_expansion: bool = False
    end_inclusive: bool = True
    end_expansion: bool = False

    def to_dict(self):
        """Converts the class to a dictionary with keys and values conforming to the expected form of the data-api of PSI.

        Returns:
            dict: Dictionary representing the information encoded in the class.
        """
        return _to_dict(self)
