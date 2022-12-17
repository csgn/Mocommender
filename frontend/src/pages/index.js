import { useState } from "react";
import CardModal from "../modules/components/card-modal";

export default function Home() {
  const [toggle, setToggle] = useState({
    t: false,
    e: null,
  });

  return (
    <>
      <button
        className="text-white"
        onClick={(e) => {
          setToggle({
            t: true,
            e: e,
          });
        }}
      >
        open modal
      </button>
      <CardModal toggle={toggle} setToggle={setToggle} />
    </>
  );
}
