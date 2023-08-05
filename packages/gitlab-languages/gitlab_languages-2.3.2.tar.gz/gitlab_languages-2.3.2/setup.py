# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gitlab_languages']

package_data = \
{'': ['*']}

install_requires = \
['maya>=0.6.1,<0.7.0',
 'prometheus-client>=0.15.0,<0.16.0',
 'python-gitlab>=3.12.0,<4.0.0']

entry_points = \
{'console_scripts': ['gitlab-languages = gitlab_languages.__main__:main',
                     'gitlab_languages = gitlab_languages.__main__:main']}

setup_kwargs = {
    'name': 'gitlab-languages',
    'version': '2.3.2',
    'description': 'Utility to generate a Prometheus data source from programming languages inside GitLab repositores',
    'long_description': '# gitlab-languages\n\n[![PyPI - License](https://img.shields.io/pypi/l/gitlab-languages.svg)](https://github.com/max-wittig/gitlab-languages/blob/master/LICENSE)\n\nUtility to generate a Prometheus data source text file for your GitLab instance\nusing the [GitLab Language API](https://docs.gitlab.com/ee/api/projects.html#languages)\n\n## installation from PyPI\n\n1. Install from PyPI as CLI\n\n   ```bash\n   pip install -U gitlab-languages\n   ```\n\n1. Run the program\n\n   ```bash\n   gitlab-languages --cache cache.json --args owned=True # more info about usage: see below\n   ```\n\n## installation from source\n\n1. Install python dependencies\n\n    ```bash\n    poetry install\n    ```\n\n1. Set the required environment variables\n\n    ```bash\n    export GITLAB_TOKEN=<SOME_TOKEN_WITH_API_SCOPE>\n    export GITLAB_URL=https://gitlab.com # optional, defaults to https://gitlab.com\n    # optional:\n    export WORKER_COUNT=24\n    ```\n\n1. Run the tool\n\n    ```bash\n    gitlab-languages\n    ```\n\n## usage\n\n```plain\nusage: gitlab_languages [-h] [--project_limit PROJECT_LIMIT]\n                        [--args ARGS [ARGS ...]]\n                        [--groups GROUPS [GROUPS ...]]\n                        [--ignore_groups IGNORE_GROUPS [IGNORE_GROUPS ...]]\n                        [--cache CACHE] [-o OUTPUT]\n\noptional arguments:\n  -h, --help            show this help message and exit\n  --project_limit PROJECT_LIMIT\n                        Set project limit to scan\n  --args ARGS [ARGS ...]\n                        Provide custom args to the GitLab API\n  --groups GROUPS [GROUPS ...]\n                        Scan only certain groups\n  --ignore_groups IGNORE_GROUPS [IGNORE_GROUPS ...]\n                        Ignore certain groups and their projects\n  --cache CACHE         Cache file to use\n  -o OUTPUT, --output OUTPUT\n                        Location of the metrics file output\n```\n\n### additional arguments\n\nYou can specify additional arguments, that will be directly supplied to the\n[python-gitlab library](https://github.com/python-gitlab/python-gitlab) or to the GitLab API endpoint.\nExample:\n\n```bash\ngitlab-languages --args owned=True\n```\n\nMore info about the available additional args can be found here:\n\n* http://python-gitlab.readthedocs.io/en/stable/\n* https://docs.gitlab.com/ee/api/\n\n### example output\n\nThe output will look something like this:\n\n```plain\nmetrics.txt\n\n# HELP languages_percent Languages scanned in percent\n# TYPE languages_percent gauge\nlanguages_percent{language="Java"} 11.73\nlanguages_percent{language="CSS"} 1.97\nlanguages_percent{language="TypeScript"} 3.5\nlanguages_percent{language="HTML"} 6.14\nlanguages_percent{language="JavaScript"} 17.16\nlanguages_percent{language="Python"} 10.4\nlanguages_percent{language="Modelica"} 3.7\nlanguages_percent{language="TeX"} 1.64\nlanguages_percent{language="Shell"} 6.35\nlanguages_percent{language="Batchfile"} 0.76\nlanguages_percent{language="HCL"} 7.15\nlanguages_percent{language="BitBake"} 0.56\nlanguages_percent{language="C"} 5.25\nlanguages_percent{language="C++"} 0.72\nlanguages_percent{language="Matlab"} 2.77\nlanguages_percent{language="TXL"} 0.05\nlanguages_percent{language="Objective-C"} 1.48\nlanguages_percent{language="XSLT"} 1.68\nlanguages_percent{language="Perl"} 1.71\nlanguages_percent{language="Ruby"} 0.03\nlanguages_percent{language="C#"} 10.3\nlanguages_percent{language="PowerShell"} 0.11\nlanguages_percent{language="Pascal"} 0.01\nlanguages_percent{language="ASP"} 0.0\nlanguages_percent{language="PLpgSQL"} 0.0\nlanguages_percent{language="Makefile"} 2.06\nlanguages_percent{language="SQLPL"} 0.0\nlanguages_percent{language="Puppet"} 0.0\nlanguages_percent{language="Groovy"} 2.56\nlanguages_percent{language="M4"} 0.01\nlanguages_percent{language="Roff"} 0.15\nlanguages_percent{language="CMake"} 0.01\nlanguages_percent{language="NSIS"} 0.01\nlanguages_percent{language="PHP"} 0.0\nlanguages_percent{language="Go"} 0.0\nlanguages_percent{language="Smalltalk"} 0.02\nlanguages_percent{language="Visual Basic"} 0.0\nlanguages_percent{language="Smarty"} 0.0\n# HELP languages_scanned_total Total languages scanned\n# TYPE languages_scanned_total gauge\nlanguages_scanned_total 38.0\n# HELP projects_scanned_total Total projects scanned\n# TYPE projects_scanned_total gauge\nprojects_scanned_total 61.0\n# HELP projects_skipped_total Total projects skipped\n# TYPE projects_skipped_total gauge\nprojects_skipped_total 0.0\n# HELP projects_no_language_total Projects without language detected\n# TYPE projects_no_language_total gauge\nprojects_no_language_total 39.0\n# HELP groups_scanned_total Total groups scanned\n# TYPE groups_scanned_total gauge\ngroups_scanned_total 0.0\n```\n\nRun the script via GitLab CI with schedules and export the metrics.txt file as GitLab pages.\nThen you can add it to your Prometheus instance as scrape source.\n',
    'author': 'Max Wittig',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/max-wittig/gitlab-languages',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
