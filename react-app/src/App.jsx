import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import AssetList from './components/AssetList';

const App = () => {
  return (
    <Router>
      <div>
        <header>
          <h1>3D Assets Platform</h1>
          <nav>
            <ul>
              <li><Link to="/">Home (Customer)</Link></li>
              <li><Link to="/creator">Creator My Page</Link></li>
              <li><Link to="/customer/purchases">My Purchases</Link></li>
              <li><Link to="/login">Login</Link></li>
            </ul>
          </nav>
        </header>
        <Routes>
          <Route path="/" element={<AssetList />} />
          <Route path="/creator" element={<div>
            <h2>Creator Dashboard</h2>
            <p>[React component for creator assets and calendar]</p>
          </div>} />
          <Route path="/customer/purchases" element={<div>
            <h2>Purchase History</h2>
            <p>[React component for purchase history and calendar]</p>
          </div>} />
          {/* Additional routes can be added here */}
        </Routes>
      </div>
    </Router>
  );
};

export default App;
