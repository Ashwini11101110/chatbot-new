async function sendMessage() {
    const input = document.getElementById("userInput");
    const chatbox = document.getElementById("chatbox");
    const message = input.value.trim();

    if (!message) return;

    chatbox.innerHTML += `<div><strong>You:</strong> ${message}</div>`;

    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message })
    });

    const data = await response.json();
    chatbox.innerHTML += `<div><strong>Bot:</strong> ${data.response}</div>`;
    input.value = "";
    chatbox.scrollTop = chatbox.scrollHeight;
}
