# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cen']

package_data = \
{'': ['*']}

install_requires = \
['cookiecutter>=2.1.1,<3.0.0', 'fire>=0.5.0,<0.6.0']

entry_points = \
{'console_scripts': ['cen = cen.cli']}

setup_kwargs = {
    'name': 'cen-dev',
    'version': '0.1.4',
    'description': 'Centra developer commanl line tool',
    'long_description': '# cen-command-line-tool\n\nКонсольная утилита cen для внутреннего использования\n\nОснова для работы как command line tool от https://github.com/google/python-fire/\n\n\n## Deploy\n\nhttps://johnfraney.ca/blog/create-publish-python-package-poetry/\nЗаливается в https://pypi.org/ из под tech@centra.ai. Логин пароль у менеджмента в ключнице',
    'author': 'Centra Dev Team',
    'author_email': 'hello@centra.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://centra.ai',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
