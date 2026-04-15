import React from "react";
import { useChatbot } from "../hooks/useChatbook";
import GenreLayout from "../components/GenreLayout";

export default function ChatBook() {
  const { genre, messages, sendMessage, changeGenre } = useChatbot();

  return (
    <GenreLayout genre={genre}>
      {/* Mensajes */}
      <div className="flex-1 overflow-y-auto p-6 space-y-4 font-sans text-base">
        {messages.map((m, i) => (
          <div
            key={i}
            className={`flex ${m.role === "user" ? "justify-end" : "justify-start"}`}
          >
            <div
              className={`px-4 py-2 rounded-lg max-w-xs shadow ${
                m.role === "user"
                  ? "bg-blue-600 text-white"
                  : "bg-gray-200 text-white"
              }`}
            >
              {m.role === "assistant" && <span className="mr-2">💡</span>}
              {m.text}
            </div>
          </div>
        ))}
      </div>

      {/* Input */}
      <div className="p-4 flex gap-2 border-t bg-white/80 backdrop-blur-sm">
        <input
          type="text"
          className="flex-1 border rounded-lg px-3 py-2 focus:outline-none focus:ring focus:border-purple-400 font-sans text-base"
          placeholder="Escribe tu mensaje..."
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              sendMessage((e.target as HTMLInputElement).value);
              (e.target as HTMLInputElement).value = "";
            }
          }}
        />
        <button
          onClick={() => changeGenre("romance")}
          className="bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700 transition font-sans text-base"
        >
          Cambiar género
        </button>
      </div>
    </GenreLayout>
  );
}
