import socket
from urllib.parse import urlparse, parse_qs
from http import HTTPStatus


def run_server(host='127.0.0.1', port=5000):
    """HTTP Echo-сервер на сокетах. Работает с GET/POST и возвращает заголовки клиента."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((host, int(port)))
        server.listen(5)
        print(f"Echo server running on http://{host}:{port}")

        while True:
            conn, addr = server.accept()
            handle_client(conn, addr)


def get_status(query: dict):
    """Получает статус из параметра ?status=..."""
    try:
        code = int(query.get("status", [200])[0])
        status = HTTPStatus(code)
    except Exception:
        status = HTTPStatus(200)
    return f"{status.value} {status.phrase}", status.value


def handle_client(conn: socket.socket, addr):
    """Обработка одного HTTP-запроса"""
    try:
        data = conn.recv(4096).decode('utf-8', errors='ignore')
        if not data:
            conn.close()
            return

        try:
            request_line = data.split("\r\n")[0]
            method, path, _ = request_line.split()
        except ValueError:
            conn.close()
            return

        parsed = urlparse(path)
        query = parse_qs(parsed.query)
        status_line, status_code = get_status(query)
        headers = {}
        for line in data.split("\r\n")[1:]:
            if not line.strip():
                break
            if ":" in line:
                key, value = line.split(":", 1)
                headers[key.strip()] = value.strip()
        body_lines = [
            f"Request Method: {method}",
            f"Request Source: {addr}",
            f"Response Status: {status_line}",
        ]
        for k, v in headers.items():
            body_lines.append(f"{k}: {v}")
        body = "\r\n".join(body_lines)
        body_bytes = body.encode("utf-8")
        response = (
            f"HTTP/1.1 {status_line}\r\n"
            f"Content-Type: text/plain; charset=utf-8\r\n"
            f"Content-Length: {len(body_bytes)}\r\n"
            f"Connection: close\r\n"
            f"\r\n"
        ).encode("utf-8") + body_bytes

        conn.sendall(response)
        print("\n----------------------------")
        print(f"Incoming request from {addr}")
        print(f"Request Method: {method}")
        print(f"Path: {path}")
        print(f"Response Status: {status_line}")
        print("Headers received:")
        for k, v in headers.items():
            print(f"  {k}: {v}")
        print("----------------------------\n")

    finally:
        conn.close()


if __name__ == '__main__':
    run_server()


