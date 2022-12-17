import Header from "./header";

export default function MainLayout({ children }) {
  return (
    <div className="container-fluid">
      <div className="flex-1 flex flex-col overflow-hidden">
        <Header />
        <div className="flex h-full bg-[#141414]">
          <main className="flex flex-col w-full h-full overflow-x-hidden overflow-y-auto mb-14 mt-14">
            <div className="flex pt-10 pb-10 bg-[#141414]">{children}</div>
          </main>
        </div>
      </div>
    </div>
  );
}
