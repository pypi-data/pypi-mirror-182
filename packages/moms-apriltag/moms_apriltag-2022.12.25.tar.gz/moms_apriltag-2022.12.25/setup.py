# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['moms_apriltag', 'moms_apriltag.tags']

package_data = \
{'': ['*']}

install_requires = \
['numpy']

setup_kwargs = {
    'name': 'moms-apriltag',
    'version': '2022.12.25',
    'description': 'Generate apriltags and calibration targets',
    'long_description': '![](https://github.com/MomsFriendlyRobotCompany/moms_apriltag/blob/master/example/apriltag_target.png?raw=true)\n\n# Apriltag Camera Calibration Board Generator\n![CheckPackage](https://github.com/MomsFriendlyRobotCompany/moms_apriltag/workflows/CheckPackage/badge.svg)\n![GitHub](https://img.shields.io/github/license/MomsFriendlyRobotCompany/moms_apriltag)\n[![Latest Version](https://img.shields.io/pypi/v/moms_apriltag.svg)](https://pypi.python.org/pypi/moms_apriltag/)\n[![image](https://img.shields.io/pypi/pyversions/moms_apriltag.svg)](https://pypi.python.org/pypi/moms_apriltag)\n[![image](https://img.shields.io/pypi/format/moms_apriltag.svg)](https://pypi.python.org/pypi/moms_apriltag)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/moms_apriltag?color=aqua)\n\nWhy? There didn\'t really seem to be an easy way to do this IMHO.\n\n## Install\n\n```\npip install moms_apriltag\n```\n\n## Usage\n\nSee the jupyter notebook in `example/examples.ipynb` for how to use this.\n\nThis package create a simple numpy image that can then be saved\nto a PNG or JPEG image and printed. For circular or custom tags,\nthere is a `toRGBA()` function to save the tag to a `png` using\nany image library that can accept `numpy` array images.\n\nSupported families are shown in the table below:\n\n| Family    | Generation | Hamming | Size | Data Bits | Unique Tags |\n|-----------|------------|---------|------|-----------|-------------|\n| `tag16h5` | 2          | 5       | 4x4  | 16        | 30\n| `tag25h9` | 2          | 9       | 5x5  | 25        | 35\n| `tag36h10`| 2          | 10      | 5x5  | 36        | 2,320\n| `tag36h11`| 2          | 11      | 5x5  | 36        | 587\n| `tagCircle21h7`| 3     | 7       | 9x9  | 36        | 38\n| `tagCircle49h12`| 3    | 12      | 11x11| 49        | 65,535\n| `tagCustom48h12`| 3    | 12      | 10x10| 48        | 42,211\n| `tagStandard41h12`| 3  | 12      | 9x9  | 41        | 2,115\n| `tagStandard52h13`| 3  | 13      | 10x10| 52        | 48,714\n\n[ref](https://optitag.io/blogs/news/designing-your-perfect-apriltag)\n\n```python\n#!/usr/bin/env python3\nimport moms_apriltag as apt\nimport imageio\n\n\nif __name__ == \'__main__\':\n    family = "tag36h10"\n    shape = (6,8)\n    filename = "apriltag_target.png"\n    size = 50\n\n    tgt = apt.board(shape, family, size)\n    imageio.imwrite(filename, tgt)\n```\n\n```python\n# for AprilTag v2\nfrom moms_apriltags import TagGenerator2\nfrom matplotlib import pyplot as plt\n\ntg = TagGenerator3("tag16h5")\ntag = tg.generate(4)\n\nplt.imshow(tag, cmap="gray)\n```\n\n```python\n# for AprilTag v3\nfrom moms_apriltags import TagGenerator3\nfrom matplotlib import pyplot as plt\n\ntg = TagGenerator3("tagStandard41h12")\ntag = tg.generate(137)\n\nplt.imshow(tag, cmap="gray)\n```\n\n# Todo\n\n- [ ] refactor board code\n- [ ] enable apriltag v3 markers in board\n\n# MIT License\n\n**Copyright (c) 2020 Kevin J. Walchko**\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.\n',
    'author': 'walchko',
    'author_email': 'walchko@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://pypi.org/project/apriltag_gen/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
