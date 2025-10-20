const userInput = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");
const sendBtn = document.getElementById("send-btn");

function appendMessage(sender, text) {
    const div = document.createElement("div");
    div.classList.add(sender);
    div.innerHTML = text;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
    const text = userInput.value.trim();
    if (!text) return;

    appendMessage("user", `<b>You:</b> ${text}`);
    userInput.value = "";

    try {
        const res = await fetch("/chatbot", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: text })
        });

        if (!res.ok) throw new Error("HTTP " + res.status);

        const data = await res.json();
        // Use data.reply
        appendMessage("bot", `<b>Bot:</b> ${data.reply}`);
    } catch (err) {
        console.error("Fetch error:", err);
    }
}


sendBtn.addEventListener("click", sendMessage);
userInput.addEventListener("keypress", e => {
    if (e.key === "Enter") sendMessage();
});

// Initial bot greeting
appendMessage("bot", "<b>Bot:</b> 👋 Hello! I’m your Payroll Assistant. How can I help you?");


chatBox.scrollTo({
    top: chatBox.scrollHeight,
    behavior: "smooth"
});

appendMessage("bot", "💬 Bot is typing...");
await new Promise(r => setTimeout(r, 800)); // delay
chatBox.lastChild.remove(); // remove typing message
appendMessage("bot", `<b>Bot:</b> ${data.reply}`);
