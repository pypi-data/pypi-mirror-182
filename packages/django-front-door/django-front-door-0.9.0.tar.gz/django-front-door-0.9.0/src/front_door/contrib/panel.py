import logging.config
from django.shortcuts import render

from front_door.conf import config

logger = logging.getLogger(__name__)


def front_door_panel(admin_site: "smart_admin.SmartAdminSite", request, extra_context=None):
    context = admin_site.each_context(request)
    context["title"] = "FrontDoor Configuration"
    context["config"] = config

    return render(request, "frontdoor_panel.html", context)

front_door_panel.verbose_name = "FrontDoor Configuration"
