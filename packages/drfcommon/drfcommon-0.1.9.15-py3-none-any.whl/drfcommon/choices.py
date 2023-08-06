#!/usr/bin/env python
import logging
from enum_choices import Choices


class ComCodeChoice(Choices):
    """
    ComCodeChoice
    """
    OK = (200, '成功')
    BAD = (400, '参数错误')
    UNAUTHORIZED_ERR = (401, "认证失败")
    FORBIDDEN_ERR = (403, '权限错误')
    API_NOT_FUND = (404, '找不到对应的服务或数据')
    HTTP_405_METHOD_NOT_ALLOWED = (405, '方法不允许')
    API_ERR = (500, '内部错误')
    DB_ERR = (507, '服务器内部数据库问题')

