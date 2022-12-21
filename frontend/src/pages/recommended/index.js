import axios from "axios";
import Link from "next/link";

import { useState, useEffect } from "react";
import { CardGrid } from "../../modules/components/card";
import Spinner from "../../modules/components/global/spinner";
import MovieItem from "../../modules/pages-components/movie-item";
import MovieItemModal from "../../modules/pages-components/movie-item-modal";

export default function Recommended() {
  const [recommends, setRecommended] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selected, setSelected] = useState({});
  const [toggle, setToggle] = useState(false);

  const getRecommended = async () => {
    await axios
      .get(
        `${process.env.NEXT_PUBLIC_API_URL}/users/1/recommend/?popularity=desc`
      )
      .then((res) => {
        setRecommended(res.data.map((el) => el.movie));
        setLoading(false);
      })
      .catch((err) => {
        setLoading(false);
      });
  };

  useEffect(() => {
    getRecommended();
  }, []);

  if (loading) {
    return <Spinner />;
  }

  return (
    <>
      <div className="w-full">
        {recommends.length > 0 ? (
          <CardGrid>
            {recommends.map((el) => (
              <MovieItem
                el={el}
                setSelected={setSelected}
                setToggle={setToggle}
              />
            ))}
          </CardGrid>
        ) : (
          <div className="flex p-10 items-center justify-center text-white w-full">
            There is no recommendation for you.&nbsp;&nbsp;
            <Link className="text-red-500" href="/">
              Explore
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
