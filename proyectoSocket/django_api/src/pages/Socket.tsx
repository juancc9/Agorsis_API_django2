import React, { useEffect, useState } from 'react';

const WebSocketComponent: React.FC = () => {
    const [socket, setSocket] = useState<WebSocket | null>(null);

    useEffect(() => {
        const createSocket = () => {
            const newSocket = new WebSocket('ws://localhost:8000/ws/objects/');

            newSocket.onopen = () => {
                console.log('Conectado a WebSocket');
                newSocket.send(JSON.stringify({ message: 'Hola desde el cliente' }));
            };

            newSocket.onmessage = (event) => {
                const data = JSON.parse(event.data);
                console.log('Mensaje recibido:', data.message);
            };

            newSocket.onclose = () => {
                console.log('Desconectado de WebSocket. Reintentando en 1 segundo...');
                setTimeout(createSocket, 1000); // Reintentar después de 1 segundo
            };

            newSocket.onerror = (error) => {
                console.error('Error en WebSocket:', error);
            };

            setSocket(newSocket);
        };

        createSocket();

        return () => {
            socket?.close();
        };
    }, []);

    return (
        <div>
            <h1>WebSocket Demo</h1>
        </div>
    );
};

export default WebSocketComponent;
