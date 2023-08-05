# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ampel',
 'ampel.nuclear.flexfit',
 'ampel.nuclear.t0',
 'ampel.nuclear.t2',
 'ampel.nuclear.t3',
 'ampel.nuclear.test']

package_data = \
{'': ['*']}

install_requires = \
['ampel-hu-astro[slack,sncosmo]>=0.8.3a2,<0.8.4',
 'ampel-ztf>=0.8.3a7,<0.8.4',
 'corner>=2.2.1,<3.0.0',
 'dropbox>=11.36.0,<12.0.0']

setup_kwargs = {
    'name': 'ampel-nuclear',
    'version': '0.8.3a5',
    'description': 'Astronomy units for the Ampel system to analyze nuclear events like TDEs',
    'long_description': "# Ampel-nuclear\nCentral repository to host AMPEL code to search for and analyze nuclear transients. At the moment, this is exclusively code from the ZTFbh science working group.\n\n## Installation\n### Prerequisites\nYou need to export environment variables for the [AMPEL ZTF archive](https://ampelproject.github.io/astronomy/ztf/index) (tokens are available [here](https://ampel.zeuthen.desy.de/live/dashboard/tokens)), for [Fritz](https://fritz.science/), and for the dropbox API (ask Sjoert). \n\nFurthermore, you need a running instance of [MongoDB](https://www.mongodb.com/docs/manual/installation/). On macOS, make sure you have the command line tools installed (in doubt, run `xcode-select –install`).\n\n### Setup\nCreate a fresh Python 3.10 conda env\n```\nconda create -n tde_filter_upgrade python=3.10\nconda activate tde_filter_upgrade\n```\nInstall is done via poetry:\n```\npip install poetry \ngit clone https://github.com/AmpelProject/ampel-nuclear\ncd Ampel-nuclear\npoetry install\n```\nNow we have to build the ampel config and install it in the conda env. Issue\n```\nampel config install\n```\nNote: this will throw some import errors, but you can ignore these because those packages are not needed locally. \n\nNow you need to export the following tokens\n```\nexport AMPEL_ARCHIVE_TOKEN='' \nexport DROPBOX_TOKEN=''\nexport FRITZ_TOKEN=''\n```\n\n## Test\nTo run the test, start your local MongoDB. And then issue\n\n```\n./run_tde_scan.py -i\n```\n\nIf you cannot execute the file, issue `chmod +x run_tde_scan.py`.\n\nNote: To push the result of a run to the dropbox, add `-p`.\n\nThe `-i` initiates (and saves) a new archive API stream token. To request one day, use `-d YYYY-MM-DD` for a certain day. The script will request alerts for the 24 hours after this date.\n\nYour can also use `--daysago n` to scan the last `n` days. \n\nNote: When requesting a full day with `-d` or the last `n` days with `--daysago n` from the archive, the first run will probably fail, as the archive database has not fully ramped up yet (`URL is locked`). In this case, just rerun `./run_tde_scan.py`, without any parameters except for `-p` if you want to enable dropbox-push to prevent requesting a new stream token and overwriting the current one until the archive starts serving alerts (you will see them getting ingested).\n\nTo check the output, go to the `temp` directory that gets created when script is run without `-p` (push to dropbox), or check the dropbox.\n\nTo see all available commands of the test script, run `./run_tde_scan.py -h`.\n\n### Examples\n```\n./run_tde_scan.py -i --daysago 4 -p\n\n```\n\nThis will perform a search for the last 4 days and push the results to the dropbox.\n```\n./run_tde_scan.py -i -d 2022-10-06\n\n```\nThis will perform a search for October 6, 2022 and save the result in a local directory.\n",
    'author': 'Valery Brinnel',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://ampelproject.github.io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
