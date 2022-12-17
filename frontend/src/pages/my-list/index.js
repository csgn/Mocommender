import axios from "axios";
import { useEffect, useState } from "react";
import Spinner from "../../modules/components/global/spinner";
import MovieList from "../../modules/pages-components/movie-list";

export default function MyList() {
  const [user, setUser] = useState([]);
  const [loading, setLoading] = useState(true);

  const getUser = async () => {
    setLoading(true);
    await axios
      .get(`http://127.0.0.1:8000/user/1/`)
      .then((res) => {
        setUser(res.data);
        setLoading(false);
      })
      .catch((err) => {
        setLoading(false);
      });
  };

  useEffect(() => {
    getUser();
  }, []);

  if (loading) return <Spinner />;

  return (
    <>
      <MovieList ids={user.user_movie} />
    </>
  );
}
