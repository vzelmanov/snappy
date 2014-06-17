import web
import json
import os
import dj_database_url

urls = (
    '/', 'Index',
    '/add', 'Add',
    '/env', 'Env',
)

database_config = dj_database_url.config()

db = web.database(dbn = 'postgres',
                    host = database_config['HOST'],
                    user = database_config['USER'],
                    pw = database_config['PASSWORD'],
                    db = database_config['NAME'])

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
