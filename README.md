# Chat Distribuído com Flask-SocketIO

![chat](https://github.com/user-attachments/assets/d14ed128-7a04-4488-95e4-c74d028d0eae)


## Descrição
Este projeto é um sistema de chat em tempo real, que permite comunicação simultânea entre múltiplos usuários via navegador web. O backend é implementado em Python usando Flask e Flask-SocketIO, e o frontend interface web elegante.

## Funcionalidades
- Comunicação simultânea entre vários usuários;
- Broadcast de mensagens para todos os clientes conectados;
- Interface web amigável acessível pelo navegador;
- Uso de WebSocket para comunicação em tempo real;
- Tolerância a falhas com possibilidade de replicação do servidor (em desenvolvimento);

## Tecnologias Utilizadas
- Python 3.10
- Flask
- Flask-SocketIO
- Eventlet
- HTML, CSS e JavaScript (Socket.IO client)

## Como executar

### Pré-requisitos
- Python 3.10 ou superior
- Pip instalado

## Passos para rodar o servidor

### 1. Instalar as dependências:

```bash
pip install -r requirements.txt
```

### 2. Executar o servidor:

```bash
python3 app.py
```

### 3. No navegador abra o endereço:

```bash
https://localhost:5000
```

### 4. Abrir múltiplas abas ou navegadore para testa ro chat em tempo real.

<br>

# Como usar o Chat
    - Digite a mensagem na caixa de texto e pressione Enviar ou Enter.

    - Para sair, feche a aba ou use Ctrl+C no terminal para parar o servidor.


## Estrutura do projeto

```
Chat-distribuido

-app.py
-cliente.py
-server.py
-reply.py
-requirements.txt
-README.md
-static/
    -script.js
    -style.css
    -particles.js
    -favicon.ico
-templates/
    -index.html
```

<br>

# Tolerância e Falhas
Para garantir a disponibilidade contínua do sistema, foi implementado um mecanismo de tolerância a falhas simples e eficaz. Um script adicional chamado `reply.py` é responsável por monitorar o status do servidor principal (`server.py`).

```bash
python3 reply.py
```

Esse monitoramento é feito por meio de tentativas de conexão com o servidor. Se a conexão for recusada, o script entende que o servidor está inativo e o reinicia automaticamente com `subprocess.Popen`.

```python
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
```

A checagem ocorre em intervalos regulares (a cada 5 segundos), o que permite reações rápidas em caso de falha. Com isso, o sistema assegura que o serviço de chat esteja sempre disponível, mesmo após falhas inesperadas.

<br>

# Considerações finais

Este sistema é um projeto acadêmico desenvolvido para a disciplina de Sistemas Distribuídos da Universidade Federal de Rio Grande (FURG), integrando conceitos de redes, concorrência e desenvolvimento web.


- **Redes:** Foi utilizado sockets TCP/IP para comunicação entre cliente e servidor, além de WebSockets para comunicação em tempo real via navegador, implementando um protocolo mais eficiente que o polling tradicional.

- **Concorrência:** O servidor web tradicional foi adaptado com `eventlet` para lidar com múltiplas conexões simultâneas de forma eficiente sem precisar criar muitas threads, técnica chamada de programação assíncrona, e ajuda o servidor e a ser mais leve e rápido mesmo com muitos usuário conectados.

    Enquanto o servidor de terminal foi utilizado múltiplas threads (`threading.Thread`) para permitir que vários clientes trocassem mensagens ao mesmo tempo. Então para cada cliente que se conecta, o servidor cria uma "linha de execução separada" como abrir uma aba nova pra cada usuário, permitindo que ele continue atendendo outros usuários sem travar.

- **Desenvolvimento Web:** O chat possui uma interface acessível via navegador, utilizando HTML, CSS e Js com a biblioteca cliente do Socket.IO.

- **Tolerância a Falhas:** O trabalho também prevê a implementação de tolerância a falhas através da replicação do servidor, garantindo maior robustez no ambiente distribuído. Demonstra a aplicação prática de conceitos da cadeira de sistemas distribuídos, como confiabilidade, disponibilidade e automação de recuperação.

## Autoria
    Flávia Cristina G. dos Passos - 157378
