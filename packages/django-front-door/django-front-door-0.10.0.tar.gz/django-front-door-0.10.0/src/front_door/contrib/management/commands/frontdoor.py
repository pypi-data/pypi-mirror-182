from django.core.exceptions import ValidationError
from django.core.management import BaseCommand, CommandError
from django.utils.translation import gettext as _


def is_writable(key):
    from front_door.conf import DjangoConstance, DjangoSettings, OSEnv, config

    if isinstance(config, DjangoConstance):
        from constance.admin import ConstanceForm, get_values

        form = ConstanceForm(initial=get_values())
        return key in form.fields
    elif isinstance(config, DjangoSettings):
        pass
    elif isinstance(config, OSEnv):
        pass


def _set_constance_value(key, value):
    """
    Parses and sets a Constance value from a string
    :param key:
    :param value:
    :return:
    """
    from constance import config
    from constance.admin import ConstanceForm, get_values

    form = ConstanceForm(initial=get_values())

    field = form.fields[key]

    clean_value = field.clean(field.to_python(value))
    setattr(config, key, clean_value)


class Command(BaseCommand):
    help = _("Get/Set In-database config settings handled by Constance")

    def run_from_argv(self, argv):
        return super().run_from_argv(argv)

    def add_arguments(self, parser):
        subparsers = parser.add_subparsers(dest="command")
        self._subparsers_add_parser(subparsers, "show", cmd=self, help="show FrontDoor configuration")

        parser_get = self._subparsers_add_parser(subparsers, "get", cmd=self, help="get the value of a FrontDoor key")
        parser_get.add_argument("key", help="name of the key to get", metavar="KEY")

        parser_set = self._subparsers_add_parser(subparsers, "set", cmd=self, help="set the value of a FrontDoor key")
        parser_set.add_argument("key", help="name of the key to get", metavar="KEY")
        parser_set.add_argument("value", help="value to set", metavar="VALUE", nargs="+")

    def _subparsers_add_parser(self, subparsers, name, **kwargs):
        # API in Django >= 2.1 changed and removed cmd parameter from add_parser
        if "cmd" in kwargs:
            kwargs.pop("cmd")
        return subparsers.add_parser(name, **kwargs)

    def handle(self, command, key=None, value=None, *args, **options):
        from front_door.conf import config

        try:
            if command == "get":
                try:
                    self.stdout.write("{}".format(getattr(config, key)), ending="\n")
                except AttributeError:
                    raise CommandError(key + " is not defined in settings.CONSTANCE_CONFIG")

            elif command == "set":
                key = f"FRONT_DOOR_{key}"
                try:
                    if len(value) == 1:
                        value = value[0]
                    if is_writable(key):
                        _set_constance_value(key, value)
                    else:
                        raise CommandError(key + " is not writeable")
                except KeyError:
                    raise CommandError(key + " is not defined in settings.CONSTANCE_CONFIG")
                except ValueError as e:
                    raise CommandError(e)
                except ValidationError as e:
                    raise CommandError(", ".join(e))

            elif command == "show":
                from front_door.conf import config

                for k, v in config.defaults.items():
                    self.stdout.write("{:16}\t{}".format(k, getattr(config, k)), ending="\n")
        except CommandError as e:
            self.stderr.write("{}".format(e), ending="\n")
