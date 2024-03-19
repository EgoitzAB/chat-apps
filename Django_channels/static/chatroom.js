document.addEventListener('DOMContentLoaded', function() {
  const chatForm = document.getElementById('chat-form');
  const chatText = document.getElementById('chat-text');
  const inputField = document.getElementById('input');

  const roomName = '{{ room_name }}';
  const userUsername = '{{ request.user.username }}';
  const wsProtocol = window.location.protocol === 'https:' ? 'wss://' : 'ws://';
  const chatSocket = new WebSocket(
      wsProtocol + window.location.host + '/ws/chat/' + roomName + '/'
  );

  chatSocket.onmessage = function(e) {
      const data = JSON.parse(e.data);
      chatText.value += data.username + ': ' + data.message + '\n';
  };

  chatForm.onsubmit = function(e) {
      e.preventDefault();
      const messageInput = inputField.value;
      chatSocket.send(JSON.stringify({
          'message': messageInput,
          'username': userUsername,
      }));
      inputField.value = '';
  };
});
