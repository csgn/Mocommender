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
      })
      .catch((err) => {
        setLoading(false);
      });
  };

  const getMovieDetail = async () => {
    await axios
      .get(`${process.env.NEXT_PUBLIC_API_URL}/user/movie/${mid}`)
      .then((res) => {
        console.log(res);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const cbs = {
    handleFocus: async () => {
      //getMovieDetail()
    },
    handlePlay: async () => {
      await axios
        .post(`http://127.0.0.1:5000/send`, {
          user_id: 1,
          movie_id: el.id,
        })
        .then((res) => {
          console.log(res);
        });
    },
    handleLike: () => {
      console.log("liked");
    },
    handleDislike: () => {
      console.log("disliked");
    },
    handleInfo: (e) => {
      setSelected &&
        setSelected({
          ...el,
          backdropPath: images.backdropPath,
        });
      setToggle &&
        setToggle({
          t: true,
          e: e,
        });
    },
  };

  useEffect(() => {
    getPosterPath();
  }, [el]);

  if (loading) return <Spinner />;

  return (
    <CardItem
      mid={el.id}
      src={
        images.posterPath
          ? `https://image.tmdb.org/t/p/original${images.posterPath}`
          : "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Image_not_available.png/640px-Image_not_available.png"
      }
      cbs={cbs}
    />
  );
}
