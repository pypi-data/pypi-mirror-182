# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stonewave',
 'stonewave.sql.udtfs',
 'stonewave.sql.udtfs.functions.faker',
 'stonewave.sql.udtfs.functions.generate_union',
 'stonewave.sql.udtfs.functions.geo_to_h3',
 'stonewave.sql.udtfs.functions.load_excel',
 'stonewave.sql.udtfs.functions.parse_binary',
 'stonewave.sql.udtfs.functions.parse_binary.formats',
 'stonewave.sql.udtfs.functions.parse_format',
 'stonewave.sql.udtfs.functions.parse_grok',
 'stonewave.sql.udtfs.functions.parse_sql',
 'stonewave.sql.udtfs.functions.pivot_table',
 'stonewave.sql.udtfs.functions.summarize',
 'stonewave.sql.udtfs.functions.transpose',
 'stonewave.sql.udtfs.functions.unpivot_table',
 'stonewave.sql.udtfs.functions.url',
 'stonewave.sql.udtfs.protocol',
 'stonewave.sql.udtfs.protocol.arrow',
 'stonewave.sql.udtfs.protocol.fsm',
 'stonewave.sql.udtfs.protocol.fsm.apply']

package_data = \
{'': ['*']}

install_requires = \
['faker-cloud>=0.1,<0.2',
 'faker>=15.3.3,<16.0.0',
 'faker_credit_score>=0.3.0,<0.4.0',
 'faker_microservice>=2.0.0,<3.0.0',
 'faker_vehicle>=0.2.0,<0.3.0',
 'faker_web>=0.3.1,<0.4.0',
 'fastapi==0.70.0',
 'h3>=3.7.3,<4.0.0',
 'httpx>=0.20.0,<0.21.0',
 'kaitaistruct>=0.10,<0.11',
 'openpyxl>=3.0.9,<4.0.0',
 'pandas==1.5.2',
 'parse>=1.19.0,<2.0.0',
 'pyarrow==10.0.0',
 'pygrok>=1.0.0,<2.0.0',
 'requests>=2.25.1,<3.0.0',
 'setuptools>=65.6.3,<66.0.0',
 'sql-metadata>=2.6.0,<3.0.0',
 'structlog>=20.2.0,<21.0.0',
 'toml>=0.10.2,<0.11.0',
 'transitions>=0.8.3,<0.9.0',
 'trio>=0.19.0,<0.20.0',
 'uvicorn>=0.15.0,<0.16.0',
 'wheel-filename>=1.3.0,<2.0.0',
 'wheel>=0.38.4,<0.39.0']

entry_points = \
{'console_scripts': ['sw_py_udtf = stonewave.sql.udtfs.main:execute_command']}

setup_kwargs = {
    'name': 'stonewave-sql-udtfs',
    'version': '0.6.3',
    'description': '',
    'long_description': 'None',
    'author': 'Yue Ni',
    'author_email': 'yni@yanhuangdata.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.yanhuangdata.com/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
