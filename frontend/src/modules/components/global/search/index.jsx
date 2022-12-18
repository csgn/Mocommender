import { useRouter } from "next/router";
import { useEffect, useRef, useState } from "react";
import { FaSearch } from "react-icons/fa";
import useClickOutside from "../../../hooks/useClickOutside";

export default function Search() {
  const ref = useRef(null);
  const r2 = useRef(null);
  const router = useRouter();

  const [term, setTerm] = useState("");
  const [t, setT] = useState(false);

  useEffect(() => {
    if (router.pathname !== "/search") {
      setTerm('');
      setT(false);
      localStorage.setItem("beforePath", router.asPath);
    }
  }, [router]);

  useClickOutside(() => {
    setT(false);
  }, [ref, r2]);

  useEffect(() => {
    if (term.length === 0) {
      router.replace(localStorage.getItem("beforePath"), null, { shallow: true });
    } else {
      router.replace(
        {
          pathname: "/search",
          query: {
            q: term,
          },
        },
        null,
        { shallow: true }
      );
    }
  }, [term]);

  useEffect(() => {
    if (router.pathname === "/search") {
      setT(true);
    }
  }, [t]);

  return (
    <>
      <div
        className={`flex flex-row gap-5  items-center ${
          t ? "bg-[#000] border-white border-[0.5px]" : ""
        } p-2 rounded-sm ${t ? "w-50" : "w-8"} ${
          t ? "pointer-events-auto" : "pointer-events-none"
        }`}
      >
        <div
          ref={ref}
          className="pointer-events-auto cursor-pointer"
          onClick={() => {
            setT(!t);
          }}
        >
          <FaSearch color="white" ref={ref} className="" />
        </div>
        <input
          ref={r2}
          className={`outline-none text-white bg-[#000] w-full  ${
            t ? "" : "overflow-hidden"
          }`}
          placeholder="Titles, people, genres"
          onChange={(e) => setTerm(prev => e.target.value)}
        />
      </div>

    </>
  );
}
