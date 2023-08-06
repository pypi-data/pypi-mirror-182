# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['poetry_sort']

package_data = \
{'': ['*']}

install_requires = \
['poetry>=1.2,<2.0']

entry_points = \
{'poetry.application.plugin': ['sort = poetry_sort.plugin:PoetrySortPlugin']}

setup_kwargs = {
    'name': 'poetry-sort',
    'version': '0.0.0',
    'description': 'Alphabetically sort your Poetry dependencies',
    'long_description': '# poetry-sort\n\npoetry-sort is a [Poetry](https://python-poetry.org/) plugin that alphabetically sorts the dependencies in your `pyproject.toml` file.\n\n## Installation\n\n```bash\npoetry self add poetry-sort\n```\n\n## Usage\n\n```bash\npoetry sort\n```\n\n`poetry sort` supports the `--with`, `--without`, and `--only` options, which function identically to `poetry install`.\nFor full usage information, run `poetry sort --help`.\n\npoetry-sort runs automatically whenever you run `poetry add` or `poetry init` and will sort only the dependency\ngroups that were modified by the command.\n\n\n## Configuration\n\npoetry-sort can be configured via a `tool.sort.config` section in your `pyproject.toml` file.\n\n```toml\n[tool.sort.config]\nsort-python = false\nformat = true\n```\n\nThe following options are available:\n\n- `sort-python`: Whether to also sort the `python` dependency. If `false`, the `python` dependency will be placed at\nthe top of `tool.poetry.dependencies`; if `true`, it will be sorted alphebetically with everything else.\nDefaults to `false`.\n\n- `format`: Whether to apply some basic formatting to `pyproject.toml` after sorting. If `true`, poetry-sort will\ntake all occurences of three or more consecutive newlines in `pyproject.toml` and replace them with two newlines.\nIf `false`, poetry-sort will not modify `pyproject.toml` beyond just sorting your dependencies. Defaults to `true`.\n\n\n## License\npoetry-sort is licensed udner the [MIT License](LICENSE.md).',
    'author': 'celsius narhwal',
    'author_email': 'hello@celsiusnarhwal.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/celsiusnarhwal/poetry-sort',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
