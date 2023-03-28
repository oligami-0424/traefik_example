//ボタン登録 ---------------------------------------------------------
document.addEventListener("DOMContentLoaded", function () {
    const text_str = document.getElementById("text_str");
    const received_text = document.getElementById("received_text");
    var send_array = [];

    const websocket = new WebSocket("wss://oligami.ml:8081/wss/traefik_example/");
    const websocket2 = new WebSocket("wss://oligami.ml:8082/wss/traefik_example/");
    const websocket3 = new WebSocket("wss://oligami.ml:8082/wss/traefik_example2/");

    websocket.onmessage = (e) => {
        message = e.data;
        console.log(message);

        var li = document.createElement('li');
        if (send_array.includes(message))
            li.style.color = 'blue';
        var text = document.createTextNode(message);
        li.appendChild(text);
        received_text.appendChild(li);
    };

    document.getElementById('writeBtn').addEventListener("click", () => {
        websocket.send(text_str.value);
        send_array.push(text_str.value);
    })

    const websocket4 = new WebSocket("wss://oligami.ml:8081/wss/");
    const websocket5 = new WebSocket("ws://oligami.ml:53005");
})
