import React, { useState, useEffect } from 'react';
import axios from 'axios';

const AssetList = () => {
  const [assets, setAssets] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get('/home/')  // Django's AssetListView is available at /home/
      .then(response => {
        // Assuming Django renders HTML, in a real API you'd return JSON.
        // For this example, you might create a JSON endpoint.
        console.log(response.data);
        // Set assets state here if using a JSON API.
      })
      .catch(error => {
        console.error('Error fetching assets:', error);
        setError('Error fetching assets.');
      });
  }, []);

  return (
    <div>
      <h2>Available 3D Assets (React)</h2>
      {error && <p>{error}</p>}
      {/* Render assets if available */}
      <ul>
        {assets.map(asset => (
          <li key={asset.id}>
            <h3>{asset.title}</h3>
            <p>{asset.description}</p>
            <p>Price: ${asset.price}</p>
            <a href={asset.file}>View/Download</a>
          </li>
        ))}
      </ul>
      <p>[Note: For a real application, create a JSON API endpoint in Django.]</p>
    </div>
  );
};

export default AssetList;
