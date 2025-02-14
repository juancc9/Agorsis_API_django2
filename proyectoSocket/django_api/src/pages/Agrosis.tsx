const socket = new WebSocket('ws://localhost:8000/ws/objects/');

socket.onopen = () => {
    console.log('Conectado a WebSocket');
};

socket.onmessage = (event) => {
    console.log('Mensaje recibido:', event.data);
};

socket.onclose = () => {
    console.log('Desconectado de WebSocket');
};

socket.onerror = (error) => {
    console.error('Error en WebSocket:', error);
};
