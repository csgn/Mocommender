import axios from "axios";
import { useState, useEffect } from "react";
import CardSlider from "../../components/card-slider";

export default function MovieSlider({ genre }) {
  const [movies, setMovies] = useState([]);
  const [moviesAll, setMoviesAll] = useState([]);

  const getMovies = async () => {
    await axios
      .get(
        `${process.env.NEXT_PUBLIC_API_URL}/movies/?genre=${genre.id}&limit=5&popularity=desc`
      )
      .then((res) => {
        setMovies(res.data);
      });
  };

  const getMoviesAll = async () => {
    await axios
      .get(
        `${process.env.NEXT_PUBLIC_API_URL}/movies/?genre=${genre.id}&popularity=desc`
      )
      .then((res) => {
        setMoviesAll(res.data);
      });
  };

  useEffect(() => {
    getMovies();
  }, [genre]);

  return (
    <>
      <CardSlider
        title={genre.name}
        movies={movies}
        moviesAll={moviesAll}
        getMoviesAll={getMoviesAll}
      />
    </>
  );
}
