import { Link } from "react-router-dom";
import { Canvas } from "@react-three/fiber"; 
import { OrbitControls } from "@react-three/drei";

export default function HomePage() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-purple-500 to-blue-600 text-white">
      <h1 className="text-4xl font-bold mb-6">Bienvenida a la App</h1>
      <p className="mb-8 text-lg">Explora el ChatBook con un solo click</p>
      <Link
        to="/chat-book"
        className="px-6 py-3 bg-white text-purple-700 font-semibold rounded-lg shadow-lg hover:bg-purple-100 transition"
      >
        Ir al ChatBook 🚀
      </Link>
      <div className="w-full h-96 mt-12">
        <Canvas>
          <ambientLight />
          <pointLight position={[10, 10, 10]} />
          <mesh rotation={[0.4, 0.2, 0]}>
            <boxGeometry args={[2, 2, 2]} />
            <meshStandardMaterial color="orange" />
          </mesh>
          <OrbitControls />
        </Canvas>
      </div>
     
    </div>
  );
}
