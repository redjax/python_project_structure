"""A __main__.py file allows the app/ dir to be run directly.

For example, this script can be run with 'python app' or 'python -m app'.

It can be treated as a main.py file, or a separate main.py file can exist and
this app can load from it.
"""
from dynaconf import settings

from main import main

if __name__ == "__main__":
    main()
