# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
# SPDX-License-Identifier: MPL-2.0
"""

#!/usr/bin/env bash
python3 setup.py sdist
twine upload dist/GridCal-2.30.tar.gz

"""
import os
from GridCalEngine.__version__ import __GridCalEngine_VERSION__
from GridCal.__version__ import __GridCal_VERSION__
from GridCalServer.__version__ import __GridCalServer_VERSION__
from gridcal_packaging import build_wheel

if __name__ == "__main__":

    if __GridCalEngine_VERSION__ == __GridCal_VERSION__:  # both packages' versions must be exactly the same

        _long_description = "# GridCal \n"
        _long_description += "This software aims to be a complete platform for power systems research and simulation.)\n"
        _long_description += "\n"
        _long_description += "[Watch the video https](https://youtu.be/SY66WgLGo54)\n"
        _long_description += "[Check out the documentation](https://gridcal.readthedocs.io)\n"
        _long_description += "\n"
        _long_description += "## Installation\n"
        _long_description += "\n"
        _long_description += "pip install GridCalEngine\n"
        _long_description += "\n"
        _long_description += "For more options (including a standalone setup one), follow the\n"
        _long_description += "[installation instructions]( https://gridcal.readthedocs.io/en/latest/getting_started/install.html)\n"
        _long_description += "from the project's [documentation](https://gridcal.readthedocs.io)\n"

        _description_content_type = 'text/markdown'

        _summary = 'GridCal is a Power Systems simulation program intended for professional use and research'

        _keywords = 'power systems planning'

        _author = 'Santiago Peñate Vera et. Al.'

        _author_email = 'santiago@gridcal.org'

        _home_page = 'https://github.com/SanPen/GridCal'

        _classifiers_list = [
            'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
            'Programming Language :: Python :: 3.10',
        ]

        _requires_pyhon = '>=3.6'

        _provides_extra = 'gch5 files'

        _license_ = 'MPL2'

        build_wheel(pkg_name='GridCalEngine',
                    setup_path=os.path.join('GridCalEngine', 'setup.py'),
                    version=__GridCalEngine_VERSION__,
                    summary=_summary,
                    home_page=_home_page,
                    author=_author,
                    email=_author_email,
                    license_=_license_,
                    keywords=_keywords,
                    classifiers_list=_classifiers_list,
                    requires_pyhon=_requires_pyhon,
                    description_content_type=_description_content_type,
                    provides_extra=_provides_extra,
                    long_description=_long_description
                    )

        build_wheel(pkg_name='GridCalServer',
                    setup_path=os.path.join('GridCalServer', 'setup.py'),
                    version=__GridCalServer_VERSION__,
                    summary=_summary,
                    home_page=_home_page,
                    author=_author,
                    email=_author_email,
                    license_=_license_,
                    keywords=_keywords,
                    classifiers_list=_classifiers_list,
                    requires_pyhon=_requires_pyhon,
                    description_content_type=_description_content_type,
                    provides_extra=_provides_extra,
                    long_description=_long_description
                    )

        build_wheel(pkg_name='GridCal',
                    setup_path=os.path.join('GridCal', 'setup.py'),
                    version=__GridCal_VERSION__,
                    summary=_summary,
                    home_page=_home_page,
                    author=_author,
                    email=_author_email,
                    license_=_license_,
                    keywords=_keywords,
                    classifiers_list=_classifiers_list,
                    requires_pyhon=_requires_pyhon,
                    description_content_type=_description_content_type,
                    provides_extra=_provides_extra,
                    long_description=_long_description,
                    ext_filter=['py'],
                    extra_files=[
                        os.path.join("data", "cables.csv"),
                        os.path.join("data", "GridCal.ico"),
                        os.path.join("data", "GridCal.svg"),
                        os.path.join("data", "sequence_lines.csv"),
                        os.path.join("data", "transformers.csv"),
                        os.path.join("data", "wires.csv")
                    ]
                    )

    else:

        print(__GridCalEngine_VERSION__, 'and', __GridCal_VERSION__, "are different :(")
