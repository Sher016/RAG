import type { AppRouteObject } from "../../types/routerTypes";
import { RootLayout } from "../../shared/Layout/RootLayout";
import GenreLayout from "./components/GenreLayout";
import ChatBook from "./pages/ChatBook";
import { FaBookOpen } from "react-icons/fa";

export const CHATBOOK_PATH = "/chat-book";

export const chatBookRoutes: AppRouteObject[] = [
  {
    path: CHATBOOK_PATH,
    // sidebar: true,
    // icon: <FaBookOpen />,
    element: <RootLayout />,
    errorElement: <div>Error cargando ChatBook</div>,
    children: [
      {
        index: true,
        // element: <ChatBook/>,
      },
    ],
  },
];