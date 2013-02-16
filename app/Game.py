import os
import sys
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class Game(webapp.RequestHandler):
	""" Page handler for current game running """
	def get(self):
		path = os.path.join(os.path.dirname(__file__),'../html','Game.html')
		#print path
		self.response.out.write(template.render(path,{}))