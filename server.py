from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
from RandomNumGenerator import RandomGen
from collections import deque


class S(BaseHTTPRequestHandler):
    """This class defines what the server do when receives a GET request"""

    queue = deque()
    randGen = RandomGen()

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        """Defines what the get response is. It is the random number that generated"""
        # TODO: create the user management if necessary.
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("{}".format(self.randGen.get_num()).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=S, port=80):
    """Starts the server using Handler 'S' defined above"""
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.timeout = 20
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
