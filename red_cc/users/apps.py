from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "red_cc.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import red_cc.users.signals  # noqa F401
        except ImportError:
            pass
