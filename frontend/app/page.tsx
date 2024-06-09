import Image from "next/image";
import landing from "../public/landing.png";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";

export default function Widget() {
  return (
    <div
      className="min-h-screen flex flex-col"
      style={{
        background:
          "radial-gradient(circle 72rem at 80% 75%, #00A3FF, #010127)",
      }}
    >
      <Navbar />

      <div className="flex text-white px-8 pl-16">
        <div className="container mx-auto flex flex-col md:flex-row items-center py-13 h-[75vh] mx  -10">
          <div className="md:w-1/2 space-y-6 p-[1.75rem]">
            <h1 className="text-4xl font-bold">
              MUSE: Inspire With Summaries: Summarizes In A Way That Inspires
              Further Learning.
            </h1>
            <ul className="list-disc list-inside space-y-2">
              <li>
                The AI tool summarizes the video into bite-sized categories or
                chapters.
              </li>
              <li>
                You can directly add a YouTube URL and click 'submit' to
                generate a short and informative summary.
              </li>
              <li>Supports Multiple Languages</li>
              <li>High accuracy</li>
            </ul>
            <button className="bg-blue-600 text-white px-6 py-3 rounded-lg">
              Try MUSE for free
            </button>
          </div>
          <div className="md:w-1/2 mt-8 md:mt-0 flex justify-center">
            <Image src={landing} height={500} width={500} alt="landing" />
          </div>
        </div>
      </div>

      <Footer />
    </div>
  );
}
