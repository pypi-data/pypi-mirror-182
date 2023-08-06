# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['planetary_coverage',
 'planetary_coverage.cli',
 'planetary_coverage.debug',
 'planetary_coverage.esa',
 'planetary_coverage.events',
 'planetary_coverage.html',
 'planetary_coverage.maps',
 'planetary_coverage.math',
 'planetary_coverage.misc',
 'planetary_coverage.projections',
 'planetary_coverage.rois',
 'planetary_coverage.spice',
 'planetary_coverage.ticks',
 'planetary_coverage.trajectory']

package_data = \
{'': ['*'],
 'planetary_coverage.maps': ['data/*'],
 'planetary_coverage.rois': ['data/*']}

install_requires = \
['Pillow>=9.2.0,<10.0.0',
 'matplotlib>=3.6.0,<4.0.0',
 'numpy>=1.23.0,<2.0.0',
 'spiceypy>=5.1.1,<6.0.0']

extras_require = \
{'juice': ['esa-ptr>=1.0,<2.0']}

entry_points = \
{'console_scripts': ['kernel-download = '
                     'planetary_coverage.cli:cli_kernel_download',
                     'mk-download = '
                     'planetary_coverage.cli:cli_metakernel_download']}

setup_kwargs = {
    'name': 'planetary-coverage',
    'version': '1.0.0',
    'description': 'Planetary coverage package',
    'long_description': 'Planetary coverage package\n==========================\n\n<img src="https://docs.planetary-coverage.org/en/1.0.0/_static/planetary-coverage-logo.svg" align="right" hspace="50" vspace="50" height="200" alt="Planetary coverage logo">\n\n[\n    ![CI/CD](https://juigitlab.esac.esa.int/python/planetary-coverage/badges/main/pipeline.svg)\n    ![Coverage](https://juigitlab.esac.esa.int/python/planetary-coverage/badges/main/coverage.svg)\n](https://juigitlab.esac.esa.int/python/planetary-coverage/pipelines/main/latest)\n[\n    ![Documentation Status](https://readthedocs.org/projects/planetary-coverage/badge/?version=latest)\n](https://readthedocs.org/projects/planetary-coverage/builds/)\n\n[\n    ![Latest version](https://img.shields.io/pypi/v/planetary-coverage.svg?label=Latest%20release&color=lightgrey)\n](https://juigitlab.esac.esa.int/python/planetary-coverage/-/tags)\n[\n    ![License](https://img.shields.io/pypi/l/planetary-coverage.svg?color=lightgrey&label=License)\n](https://juigitlab.esac.esa.int/python/planetary-coverage/-/blob/main/LICENSE.md)\n[\n    ![PyPI](https://img.shields.io/badge/PyPI-planetary--coverage-blue?logo=Python&logoColor=white)\n    ![Python](https://img.shields.io/pypi/pyversions/planetary-coverage.svg?label=Python&logo=Python&logoColor=white)\n](https://docs.planetary-coverage.org/pypi)\n\n[\n    ![Docs](https://img.shields.io/badge/Docs-planetary--coverage.univ--nantes.fr-blue?&color=orange&logo=Read%20The%20Docs&logoColor=white)\n](https://docs.planetary-coverage.org)\n[\n    ![DataLab](https://img.shields.io/badge/Datalab-datalabs.esa.int-blue?&color=orange&logo=Jupyter&logoColor=white)\n](https://docs.planetary-coverage.org/datalab)\n[\n    ![Software Heritage](https://archive.softwareheritage.org/badge/origin/https://juigitlab.esac.esa.int/python/planetary-coverage/)\n](https://docs.planetary-coverage.org/swh)\n\n---\n\nThe [planetary-coverage](https://docs.planetary-coverage.org)\npackage is a toolbox to perform surface coverage analysis based on orbital trajectory calculations.\nIts main intent is to provide an easy way to compute observation\nopportunities of specific region of interest above the Galilean\nsatellites for the ESA-JUICE mission but could be extended in the\nfuture to other space mission.\n\nIt is actively developed by the\n[Observatoire des Sciences de l\'Univers Nantes Atlantique](https://osuna.univ-nantes.fr)\n(OSUNA, CNRS-UAR 3281) and the\n[Laboratory of Planetology and Geosciences](https://lpg-umr6112.fr)\n(LPG, CNRS-UMR 6112) at Nantes University (France), under\n[ESA-JUICE](https://sci.esa.int/web/juice) and [CNES](https://cnes.fr) founding support.\n\n<p align="center">\n  <img src="https://docs.planetary-coverage.org/en/1.0.0/_images/logos.png" alt="logos"/>\n</p>\n\n📦 Installation\n---------------\n\nThe package is available on [PyPI](https://pypi.org/project/planetary-coverage/) and can be installed very easily:\n\n- If you are in a [`Jupyter environnement`](https://jupyter.org/), you can use the magic command `%pip` in a notebook cell and ▶️ `Run` it:\n```bash\n%pip install --upgrade planetary-coverage\n```\n\n- or, if you are using a `terminal environment`, you can do:\n```bash\npip install --upgrade planetary-coverage\n```\n\n> __Note:__ If you plan to use this package with JUICE and you want to enable [PTR simulation with AGM](https://esa-ptr.readthedocs.io/).\n> You can add a `juice` extra parameter in the `pip` install command: `pip install planetary-coverage[juice]`\n\n\n✏️ How to cite this package\n---------------------------\n\nIf you use this package for your analyses, please consider using the following citation:\n\n> Seignovert et al. 2023,\n> Planetary coverage package (1.0.0),\n> [planetary-coverage.org](https://docs.planetary-coverage.org/en/1.0.0/),\n> [swh:1:rel:3900e871fe34fdeead5a4d8d6b3aa86a063e82df](https://archive.softwareheritage.org/browse/origin/directory/?origin_url=https://juigitlab.esac.esa.int/python/planetary-coverage&release=1.0.0)\n\nor can use this 📙 [BibTeX file](https://juigitlab.esac.esa.int/python/planetary-coverage/-/raw/main/planetary-coverage.bib?inline=false).\n\n\n⚡️ Issues and 💬 feedback\n-------------------------\n\nIf you have any issue with this package, we highly recommend to take a look at:\n\n- 📚 our [extended documentation online](https://docs.planetary-coverage.org/).\n- 📓 the collection of [notebook examples](https://juigitlab.esac.esa.int/notebooks/planetary-coverage).\n\nIf you did not find a solution there, feel free to:\n\n- 📝 [open an issue](https://juigitlab.esac.esa.int/python/planetary-coverage/-/issues/new) (if you have an account on the [JUICE Gitlab](https://juigitlab.esac.esa.int/python/planetary-coverage)).\n- ✉️ send us an email at [&#99;&#111;&#110;&#116;&#97;&#99;&#116;&#64;&#112;&#108;&#97;&#110;&#101;&#116;&#97;&#114;&#121;&#45;&#99;&#111;&#118;&#101;&#114;&#97;&#103;&#101;&#46;&#111;&#114;&#103;](&#109;&#97;&#105;&#108;&#116;&#111;&#58;&#99;&#111;&#110;&#116;&#97;&#99;&#116;&#64;&#112;&#108;&#97;&#110;&#101;&#116;&#97;&#114;&#121;&#45;&#99;&#111;&#118;&#101;&#114;&#97;&#103;&#101;&#46;&#111;&#114;&#103;\n)\n\n\n🎨 Contribution and 🐛 fix bugs\n-------------------------------\n\nContributions are always welcome and appreciated.\nAn account on the [JUICE Giltab](https://juigitlab.esac.esa.int/python/planetary-coverage) is required.\nYou also need to install the latest version of [Poetry](https://python-poetry.org/docs/) (`≥1.2`), for example on _Linux/macOS_, you can run this command:\n\n```bash\ncurl -sSL https://install.python-poetry.org | python3 -\n```\n\nThen you are good to go!\n\n1. 🍴 [Fork this project](https://juigitlab.esac.esa.int/python/planetary-coverage/-/forks/new)\n\n2. 🐑 Clone and 📦 install the repository locally:\n\n```bash\ngit clone https://juigitlab.esac.esa.int/<YOUR_USERNAME>/planetary-coverage\ncd planetary-coverage\n\npoetry install --extras juice\n```\n\n3. ✍️ Make your edits and 🚧 write the tests.\n\n4. 🚦 Double-check that the linters are happy 😱 🤔 😃 :\n```bash\npoetry run flake8 src/ tests/ docs/conf.py\npoetry run pylint src/ tests/\n```\n\n5. 🛠 Check that your tests succeed 👍 and you have a coverage of 100% ✨ :\n\n```bash\npoetry run pytest\n```\n\n6. 📖 Complete and ⚙️ build the documentation (if needed):\n```bash\ncd docs/\npoetry run make docs\n```\n\n7. 📤 Push your changes to your forked branch and 🚀 open a [new merge request](https://juigitlab.esac.esa.int/python/planetary-coverage/-/merge_requests/new) explaining what you changed 🙌 👏 💪.\n',
    'author': 'Seignovert et al.',
    'author_email': 'contact@planetary-coverage.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://juigitlab.esac.esa.int/python/planetary-coverage',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
