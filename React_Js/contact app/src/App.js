import {BrowserRouter as Router, Routes, Route} from "react-router-dom"
import Contact from "./compo/Contact";
import AddContact from "./compo/Addontact";


const App = () => {
  return (
    <div>

     <Router>
     <Routes>
        <Route path="/" element= {<Contact/>}/>
        <Route path="/N" element= {<AddContact/>}/>
      </Routes>
     </Router>
     
     {/* <Contact/> */}
     
    </div>
  );
}

export default App;
