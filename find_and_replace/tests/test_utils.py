from django.db.models.loading import get_apps, get_models
from django.test import SimpleTestCase
from django.db import backend, connection

class UtilsTest(SimpleTestCase):
    def test(self):

        skip_types=(
            "integer", "datetime", "bool"
        )

        model_fields = []
        for app in get_apps():
            print("\n***", app.__name__)
            for model in get_models(app):
                print("\n++++", model._meta.object_name)
                for field in model._meta.fields:
                    print("\nfield:", field)

                    db_type = field.db_type(connection)
                    print("db_type: %r" % db_type)
                    if db_type in skip_types:
                        print("Skip")
                        continue

                    print("attname:", field.get_attname())
                    print("description:", field.description)
                    help(db_type)
                    # help(field)
                    # model_fields.append(
                    #     "%s.%s" % (app.__name__, model._meta.object_name)
                    # )
                    # raise