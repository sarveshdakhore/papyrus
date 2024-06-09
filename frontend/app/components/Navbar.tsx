const Navbar = () => {
  return (
    <nav className="text-white p-4 bg-[#0101272d] px-6">
          <div className="container mx-auto flex justify-between items-center">
            <div className="text-lg font-bold"><img src="./logo1.png" width={50} height={50}/><img src="./logo2.png" width={50} height={50}/></div>
            <ul className="flex space-x-4 ml-16">
              <li><a href="#" className="hover:text-zinc-400">Dashboard</a></li>
              <li><a href="#" className="hover:text-zinc-400">Resume Ranking</a></li>
              <li><a href="#" className="hover:text-zinc-400">Git Tracking</a></li>
              <li><a href="#" className="hover:text-zinc-400">Amet</a></li>
            </ul>
            <div className="flex space-x-4 items-center">
              <button className="focus:outline-none">
                <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6 6 0 10-12 0v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"></path>
                </svg>
              </button>
              <button className="bg-blue-500 text-white px-4 py-2 rounded-lg">Login</button>
            </div>
          </div>
        </nav>
  )
}

export default Navbar
