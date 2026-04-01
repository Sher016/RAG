import React from "react";
import { Navigate } from "react-router-dom";

interface AuthGuardProps {
  children: React.ReactNode;
}

export function AuthGuard({ children }: AuthGuardProps) {
  const isAuthenticated = true; // aquí luego conectas con tu store o contexto

  if (!isAuthenticated) {
    return <Navigate to="/signin" replace />;
  }

  return <>{children}</>;
}
