import React from "react";
import { Outlet } from "react-router-dom";

export function RootLayout() {
  return (
    <div className="min-h-screen flex flex-col bg-gray-50">
      {/* Área principal del chat */}
      <main className="flex-1 flex flex-col p-4 overflow-y-auto">
        <Outlet />
      </main>

      {/* Input global opcional */}
      <footer className="border-t bg-white p-4">
        <div className="flex items-center space-x-2">
          <input
            type="text"
            placeholder="Escribe tu mensaje..."
            className="flex-1 border rounded px-3 py-2 focus:outline-none focus:ring focus:border-blue-400"
          />
          <button className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
            Enviar
          </button>
        </div>
      </footer>
    </div>
  );
}
