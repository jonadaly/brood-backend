import sys
import traceback

import flask
from loguru import logger


def init_error_handler(app):
    app.errorhandler(ValueError)(_catch_bad_request)
    app.errorhandler(KeyError)(_catch_bad_request)
    app.errorhandler(TypeError)(_catch_bad_request)
    app.errorhandler(PermissionError)(_catch_unauthorised)
    app.errorhandler(EntityNotFoundException)(_catch_not_found)
    app.errorhandler(ServiceUnavailableException)(_catch_upstream)


def _catch_bad_request(error):
    return _catch(error, logger.warning, 400)


def _catch_internal_error(error):
    return _catch(error, logger.critical, 500)


def _catch_not_found(error):
    return _catch(error, logger.warning, 404)


def _catch_unauthorised(_error):
    return _catch("Forbidden", logger.error, 403)


def _catch_upstream(error):
    return _catch(error, logger.error, 502)


def _catch(error, log_method, code):
    exc_type, exc_value, exc_traceback = sys.exc_info()
    log_method("".join(traceback.format_exception(exc_type, exc_value, exc_traceback)))
    structure = {"message": str(error)}
    return flask.jsonify(structure), code


class EntityNotFoundException(Exception):
    pass


class ServiceUnavailableException(Exception):
    pass
