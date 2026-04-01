import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { chatBookRoutes } from "../modules/chatbook/routes";
import HomePage from "../shared/Layout/MainPage";
import type { AppRouteObject } from "../types/routerTypes";
import { AuthGuard } from "./guards";

function protectRoutes(
  elementsToProtect: AppRouteObject[]
): AppRouteObject[] {
  return elementsToProtect.map((element) => {
    element.element = <AuthGuard>{element.element}</AuthGuard>;
    if (element.children) {
      element.children = protectRoutes(element.children);
    }
    return element;
  });
}

const appRoutes: AppRouteObject[] = [
  {
    path: "/",
    element: <HomePage />, 
  },
  ...protectRoutes(chatBookRoutes),
];

export function RootRouter() {
  const router = createBrowserRouter(appRoutes);
  return <RouterProvider router={router} />;
}
