"use client";
import React from "react";

const Plugin = () => {
  const handlegithub = async () => {
    const token = localStorage.getItem("token");
    console.log(token);
    const response = await fetch("http://127.0.0.1:8000/git_login", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`,
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)",
      },
      redirect: "manual",
    });

    if (response.type === "opaqueredirect") {
      window.location.href = response.url;
    } else {
      console.error("Failed to login with GitHub");
    }
  };
  return (
    <div className="flex flex-col items-center justify-center min-h-screenp-4">
      <div
        className="text-white rounded-xl p-6 shadow-lg w-full max-w-md border border-1 border-white"
        style={{ backgroundColor: "rgba(53, 64, 85, 0.2)" }}
      >
        <div className="flex items-center mb-6">
          <img
            src="https://placehold.co/40x40"
            alt="plugin icon"
            className="mr-4"
          />
          <h2 className="text-xl font-semibold">Add Plugins</h2>
        </div>
        <div className="space-y-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center">
              <img
                src="https://placehold.co/40x40"
                alt="Gmail icon"
                className="mr-4"
              />
              <span className="text-lg font-semibold">Gmail</span>
            </div>
            <div className="flex items-center space-x-4">
              <div className="flex items-center">
                <img
                  src="https://placehold.co/20x20"
                  alt="heart icon"
                  className="mr-1"
                />
                <span>143</span>
              </div>
              <div className="flex items-center">
                <img
                  src="https://placehold.co/20x20"
                  alt="user icon"
                  className="mr-1"
                />
                <span>7.2k</span>
              </div>
              <button className="bg-gradient-to-r from-purple-400 to-pink-500 text-white px-4 py-2 rounded-full">
                Connect
              </button>
            </div>
          </div>
          <div className="flex items-center justify-between">
            <div className="flex items-center">
              <img
                src="https://placehold.co/40x40"
                alt="LinkedIn icon"
                className="mr-4"
              />
              <span className="text-lg font-semibold">LinkedIn</span>
            </div>
            <div className="flex items-center space-x-4">
              <div className="flex items-center">
                <img
                  src="https://placehold.co/20x20"
                  alt="heart icon"
                  className="mr-1"
                />
                <span>143</span>
              </div>
              <div className="flex items-center">
                <img
                  src="https://placehold.co/20x20"
                  alt="user icon"
                  className="mr-1"
                />
                <span>7.2k</span>
              </div>
              <button className="bg-gradient-to-r from-purple-400 to-pink-500 text-white px-4 py-2 rounded-full">
                Connect
              </button>
            </div>
          </div>
          <div className="flex items-center justify-between">
            <div className="flex items-center">
              <img
                src="https://placehold.co/40x40"
                alt="GitHub icon"
                className="mr-4"
              />
              <span className="text-lg font-semibold">Git Hub</span>
            </div>
            <div className="flex items-center space-x-4">
              <div className="flex items-center">
                <img
                  src="https://placehold.co/20x20"
                  alt="heart icon"
                  className="mr-1"
                />
                <span>143</span>
              </div>
              <div className="flex items-center">
                <img
                  src="https://placehold.co/20x20"
                  alt="user icon"
                  className="mr-1"
                />
                <span>7.2k</span>
              </div>
              <button
                className="bg-gradient-to-r from-purple-400 to-pink-500 text-white px-4 py-2 rounded-full"
                onClick={handlegithub}
              >
                Connect
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Plugin;
