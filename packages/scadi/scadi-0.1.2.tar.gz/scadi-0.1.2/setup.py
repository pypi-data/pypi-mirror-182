# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scadi']

package_data = \
{'': ['*']}

install_requires = \
['cliff>=3.10.0,<4.0.0']

entry_points = \
{'cliff.scadi': ['inline = scadi.inline:Inline'],
 'console_scripts': ['scadi = scadi.main:main']}

setup_kwargs = {
    'name': 'scadi',
    'version': '0.1.2',
    'description': 'SCAD Inliner: Roll up OpenSCAD includes into the main file for easy sharing.',
    'long_description': '.. image:: https://static.pepy.tech/personalized-badge/scadi?period=month&units=international_system&left_color=black&right_color=orange&left_text=downloads/month\n   :target: https://pepy.tech/project/scadi\n   :alt: downloads/month\n\n=====\nscadi\n=====\n\nCommand-line tool for rolling up all includes into the main file of your model so that you can easily share it online.\n\nInstallation\n============\n\n::\n\n   pip3 install scadi\n\nUsage\n=====\n\n::\n\n   scadi inline ./my-model.scad\n\nThe above command will create a file called ``./inline-my-model.scad`` that can be shared on sites that have OpenSCAD customizers.\n\nSupport me\n==========\n\nIf you found that this tool saved you some time and you want to give back, please consider using Ko-Fi to buy me a coffee.\n\n.. image:: https://ko-fi.com/img/githubbutton_sm.svg\n   :target: https://ko-fi.com/S6S7GJUG3\n   :alt: ko-fi\n',
    'author': 'Nascent Maker',
    'author_email': 'hello@nascentmaker.com',
    'maintainer': 'Nascent Maker',
    'maintainer_email': 'hello@nascentmaker.com',
    'url': 'https://nascentmaker.com/py/scadi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
