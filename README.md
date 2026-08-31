# Venus Foam

[![Code DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22148026.svg)](https://doi.org/10.5281/zenodo.22148026)
[![Preprint DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22148407.svg)](https://doi.org/10.5281/zenodo.22148407)

Engineering analysis of a modular floating station concept in the cloud layer
of Venus (55.7 km). Every number is either computed from physical constants
or cited to a real source/precedent — not a pitch, a worked calculation.

- **[venus-foam.md](venus-foam.md)** — English translation, base filename.
- **[venus-foam-ru.md](venus-foam-ru.md)** — Russian original, the primary
  working document; all edits and calculations start here, English is
  synced from it.
- **[venus_calc/verify.py](venus_calc/verify.py)** — the source of truth for
  every number in the documents. Recomputes everything from scratch:
  `python3 venus_calc/verify.py`.
- **[preprint/](preprint/)** — PDF build pipeline (`build_preprint.py`,
  `make_figures.py`, `header.tex`) and figures. Compiled PDFs are not
  tracked in this repo (see `.gitignore`) — the archived preprint lives on
  Zenodo, cross-linked from here. To build locally:
  ```
  python3 preprint/build_preprint.py venus-foam-ru.md        # RU
  python3 preprint/build_preprint.py venus-foam.md --en       # EN
  ```
  Requires `pandoc`, `xelatex`, DejaVu fonts, and a Russian hyphenation
  package for the RU build.

Code comments and the project's own working notes (`CLAUDE.md`) are in
Russian; the documents themselves are maintained in both languages.

## License

[MIT](LICENSE).
