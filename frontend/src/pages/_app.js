import MainLayout from "../modules/components/layout";
import "../styles/globals.css";

export default function App({ Component, pageProps }) {
  return (
    <MainLayout>
      <Component {...pageProps} />
    </MainLayout>
  );
}
