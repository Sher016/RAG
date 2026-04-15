import React from "react";
import { Outlet } from "react-router-dom";
import Sidebar from "./sidebar/SideBar";

export function RootLayout() {
  return (
    <div className="flex w-full h-screen overflow-hidden">
      <Sidebar />
      <main className="flex-1 h-full overflow-y-auto">
        <Outlet />
      </main>
    </div>
  );
}



