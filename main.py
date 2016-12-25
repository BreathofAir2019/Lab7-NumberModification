
import webapp2
import random
import os
import urllib
import jinja2

myList=[]

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        template_values = {
            'title': 'My Title'
        }
        self.response.write(template.render(template_values))

class Lister(webapp2.RequestHandler):
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('list.html')
        n = int(self.request.get("num"))
        r = int(random.random()*n)+1
        color= int(float(r)*255/n)
        test = (n, r, color)
        myList.append(test)
        template_values = {'myList': myList}
        self.response.write(template.render(template_values))
        
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ("/list", Lister)
], debug=True)
