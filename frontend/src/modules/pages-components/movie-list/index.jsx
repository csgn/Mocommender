import axios from "axios";
import { useEffect, useState } from "react";

import { CardGrid, CardItem } from "../../components/card";
import CardModal from "../../components/card-modal";
import Spinner from "../../components/global/spinner";
import MovieItem from "../movie-item";

export default function MovieList({ ids }) {
  const [loading, setLoading] = useState(true);
  const [movies, setMovies] = useState([]);

  const [selected, setSelected] = useState(null);
  const [toggle, setToggle] = useState({
    t: false,
  });


  if (loading) return <Spinner />;

  return (
    <>
      <CardGrid>
        {movies.map((el) => (
          <MovieItem el={el} setSelected={setSelected} setToggle={setToggle} />
        ))}
      </CardGrid>
      <CardModal
        toggle={toggle}
        setToggle={setToggle}
        data={selected}
        setData={setSelected}
      />
    </>
  );
}
