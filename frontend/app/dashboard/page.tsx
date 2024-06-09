import React from "react";
import Tasks from "../components/Tasks";
import Attendance from "../components/Attendance";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

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
      <div className="flex flex-row justify-center items-center">
        <Tasks />
        <Attendance />
      </div>
      <Footer />
    </div>
  );
};

export default Dashboard;
