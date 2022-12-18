import { useEffect } from "react";

export default function useClickOutside(callback, except) {
  useEffect(() => {
    let event = (e) => {
      const t = except
        .map((m) => {
          return m?.current?.contains(e.target);
        })
        .filter((f) => {
          return f;
        });

      if (t.length === 0) {
        callback();
      }
    };
    document.addEventListener("pointerdown", event);
    return () => document.removeEventListener("pointerdown", event);
  }, []);
}
