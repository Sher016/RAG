// src/components/FantasyScene.tsx
import { Canvas, useFrame } from "@react-three/fiber";
import { OrbitControls, Stars } from "@react-three/drei";
import { useRef } from "react";
import type { Group } from "three";

function Tree({ position }: { position: [number, number, number] }) {
     const ref = useRef<Group>(null!);
  useFrame(() => {
    if (ref.current) ref.current.rotation.y += 0.001; // movimiento suave
  });
  return (
    <group ref={ref} position={position}>
      <mesh>
        <cylinderGeometry args={[0.2, 0.2, 2]} />
        <meshStandardMaterial color="brown" />
      </mesh>
      <mesh position={[0, 2, 0]}>
        <coneGeometry args={[2, 4, 8]} />
        <meshStandardMaterial color="green" />
      </mesh>
    </group>
  );
}

export default function FantasyScene() {
  return (
      <Canvas>
          <color attach="background" args={["#d8a7f9"]} />
          <fog attach="fog" args={["#d8a7f9", 10, 50]} />
      <ambientLight intensity={0.5} />
      <directionalLight position={[10, 10, 5]} intensity={1} />
      <OrbitControls />

      <Stars radius={100} depth={50} count={5000} factor={4} fade />
      <mesh position={[0, 0, -20]}>
        <boxGeometry args={[10, 15, 10]} />
        <meshStandardMaterial color="purple" />
      </mesh>

      {/* Árboles a los lados del camino */}
      <Tree position={[-5, 0, -10]} />
      <Tree position={[5, 0, -10]} />
      <Tree position={[-7, 0, -5]} />
      <Tree position={[7, 0, -5]} />

      {/* Camino central */}
      <mesh rotation={[-Math.PI / 2, 0, 0]} position={[0, -1, 0]}>
        <planeGeometry args={[50, 10]} />
        <meshStandardMaterial color="gray" />
      </mesh>

      {/* Cielo morado/rosado */}
      <color attach="background" args={["#d8a7f9"]} />
      <fog attach="fog" args={["#d8a7f9", 10, 50]} />
    </Canvas>
  );
}
