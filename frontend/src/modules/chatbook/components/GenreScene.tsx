import { Canvas } from '@react-three/fiber'
import { OrbitControls } from '@react-three/drei'
import FantasyScene from './FantasyScene';

export default function GenreScene({ genre }: { genre: string }) {
  switch (genre) {
    case "fantasia":
      return <FantasyScene />;
    case "romance":
    //   return <RomanceScene />;
    case "terror":
    //   return <TerrorScene />;
    default:
      return null;
  }
}