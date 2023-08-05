# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tests', 'typesafe_parmap']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'typesafe-parmap',
    'version': '1.0.4',
    'description': 'Run functions in parallel safely with typesafe parmap!.',
    'long_description': '# Typesafe parmap\n\n\n[![pypi](https://img.shields.io/pypi/v/typesafe-parmap.svg)](https://pypi.org/project/typesafe-parmap)\n[![python](https://img.shields.io/pypi/pyversions/typesafe-parmap.svg)](https://pypi.org/project/typesafe-parmap)\n[![Build Status](https://github.com/thejaminator/typesafe_parmap/actions/workflows/dev.yml/badge.svg)](https://github.com/thejaminator/typesafe_parmap/actions/workflows/dev.yml)\n\n```\npip install typesafe-parmap\n```\n\nRun functions in parallel safely with your type checkers\n\n\n* GitHub: <https://github.com/thejaminator/typesafe_parmap>\n\n\n## Features\n\nEasy run different functions in parallel\n```python\nfrom typesafe_parmap import par_map_2\nimport time\nfrom concurrent.futures import ThreadPoolExecutor\n\ntp = ThreadPoolExecutor(5)\n\ndef long_running_int(param: int) -> int:\n    time.sleep(5)  # long IO task here\n    return 123\n\ndef long_running_str(param: str) -> str:\n    time.sleep(5)  # long IO task here\n    return "hello world"\n\nint_result, str_result = par_map_2(\n                        lambda: long_running_int(5),\n                        lambda: long_running_str("test"),\n                        executor=tp)\nassert int_result == 123, str_result == "hello world"  # should finish in around 5 seconds\n```\n\nFunction return types are inferred correctly by mypy / pycharm\n\n```python\nreveal_type(int_result) # mypy infers int\nreveal_type(str_result) # mypy infers str\n```\n\nAccidentally unpacked too many / little values? Type inference checks that for you!\n```python\none, two, three, four = par_map_3(\n        lambda: long_running_int(5), lambda: long_running_str("test"), lambda: "something", executor=tp\n    ) # Error: Need more than 3 values to unapck, (4 expected)\n```\n\nGot more than a few functions to run? We got you covered...\n```python\nfrom typesafe_parmap import par_map_4 # ... all the way to par_map_22!\n```\n\nWant to change the number of functions to run in parallel? Hate having to import a different one each time?\nUse par_map_n!\n```python\nfrom typesafe_parmap import par_map_2, par_map_3, par_map_n\na = par_map_2(lambda: long_running_int(5), lambda: long_running_str("test"), executor=executor)\nb = par_map_n(lambda: long_running_int(5), lambda: long_running_str("test"), executor=executor)\n\nassert a == b\n\nc = par_map_3(\n    lambda: long_running_int(5),\n    lambda: long_running_str("test"),\n    lambda: long_running_str("test"),\n    executor=executor,\n)\nd = par_map_n(\n    lambda: long_running_int(5),\n    lambda: long_running_str("test"),\n    lambda: long_running_str("test"),\n    executor=executor,\n)\n\nassert c == d\n```\n\n## Timeouts\nSuppose you want to run a bunch of functions that might take a long time, but you don\'t want to wait forever.\nUse par_map_timeout_n!\n```python\nfrom concurrent.futures import ThreadPoolExecutor\nfrom datetime import timedelta\nfrom typesafe_parmap import par_map_timeout_n\n# Since there are 3 threads, we should be able to run 3 functions at once\nexecutor = ThreadPoolExecutor(3)\nint_result, str_result_1, str_result_2 = par_map_timeout_n(\n    lambda: long_running_int(5),\n    lambda: short_running_str("test 1"),\n    lambda: short_running_str("test 2"),\n    executor=executor,\n    timeout=timedelta(seconds=5),\n)\nassert int_result is None # This function timed out\nassert str_result_1 == "test 1" # This still finished in time\nassert str_result_2 == "test 2" # This still finished in time\n```\nNote that as a result of the timeout, the return types of the int_result and str_result_1 are now Optional[str] and Optional[int] respectively.\n\n\n### Logging timeouts\npar_map_timeout_n accepts a logger parameter.\nWe also provide a class `NamedThunk`, which allows you to name your thunks so that the name is not just `<lambda>` in the logs.\n```python\nfrom concurrent.futures import ThreadPoolExecutor\nfrom datetime import timedelta\nfrom typesafe_parmap import par_map_timeout_n, NamedThunk\nexecutor = ThreadPoolExecutor(2)\npar_map_timeout_n(\n    NamedThunk(lambda: long_running_int(5), name="Long Running Int"),\n    lambda: short_running_str("test 2"),\n    executor=executor,\n    timeout=timedelta(seconds=3),\n    logger=print,\n)\n# Prints:\n# par_map func1: Long Running Int timed out after 3 seconds\n```\n',
    'author': 'James Chua',
    'author_email': 'chuajamessh@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/thejaminator/typesafe_parmap',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
