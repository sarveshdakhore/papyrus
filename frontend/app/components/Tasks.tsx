import React from "react";

const Tasks = () => {
  return (
    <div className="p-4 bg-gradient-to-r border border-white border-1 rounded-lg text-white max-w-4xl w-[50%] m-4" style={{ backgroundColor: 'rgba(53, 64, 85, 0.2)' }}>
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-lg font-semibold">Task Checklist</h2>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="bg-zinc-800 p-4 rounded-lg" >
          <div className="grid grid-cols-2 gap-4">
            <div className="bg-zinc-700 p-4 rounded-lg flex flex-col items-center">
              <img
                src="https://placehold.co/32x32"
                alt="Today"
                className="mb-2"
              />
              <span className="text-2xl font-bold">2</span>
              <span>Today</span>
            </div>
            <div className="bg-zinc-700 p-4 rounded-lg flex flex-col items-center">
              <img
                src="https://placehold.co/32x32"
                alt="Scheduled"
                className="mb-2"
              />
              <span className="text-2xl font-bold">3</span>
              <span>Scheduled</span>
            </div>
            <div className="bg-zinc-700 p-4 rounded-lg flex flex-col items-center">
              <img
                src="https://placehold.co/32x32"
                alt="Flagged"
                className="mb-2"
              />
              <span className="text-2xl font-bold">5</span>
              <span>Flagged</span>
            </div>
            <div className="bg-zinc-700 p-4 rounded-lg flex flex-col items-center">
              <img
                src="https://placehold.co/32x32"
                alt="All"
                className="mb-2"
              />
              <span className="text-2xl font-bold">10</span>
              <span>All</span>
            </div>
          </div>
        </div>
        <div className="bg-zinc-800 p-4 rounded-lg">
          <div className="flex justify-between items-center mb-4">
            <h3 className="text-lg font-semibold">Today</h3>
            <button className="flex items-center space-x-2 text-blue-400">
              <img src="https://placehold.co/16x16" alt="Add Task" />
              <span>Add Task</span>
            </button>
          </div>
          <div className="space-y-4">
            <div className="flex items-center space-x-2">
              <input
                type="checkbox"
                className="form-checkbox h-5 w-5 text-blue-600"
              />
              <div>
                <p>Hi there</p>
                <p className="text-sm text-zinc-400">Task-1</p>
              </div>
            </div>
            <div className="flex items-center space-x-2">
              <input
                type="checkbox"
                className="form-checkbox h-5 w-5 text-blue-600"
              />
              <div>
                <p>Hi there</p>
                <p className="text-sm text-zinc-400">Task-2</p>
              </div>
            </div>
            <div className="flex items-center space-x-2">
              <input
                type="checkbox"
                className="form-checkbox h-5 w-5 text-blue-600"
              />
              <div>
                <p>Hi there</p>
                <p className="text-sm text-zinc-400">Task-3</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Tasks;
