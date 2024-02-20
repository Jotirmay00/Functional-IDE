// eslint-disable-next-line no-unused-vars
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Submissions = () => {
  const [codes, setCodes] = useState([]);

  useEffect(() => {
    // Fetch the codes from the API
    axios.get('http://127.0.0.1:8000/api/submission/view/')
      .then(response => {
        // Update the state with the fetched codes
        setCodes(response.data);
      })
      .catch(error => {
        console.error('Error fetching codes:', error);
        // Handle errors
      });
  }, []); // Empty dependency array to ensure the effect runs only once

  // Function to convert timestamp to readable date format
  const formatTimestamp = (timestamp) => {
    const date = new Date(timestamp);
    return date.toLocaleString(); // Adjust the date format as needed
  };

  return (
    <div className="mb-4 overflow-auto max-h-96">
      {/* Display the fetched codes */}
      <h2 className="text-xl font-semibold text-white">Submitted Codes</h2>
      {codes.map(code => (
        <div key={code.id} className="bg-gray-800 rounded p-4 mt-2">
          <pre className="text-gray-300">{code.code}</pre>
          <p className="text-gray-400">Submitted at: {formatTimestamp(code.timestamp)}</p>
        </div>
      ))}
    </div>
  );
};

export default Submissions;
