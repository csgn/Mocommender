import axios from "axios";
import { useEffect, useState } from "react";
import CardModal from "../modules/components/card-modal";
import CardSlider from "../modules/components/card-slider";
import MovieList from "../modules/pages-components/movie-list";

export default function Home() {
  const [loading, setLoading] = useState(true);
  const [genres, setGenres] = useState([]);

  const getGenres = async () => {
    const _genres = localStorage.getItem("genres");

    if (_genres) {
      setGenres(JSON.parse(_genres));
      return;
    }

    setLoading(true);

    await axios
      .get(`${process.env.NEXT_PUBLIC_API_URL}/genres/`)
      .then((res) => {
        localStorage.setItem("genres", JSON.stringify(res.data));
        setGenres(res.data);
        setLoading(false);
      });
  };

  useEffect(() => {
    getGenres();
  }, []);

  return (
    <>
      <div className="flex flex-col gap-5 pl-10 mt-5 w-full">
        {genres.slice(0, 3).map((genre) => (
          <CardSlider genre={genre} />
        ))}
      </div>
    </>
  );
}
