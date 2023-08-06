Planetary coverage package
==========================

<img src="https://docs.planetary-coverage.org/en/1.0.0/_static/planetary-coverage-logo.svg" align="right" hspace="50" vspace="50" height="200" alt="Planetary coverage logo">

[
    ![CI/CD](https://juigitlab.esac.esa.int/python/planetary-coverage/badges/main/pipeline.svg)
    ![Coverage](https://juigitlab.esac.esa.int/python/planetary-coverage/badges/main/coverage.svg)
](https://juigitlab.esac.esa.int/python/planetary-coverage/pipelines/main/latest)
[
    ![Documentation Status](https://readthedocs.org/projects/planetary-coverage/badge/?version=latest)
](https://readthedocs.org/projects/planetary-coverage/builds/)

[
    ![Latest version](https://img.shields.io/pypi/v/planetary-coverage.svg?label=Latest%20release&color=lightgrey)
](https://juigitlab.esac.esa.int/python/planetary-coverage/-/tags)
[
    ![License](https://img.shields.io/pypi/l/planetary-coverage.svg?color=lightgrey&label=License)
](https://juigitlab.esac.esa.int/python/planetary-coverage/-/blob/main/LICENSE.md)
[
    ![PyPI](https://img.shields.io/badge/PyPI-planetary--coverage-blue?logo=Python&logoColor=white)
    ![Python](https://img.shields.io/pypi/pyversions/planetary-coverage.svg?label=Python&logo=Python&logoColor=white)
](https://docs.planetary-coverage.org/pypi)

[
    ![Docs](https://img.shields.io/badge/Docs-planetary--coverage.univ--nantes.fr-blue?&color=orange&logo=Read%20The%20Docs&logoColor=white)
](https://docs.planetary-coverage.org)
[
    ![DataLab](https://img.shields.io/badge/Datalab-datalabs.esa.int-blue?&color=orange&logo=Jupyter&logoColor=white)
](https://docs.planetary-coverage.org/datalab)
[
    ![Software Heritage](https://archive.softwareheritage.org/badge/origin/https://juigitlab.esac.esa.int/python/planetary-coverage/)
](https://docs.planetary-coverage.org/swh)

---

The [planetary-coverage](https://docs.planetary-coverage.org)
package is a toolbox to perform surface coverage analysis based on orbital trajectory calculations.
Its main intent is to provide an easy way to compute observation
opportunities of specific region of interest above the Galilean
satellites for the ESA-JUICE mission but could be extended in the
future to other space mission.

It is actively developed by the
[Observatoire des Sciences de l'Univers Nantes Atlantique](https://osuna.univ-nantes.fr)
(OSUNA, CNRS-UAR 3281) and the
[Laboratory of Planetology and Geosciences](https://lpg-umr6112.fr)
(LPG, CNRS-UMR 6112) at Nantes University (France), under
[ESA-JUICE](https://sci.esa.int/web/juice) and [CNES](https://cnes.fr) founding support.

<p align="center">
  <img src="https://docs.planetary-coverage.org/en/1.0.0/_images/logos.png" alt="logos"/>
</p>

📦 Installation
---------------

The package is available on [PyPI](https://pypi.org/project/planetary-coverage/) and can be installed very easily:

- If you are in a [`Jupyter environnement`](https://jupyter.org/), you can use the magic command `%pip` in a notebook cell and ▶️ `Run` it:
```bash
%pip install --upgrade planetary-coverage
```

- or, if you are using a `terminal environment`, you can do:
```bash
pip install --upgrade planetary-coverage
```

> __Note:__ If you plan to use this package with JUICE and you want to enable [PTR simulation with AGM](https://esa-ptr.readthedocs.io/).
> You can add a `juice` extra parameter in the `pip` install command: `pip install planetary-coverage[juice]`


✏️ How to cite this package
---------------------------

If you use this package for your analyses, please consider using the following citation:

> Seignovert et al. 2023,
> Planetary coverage package (1.0.0),
> [planetary-coverage.org](https://docs.planetary-coverage.org/en/1.0.0/),
> [swh:1:rel:3900e871fe34fdeead5a4d8d6b3aa86a063e82df](https://archive.softwareheritage.org/browse/origin/directory/?origin_url=https://juigitlab.esac.esa.int/python/planetary-coverage&release=1.0.0)

or can use this 📙 [BibTeX file](https://juigitlab.esac.esa.int/python/planetary-coverage/-/raw/main/planetary-coverage.bib?inline=false).


⚡️ Issues and 💬 feedback
-------------------------

If you have any issue with this package, we highly recommend to take a look at:

- 📚 our [extended documentation online](https://docs.planetary-coverage.org/).
- 📓 the collection of [notebook examples](https://juigitlab.esac.esa.int/notebooks/planetary-coverage).

If you did not find a solution there, feel free to:

- 📝 [open an issue](https://juigitlab.esac.esa.int/python/planetary-coverage/-/issues/new) (if you have an account on the [JUICE Gitlab](https://juigitlab.esac.esa.int/python/planetary-coverage)).
- ✉️ send us an email at [&#99;&#111;&#110;&#116;&#97;&#99;&#116;&#64;&#112;&#108;&#97;&#110;&#101;&#116;&#97;&#114;&#121;&#45;&#99;&#111;&#118;&#101;&#114;&#97;&#103;&#101;&#46;&#111;&#114;&#103;](&#109;&#97;&#105;&#108;&#116;&#111;&#58;&#99;&#111;&#110;&#116;&#97;&#99;&#116;&#64;&#112;&#108;&#97;&#110;&#101;&#116;&#97;&#114;&#121;&#45;&#99;&#111;&#118;&#101;&#114;&#97;&#103;&#101;&#46;&#111;&#114;&#103;
)


🎨 Contribution and 🐛 fix bugs
-------------------------------

Contributions are always welcome and appreciated.
An account on the [JUICE Giltab](https://juigitlab.esac.esa.int/python/planetary-coverage) is required.
You also need to install the latest version of [Poetry](https://python-poetry.org/docs/) (`≥1.2`), for example on _Linux/macOS_, you can run this command:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Then you are good to go!

1. 🍴 [Fork this project](https://juigitlab.esac.esa.int/python/planetary-coverage/-/forks/new)

2. 🐑 Clone and 📦 install the repository locally:

```bash
git clone https://juigitlab.esac.esa.int/<YOUR_USERNAME>/planetary-coverage
cd planetary-coverage

poetry install --extras juice
```

3. ✍️ Make your edits and 🚧 write the tests.

4. 🚦 Double-check that the linters are happy 😱 🤔 😃 :
```bash
poetry run flake8 src/ tests/ docs/conf.py
poetry run pylint src/ tests/
```

5. 🛠 Check that your tests succeed 👍 and you have a coverage of 100% ✨ :

```bash
poetry run pytest
```

6. 📖 Complete and ⚙️ build the documentation (if needed):
```bash
cd docs/
poetry run make docs
```

7. 📤 Push your changes to your forked branch and 🚀 open a [new merge request](https://juigitlab.esac.esa.int/python/planetary-coverage/-/merge_requests/new) explaining what you changed 🙌 👏 💪.
