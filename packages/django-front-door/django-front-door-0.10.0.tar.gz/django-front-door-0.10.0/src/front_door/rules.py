import logging

from django.conf import settings

from .conf import config
from .exception import FrontDoorAccessDenied

logger = logging.getLogger(__name__)


def allowed_ip(request, ip, **kwargs):
    return ip in config.ALLOWED_IPS


def internal_ip(request, ip, **kwargs):
    return ip in settings.INTERNAL_IPS


def special_header(request, ip, **kwargs):
    if config.HEADER and config.TOKEN:
        return request.headers.get(config.HEADER) == config.TOKEN


def has_header(request, ip, **kwargs):
    if config.HEADER:
        return config.HEADER in request.headers


def allowed_path(request, ip, **kwargs):
    return request.path in config.ALLOWED_PATHS


def forbidden_path(request, ip, **kwargs):
    if request.path in config.FORBIDDEN_PATHS:
        raise FrontDoorAccessDenied


def cookie_exists(request, ip, **kwargs):
    return config.COOKIE_NAME in request.COOKIES


def cookie_value(request, ip, **kwargs):
    if not config.COOKIE_PATTERN and config.COOKIE_NAME:
        return False
    try:
        value = request.COOKIES[str(config.COOKIE_NAME)]
    except KeyError:
        return False
    return bool(config.COOKIE_PATTERN.match(value))
