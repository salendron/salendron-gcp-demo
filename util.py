#!/usr/bin/env python

## @package util
# @author Bruno Hautzenberger

import endpoints

def get_user():
    current_user = endpoints.get_current_user()
    if current_user is None:
        raise endpoints.UnauthorizedException('Invalid token.')
    
    return current_user