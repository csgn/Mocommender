import { useEffect, useRef, useState } from "react";

import { AiFillCloseCircle } from "react-icons/ai";

export default function CardModal({ toggle, setToggle, children }) {
  const ref = useRef(null);

  if (ref.current && toggle.e) {
    const x =
      toggle.e.clientX - window.innerWidth / 2 + ref.current.offsetWidth / 2;
    const y =
      toggle.e.clientY - window.innerHeight / 2 + ref.current.offsetHeight / 2;

    ref.current.style.transformOrigin = `${x}px ${y}px`;
  }

  document.body.style.overflow = toggle.t ? "hidden" : "auto";

  return (
    <>
      <div
        className={`fixed top-0 left-0 w-full h-full overflow-auto z-50 ${
          !toggle.t ? "pointer-events-none" : "pointer-events-auto"
        }`}
      >
        <div
          ref={ref}
          className={`${
            toggle.t ? "scale-100 opacity-100" : "scale-0 opacity-0"
          } rounded-tr-lg rounded-tl-lg transition duration-700 absolute top-[5vh] left-[50%] -translate-x-2/4 min-w-[850px] max-w-[1250px] bg-[#181818] h-fit min-h-[100vh] text-white shadow-[0_0_0_100000px_rgba(0,0,0,0.7)]`}
        >
          <div
            className="z-10 absolute top-5 right-5 hover:scale-110 hover:opacity-100 opacity-30 transition duration-250 cursor-pointer"
            onClick={() => {
              setToggle({
                t: false,
              });
            }}
          >
            <AiFillCloseCircle size={40} />
          </div>
          {children}
        </div>
      </div>
    </>
  );
}
