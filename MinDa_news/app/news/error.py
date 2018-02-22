# ！/usr/bin/python
# -*- coding: utf-8 -*-

from .view import news
from flask import jsonify

__author__ = 'AidChow'


@news.app_errorhandler(404)
def request_not_found(e):
    return jsonify({'code': 404, 'msg': 'request not found', 'content': None}), 404


@news.app_errorhandler(500)
def inner_server_error(e):
    return jsonify({'code': 500, 'msg': 'inner server error', 'content': None}), 500
