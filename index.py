import tornado.web
import tornado.ioloop

class uploadHandler(tornado.web.RequestHandler):
    def post(self):
        files = self.request.files["fileImage"]
        for f in files:
            fh = open(f"upload/{f.filename}", "wb")
            fh.write(f.body)
            fh.close()
        self.write(f"http://localhost:8080/upload/{f.filename}")
    def get(self):
        self.render("index.html")

if (__name__ == "__main__"):
    app = tornado.web.Application([
        ("/", uploadHandler),
        ("/upload/(.*)", tornado.web.StaticFileHandler, {
            "path" : "upload"
        })
    ])
    port = 8080
    app.listen(port)
    print("Listening on port 8080 ...")

    tornado.ioloop.IOLoop.instance().start()