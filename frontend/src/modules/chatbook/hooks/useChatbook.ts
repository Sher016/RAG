// src/hooks/useChatbot.ts
import { useState } from "react";

export function useChatbot() {
  const [genre, setGenre] = useState<string>("fantasia"); // quemado por ahora
  const [messages, setMessages] = useState<any[]>([]);

  const sendMessage = (text: string) => {
    const fakeResponse = `Respuesta del género ${genre}`;
    setMessages([...messages, { role: "user", text }, { role: "bot", text: fakeResponse }]);
  };

  const changeGenre = (newGenre: string) => {
    setGenre(newGenre);
    setMessages([]); 
  };

  return { genre, messages, sendMessage, changeGenre };
}
