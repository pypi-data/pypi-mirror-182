import http.server
import socketserver
from os import path
import webbrowser
import tempfile
from chunklog.browser_output import parse_html_output

my_host_name = "localhost"
my_port = 8888
handle, html_output_temp_path = tempfile.mkstemp(suffix=".html")


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):  # pragma: no cover
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", path.getsize(self.getPath()))
        self.end_headers()

    def getPath(self):
        if self.path == "/":
            content_path = html_output_temp_path
        # else:
        # content_path = path.join(my_html_folder_path, str(self.path).split('?')[0][1:])
        return content_path

    def getContent(self, content_path):
        with open(content_path, mode="rb") as f:
            return f.read()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(self.getContent(self.getPath()))


def run_server(entries, highlight_diff):
    my_handler = MyHttpRequestHandler

    parse_html_output(entries, highlight_diff, handle)

    with socketserver.TCPServer(("", my_port), my_handler) as httpd:
        print("Http Server Serving at port", my_port)
        webbrowser.open("http://localhost:8888/")
        run_request_handler(httpd)
    return httpd


def run_request_handler(httpd):
    httpd.handle_request()  # pragma: no cover
