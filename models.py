#!/usr/bin/env python

## @package models
# @brief ndb models
# @author Bruno Hautzenberger

import endpoints
import logging
from google.appengine.ext import ndb

from api_messages import TodoMessage

from util import get_user

## ndb model to store a client user
class Todo(ndb.Model):
    user_email = ndb.StringProperty(required=True)
    text = ndb.TextProperty(required=True)
    is_done = ndb.BooleanProperty(required=True)
    
    def to_message(self):
        return TodoMessage(
            id=self.key.id(),
            text=self.text,
            is_done='true' if self.is_done else 'false'
        )
    
    @classmethod
    def put_from_message(cls, message):
        entity = None
        
        if hasattr(message, 'id') and message.id != None:
            entity = ndb.Key('Todo',message.id).get()
            entity.text = message.text
            entity.is_done = True if message.is_done == 'true' else False
        else:
            entity = cls(
                user_email=get_user().email(),
                text=message.text,
                is_done=True if message.is_done == 'true' else False
            )
            
        entity.put()
        
        return entity
    
    @classmethod
    def get_todos_of_user(cls, done):        
        query = Todo.query(Todo.user_email == get_user().email()) #TODO
        query = query.filter(Todo.is_done == done)
        
        return query.fetch()
            
            
       
        