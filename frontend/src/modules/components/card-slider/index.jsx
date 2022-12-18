import axios from "axios";
import { useEffect, useState } from "react";
import MovieItem from "../../pages-components/movie-item";
import CardModal from "../card-modal";

import { AiOutlineDoubleRight } from "react-icons/ai";
import MovieItemModal from "../../pages-components/movie-item-modal";
import CardGrid from "../card/CardGrid";

export default function CardSlider({ genre }) {
  const [selected, setSelected] = useState(null);
  const [movies, setMovies] = useState([]);
  const [moviesAll, setMoviesAll] = useState([]);

  const [toggleMovieItem, setToggleMovieItem] = useState({
    t: false,
  });

  const [toggleMoviesModal, setToggleMoviesModal] = useState({
    t: false,
  });

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
    setToggleMoviesModal({ t: true });

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
      <div className="flex flex-col gap-5">
        <span className="text-[24px] leading-5 text-white">{genre.name}</span>
        <div className="flex flex-row gap-5 p-auto overflow-y-auto">
          {movies.map((el) => (
            <MovieItem
              el={el}
              setSelected={setSelected}
              setToggle={setToggleMovieItem}
            />
          ))}
          <div
            className="h-100 flex transition justify-center items-center opacity-10 hover:bg-[#ffffff55] duration-300 hover:opacity-50 rounded-md p-10 mr-5 cursor-pointer"
            onClick={getMoviesAll}
          >
            <AiOutlineDoubleRight size="48" color="#fff" />
          </div>
        </div>
      </div>
      {toggleMovieItem && (
        <MovieItemModal
          toggle={toggleMovieItem}
          setToggle={setToggleMovieItem}
          data={selected}
          setData={setSelected}
        />
      )}
      {toggleMoviesModal && (
        <CardModal toggle={toggleMoviesModal} setToggle={setToggleMoviesModal}>
          <div className="flex flex-col gap-5">
            <div className="flex justify-center p-24">
              <span className="text-white text-[50px] font-semibold tracking-wide">
                {genre.name}
              </span>
            </div>
            <CardGrid>
              {moviesAll.map((el) => (
                <MovieItem el={el} />
              ))}
            </CardGrid>
          </div>
        </CardModal>
      )}
    </>
  );
}
