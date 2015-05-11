
from colander import (Schema, SchemaNode, String, OneOf, SequenceSchema, Integer, 
    MappingSchema, deferred, Boolean, Set)
from deform import FileData
from deform.widget import SelectWidget, TextAreaWidget, FileUploadWidget
from pyramid.security import Everyone

class MenuItem(Schema):
    name = SchemaNode(String())
    url = SchemaNode(String())
    permissions = SchemaNode(String())
    position = SchemaNode(Integer())
    
class Menu(SequenceSchema):
    menu_item = MenuItem()

class EditMenuItems(Schema):
    menu = Menu()