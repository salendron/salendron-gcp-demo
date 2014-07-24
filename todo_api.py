#!/usr/bin/env python

## @package todo_api
# @brief This files contains a class TodoApi 
# @author Bruno Hautzenberger

import logging
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

from models import Todo

from api_messages import GetTodosRequestMessage
from api_messages import TodoListResponseMessage
from api_messages import TodoMessage

from util import get_user


## Contains all API methods.
@endpoints.api(name='todoapi',
               version='v1',
               description='Todo API',
               allowed_client_ids=[endpoints.API_EXPLORER_CLIENT_ID],
               scopes=[endpoints.EMAIL_SCOPE])
class TodoAPI(remote.Service):

    @endpoints.method(TodoMessage, TodoMessage,path='todo_save', http_method='POST',name='todo.save')
    def save_todo(self, request):
        get_user() #check auth
        
        todo = Todo.put_from_message(request)
        
        return todo.to_message()
    
    @endpoints.method(GetTodosRequestMessage, TodoListResponseMessage,path='get_todos', http_method='GET',name='todos.get')
    def get_todos(self, request):
        get_user() #check auth
        
        done = True if request.done == 'true' else False
        todo_items = [todo.to_message() for todo in Todo.get_todos_of_user(done)]
        
        return TodoListResponseMessage(items=todo_items)
    
    
# The API server instance
APPLICATION = endpoints.api_server([TodoAPI,])