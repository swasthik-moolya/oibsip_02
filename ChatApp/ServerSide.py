import socket
import threading

clients = []
addresses = []

def handle_client(conn, addr):
    print(f"Connected by {str(addr)}")
    connected = True

    while connected:
        try:
            msg = conn.recv(1024)
            if not msg:
                break

            message = msg.decode()
            print(f"{str(addr)} says: {message}")

            # Broadcast message to other clients
            broadcast(message, conn)
        except:
            index = clients.index(conn)
            clients.remove(conn)
            conn.close()
            address = addresses[index]
            addresses.remove(address)
            print(f"Connection with {str(address)} lost.")
            broadcast(f"{str(address)} has left the chat!", conn)
            break

def broadcast(message, connection):
    for client in clients:
        if client != connection:
            try:
                client.send(message.encode())
            except:
                client.close()
                index = clients.index(client)
                clients.remove(client)
                addresses.remove(addresses[index])
                print(f"Connection with {str(addresses[index])} lost.")
                broadcast(f"{str(addresses[index])} has left the chat!", client)

def start_server():
    host = '172.22.112.1'
    port = 12345

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"Server listening on {host}:{port}")


    while True:
        conn, addr = server.accept()
        clients.append(conn)
        addresses.append(addr)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


if __name__ == "__main__":
    start_server()
