# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiohttp_asgi']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3,<4']

extras_require = \
{':python_version < "3.8"': ['typing_extensions']}

entry_points = \
{'console_scripts': ['aiohttp-asgi = aiohttp_asgi.__main__:main']}

setup_kwargs = {
    'name': 'aiohttp-asgi',
    'version': '0.5.0',
    'description': 'Adapter to running ASGI applications on aiohttp',
    'long_description': 'aiohttp-asgi\n============\n\n[![PyPI - License](https://img.shields.io/pypi/l/aiohttp-asgi)](https://pypi.org/project/aiohttp-asgi) [![Wheel](https://img.shields.io/pypi/wheel/aiohttp-asgi)](https://pypi.org/project/aiohttp-asgi) [![PyPI](https://img.shields.io/pypi/v/aiohttp-asgi)](https://pypi.org/project/aiohttp-asgi) [![PyPI](https://img.shields.io/pypi/pyversions/aiohttp-asgi)](https://pypi.org/project/aiohttp-asgi) [![Coverage Status](https://coveralls.io/repos/github/mosquito/aiohttp-asgi/badge.svg?branch=master)](https://coveralls.io/github/mosquito/aiohttp-asgi?branch=master) ![tox](https://github.com/mosquito/aiohttp-asgi/workflows/tox/badge.svg?branch=master)\n\nThis module provides a way to use any ASGI compatible frameworks and aiohttp together.\n\nExample\n-------\n\n```python\nfrom aiohttp import web\nfrom fastapi import FastAPI\nfrom starlette.requests import Request as ASGIRequest\n\nfrom aiohttp_asgi import ASGIResource\n\n\nasgi_app = FastAPI()\n\n\n@asgi_app.get("/asgi")\nasync def root(request: ASGIRequest):\n    return {\n        "message": "Hello World",\n        "root_path": request.scope.get("root_path")\n    }\n\n\naiohttp_app = web.Application()\n\n# Create ASGIResource which handle\n# any request startswith "/asgi"\nasgi_resource = ASGIResource(asgi_app, root_path="/asgi")\n\n# Register resource\naiohttp_app.router.register_resource(asgi_resource)\n\n# Mount startup and shutdown events from aiohttp to ASGI app\nasgi_resource.lifespan_mount(aiohttp_app)\n\n# Start the application\nweb.run_app(aiohttp_app)\n\n```\n\nInstallation\n------------\n\n```bash\npip install aiohttp-asgi\n```\n\nASGI HTTP server\n----------------\n\nCommand line tool for starting aiohttp web server with ASGI app.\n\n#### Example\n\nCreate the `test_app.py`\n\n```python\nfrom starlette.applications import Starlette\nfrom starlette.responses import JSONResponse\nfrom starlette.routing import Route\n\n\nasync def homepage(request):\n    return JSONResponse({\'hello\': \'world\'})\n\nroutes = [\n    Route("/", endpoint=homepage)\n]\n\napplication = Starlette(debug=True, routes=routes)\n```\n\nand run the `test_app.py` with `aiohttp-asgi`\n\n```bash\naiohttp-asgi \\\n    --address "[::1]" \\\n    --port 8080 \\\n    test_app:application\n```\n\nalternatively using `python -m`\n\n```bash\npython -m aiohttp_asgi \\\n    --address "[::1]" \\\n    --port 8080 \\\n    test_app:application\n```\n',
    'author': 'Dmitry Orlov',
    'author_email': 'me@mosquito.su',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mosquito/aiohttp-asgi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
