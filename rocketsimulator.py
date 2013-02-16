import os
import sys
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
sys.path.append('./app')
from MorePhysics import MorePhysics
from Game import Game

class MainPage(webapp.RequestHandler):
	"""default get handler for the Main Page"""
	def get(self):
		path = os.path.join(os.path.abspath(__file__),'../html','main.html')
		self.response.out.write(template.render(path,{}))
		

application = webapp.WSGIApplication(
                                     [('/', MainPage), 
									  ('/More',MorePhysics), 
									  ('/Game',Game)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()