import socket # pra comunicação tcp, com o servidor
import threading # pra permitir multiplas conexoes simultaneas

#criar lista global de clientes pra enviar mensagens(broadcast)
clientes = []

# enviar mensagem para todos os clientes, menos o que enviou
def broadcast(message, source_conn):
#Envia a mensagem para todos os clientes conectados
#exceto o cliente que enviou originalmente (source_conn)
    for client in clientes:
        conn, _ = client  # desestrutura a tupla (conn, addr)
        if conn != source_conn:
            try:
                conn.sendall(message)  # envia a mensagem em bytes
            except:
                # Remove o cliente com erro da lista
                clientes.remove(client)
                conn.close()

def handle_client(conn, addr):
#Função executada por uma thread para lidar com um cliente individual.
#Recebe mensagens e repassa para os outros clientes.
    print(f"[+] Nova conexão de {addr}")
    clientes.append((conn, addr))  # adiciona cliente à lista global

    try:
        while True:
            message = conn.recv(1024)  # recebe até 1024 bytes
            if not message:
                break  # cliente desconectou
            print(f"[{addr}] {message.decode()}")
            broadcast(message, conn)  # repassa pros outros clientes
    except:
        # Erros tipo queda de conexão vao ser ignorados
        pass
    finally:
        # Remove cliente da lista e fecha a conexão
        print(f"[-] Cliente {addr} desconectado")
        conn.close()
        clientes.remove((conn, addr))

def start_server(host='127.0.0.1', port=12345):
#Função principal do servidor: aceita conexões de clientes
#e cria uma nova thread para cada um
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))  # associa o socket ao IP e porta
    server.listen()  # começa a aguardar conexões
    print(f"Servidor ouvindo em {host}:{port}")

    while True:
        # Espera por nova conexão
        conn, addr = server.accept()
        # Cria nova thread para lidar com o cliente conectado
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()


