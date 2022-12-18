import { useEffect, useState } from "react";
import CardModal from "../../components/card-modal";

export default function MovieItemModal({ toggle, setToggle, data, setData }) {
  useEffect(() => {
    if (!toggle) {
      setData(null);
    }
  }, [toggle]);

  return (
    <>
      <CardModal toggle={toggle} setToggle={setToggle}>
        <div className="flex flex-col h-full gap-1">
          <div className="flex flex-[2]">
            {data?.backdropPath && (
              <div className="relative">
                <img
                  className="rounded-tr-lg rounded-tl-lg"
                  src={`https://image.tmdb.org/t/p/original${data?.backdropPath}`}
                />
                <div className="absolute w-full bottom-0 pt-32 bg-gradient-to-t from-[#181818] to-transparent"></div>
              </div>
            )}
          </div>
          <div className="flex flex-auto p-5">
            <span>{data?.overview}</span>
          </div>
          <div className="flex  flex-auto p-5">FOOTER</div>
        </div>
      </CardModal>
    </>
  );
}
