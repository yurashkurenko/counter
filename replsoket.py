Вот пример создания REPL (Read-Eval-Print Loop) на Socket в Micropython:


import socket
import sys
import micropython

def create_repl_socket(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(1)
    print(f"Listening on {host}:{port}...")
    return sock

def handle_client(sock):
    conn, addr = sock.accept()
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        try:
            result = eval(data.decode())
            conn.sendall(str(result).encode())
        except Exception as e:
            conn.sendall(str(e).encode())
    conn.close()

if __name__ == "__main__":
    host = "localhost"
    port = 12345
    sock = create_repl_socket(host, port)
    while True:
        handle_client(sock)
В этом примере мы создаем socket, который слушает подключения на порту 12345. Когда клиент подключается, мы создаем новый поток, в котором обрабатываем сообщения клиента. Каждое сообщение клиента мы интерпретируем как Python-код с помощью функции eval, а результат отправляем обратно клиенту. Еслиduring evaluation occurred an error, we send the error message back to the client.

To use this REPL, you can run the script and then connect to it using a tool like netcat or telnet:


$ python repl_socket.py
Listening on localhost:12345...
$ telnet localhost 12345
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
2 + 2
4
Now you can interact with the REPL by sending Python code as strings, and the server will respond with the result. Note that this is a very basic implementation and you may want to add additional features, such as handling multiple clients, implementing a proper command-line interface, or implementing security measures to prevent code injection attacks.