# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cmake_presets']

package_data = \
{'': ['*']}

install_requires = \
['dataclasses-json>=0.5.7,<0.6.0', 'pytest>=7.2.0,<8.0.0']

entry_points = \
{'pytest11': ['cmake-presets = cmake_presets']}

setup_kwargs = {
    'name': 'pytest-cmake-presets',
    'version': '0.0.0.dev0',
    'description': 'Execute CMake Presets via pytest',
    'long_description': '# Overview\n\n`pytest-cmake-presets` was written to find and "test" [cmake-presets(7)][1] as\npart of the [IXM][2] test harness. Each test is a single CMake preset that\nmight be part of a larger project. There are two aspects to tests: running\npresets directly, and then testing the layout/result of the\n[cmake-file-api(7)][3] after the fact. These second tests are performed via\nnormal pytest functions.\n\nTests can use the `vendor.pytest-cmake-presets` field to modify the expected\noutcome of some tests.\n\nSpecifically, fields like `pass-regex`, `will-fail`, etc., can all modify the\nbehavior of an executed `CMakePresetItem`, allowing for *some* behavior to be\nmodified in a data-oriented fashion, instead of requiring pytest fixtures to\nexecute.\n\n[1]: https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html\n[2]: https://github.com/ixm-one/ixm\n[3]: https://cmake.org/cmake/help/latest/manual/cmake-file-api.7.html\n',
    'author': 'Izzy Muerte',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
