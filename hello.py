import web
import json
import os

urls = (
    '/', 'Index',
    '/add', 'Add',
    '/env', 'Env',
)

db = web.database(dbn='postgres', user='lordlandon', db='snappy')
app = web.application(urls, globals())
wsgi_app = web.application(urls, globals()).wsgifunc()

        

class Index:
    def GET(self):
        junk = db.select('junk')
        return web.template.render('.').index(junk)

class Env:
    def GET(self):
        return os.environ

class Add:
    def POST(self):
        i = web.data()
        print json.loads(i)

if __name__ == "__main__":
    app.run()
