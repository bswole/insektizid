import React from 'react';
import Home from 'comp/Home'; //comp is an alias for 'front-end/components/' defined in webpack.config.js
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

function App() {
    return (
        <Router basename="/my-react-page/"> 
            <Routes>
                <Route path="/" element={<Home />} />
            </Routes>
        </Router>
    );
}

export default App;