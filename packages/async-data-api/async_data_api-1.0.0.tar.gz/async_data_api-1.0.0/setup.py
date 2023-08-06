# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['async_data_api']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.1,<0.24.0', 'isodate>=0.6.1,<0.7.0', 'pandas>=1.5.2,<2.0.0']

setup_kwargs = {
    'name': 'async-data-api',
    'version': '1.0.0',
    'description': 'Async Client for PSIs REST DataApi (https://data-api.psi.ch)',
    'long_description': '# async_data_api - Async DataApi Client\n\n[![pipeline status](https://git.psi.ch/proscan_data/async_data_api/badges/main/pipeline.svg)](https://git.psi.ch/proscan_data/async_data_api/-/commits/main)\n\n[![coverage report](https://git.psi.ch/proscan_data/async_data_api/badges/main/coverage.svg)](https://git.psi.ch/proscan_data/async_data_api/-/commits/main)\n\n#### Table of Contents\n- [Introduction](#introduction)\n- [Installation](#installation)\n- [Quick-start Guid](#quick-start-guide)\n- [Documentation](#documentation)\n- [Dependencies](#dependencies)\n- [Contribute](#contribute)\n- [Project Changes and Tagged Releases](#project-changes-and-tagged-releases)\n- [Developer Notes](#developer-notes)\n- [Contact](#contact)\n\n# Introduction\nThis project/package aims to provide a fully asynchronous client for PSIs REST DataAPI.\n\n# Installation\nInstall with pip\n```bash\npip install async_data_api\n```\n# Quick-start Guide\nHere are some simple examples to get you started:\n```python\nimport asyncio\nfrom datetime import datetime, timedelta\n\nfrom async_data_api import (\n    Aggregation,\n    Backends,\n    ChannelName,\n    DataApi,\n    EventFields,\n    RangeByDate,\n)\n\n\nasync def search_channels_example():\n    """Example of how to find a channel by it\'s name on any backend.\n    """\n    async with DataApi(base_url="https://data-api.psi.ch/") as api:\n        channels = await api.find_channels(\n                regex="MMAC3:STR:2",\n                return_config=True,\n            )\n    print(channels)\n\n\nasync def get_data_example():\n    """Example to get the data for a channel of the last 3 days, aggregated and binned to 500 bins, as pandas dataframe.\n    """\n    async with DataApi(base_url="https://data-api.psi.ch/") as api:\n        async for result in api.get_data(\n            channels=ChannelName(name="MMAC3:STR:2", backend=Backends.proscan),\n            range=RangeByDate(\n                start_date=datetime.now() - timedelta(days=3),\n                endDate=datetime.now(),\n                start_expansion=False,\n            ),\n            event_fields=[EventFields.global_millis, EventFields.raw_value],\n            aggregation=Aggregation(\n                aggregations=[\n                    Aggregation.Aggregations.min,\n                    Aggregation.Aggregations.mean,\n                    Aggregation.Aggregations.max,\n                ],\n                nr_of_bins=500,\n            ),\n        ):\n            df = api.json_to_dataframe(result)\n            print(df)\n\n\nasync def main():\n    """Uncomment the example you want to run\n    """\n    #await search_channels_example()\n    #await get_data_example()\n    pass\n\nif __name__ == "__main__":\n    asyncio.run(main())\n\n```\n\n\n# Documentation\nCurrent Features:\n* Fully asynchronous\n* 100% Test coverage\n* Search for channels\n* get data as pandas dataframe\n\n\nCheck out the wiki for more info!\n\n# Dependencies\n* [httpx](https://github.com/encode/httpx/)\n* [isodate](https://github.com/gweis/isodate/)\n* [pandas](https://pandas.pydata.org/)\n\n\n# Contribute\nTo contribute, simply clone the project.\nYou can uses ``` pip -r requirements.txt ``` or the Makefile to set up the project.\nAfter that you can make changes and create a pull request or if allowed merge your changes.\n\n\n# Project Changes and Tagged Releases\n* See the Changelog file for further information\n* Project releases are available in pypi (NOT YET)\n\n# Developer Notes\nCurrently None\n\n# Contact\nIf you have any questions pleas contract \'niklas.laufkoetter@psi.ch\'\n',
    'author': 'Niklas Laufkoetter',
    'author_email': 'niklas.laufkoetter@psi.ch',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
