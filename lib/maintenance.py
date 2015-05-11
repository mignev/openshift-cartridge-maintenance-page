#!/usr/bin/env python

# BASED ON
# https://gist.github.com/vimishor/7944395

import os
import time
import BaseHTTPServer
import urllib

CUSTOM_PAGE = os.getenv("MAINTENANCE_URL", None)

HOST_NAME = os.getenv("OPENSHIFT_HAPROXY_IP") \
            or os.getenv("OPENSHIFT_RUBY_IP") \
            or os.getenv("OPENSHIFT_PHP_IP") \
            or os.getenv("OPENSHIFT_NODEJS_IP") \
            or os.getenv("OPENSHIFT_PYTHON_IP") \
            or os.getenv("OPENSHIFT_PERL_IP") \
            or os.getenv("OPENSHIFT_DIY_IP")

PORT_NUMBER = os.getenv("OPENSHIFT_HAPROXY_PORT") \
                or os.getenv("OPENSHIFT_RUBY_PORT") \
                or os.getenv("OPENSHIFT_PHP_PORT") \
                or os.getenv("OPENSHIFT_NODEJS_PORT") \
                or os.getenv("OPENSHIFT_PYTHON_PORT") \
                or os.getenv("OPENSHIFT_PERL_PORT") \
                or os.getenv("OPENSHIFT_DIY_PORT")

PORT_NUMBER = int(PORT_NUMBER)

class MaintenanceHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.curDir = os.path.dirname(os.path.realpath(__file__))

        if self.path=="/":
            self.path = "/503.html"
        # If requested file does not exists, show 503 page
        elif os.path.exists(self.curDir+self.path) == False:
            self.path = "/503.html"

        try:
            # Check extensions and set the mime type accordingly
            sendReply = False

            if self.path.endswith(".html"):
                mimetype    = "text/html"
                sendReply   = True
            if self.path.endswith(".png"):
                mimetype    = "image/png"
                sendReply   = True
            if self.path.endswith(".jpg"):
                mimetype    = "image/jpg"
                sendReply   = True
            if self.path.endswith(".gif"):
                mimetype    = "image/gif"
                sendReply   = True
            if self.path.endswith(".js"):
                mimetype    = "application/javascript"
                sendReply   = True
            if self.path.endswith(".css"):
                mimetype    = "text/css"
                sendReply   = True


            if sendReply == True:
                if CUSTOM_PAGE:
                    # Load the content of the url and send it
                    f = urllib.urlopen(CUSTOM_PAGE)
                else:
                    # Open the static file requested and send it
                    f = open(self.curDir+self.path)

                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()

            return
        except IOError:
            self.send_error(404, 'File not found: %s' % self.path)

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer

    for retry in range(100):
        try:
            httpd = server_class((HOST_NAME, PORT_NUMBER), MaintenanceHandler)
        except:
            print "Retry"
            time.sleep(0.1)

        try:
            httpd
        except NameError, e:
            pass
        else:
            break

    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)

    try:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass

        httpd.server_close()
    except NameError, e:
        pass

    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
