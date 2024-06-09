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
      <JobForm/>
      <Footer />
    </div>
  );
};

export default resume;
