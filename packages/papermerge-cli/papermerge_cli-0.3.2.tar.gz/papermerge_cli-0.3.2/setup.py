# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['papermerge_cli']

package_data = \
{'': ['*']}

install_requires = \
['backoff>=2.2.1,<3.0.0',
 'click>=8.1.3,<9.0.0',
 'papermerge-restapi-client>=1.0.34,<2.0.0',
 'rich>=12.6.0,<13.0.0']

entry_points = \
{'console_scripts': ['papermerge-cli = papermerge_cli.main:cli']}

setup_kwargs = {
    'name': 'papermerge-cli',
    'version': '0.3.2',
    'description': 'Command line utility for your Papermerge DMS instance',
    'long_description': "# Papermerge Cli\n\nCommand line utility which uses REST API to interact with your Papermerge DMS\ninstance. You can use `papermerge-cli`, for example, to recursively import local folder to\nyour Papermerge DMS instance.\n\n## Requirements\n\nIn order to use `papermerge-cli` you need to have python installed.\nYou need [python](https://www.python.org/) version >= 3.10.\n\n## Install\n\n    $ pip install papermerge-cli\n\n[pip](https://pypi.org/project/pip/) is package installer for python - it usually comes with python\ninterpreter. In order to install `pip` on Ubuntu use following command:\n\n    $ sudo apt install python3-pip\n\n## Usage\n\nGet you REST API authentication token from your instance:\n\n    $ papermerge-cli --host=https://mydms.some-vps.com auth\n\nOr you can provide host as environment variable:\n\n    $ export PAPERMERGE_CLI__HOST=https://mydms.some-vps.com\n    $ papermerge-cli auth\n\nPapermerge Cli will prompt you for username and password. On successfull\nauthentication your REST API token will be displayed - now you can use\nthis token for all subsequent authentications.\n\nUse token for authentication by exporting token as `PAPERMERGE_CLI__TOKEN`\nenvironment variable:\n\n    $ export PAPERMERGE_CLI__TOKEN=mytoken\n\n### list\n\nNow, with `PAPERMERGE_CLI__HOST` and `PAPERMERGE_CLI__TOKEN` environment\nvariables set you can use list content of you home folder:\n\n    $ papermerge-cli list\n\nIn order to list content of specific folder (including inbox folder):\n\n    $ papermerge-cli list --parent-uuid=UUID-of-the-folder\n\n### me\n\nIn order to see current user details (current user UUID, home folder UUID, inbox\nfolder UUID, username etc):\n\n    $ papermerge-cli me\n\n### pref-list\n\nList all preferences:\n\n    $ papermerge-cli pref-list\n\nList specific section of the preferences\n\n    $ papermerge-cli pref-list --section=ocr\n\nShow value of preference `trigger` from section `ocr`:\n\n    $ papermerge-cli pref-list --section=ocr --name=trigger\n\n### pref-update\n\nUpdate value of the preference `trigger` from section `ocr`:\n\n    $ papermerge-cli pref-update --section=ocr --name=trigger --value=auto\n\n### import\n\nRecursively imports folder from local filesystem. For example, in order\nto import recursively all documents from local folder:\n\n    $ papermerge-cli import /path/to/local/folder/\n\nYou can also import one single document\n\n    $ papermerge-cli import /path/to/some/document.pdf\n\nIf you want the local copy the uploaded documents **to be deleted** after\nsuccessful import - add `--delete` flag:\n\n    $ papermerge-cli import --delete /path/to/folder/\n\nPLEASE BE CAREFUL WITH `--delete` FLAG AS IT WILL IRREVERSIBLE DELETE THE LOCAL\nCOPY OF THE UPLOADED DOCUMENT!\n\n### search\n\nSearch for node (document or folder) by text or by tags:\n\n    $ papermerge-cli search -q apotheke\n\nReturns all documents (or folders with such title) containing OCRed\ntext 'apotheke'.\n\nYou can search by tags only:\n\n    $ papermerge-cli search --tags important\n\nWill search for all documents (and folders) which were tagged with\ntag 'important' When multiple tags are provided, by default, will search for\nnodes with all mentioned tags:\n\n    $ papermerge-cli search --tags important,letters  # returns nodes with both tags important AND letters\n\nIn case you want to search for nodes with ANY of the provided tags, use\n`tags-op` parameter:\n\n    $ papermerge-cli search --tags important,letters --tags-op any\n\nFinally, `tags` and `q` may be combined:\n\n    $ papermerge-cli search --tags important -q apartment\n\n### download\n\nDownloads a folder or a document:\n\n    $ papermerge-cli download --uuid <document or folder uuid>\n\nIn case uuid is the ID of specific folder - a zip file will be downloaded; zip\nfile will contain all nodes insides specified folder.\n\nYou can use `--uuid` multiple times:\n\n    $ papermerge-cli download --uuid <uuid of doc1> --uuid <uuid of doc2> --uuid <uuid of folder 1>\n\nIf you want to download content to specific file on your file-system, use `-f`\noption:\n\n    $ papermerge-cli download --uuid <doc-uuid> -f /path/to/file-system/document.pdf\n\nor in case of uuid is a folder:\n\n    $ papermerge-cli download --uuid <folder-uuid>  -f /path/to/file-system/folder.zip\n\nYou can also specify the format/type of the downloaded archive (e.g. in case node is either a folder):\n\n     $ papermerge-cli download --uuid <folder-uuid>  -f /path/to/file-system/folder.targz -t targz\n",
    'author': 'Eugen Ciur',
    'author_email': 'eugen@papermerge.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
