import { useEffect, useState } from 'react';
import axios from 'axios';

export default function Home() {
  const [assets, setAssets] = useState([]);

  useEffect(() => {
    // Replace the URL with your backend endpoint
    axios.get('http://localhost:8000/api/assets/list/')
      .then(response => setAssets(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h1>Main Page - List of 3D Assets</h1>
      <ul>
        {assets.map(asset => (
          <li key={asset.id}>
            <h2>{asset.title}</h2>
            <p>{asset.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
