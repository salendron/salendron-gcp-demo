#!/usr/bin/env python

## @package demo_api
# @brief This files contains a class DemoApi 
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

#Google OAuth
WEB_CLIENT_ID = '978138777882-qadj1kucb9qeb8qnueoi7fk2tl7ldufb.apps.googleusercontent.com'


## Contains all API methods.
@endpoints.api(name='TodoAPI',
               version='v1',
               description='Demo API',
               allowed_client_ids=[WEB_CLIENT_ID,],
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
        
        done = True if request.is_done == 'true' else False
        todo_items = [todo.to_message() for todo in Todo.get_todos_of_user(todo)]
        
        return TodoListResponseMessage(items=todo_items)
    
    
# The API server instance
APPLICATION = endpoints.api_server([TodoAPI,])