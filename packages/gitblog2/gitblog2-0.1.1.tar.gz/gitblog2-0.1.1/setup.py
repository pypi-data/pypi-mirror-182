# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gitblog2']

package_data = \
{'': ['*'], 'gitblog2': ['media/*', 'templates/*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'Markdown>=3.4.1,<4.0.0',
 'pygit2>=1.11.1,<2.0.0',
 'typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['gitblog = gitblog2.cli:main']}

setup_kwargs = {
    'name': 'gitblog2',
    'version': '0.1.1',
    'description': 'Git + Markdown = blog',
    'long_description': '# ![Git-blog Logo](media/favicon.svg "title") Git-blog\n\nGit + Markdown = Your blog\n\n## TODO\n\n* Add bio and picture from github\n* Look at cool HTML elements: <https://tapajyoti-bose.medium.com/7-cool-html-elements-nobody-uses-436598d85668>\n* css toolchain like <https://github.com/FullHuman/purgecss/issues/264>\n* Live update locally\n* Draft support (set publish_date to first `mv`)\n* Fix root index.html not served by redbean\n\n## Internals\n\nStylesheet is based on water.css\n\n## Development\n\nYou can lively check your local changes by running the following commands in 2 separate terminals:\n\n```bash\ncurl https://redbean.dev/redbean-tiny-2.2.com > redbean.zip\nzip redbean.zip .init.lua\n./redbean.zip -D www/\n\n# Lively rebuild\n./live-build.sh\n\n# Serve the blog\ndocker run -v "${PWD}/.out/blog":/usr/share/nginx/html:ro -p 127.0.0.1:8080:80 nginx:alpine\n```\n\nReload <http://127.0.0.1:8080/tech> to check the results.\n',
    'author': 'Henri Hannetel',
    'author_email': 'henri.hannetel@pm.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
