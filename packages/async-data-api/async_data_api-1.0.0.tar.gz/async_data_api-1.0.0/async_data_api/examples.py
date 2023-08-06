# import asyncio
# from async_data_api import (DataApi,
#                             Backends,
#                             ChannelName,
#                             Aggregation,
#                             EventFields,
#                             RangeByDate)
# from datetime import datetime, timedelta


# async def search_channels_example():
#     """Example of how to find a channel by it's name on any backend.
#     """
#     async with DataApi(base_url="https://data-api.psi.ch/") as api:
#         channels = await api.find_channels(
#                 regex="MMAC3:STR:2",
#                 return_config=True,
#             )
#     print(channels)


# async def get_data_example():
#     """Example to get the data for a channel of the last 3 days, aggregated and binned to 500 bins, as pandas dataframe.
#     """
#     async with DataApi(base_url="https://data-api.psi.ch/") as api:
#         async for result in api.get_data(
#             channels=ChannelName(name="MMAC3:STR:2", backend=Backends.proscan),
#             range=RangeByDate(
#                 start_date=datetime.now() - timedelta(days=3),
#                 endDate=datetime.now(),
#                 start_expansion=False,
#             ),
#             event_fields=[EventFields.global_millis, EventFields.raw_value],
#             aggregation=Aggregation(
#                 aggregations=[
#                     Aggregation.Aggregations.min,
#                     Aggregation.Aggregations.mean,
#                     Aggregation.Aggregations.max,
#                 ],
#                 nr_of_bins=500,
#             ),
#         ):
#             df = api.json_to_dataframe(result)
#             print(df)


# async def main():
#     """Uncomment the example you want to run
#     """
#     await search_channels_example()
#     #await get_data_example()
#     pass

# if __name__ == "__main__":
#     asyncio.run(main())
