// src/components/ChatBox.js
import React from "react";

const ChatBox = ({ chats }) => {
  return (
    <div>
      {chats.map((msg, index) => (
        <div
          key={index}
          style={{
            backgroundColor: msg.sender === "user" ? "#d1f0d1" : "#f8d7da",
            padding: "10px",
            margin: "10px 0",
            borderRadius: "6px",
          }}
        >
          <strong>{msg.sender}: </strong>
          {msg.text}
        </div>
      ))}
    </div>
  );
};

export default ChatBox;
