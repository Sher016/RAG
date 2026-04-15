import { leftFantasy, rightFantasy } from "../../../assets/images";
import "../styles/GenreStyle.css";

export default function GenreLayout({ genre, children }: { genre: string; children: React.ReactNode }) {
  const backgrounds: Record<string, string> = {
    fantasia: "genre-background-fantasia",
    romance: "genre-background-romance",
    terror: "genre-background-terror",
    drama: "genre-background-drama",
    default: "",
  };

  const style = backgrounds[genre] || backgrounds.default;

  return (
    <div className={`genre-layout ${style}`}>
      {genre === "fantasia" && (
        <>
          <img src={leftFantasy} alt="Decoración izquierda" className="genre-image genre-left" />
          <img src={rightFantasy} alt="Decoración derecha" className="genre-image genre-right" />
        </>
      )}
      <div className="chat-container">
        {children}
      </div>
    </div>
  );
}
