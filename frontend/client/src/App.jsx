// eslint-disable-next-line no-unused-vars
import React, { useState } from 'react';
import AceEditor from 'react-ace';
import 'ace-builds/src-noconflict/theme-dracula'; // Import the dracula theme
import 'ace-builds/src-noconflict/mode-python';
import 'ace-builds/src-noconflict/ext-language_tools'; // for autocompletion
import 'ace-builds/src-noconflict/ext-beautify'; // for code formatting
import 'ace-builds/src-noconflict/ext-error_marker'; // for error highlighting
import Description from './components/Description';
import Submissions from './components/Submissions';
import axios from 'axios';

function App() {

  const defaultCode = `def find_two_sum(nums, target):\n `;
  const [code, setCode] = useState(defaultCode);
  const [output, setOutput] = useState('');
  const [showSubmittedCodes, setShowSubmittedCodes] = useState(false);

  const handleRun = () => {
    const requestData = { code: code };

    // Make a POST request using Axios
    axios.post('http://127.0.0.1:8000/api/evaluate/', requestData, {
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(response => {
        // Check if response is OK
        if (response.status === 200) {
          const data = response.data;
          // Extract the verdict from the data
          const verdict = data.verdict;
          // Set the output to display the verdict
          setOutput(`Verdict: ${verdict}`);
        } else {
          throw new Error('Network response was not ok');
        }
      })
      .catch(error => {
        console.error('Error fetching data:', error);

      });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const requestData = { code: code };

    // Make a POST request using Axios
    axios.post('http://127.0.0.1:8000/api/submission/submit/', requestData, {
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(response => {
        // Check if response is OK
        if (response.status === 200) {
          // Display a text message indicating successful submission
          alert('Submission successful!');
        } else {
          throw new Error('Network response was not ok');
        }
      })
      .catch(error => {
        console.error('Error fetching data:', error);
        // Handle errors
      });
  };

  const isSubmitDisabled = output !== 'Verdict: Passed';

  const handleBackToDescription = () => {
    setShowSubmittedCodes(false);
  };

  const handleShowSubmittedCodes = () => {
    setShowSubmittedCodes(true);
  };

  return (
    <div className="bg-white min-h-screen flex flex-col">
      <header className="bg-gray-900 text-white p-2 flex justify-between items-center">
        <h1 className="text-3xl font-bold text-center flex-grow">CODE IDE</h1>
        {!showSubmittedCodes ? (
          <button className="bg-gray-600 text-white px-4 py-2 rounded" onClick={handleShowSubmittedCodes}>Submissions</button>
        ) : (
          <button className="bg-gray-600 text-white px-4 py-2 rounded" onClick={handleBackToDescription}>Description</button>
        )}
      </header>
      <div className="flex flex-grow">
        <div className="w-1/2 bg-gray-700 p-1">
          {showSubmittedCodes ? (
            <>
              <Submissions />
            </>
          ) : (
            <Description />
          )}
          <form onSubmit={handleSubmit} className="mb-2">
            <div className="flex justify-end mb-2">
              <button className="bg-gray-900 text-white px-4 py-2 rounded mr-2" type="button" onClick={handleRun}>Run</button>
              <button className="bg-gray-900 text-white px-4 py-2 rounded" type="submit" disabled={isSubmitDisabled}>Submit</button>

            </div>
            <textarea className="w-full h-32 bg-gray-900 text-gray-300 p-2" name="output_area" value={output} placeholder='Output' disabled></textarea>
          </form>
        </div>
        <div className="w-1/2 bg-gray-400 p-2">
          <h2 className="text-xl font-bold mb-2">Code</h2>
          <AceEditor
            mode="python"
            theme="dracula"
            onChange={setCode}
            name="code-editor"
            value={code}
            fontSize={16}
            showPrintMargin={false}
            width="100%"
            height="83vh"
            setOptions={{
              enableBasicAutocompletion: true,
              enableLiveAutocompletion: true,
              enableSnippets: true,
              showLineNumbers: true,
              tabSize: 3
            }}
          />
        </div>
      </div>
    </div>
  );
}

export default App;