# -*- coding: utf-8 -*-
# @Author: CodyKochmann
# @Date:   2016-03-22 14:58:26
# @Last Modified 2016-03-22me>
# @Last Modified time: 2016-03-22 14:59:16
"""

# this is the model were basing the REST design off of

import os, os.path
 import random
 import string

 import cherrypy

 class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')

 class StringGeneratorWebService(object):
     exposed = True

     @cherrypy.tools.accept(media='text/plain')
     def GET(self):
         return cherrypy.session['mystring']

     def POST(self, length=8):
         some_string = ''.join(random.sample(string.hexdigits, int(length)))
         cherrypy.session['mystring'] = some_string
         return some_string

     def PUT(self, another_string):
         cherrypy.session['mystring'] = another_string

     def DELETE(self):
         cherrypy.session.pop('mystring', None)

 if __name__ == '__main__':
     conf = {
         '/': {
             'tools.sessions.on': True,
             'tools.staticdir.root': os.path.abspath(os.getcwd())
         },
         '/generator': {
             'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
             'tools.response_headers.on': True,
             'tools.response_headers.headers': [('Content-Type', 'text/plain')],
         },
         '/static': {
             'tools.staticdir.on': True,
             'tools.staticdir.dir': './public'
         }
     }
     webapp = StringGenerator()
     webapp.generator = StringGeneratorWebService()
     cherrypy.quickstart(webapp, '/', conf)
"""