# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['googletable']
install_requires = \
['pandas>=1.5.2,<2.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'googletable',
    'version': '1.1.3',
    'description': 'The module that collects data from the Google table',
    'long_description': "# ***Получение данных с Google таблиц***\n____\n### Установка\n```cmd\npip install googletable\n```\n### Импорт и инициализация\n\n```python\nfrom GoogleTable import GoogleTable\n\ntableid = '1iVSut_5LLcXAeecJI73y0EmltL8mwg-9hEHaWP2UOp0'\ngid = '0'\nencoding = 'utf-8'\n\nGoogleTable(tableid,gid,encoding)\n```\n### Где найти tableid ?\n>tableid - ID таблицы гугл (Под верхними стрелками)\n> \n>gid - ID листа таблицы (Над нижними стрелками )\n\n                                           ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n    https://docs.google.com/spreadsheets/d/1iVSut_5LLcXAeecJI73y0EmltL8mwg-9hEHaWP2UOp0/edit#gid=0  \n                                                                                        ↑↑↑↑↑↑↑↑↑↑\n\n\n### Примечание\n> ## Важно чтобы таблица была открыта для общего доступа!\n### Полезные ссылки\n>[Страница на GitHub](https://github.com/DaniEruDai/GoogleTable)\n> | [Страница на PyPi](https://pypi.org/project/googletable/)\n",
    'author': 'DaniEruDai',
    'author_email': 'DaniEruDai@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3,<4',
}


setup(**setup_kwargs)
