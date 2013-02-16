import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class MorePhysics(webapp.RequestHandler):
	""" Page Handler for More Physics """
	def get(self):
		path = os.path.join(os.path.abspath(__file__), '../html', 'learnPhysics.html')
		self.response.out.write(template.render(path, {}))
		
