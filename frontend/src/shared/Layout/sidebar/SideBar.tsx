import React from "react";
import "./Sidebar.css"; // importa el CSS específico

import { darkfantasy } from "../../../assets/images";

export default function Sidebar() {
  return (
    <aside className="sidebar">

     <div className="flex items-center gap-10 border border-red-500">
  <div className="sidebar-icon border border-blue-500">
    <img src={darkfantasy} alt="Icono" />
  </div>

  <h2 className="font-times text-xl tracking-tight border border-green-500">
    Contador de historias
  </h2>
</div>



      <div className="flex flex-col space-y-3">
        <button className="bg-[var(--color-tertiary-container)] text-[var(--color-tertiary)] px-4 py-2 rounded-sm font-body hover:opacity-90 transition">
          Nueva narrativa
        </button>
        <button className="bg-blue-600 text-white px-4 py-2 rounded-sm font-body shadow-inner">
          Narrativa actual
        </button>
      </div>

      {/* Secciones */}
      <nav className="flex flex-col space-y-2 mt-4 font-times">
        <button className="hover:text-[var(--color-primary)]">Library</button>
        <button className="hover:text-[var(--color-primary)]">Género del Grimorio</button>
        <button className="hover:text-[var(--color-primary)]">Crónicas</button>
      </nav>
    </aside>
  );
}
