// src/App.js
import React, { useState } from "react";
import ChatBox from "./components/ChatBox";
import { consult } from "./api/consult";

function App() {
  const [symptom, setSymptom] = useState("");
  const [chats, setChats] = useState([]);

  const handleSend = async () => {
    if (!symptom.trim()) return;

    const newChats = [...chats, { sender: "user", text: symptom }];
    setChats(newChats);
    setSymptom("");

    try {
      const reply = await consult(symptom);
      setChats([...newChats, { sender: "system", text: reply }]);
    } catch (err) {
      setChats([...newChats, { sender: "system", text: "Error contacting backend." }]);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Healthcare Chatbot</h1>
      <ChatBox chats={chats} />
      <input
        type="text"
        value={symptom}
        onChange={(e) => setSymptom(e.target.value)}
        placeholder="Describe your symptoms..."
        style={{ width: "70%", marginRight: "10px" }}
      />
      <button onClick={handleSend}>Send</button>
    </div>
  );
}

export default App;
