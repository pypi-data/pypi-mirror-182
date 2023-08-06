from django.conf import settings

try:
    # we use django.urls import as version detection as it will fail on django 1.11 and thus we are safe to use
    # gettext_lazy instead of ugettext_lazy instead
    from django.utils.translation import gettext_lazy as _
except ImportError:
    from django.utils.translation import ugettext_lazy as _


def admin_tools(request):
    environment = getattr(settings, "ENVIRONMENT", "local")
    environment_text = {
        "local": _("Local Environment"),
        "develop": _("Develop Environment"),
        "staging": _("Staging Environment"),
        "production": _("Production Environment"),
    }
    return {
        "ENVIRONMENT_TEXT": environment_text[environment]
    }
