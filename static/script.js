const socket = io();

socket.on('message', function(mensagem) {
  const item = document.createElement('li');
  item.textContent = mensagem;
  document.getElementById('mensagens').appendChild(item);
});

document.getElementById('form').addEventListener('submit', function(e) {
  e.preventDefault();  // impede que a página recarregue
  const input = document.getElementById('mensagem');
  if (input.value.trim() !== '') {
    socket.send(input.value);
    input.value = '';
  }
});
