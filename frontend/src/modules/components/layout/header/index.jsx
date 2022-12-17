import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import Link from "next/link";

import routes from "../../../../static/routes";

export default function Header() {
  const router = useRouter();

  const [active, setActive] = useState(0);
  const [scroll, setScroll] = useState(false);

  useEffect(() => {
    setActive(
      routes.filter((el) => el.href === router.pathname).map((el) => el.id)[0]
    );
  }, [router]);

  useEffect(() => {
    const handleScroll = (event) => {
      setScroll(window.scrollY > 48);
    };

    const scroll = window.addEventListener("scroll", handleScroll);

    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  return (
    <>
      <header
        className={`flex justify-between items-center ${
          scroll ? "bg-[#0b0b0b]" : "bg-transparent"
        } fixed top-0 z-30 w-full pl-10 pt-5 pb-5 pr-10`}
      >
        <div className="flex text-white items-center">
          <ul className="flex flex-row gap-5 items-center">
            <Link href="/">
              <img src="/logo.png" width={164} />
            </Link>
            {routes.map((el) => (
              <li
                key={el.id}
                className={` 
                    hover:opacity-50 transition duration-300 tracking-wide font-semibold
                 ${
                   active === el.id ? "#fff pointer-events-none" : "opacity-70"
                 } text-sm text-white
                `}
              >
                <Link href={el.href}>{el.text}</Link>
              </li>
            ))}
          </ul>
        </div>
        <div className="flex">
          <div>Sign Out</div>
        </div>
      </header>
    </>
  );
}
