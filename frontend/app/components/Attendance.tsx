"use client";
import React from "react";
import { Doughnut } from "react-chartjs-2";

import { Chart, ArcElement, CategoryScale, DoughnutController } from "chart.js";

Chart.register(DoughnutController, ArcElement, CategoryScale);

const Attendance = () => {
  const data = {
    labels: ["Remaining", "Used"],
    datasets: [
      {
        data: [3, 4],
        backgroundColor: ["white", "#9473F1"],
      },
      
    ],
  };
  const data1 = {
    labels: ["Remaining", "Used"],
    datasets: [
      {
        data: [3, 4],
        backgroundColor: ["white", "#9473F1"],
      },
      
    ],
  };
  const data2 = {
    labels: ["Remaining", "Used"],
    datasets: [
      {
        data: [3, 4],
        backgroundColor: ["white", "#9473F1"],
      },
      
    ],
  };
  const data3 = {
    labels: ["Remaining", "Used"],
    datasets: [
      {
        data: [3, 4],
        backgroundColor: ["white", "#9473F1"],
      },
      
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
  };

  return (
    <div className="flex flex-col items-center justify-center w-[50%]">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="text-white p-4 rounded-lg shadow-lg flex flex-row items-center border border-white border-1" style={{ backgroundColor: 'rgba(53, 64, 85, 0.2)' }}>
          <div className="w-[38%] p-1 mt-2">
            <Doughnut data={data} options={options} width={80} height={80}/>
          </div>
          <div className="flex justify-center items-center flex-col m-4  w-[62%]">
            <h3 className="text-lg font-semibold">Sick leave</h3>
            <ul className="mt-2 space-y-1">
              <li className="flex items-center">
                <span className="w-3 h-3 bg-white rounded-full mr-2"></span>
                Remaining - 3
              </li>
              <li className="flex items-center">
                <span className="w-3 h-3 bg-purple-500 rounded-full mr-2"></span>
                Used - 4
              </li>
              <li className="flex items-center">
                <span className="w-3 h-3 bg-black rounded-full mr-2"></span>
                Total - 7
              </li>
            </ul>
          </div>
        </div>
        <div className="text-white p-4 rounded-lg shadow-lg flex flex-row items-center border border-white border-1" style={{ backgroundColor: 'rgba(53, 64, 85, 0.2)' }}>
        <div className="w-[38%] p-1 mt-2">
            <Doughnut data={data1} options={options} width={80} height={80}/>
          </div>
          <div className="flex justify-center items-center flex-col m-4  w-[62%]">
            <h3 className="text-lg font-semibold">Casual leave</h3>
            <ul className="mt-2 space-y-1">
              <li className="flex items-center">
                <span className="w-3 h-3 bg-white rounded-full mr-2"></span>
                Remaining - 3
              </li>
              <li className="flex items-center">
                <span className="w-3 h-3 bg-purple-500 rounded-full mr-2"></span>
                Used - 4
              </li>
              <li className="flex items-center">
                <span className="w-3 h-3 bg-black rounded-full mr-2"></span>
                Total - 7
              </li>
            </ul>
          </div>
        </div>
        <div className="text-white p-4 rounded-lg shadow-lg flex flex-row items-center border border-white border-1" style={{ backgroundColor: 'rgba(53, 64, 85, 0.2)' }}>
        <div className="w-[38%] p-1 mt-2">
            <Doughnut data={data2} options={options} width={80} height={80}/>
          </div>
          <div className="flex justify-center items-center flex-col m-4 w-[62%]">
            <h3 className="text-lg font-semibold">Unpaid Leave</h3>
            <ul className="mt-2 space-y-1">
              <li className="flex items-center">
                <span className="w-3 h-3 bg-white rounded-full mr-2"></span>
                Remaining - 3
              </li>
              <li className="flex items-center">
                <span className="w-3 h-3 bg-purple-500 rounded-full mr-2"></span>
                Used - 4
              </li>
              <li className="flex items-center">
                <span className="w-3 h-3 bg-black rounded-full mr-2"></span>
                Total - 7
              </li>
            </ul>
          </div>
        </div>
        <div className="text-white p-4 rounded-lg shadow-lg flex flex-row items-center border border-white border-1" style={{ backgroundColor: 'rgba(53, 64, 85, 0.2)' }}>
        <div className="w-[38%] p-1 mt-2">
            <Doughnut data={data3} options={options} width={80} height={80}/>
          </div>
          <div className="flex justify-center items-center flex-col m-4  w-[62%]">
            <h3 className="text-lg font-semibold">Half leave</h3>
            <ul className="mt-2 space-y-1">
              <li className="flex items-center">
                <span className="w-3 h-3 bg-white rounded-full mr-2"></span>
                Remaining - 3
              </li>
              <li className="flex items-center">
                <span className="w-3 h-3 bg-purple-500 rounded-full mr-2"></span>
                Used - 4
              </li>
              <li className="flex items-center">
                <span className="w-3 h-3 bg-black rounded-full mr-2"></span>
                Total - 7
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Attendance;
