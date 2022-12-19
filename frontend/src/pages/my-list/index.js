import axios from "axios";
import { useEffect, useState } from "react";
import { CardGrid } from "../../modules/components/card";
import Spinner from "../../modules/components/global/spinner";
import MovieItem from "../../modules/pages-components/movie-item";
import MovieItemModal from "../../modules/pages-components/movie-item-modal";

import { MdLocalMovies } from "react-icons/md";
import Link from "next/link";

export default function MyList() {
  const [userMovieList, setUserMovieList] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selected, setSelected] = useState({});
  const [toggle, setToggle] = useState(false);

  const getUserMovieList = async () => {
    await axios
      .get(`${process.env.NEXT_PUBLIC_API_URL}/users/1/movies/`)
      .then((res) => {
        setUserMovieList(res.data.map((_) => _.movie));
        setLoading(false);
      })
      .catch((err) => {
        setLoading(false);
      });
  };

  useEffect(() => {
    getUserMovieList();
  }, []);

  if (loading) return <Spinner />;

  return (
    <>
      <div className="w-full">
        {userMovieList.length > 0 ? (
          <CardGrid>
            {userMovieList.map((el) => (
              <MovieItem
                el={el}
                setSelected={setSelected}
                setToggle={setToggle}
              />
            ))}
          </CardGrid>
        ) : (
          <div className="flex p-10 items-center justify-center text-white w-full flex-col">
            <MdLocalMovies size={128} color="#333" />
            <span className="text-gray-500">
              You haven't added any movies to your list yet
            </span>
            &nbsp;
            <Link href="/" className="text-red-500 underline">
              Explore Trends
            </Link>
          </div>
        )}
      </div>
      <MovieItemModal
        toggle={toggle}
        setToggle={setToggle}
        data={selected}
        setData={setSelected}
      />
    </>
  );
}
