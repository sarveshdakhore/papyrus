const Footer = () => {
  return (
    <footer className="text-white bottom-0 fixed left-1/2 transform -translate-x-1/2 p-4 w-[100%] bg-[#0101272d]">
          <div className="container mx-auto text-center">
            <div className="flex justify-center space-x-4">
              <a href="#" className="hover:text-zinc-400">About</a>
              <a href="#" className="hover:text-zinc-400">Features</a>
              <a href="#" className="hover:text-zinc-400">Pricing</a>
              <a href="#" className="hover:text-zinc-400">Gallery</a>
              <a href="#" className="hover:text-zinc-400">Team</a>
            </div>
            <div className="flex justify-center space-x-2">
              <a href="#" className="hover:text-zinc-400"><img alt="facebook" src="/icons/facebook.svg" /></a>
              <a href="#" className="hover:text-zinc-400"><img alt="twitter" src="/icons/github.svg" /></a>
              <a href="#" className="hover:text-zinc-400"><img alt="instagram" src="/icons/instagram.svg" /></a>
              <a href="#" className="hover:text-zinc-400"><img alt="linkedin" src="/icons/linkedin.svg" /></a>
              <a href="#" className="hover:text-zinc-400"><img alt="pinterest" src="/icons/pintrest.svg" /></a>
            </div>
            <div className="border border-t-1 white w-[80%] mx-auto"></div>
            <div className="text-zinc-400 mt-2">&copy; 2024 All Rights Reserved</div>
          </div>
        </footer>
  )
}

export default Footer