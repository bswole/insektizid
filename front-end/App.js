import React from 'react';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from '@comp/Home'
import DashBoard from '@comp/DashBoard'

function App() {
    return (
        <Router basename="/app/">
            <Routes>
                <Route path="/" element={<DashBoard />} />
                <Route path="/home" element={<Home />} />
            </Routes>
        </Router>
    );
}

export default App;