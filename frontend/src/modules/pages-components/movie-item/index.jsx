import axios from "axios";
import { useEffect, useState } from "react";

import { CardItem } from "../../components/card";
import Spinner from "../../components/global/spinner";

export default function MovieItem({ el, setSelected, setToggle }) {
  const [loading, setLoading] = useState(true);
  const [images, setImages] = useState({
    posterPath: null,
    backdropPath: null,
  });

  const getPosterPath = async () => {
    await axios
      .get(
        `https://api.themoviedb.org/3/movie/${el.imdb_id}?api_key=27e5eccb8a9dccab98e669f1be3cc20d`
      )
      .then((res) => {
        setImages({
          posterPath: res.data.poster_path,
          backdropPath: res.data.backdrop_path,
        });
        setLoading(false);
      });
  };

  const cbs = {
    handlePlay: () => {
      console.log("played");
    },
    handleLike: () => {
      console.log("liked");
    },
    handleDislike: () => {
      console.log("disliked");
    },
    handleInfo: (e) => {
      setSelected({
        ...el,
        backdropPath: images.backdropPath,
      });
      setToggle({
        t: true,
        e: e,
      });
    },
  };

  useEffect(() => {
    getPosterPath();
  }, []);

  if (loading) return <Spinner />;

  return (
    <CardItem
      src={`https://image.tmdb.org/t/p/original${images.posterPath}`}
      cbs={cbs}
    />
  );
}
