#!/usr/bin/env python
"""
exceptions.py
"""

import logging

from django.core.paginator import EmptyPage
from django.db import DatabaseError
from django.http import Http404
from django.utils.translation import gettext_lazy as _
from rest_framework import status, exceptions
from rest_framework.exceptions import (
    APIException,
    ValidationError,
    AuthenticationFailed,
    PermissionDenied,
    NotAuthenticated,
    MethodNotAllowed,
    NotFound, ParseError,
)
from rest_framework.views import exception_handler, set_rollback

from drfcommon.choices import ComCodeChoice
from drfcommon.helper import _handler_err
from drfcommon.log import logger_print_by_code
from drfcommon.response import done


class ComValidationError(ValidationError):
    """
    ComValidation Error
    """
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, detail=None, code=None):
        if code:
            self.status_code = code
        super().__init__(detail=detail, code=code)


class ComAPIException(APIException):
    """
    ComAPIException detail 只返回string
    """
    status_code = status.HTTP_200_OK
    default_detail = _('A server error occurred.')
    default_code = 'error'
    err_code = status.HTTP_200_OK

    def __init__(self, detail=None, err_code=None):
        if err_code:
            self.err_code = err_code
        super().__init__(detail=detail, code=self.status_code)


def exception_handler(exc, context):
    """
    Returns the response that should be used for any given exception.

    By default we handle the REST framework `APIException`, and also
    Django's built-in `Http404` and `PermissionDenied` exceptions.

    Any unhandled exceptions may return `None`, which will cause a 500 error
    to be raised.
    """
    code = ComCodeChoice.API_ERR
    msg = None
    if isinstance(exc, Http404):
        code = ComCodeChoice.API_NOT_FUND
    elif isinstance(exc, EmptyPage):
        # 404
        code = ComCodeChoice.API_NOT_FUND
    elif isinstance(exc, NotFound):
        # 404
        code = ComCodeChoice.API_NOT_FUND
    elif isinstance(exc, ParseError):
        # 400
        code = ComCodeChoice.BAD
        msg = _handler_err(exc.detail)
    elif isinstance(exc, ValidationError):
        # 400
        code = ComCodeChoice.BAD
        msg = _handler_err(exc.detail)
    elif isinstance(exc, ComValidationError):
        # 400
        code = ComCodeChoice.BAD
        msg = _handler_err(exc.detail)
    elif isinstance(exc, NotAuthenticated):
        # 401
        code = ComCodeChoice.UNAUTHORIZED_ERR
    elif isinstance(exc, AuthenticationFailed):
        # 401
        code = ComCodeChoice.UNAUTHORIZED_ERR
    elif isinstance(exc, MethodNotAllowed):
        code = ComCodeChoice.HTTP_405_METHOD_NOT_ALLOWED
    elif isinstance(exc, PermissionDenied):
        # 403
        code = ComCodeChoice.FORBIDDEN_ERR
    elif isinstance(exc, DatabaseError):
        code = ComCodeChoice.DB_ERR
    else:
        # 如果没有处理，保留原始的错误
        msg = "{}".format(exc)
    logger_print_by_code(code, exc)
    # msg 是否被设置. 无，使用自定义
    if not msg:
        msg = ComCodeChoice.choices_map[code]
    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        if isinstance(exc.detail, (list, dict)):
            data = exc.detail
        else:
            data = {'detail': exc.detail}
        set_rollback()
        return done(
            code=code,
            msg=msg,
            # dict
            errors=data,
        )
    return done(code=code, msg=msg)


def com_exception_handler(exc, context):
    """
    处理views中的异常, 视图函数只返回200，errmsg/errcode

    exc.detail
        if isinstance(exc.detail, (list, dict)):
            data = exc.detail
        else:
            data = {'detail': exc.detail}

    :param exc: APIException
    :param context:
    :return:
    """
    response = exception_handler(exc, context)
    return response

