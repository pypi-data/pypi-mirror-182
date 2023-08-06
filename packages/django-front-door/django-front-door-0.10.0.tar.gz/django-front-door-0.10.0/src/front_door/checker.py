import logging

from .conf import LOG_FAIL, LOG_PASS, LOG_RULE_FAIL, LOG_RULE_PASS, config
from .exception import FrontDoorAccessDenied
from .utils import get_client_ip

logger = logging.getLogger(__name__)


def front_door_check_access(request):
    if not config.ENABLED:
        access_allowed = True
    else:
        access_allowed = config.DEFAULT_POLICY
        ip = get_client_ip(request)
        path = request.path
        extra = {"ip": ip,
                 "path": path}
        for check in config.rules:
            try:
                if check(request, ip):
                    if config.LOG_LEVEL & LOG_RULE_PASS:
                        logger.error(f"{check.__name__}() PASS", extra=extra)
                    access_allowed = True
                    break
                else:
                    if config.LOG_LEVEL & LOG_RULE_FAIL:
                        logger.error(f"{check.__name__}() FAIL", extra=extra)
            except FrontDoorAccessDenied:
                if config.LOG_LEVEL & LOG_RULE_FAIL:
                    logger.error(f"{check.__name__}() DENY", extra=extra)
                access_allowed = False
                break
            except Exception as e:
                logger.exception(e)
        if access_allowed and (config.LOG_LEVEL & LOG_PASS):
            logger.error("Access ALLOWED", extra=extra)
        elif (not access_allowed) and config.LOG_LEVEL & LOG_FAIL:
            logger.error("Access DENIED", extra=extra)

    return access_allowed
