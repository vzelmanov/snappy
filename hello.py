import web
        
urls = (
    '/', 'index'
)

class index:        
    def GET(self):
        return web.template.render('.').index('junk')

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
