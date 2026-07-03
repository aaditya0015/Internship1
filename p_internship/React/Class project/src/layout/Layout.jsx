
import { Outlet } from "react-router-dom";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

function Layout() {
  return (
    <>
      <Navbar />
      <Outlet />
      <Footer />
    </>
  );
}

export default Layout;

// import React from "react";
// import { Outlet } from "react-router-dom";

// function Layout() {
//   return (
//     <>
//       <header>
//         <h1>My Website</h1>
//       </header>

//       <main>
//         <Outlet />
//       </main>

//       <footer>
//         <p>© 2026 My Website</p>
//       </footer>
//     </>
//   );
// }

// export default Layout;