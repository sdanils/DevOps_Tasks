import socket
import os

HOST = '0.0.0.0'    
HTML_STR = 'server/index.html'

AUTHOR = os.getenv("AUTHOR") 
PORT = os.getenv("PORT") 

def get_host_info():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return hostname, ip

def render_html(hostname, ip):
    with open(HTML_STR, "r",  encoding="utf-8") as file:
        html = file.read()
    
    return html \
        .replace("{{hostname}}", hostname) \
        .replace("{{ip}}", ip) \
        .replace("{{author}}", AUTHOR)

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, int(PORT)))
        s.listen()

        while True:
            conn, _ = s.accept()            

            request = conn.recv(1024).decode()             
            if "GET /favicon.ico" in request:
                conn.sendall(b"HTTP/1.1 204 No Content\r\n\r\n")
                conn.close()
                continue 

            hostname, ip = get_host_info()
            html = render_html(hostname, ip)

            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html\r\n"
                f"Content-Length: {len(html)}\r\n"
                "\r\n" + html
            )
            
            conn.sendall(response.encode())
            conn.close()

if __name__ == "__main__":
    start_server()