def add(a, b):
    return a + b

def hello(name):
    return f"Hello, {name}!"

def multiply(a, b):
    return a * b  # bug intentionnel — devrait être a * b

if __name__ == "__main__":
    from http.server import HTTPServer, BaseHTTPRequestHandler

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(hello("World").encode())

    print("Server running on port 8000")
    HTTPServer(("", 8000), Handler).serve_forever()
