# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['mape',
 'mape.remote',
 'mape.remote.influxdb',
 'mape.remote.redis',
 'mape.remote.rest']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'Rx>=3.2.0,<4.0.0',
 'aiohttp>=3.8.1,<4.0.0',
 'fastapi>=0.73,<0.74',
 'influxdb-client>=1.26.0,<2.0.0',
 'redis-purse>=0.25.0,<0.26.0',
 'uvicorn>=0.17.4,<0.18.0']

setup_kwargs = {
    'name': 'pymape',
    'version': '0.1.0a5',
    'description': 'Framework to develop Self-Adaptive system based on MAPE-K loop.',
    'long_description': '<p align="center">\n    <a href="https://pypi.org/project/pymape/"><img\n        src="https://img.shields.io/pypi/v/pymape?style=flat-square"\n        alt="PyPI Version"\n    /></a>\n    <a href="https://pypi.org/project/pymape/"><img\n        src="https://img.shields.io/pypi/pyversions/pymape?style=flat-square"\n        alt="Py Version"\n    /></a>\n    <a href="https://github.com/elbowz/pymape/issues"><img\n        src="https://img.shields.io/github/issues/elbowz/pymape.svg?style=flat-square"\n        alt="Issues"\n    /></a>\n    <a href="https://raw.githubusercontent.com/elbowz/PyMAPE/main/LICENSE"><img\n        src="https://img.shields.io/github/license/elbowz/pymape.svg?style=flat-square"\n        alt="GPL License"\n    /></a>\n    <a href="https://raw.githubusercontent.com/elbowz/PyMAPE/main/LICENSE"><img\n        src="https://img.shields.io/static/v1?label=Powered&message=RxPY&style=flat-square&color=informational"\n        alt="RxPY"\n    /></a>\n</p>\n\n<p align="center">\n    <img src="https://github.com/elbowz/PyMAPE/raw/main/docs/assets/img/logo.png" alt="PyMAPE" width="400">\n    <h4 align="center">Distributed and decentralized MonitorAnalyzePlanExecute-Knowledge loops framework</h3>\n    <p align="center">\n        Framework to support the development and deployment of Autonomous (Self-Adaptive) Systems\n    </p>\n</p>\n\n---\n\n* __Source Code__: [https://github.com/elbowz/PyMAPE](https://github.com/elbowz/PyMAPE)\n* __Documentation__: [https://elbowz.github.io/PyMAPE](https://elbowz.github.io/PyMAPE) - _WIP_\n\n---\n\n## Install\n\n```bash\npip install pymape\n```\n\n## Examples\n\nImplementation of the 5 decentralized (and distributed) MAPE patterns described in the paper:  \n["On Patterns for Decentralized Control in Self-Adaptive Systems", Danny Weyns](https://www.ics.uci.edu/~seal/publications/2012aSefSAS.pdf)\n\n* **Ambulance-Car Emergency** (Information Sharing and Coordinated Control)\n* **Average Speed Enforcement** (Master/Slave)\n* **Dynamic Carriageway** (Regional Planning)\n* **Cruise Control with Distance Hold** (Hierarchical Control)\n\nIf you want try some examples (path `examples/`), refer to section `# CLI EXAMPLES` inside the source code of each one.\n\n[Slide - Introduction to PyMAPE](https://github.com/elbowz/PyMAPE/raw/main/docs/slides.pdf) with examples\n\nThe examples need furthers requirements, please see [pyproject.toml](https://github.com/elbowz/PyMAPE/raw/main/pyproject.toml) or use poetry to [install them](https://github.com/elbowz/PyMAPE#install-for-developers-and-contributors).  \n\nYou also need a Redis and InfluxDB instance running, for example:\n\n```bash\ndocker run --name mape-redis -p 6379:6379  \\\n-v $(pwd)/docker/redis:/usr/local/etc/redis  \\\n--rm redis redis-server /usr/local/etc/redis/redis.conf\n```\n\n```bash\ndocker run --name mape-influxdb -p 8086:8086 \\\n-v $(pwd)/docker/influxdb/data:/var/lib/influxdb2 \\\n-v $(pwd)/docker/influxdb/conf:/etc/influxdb2 \\\n-e DOCKER_INFLUXDB_INIT_MODE=setup \\\n-e DOCKER_INFLUXDB_INIT_USERNAME=user \\\n-e DOCKER_INFLUXDB_INIT_PASSWORD=qwerty123456 \\\n-e DOCKER_INFLUXDB_INIT_ORG=univaq \\\n-e DOCKER_INFLUXDB_INIT_BUCKET=mape \\\n-e DOCKER_INFLUXDB_INIT_RETENTION=1w \\\n-e DOCKER_INFLUXDB_INIT_ADMIN_TOKEN=<GENERATE_OR_TAKE_FROM_CONFIG_YAML> \\\n--rm influxdb:2.0\n```\n\nSee source for more information.',
    'author': 'Emanuele Palombo',
    'author_email': 'muttley.bd@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://elbowz.github.io/PyMAPE/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
