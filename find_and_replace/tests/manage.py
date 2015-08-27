#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "find_and_replace.tests.settings")
    print("\nUse DJANGO_SETTINGS_MODULE=%r" % os.environ["DJANGO_SETTINGS_MODULE"])

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

    sys.exit(0) # if called from 'setup.py test' and tests are ok.


if __name__ == "__main__":
    main()

