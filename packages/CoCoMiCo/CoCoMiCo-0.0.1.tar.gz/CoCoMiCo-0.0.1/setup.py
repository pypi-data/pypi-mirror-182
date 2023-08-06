# -*- coding: utf-8 -*-

# Copyright (C) 2022 Maxime Lecomte - David Sherman - Clémence Frioux - Inria BSO - Pleiade
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from setuptools import setup
import CoCoMiCo

setup(
    name             = 'CoCoMiCo',
    version          = CoCoMiCo.__version__,
    url              = 'https://gitlab.inria.fr/mlecomte/CoCoMiCo',
    download_url     = f'https://gitlab.inria.fr/mlecomte/CoCoMiCo/tarball/{CoCoMiCo.__version__}',
    license          = 'GPLv3+',
    description      = 'COoperation and COmpetition potentials in MIcrobial COmunities',
    long_description = '',
    author           = 'Maxime lecomte',
    author_email     = 'maxime.lecomte@inria.fr,clemence.frioux@inria.fr',
    classifiers      =[
                            'Programming Language :: Python :: 3.8',
                            'Operating System :: MacOS :: MacOS X',
                            'Operating System :: Unix',
                        ],
    packages         = ['CoCoMiCo'],
    package_dir      = {'CoCoMiCo' : 'CoCoMiCo'},
    package_data     = {'CoCoMiCo' : ['src/encodings/score.lp']},
    #scripts          = ['menetools/menecof.py','menetools/menescope.py','menetools/menepath.py','menetools/menecheck.py'],
    # entry_points     = {'console_scripts': ['mene = menetools.__main__:main']},
    install_requires = ['clyngor_with_clingo']
)