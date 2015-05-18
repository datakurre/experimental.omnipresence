# -*- coding: utf-8 -*-
import re
from webdav.common import rfc1123_date


bad_id = re.compile(r'[^a-zA-Z0-9-_~,.$\(\)# @:]').search


def dav__init(self, request, response):
    # We are allowed to accept a url w/o a trailing slash
    # for a collection, but are supposed to provide a
    # hint to the client that it should be using one.
    # [WebDAV, 5.2]
    pathinfo = request.get('PATH_INFO', '')
    if pathinfo and pathinfo[-1] != '/':
        location = '%s/' % request['URL1']
        response.setHeader('Content-Location', location)
    # We sniff for a ZServer response object, because we don't
    # want to write duplicate headers (since ZS writes Date
    # and Connection itself).
    if not hasattr(response, '_server_version'):
        response.setHeader('Connection', 'close', 1)
        response.setHeader('Date', rfc1123_date(), 1)
