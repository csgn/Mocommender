import { useState } from "react";
import { FaPlay } from "react-icons/fa";
import { AiFillLike, AiFillDislike, AiFillInfoCircle } from "react-icons/ai";

export default function CardItem({ src, cbs }) {
  const [showContent, setShowContent] = useState(false);
  const [loading, setLoading] = useState(false);

  return (
    <div className="w-full sm:w-1/2 md:w-1/4 xl:w-1/6 p-3">
      <div
        className="relative hover:cursor-pointer group hover:scale-105 hover:ease-in transition duration-150"
        onPointerEnter={() => setShowContent(true)}
        onPointerLeave={() => setShowContent(false)}
      >
        <img
          className={`h-full w-full object-cover rounded-lg ${
            showContent && "group-hover:blur-sm group-hover:brightness-50"
          }`}
          src={src}
        />
        {showContent && (
          <>
            <div className="absolute top-[10px] right-[10px] transition duration-150 hover:ease-in-out hover:scale-105 hover:animate-pulse">
              <AiFillInfoCircle
                size="48"
                color="#fff"
                onClick={cbs.handleInfo}
              />
            </div>
            <div className="absolute top-1/2 left-1/2 translate-y-[-50%] translate-x-[-50%]">
              {loading ? (
                <Spinner />
              ) : (
                <FaPlay
                  size="64"
                  color="#fff"
                  className="transition duration-150 ease-in-out hover:scale-125 hover:animate-pulse"
                  onClick={cbs.handlePlay}
                />
              )}
            </div>
            <div className="absolute bottom-0 left-1/2 translate-x-[-50%] flex items-center gap-5 w-full justify-center p-3">
              <i className="hover:rotate-[10deg] transition duration-150 hover:ease-in-out hover:scale-150 ">
                <AiFillDislike
                  size="32"
                  color="#fff"
                  onClick={cbs.handleDislike}
                />
              </i>

              <i className="hover:rotate-[10deg] transition duration-150 hover:ease-in-out hover:scale-150">
                <AiFillLike size="32" color="#fff" onClick={cbs.handleLike} />
              </i>
            </div>
          </>
        )}
      </div>
    </div>
  );
}
