const login = () => {
  return (
    <div className="flex items-center justify-center min-h-screen bg-zinc-900 ">
      <div className="bg-zinc-800 text-white rounded-lg p-8 shadow-lg w-full max-w-md border border-blue-500">
        <div className="flex items-center mb-6">
          <button className="text-white">
            <svg
              className="w-6 h-6"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M15 19l-7-7 7-7"
              ></path>
            </svg>
          </button>
        </div>
        <div className="flex">
          <div>
            <div className="ml-4 flex items-centre ">
              <img
                src="https://placehold.co/100x40?text=SAVVY&font=roboto&bg=000000&colors=ff0000,ff00ff"
                alt="SAVVY logo"
                className="h-10 "
              />
            </div>
          </div>
          <div>
            <h2 className="text-2xl font-bold mb-6">
              Hello!
              <br />
              Welcome Back...
            </h2>
            <form>
              <div className="mb-4">
                <label className="block text-zinc-400 mb-2" htmlFor="email">
                  Your email address
                </label>
                <div className="flex items-center border border-zinc-600 rounded-lg overflow-hidden">
                  <input
                    className="bg-zinc-800 text-white w-full p-2 outline-none"
                    type="email"
                    id="email"
                    placeholder="Your email address"
                  />
                  <div className="p-2">
                    <svg
                      className="w-6 h-6 text-zinc-400"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth="2"
                        d="M16 12H8m0 0l-4 4m4-4l4-4"
                      ></path>
                    </svg>
                  </div>
                </div>
              </div>
              <div className="mb-6">
                <label className="block text-zinc-400 mb-2" htmlFor="password">
                  Your Password
                </label>
                <div className="flex items-center border border-zinc-600 rounded-lg overflow-hidden">
                  <input
                    className="bg-zinc-800 text-white w-full p-2 outline-none"
                    type="password"
                    id="password"
                    placeholder="Your Password"
                  />
                  <div className="p-2">
                    <svg
                      className="w-6 h-6 text-zinc-400"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth="2"
                        d="M12 11c0-1.104.896-2 2-2s2 .896 2 2-2 2-2 2-2-.896-2-2zm0 0v4m0 0H8m4 0h4"
                      ></path>
                    </svg>
                  </div>
                </div>
              </div>
              <button className="w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 transition duration-200">
                Login
              </button>
            </form>
            <div className="mt-6 text-center">
              <p className="text-zinc-400 mt-2">
                Forgotten your password?{" "}
                <a href="#" className="text-blue-400">
                  Reset
                </a>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default login;
