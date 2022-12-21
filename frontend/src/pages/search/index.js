import axios from "axios";

import { useRouter } from "next/router";
import { useEffect, useState } from "react";

import { useDebouncedCallback } from "use-debounce";

import Spinner from "../../modules/components/global/spinner";
import MovieItem from "../../modules/pages-components/movie-item";

import { CardGrid } from "../../modules/components/card";
import MovieItemModal from "../../modules/pages-components/movie-item-modal";

export default function Search() {
  const router = useRouter();
  const { q } = router.query;

  const [loading, setLoading] = useState(true);
  const [movies, setMovies] = useState([]);
  const [selected, setSelected] = useState({});
  const [toggle, setToggle] = useState(false);

  const handleQuery = async () => {
    await axios
      .get(`${process.env.NEXT_PUBLIC_API_URL}/movies/?q=${q}`)
      .then((res) => {
        setMovies(res.data);
        setLoading(false);
      });
  };

  const debounced = useDebouncedCallback(handleQuery, 500);

  useEffect(() => {
    const beforePath = localStorage.getItem("beforePath");
    if (!beforePath) return;

    setLoading(true);

    if (!q) {
      router.replace("/", null, {
        shallow: true,
      });
    } else {
      debounced();
    }
  }, [q]);

  if (loading) {
    return <Spinner />;
  }

  return (
    <>
      <div className="w-full">
        {movies.length > 0 ? (
          <CardGrid>
            {movies.map((el) => (
              <MovieItem
                el={el}
                setSelected={setSelected}
                setToggle={setToggle}
              />
            ))}
          </CardGrid>
        ) : (
          <div className="flex p-10 items-center justify-center text-white w-full">
            Your search <i>&nbsp;"{q}"&nbsp;</i> did not have any matches
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
