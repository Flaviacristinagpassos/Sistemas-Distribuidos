import socket
import threading

def receive_messages(sock):
#Thread responsável por receber mensagens do servidor de forma contínua
#Essa função roda em paralelo pro usuário poder digitar enquanto recebe mensagens
    while True:
        try:
            message = sock.recv(1024)  # espera por mensagem do servidor
            if not message:
                break  # servidor desconectou
            print("Servidor: " + message.decode())  # exibe mensagem recebida
        except:
            print("Erro ao receber mensagem ou conexão encerrada.")
            break

def start_client(host='127.0.0.1', port=12345):
#Função principal do cliente: conecta ao servidor e inicia a thread de recepção de mensagens
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # cria o socket TCP
    sock.connect((host, port))  # conecta ao servidor
    print("Conectado ao servidor de chat.")

    # Inicia uma thread que aguarda mensagens recebidas do servidor
    thread = threading.Thread(target=receive_messages, args=(sock,))
    thread.start()
    try:
        while True:
            message = input("Você: ")  # leitura da mensagem digitada
            if message.lower() == 'sair':
                break  # permite o usuário sair do chat com "sair"
            sock.sendall(message.encode())  # envia mensagem para o servidor
    except KeyboardInterrupt:
        print("\nSaindo do chat...")
    finally:
        sock.close()  # encerra a conexão com o servidor

if __name__ == "__main__":
    start_client()

