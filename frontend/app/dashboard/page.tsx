import React from "react";
import Tasks from "../components/Tasks";
import Attendance from "../components/Attendance";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import Plugin from "../components/Plugin";

const Dashboard = () => {
  return (
    <div
      className="min-h-screen flex flex-col"
      style={{
        background:
          "radial-gradient(circle 72rem at 80% 75%, #00A3FF, #010127)",
      }}
    >
      <Navbar />
      <div className="flex flex-col justify-center items-center m-5">
        <div className="flex flex-row">
        <Tasks />
        <Attendance />
        </div>
        <Plugin/>
      </div>
      <Footer />
    </div>
  );
};

export default Dashboard;
