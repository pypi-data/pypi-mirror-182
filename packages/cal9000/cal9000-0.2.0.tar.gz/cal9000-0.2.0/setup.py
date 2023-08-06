# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cal9000', 'cal9000.render']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['cal9000 = cal9000.__main__:main']}

setup_kwargs = {
    'name': 'cal9000',
    'version': '0.2.0',
    'description': 'Vim enabled version of cal(1)',
    'long_description': "# cal9000\n\nVim enabled version of [cal(1)](https://linux.die.net/man/1/cal).\n\n## Why?\n\nI want to get better about using calendars, but I don't like the thought of\nusing an online one. I also wanted something that I could use from the CLI\nwith ease, and be very effecient with it.\n\n## Installing and Running\n\n```\n$ pip install cal9000\n$ cal9000\n```\n\n## Usage\n\nIn short, the following Vim keybindings are supported:\n\n| Key(s)     | Action |\n|------------|--------|\n| `q`        | Quit |\n| `h`        | Go to previous day |\n| `j`        | Go to next week |\n| `J`        | Go 4 weeks forward |\n| `k`        | Go to last week |\n| `K`        | Go 4 weeks back |\n| `l`        | Go to next day |\n| `u`        | Go to to today |\n| `i`        | Insert an item/event |\n| `x`        | Delete an event or item |\n| `g`        | Open event manager |\n| `o`        | Open the selected day |\n| `?`        | Open help menu |\n| `:command` | Run the command `command`, see below for supported commands |\n| *count*`verb` | Run `verb` (`h`/`j`/`k`/`l`, etc) `count` times |\n\n## Commands\n\nCurrently supported commands are:\n\n| Command       | Description |\n|---------------|-------------|\n| `h` or `help` | Open help dialog |\n| `q` or `quit` | Quit cal9000 |\n| *number*      | Go to day *number* of the current month |\n\n## Configuration\n\nTBD\n\n## Testing\n\n```\n$ git clone https://github.com/dosisod/cal9000\n$ cd cal9000\n$ python3 -m virtualenv .venv\n$ source .venv/bin/activate\n$ pip3 install -r dev-requirements.txt\n```\n",
    'author': 'dosisod',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/dosisod/cal9000',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
}


setup(**setup_kwargs)
