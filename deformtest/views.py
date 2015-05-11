from deform import Form, ValidationFailure
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    MyModel,
    )

from zope.interface import Interface
from zope.interface import alsoProvides
from .userarea_admin import EditMenuItems


def form_view(request):
    schema = EditMenuItems()
    myform = Form(schema, buttons=('submit',))
    reqt = myform.get_widget_resources(myform.get_widget_requirements())
    if 'submit' in request.POST:
        controls = request.POST.items()
        try:
            myform.validate(controls)

        except ValidationFailure as e:
            return {'form':e.render()}
        return {'form':'OK'}
    return {'form': myform.render(), 'project': 'poop',
            'css': reqt['css'], 'js': reqt['js']}


conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_deformtest_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

