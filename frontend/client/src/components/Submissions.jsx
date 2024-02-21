// eslint-disable-next-line no-unused-vars
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Submissions = () => {
  const [codes, setCodes] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/submission/view/')
      .then(response => {
        // Sorting the codes according to their submission time
        const sortedCodes = response.data.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));
        setCodes(sortedCodes);
      })
      .catch(error => {
        console.error('Error fetching codes:', error);

      });
  }, []);

  // Function to convert timestamp to readable date format
  const formatTimestamp = (timestamp) => {
    const date = new Date(timestamp);
    return date.toLocaleString(); 
  };

  return (
    <div className="mb-4 overflow-auto max-h-96">
      <h2 className="text-xl font-semibold text-white">Submitted Codes</h2>
      {codes.map(code => (
        <div key={code.id} className="bg-gray-800 rounded p-4 mt-2">
          <pre className="text-gray-300">{code.code}</pre><br />
          {code.verdict && (
            <p className="text-gray-300">Verdict: {code.verdict}</p> 
          )}<br/>
          <p className="text-gray-300">Submitted at: {formatTimestamp(code.timestamp)}</p>
        </div>
      ))}
    </div>
  );
};

export default Submissions;
