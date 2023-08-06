# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['markers',
 'markers.management',
 'markers.management.commands',
 'markers.templatetags']

package_data = \
{'': ['*'], 'markers': ['static/markers/fonts/*']}

install_requires = \
['django>=3.2', 'numpy>=1.14.0,<2.0.0', 'pillow>=3.1.0']

setup_kwargs = {
    'name': 'django-markers',
    'version': '1.4.0',
    'description': 'Dynamic map marker generation using template images and arbitrary text',
    'long_description': '# django-markers\n\nA dynamic map marker generator using template images and arbitrary text.\n\n\n## Why\n\nSometimes you need to use a lot of markers on a map, many of which are similar,\nbut slightly different, using text labels, or even different colours or\nopacities.  This will do that for you.\n\nTheoretically, you could also use it to caption memes, but I think there\'s\nother stuff out there for that sort of thing.\n\n\n## How\n\nYou can reference the markers in three ways: using a django template tag, via\nURL parameters, or in Python, by using the `Marker` class.  The preferred\nmethod is the template tag, and I don\'t recommend using direct URL requests,\nsince it requires a hit to your application server every time.\n\n### Using a Template Tag\n\nThis will generate a media URL pointing to a newly-created marker based on a\n`template.png`, with the text `42`, positioned `3` pixels right, and `3` pixels\ndown from the upper left corner of the template, with an opacity of `50%`, a\nhue-shift of `105`, and using the hex colour `#333333` for the text.  All the\narguments, save for the first, are optional:\n\n```django\n{% load markers %}\n{% marker \'path/to/template.png\' text=\'42\' text_x=3 text_y=3 opacity=0.5 hue=105 text_colour=\'333333\' %}\n```\n\nTypically, you\'ll use this in your template to assign marker paths to some\njavascript variables:\n\n``django\n<script>\n  var marker1 = "{% marker \'path/to/template.png\' text=\'1\' %}";\n  var marker2 = "{% marker \'path/to/template.png\' text=\'3\' hue=105 %}";\n</script>\n``\n\nAfter you have the URLs in your Javascript, you can do whatever you like with\nthem, they\'re just URLs to existing static files.\n\n\n### Using Direct Links\n\nThe same arguments passed to the template tag can be passed in a URL:\n\n```\nhttps://localhost:8000/markers/path/to/template.png?text=42&opacity=0.5&text_x=3&text_y=3&text_colour=333333&hue=105\n```\n\n\n### Using the Python Model\n\nMarker generation is as easy as instantiating a model:\n\n``python\nfrom markers.models import Marker\n\nmymarker = Marker(\n    "path/to/template.png",\n    text="42",\n    opacity=0.5,\n    text_x=3,\n    text_y=3,\n    text_colour="333333",\n    hue=105\n)\n``\n\n\n### The Templates\n\nThe template path you pass to `django-markers`, must be part of one of your\napps, and referenced as such.  So for example, if you have a template living in\n`mapping/static/mapping/img/markers/mytemplate.png`, the argument you\'re\nlooking for is: `mapping/img/markers/mytemplate.png`.\n\nIf you\'re calling the URL directly, then you\'ll append this path to the URL\nlike so:\n\n```\nhttps://localhost:8000/markers/mapping/img/markers/mytemplate.png?hue=105&opacity=0.8\n```\n\n\n### A Note on Text Positioning\n\nBy default, we try to centre text along the x/y axis, so if that\'s your\nintention, don\'t specify either.  Specifying an `x` value without a `y` one\nwill assume `y` to be centred and vice versa.\n\n\n### A Note on Template Images\n\nYou can use whatever image you like for your templates, but since the\nhue-shifting starts at red (0), and progresses through the spectrum to red\nagain at 360, you\'d do well to use a redish image as your template.\nOtherwise, requests that don\'t specify a `hue` will look out of step with\nones that have `hue` set to `1`.\n\n\n\n## Installation\n\nYou can install it from pypi using `pip`:\n\n```shell\n$ pip install django-markers\n```\n\nOr you can install it from GitHub:\n\n```shell\n$ pip install git+https://github.com/danielquinn/django-markers.git#egg=django-markers\n```\n\n\nThen in your `settings.py`:\n\n```python\nINSTALLED_APPS = (\n    ...\n    "markers",\n)\n```\n\nAnd if you want to make use of the direct URL requests, you\'ll need to add this\nto your `urls.py`:\n\n```python\nurl(r"^some/arbitrary/path/", include("markers.urls")),\n```\n\nSo for example, you would have something like this in your `urls.py`:\n\n```python\nurl(r"^mapping/markers/", include("markers.urls")),\n```\n\n\n### Requirements\n\nWe\'re doing image processing here, so `PIL` is required.  You should probably\nuse `Pillow` though, since that\'s what this was developed against.\nAdditionally, `numpy` is required to handle the hue-shifting.  Both will\ninstall automatically if you follow the installation instructions above.\n\nIn addition to these Python dependencies, Django 1.6+ is required if you\nintend to make use of the on-the-fly generation via calling a specific URL.\n\n\n### Licensing\n\nThe whole project is licensed under the GPL-3, but the default font used is\nlicensed under Apache 2.0.',
    'author': 'Daniel Quinn',
    'author_email': 'code@danielquinn.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/danielquinn/django-markers',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
