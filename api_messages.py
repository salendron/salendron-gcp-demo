#!/usr/bin/env python

## @package api_messages
# @brief This files contains all Proto-RPC message definitions for DemoApi.
# @author Bruno Hautzenberger

from protorpc import messages

class TodoMessage(messages.Message):
    id = messages.IntegerField(1)
    text =  messages.StringField(2,required=True)
    is_done = messages.StringField(3,required=True)
    
class GetTodosRequestMessage(messages.Message):
    done = messages.IntegerField(1,required=True)
    
class TodoListResponseMessage(messages.Message):
    items = messages.MessageField(TodoMessage, 1, repeated=True)