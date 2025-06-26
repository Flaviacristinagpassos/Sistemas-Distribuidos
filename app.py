import eventlet
eventlet.monkey_patch()#corrigir bilioteca incompativel

from flask import Flask, render_template
from flask_socketio import SocketIO, send
import webbrowser



app = Flask(__name__)
app.config['SECRET_KEY'] = 'segredo!'
socketio = SocketIO(app, async_mode='eventlet')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(mensagem):
    print("Mensagem recebida:", {mensagem})
    send(mensagem, broadcast=True)

if __name__ == '__main__':
    webbrowser.open('http://localhost:5000')
    print("Servidor iniciado! (em http://localhost:5000)")
    socketio.run(app, host='0.0.0.0', port=5000)

    