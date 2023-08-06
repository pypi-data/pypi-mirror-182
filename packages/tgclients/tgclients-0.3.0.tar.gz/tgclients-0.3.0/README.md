<!--
SPDX-FileCopyrightText: 2022 Georg-August-Universität Göttingen

SPDX-License-Identifier: CC0-1.0
-->

# TextGrid Python clients

The TextGrid Python clients provide access to the [TextGrid Repository](https://textgridrep.org/)
services [API](http://textgridlab.org/doc/services/index.html).


## Installation and Usage

```sh
pip install tgclients
```

```python
import tgclients
```

## Development

1. Prerequisites
    - Python > 3.8

1. Create/activate virtual environment (ensure you use the correct python version!).

    ```sh
    python -m venv venv
    . venv/bin/activate
    pip install --upgrade pip
    ```

1. Install requirements.

    ```sh
    pip install -e .[dev]
    ```

1. For the use with repdav, add `-e /path/to/tgclients/source/code` to your requirements or install it manually.

    ```sh
    pip install -e /path/to/tgclients/source/code
    ```

## requirements.txt and requirements.dev.txt

If a requirements.txt is needed, it can be generated out of setup.py with [pip-tools](https://github.com/jazzband/pip-tools#requirements-from-setuppy):

    ```sh
    pip-compile setup.cfg
    ```

If a requirements.txt for the dev dependencies (or a requirements.dev.txt) is needed, enter:

    ```sh
    pip-compile setup.cfg --extra dev --allow-unsafe -o requirements.dev.txt
    ```

## ICU dependency
If you rely on filename_from_metadata() feature you should possibly install PyICU, as this makes sure the same transliteration as in TextGrid
aggregator and TextGridLab is used. Then install with:

    ```sh
    pip install -e .[icu,dev]
    ```

or just

    ```sh
    pip install -e .[icu]
    ```

There is a minimal fallback implememted for use without PyICU, which is only sufficient to pass the integration tests.

## Contributing

Commit convention:

- Use [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/)

Style constraints:

- Code: [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Documentation: [Google style docstrings (Chapter 3.8 from Google styleguide)](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings)

Coding constraints:

- Objects that are not supposed to be used outside the current scope MUST be named starting with `_` (underscore): [PEP 316](https://www.python.org/dev/peps/pep-0316/#id12)

For your convenience, pre-commit hooks are configured to check against these constraints. Provided, you have installed the development requirements (see above), activate `pre-commit` to run on every `git commit`:

```sh
pre-commit install
```

Also, a helper with conventional commits is installed with the development requirements that you could leverage to easily comply with it. Just use `cz c` instead of `git commit`

## Testing

### Unit Tests

```sh
pytest
```

### Integration Tests

For Integration tests create a project in TextGridLab and get a [SessionID](https://textgridlab.org/1.0/Shibboleth.sso/Login?target=/1.0/secure/TextGrid-WebAuth.php?authZinstance=textgrid-esx2.gwdg.de).

Then create a file '.env' containing the following entries:

```sh
SESSION_ID=YOUR-SESSION-ID
PROJECT_ID=YOUR-PROJECT-ID
```

For testing on another TextGrid server than the default production system you may also set the `TEXTGRID_HOST` environment variable.

```sh
set -o allexport; source .env; set +o allexport
pytest --integration
```

to capture print() output (only works if assert failed):

```sh
pytest -o log_cli=true --capture=sys --integration
```

to capture with debug log enabled

```sh
pytest -o log_cli=true --log-cli-level=DEBUG --capture=sys --integration
```

## Databinding
to re-generate the databinding do

```sh
pip install xsdata[cli]
cd src
xsdata https://gitlab.gwdg.de/dariah-de/textgridrep/tg-search/-/raw/main/tgsearch-api/src/main/resources/tgsearch.xsd --package tgclients.databinding --docstring-style Google
```

## Logging

The tgclients log communicaction problems with the services with log level WARNING, to have them visible in Jupyter notebooks.
If you use the clients and do not want to pollute your log files you may change the log level of the clients to ERROR, e.g.:

```python
import logging
logging.getLogger('tgclients').setLevel(logging.ERROR)
```

or more specific, e.g. for not getting crud warnings:
```python
import logging
logging.getLogger('tgclients.crud').setLevel(logging.ERROR)
```


## License

This project aims to be [REUSE compliant](https://api.reuse.software/info/gitlab.gwdg.de/dariah-de/textgridrep/textgrid-python-clients).
Original parts are licensed under AGPL-3.0-or-later.
Derivative code is licensed under the respective license of the original.
Documentation, configuration and generated code files are licensed under CC0-1.0.

## Badges

[![REUSE status](https://api.reuse.software/badge/gitlab.gwdg.de/dariah-de/textgridrep/textgrid-python-clients)](https://api.reuse.software/info/gitlab.gwdg.de/dariah-de/textgridrep/textgrid-python-clients)
[![PyPI version](https://badge.fury.io/py/tgclients.svg)](https://badge.fury.io/py/tgclients)
[![Coverage](https://gitlab.gwdg.de/dariah-de/textgridrep/textgrid-python-clients/badges/main/coverage.svg)](https://dariah-de.pages.gwdg.de/textgridrep/textgrid-python-clients/htmlcov/index.html)
