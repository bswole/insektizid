import React from 'react';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

import DashBoard from '@page/DashBoard'

function App() {
    return (
        <Router basename="/app/">
            <Routes>
                <Route path="/" element={<DashBoard />} />
            </Routes>
        </Router>
    );
}

export default App;