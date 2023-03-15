## About

Made for a discussion regarding `anyio`: https://github.com/agronholm/anyio/discussions/543

## Setup

Try in an environment where `sniffio` is installed. Make sure the repo-root is in `PYTHONPATH` by using an IDE or installing as editable: `pip install -e .`

Tested with Python 3.10.

## Demo

Simply running `python -m demo` will load a dynamic asyncio selecting backend-mock. This has the overhead of selecting the backend on each access.

An explicit backend can be selected by setting an envvar: `DYNMOD_BACKEND=asyncio python -m demo` this provides zero overhead.
