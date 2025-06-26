#nesse script, o objetivo é verificar de forma periodica se:
#  o servidor esta ativo e se não tiver, inicializa
import socket
import os
import time
import subprocess

HOST = "127.0.0.1"
PORT = 12345

def servidor_ativo(host, port):
# tenta se conectar no servidor pra verificar se esta ativo
    try:
#espera alguns segundos e verifica se o servidor esta ativo        
        with socket.create_connection((host, port), timeout=3 ):
            return True # se a conexao for bem sucedida retorna true
    except:
        return False # se nao, false


def inicializa_servidor():
#inicializa o servidor principal em segundo plano
    print("Iniciando o servidor principal...")
    subprocess.Popen(["python3", "server.py"])

if __name__ == "__main__":
    while True:
        if not servidor_ativo(HOST, PORT):
            print("O servidor principal nao esta ativo. Inicializando...")
            inicializa_servidor()
        else:
            print("O servidor principal esta ativo!")
        time.sleep(5) # espera 5s antes de verificar novamente

