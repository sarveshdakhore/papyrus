import React from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import JobForm from "../components/ResumeForm";

const resume = () => {
  return (
    <div
      className="min-h-screen flex flex-col"
      style={{
        background:
          "radial-gradient(circle 72rem at 80% 75%, #00A3FF, #010127)",
      }}
    >
      <Navbar />
      <div className="flex flex-row m-[60px] text-black">
        <div className="p-[50px] bg-[#d8d9d9b8]  rounded-[30px] ">
          <JobForm/>
        </div>
        <div>
          {/* here comes the resume */}
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default resume;


{/* <html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
  </head>
  <body>
    <div class="flex items-center justify-between w-full p-4 bg-zinc-200 dark:bg-zinc-800 rounded-lg border-2 border-blue-500">
  <span class="text-zinc-800 dark:text-zinc-200">Job Experience</span>
  <svg class="w-4 h-4 text-zinc-800 dark:text-zinc-200" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
  </svg>
</div>
  </body>
</html> */}