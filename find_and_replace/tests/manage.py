#!/usr/bin/env python
# coding: utf-8

"""
    django find&replace
    ~~~~~~~~~~~~~~~~~~~

    :copyleft: 2015 by find&replace team, see AUTHORS for more details.
    :created: 2015 by JensDiemer.de
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""

import os
import sys

from django.core.management import call_command
from django.db.utils import OperationalError
import django
from django.conf import settings



def create_db():
    django.setup()

    print("\n")
    from django.contrib.auth.models import User
    try:
        user_exists = User.objects.filter(username=settings.TEST_USER_NAME).exists()
    except OperationalError as err:
        print(err)
        user_exists = False
        print("\n *** call 'migrate' command:")
        call_command("migrate", interactive=False, verbosity=1)

    if not user_exists:
        print("*"*79)
        print("*** Create User %r with password %r" % (settings.TEST_USER_NAME, settings.TEST_USER_PASS))
        print("*"*79)
        user, created = User.objects.get_or_create(username=settings.TEST_USER_NAME)
        user.is_staff=True
        user.is_superuser=True
        user.set_password(settings.TEST_USER_PASS)
        user.save()

    assert User.objects.filter(username=settings.TEST_USER_NAME).exists() == True



def main():
    sys.stderr = sys.stdout # Hack for Eclipse, PyCharm & Co. to "sync" output

    create_db()

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

    sys.exit(0) # if called from 'setup.py test' and tests are ok.



def run_test_server():
    """
    INFO: The django reloader will call this multiple times!
    We check RUN_MAIN, that will be set in django.utils.autoreload
    So we can skip the first migrate run.
    """
    django.setup()

    if os.environ.get("RUN_MAIN"):
        create_db()
        # call_command("cms", "check")

    call_command("runserver",
         use_threading=False,
         use_reloader=True,
         verbosity=2
    )



if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "find_and_replace.tests.settings")
    print("\nUse DJANGO_SETTINGS_MODULE=%r" % os.environ["DJANGO_SETTINGS_MODULE"])
    main()

