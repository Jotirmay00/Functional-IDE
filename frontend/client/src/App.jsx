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

  const defaultCode = `def find_two_sum(nums, target): `;
  const [code, setCode] = useState(defaultCode);
  const [output, setOutput] = useState('');
  const [showSubmittedCodes, setShowSubmittedCodes] = useState(false);

  const handleRun = async () => {
    try {
        const requestData = { code: code };
        // Make a POST request using Axios
        const response = await axios.post('/api/evaluate/', requestData, {
            headers: {
                'Content-Type': 'application/json'
            }
        });
        // Check if response is OK
        if (response.status === 200) {
            const data = response.data;
            // Extract the verdict from the data
            const verdict = data.verdict;
            // Check if there's any error message
            const errorMessage = data.error ? `Error: ${data.error}` : '';
            // Set the output to display the verdict
            const color = verdict === 'Passed' ? 'green' : 'red';
            setOutput(<span style={{ color }}>TestCases: {verdict}<br />{errorMessage}</span>);
        } else {
            throw new Error('Network response was not ok');
        }
    } catch (error) {
        console.error('Error fetching data:', error);
        setOutput(`Error: ${error.message}`);
    }
};


const handleSubmit = async (e) => {
  e.preventDefault();

  if (!code.trim()) {
    alert('Please enter some code before submitting.');
    return;
  }

  const requestData = { code: code };
  try {
      const response = await axios.post('/api/evaluate/', requestData, {
          headers: {
              'Content-Type': 'application/json'
          }
      });

      // Check if response is OK
      if (response.status === 200) {
          const data = response.data;
          // Extract the verdict from the data
          const verdict = data.verdict;
          // Include the verdict in the requestData for submission
          requestData.verdict = verdict;

          // Make a POST request to submit the code along with the verdict
          const submissionResponse = await axios.post('/api/submission/submit/', requestData, {
              headers: {
                  'Content-Type': 'application/json'
              }
          });

          // Check if submission response is OK
          if (submissionResponse.status === 200) {
              // Display a text message indicating successful submission
              alert('Submission successful!');
          } else {
              throw new Error('Network response was not ok');
          }
      } else {
          throw new Error('Network response was not ok');
      }
  } catch (error) {
      console.error('Error submitting data:', error);
      // Handle submission errors
  }
};

  const BackToDescription = () => {
    setShowSubmittedCodes(false);
  };

  const ShowSubmittedCodes = () => {
    setShowSubmittedCodes(true);
  };

  return (
    <div className="bg-white min-h-screen flex flex-col">
      <header className="bg-gray-900 text-white p-2 flex justify-between items-center">
        <h1 className="text-3xl font-bold text-center flex-grow">CODE IDE</h1>
        {!showSubmittedCodes ? (
          <button className="bg-gray-600 text-white px-4 py-2 rounded" onClick={ShowSubmittedCodes}>Submissions</button>
        ) : (
          <button className="bg-gray-600 text-white px-4 py-2 rounded" onClick={BackToDescription}>Description</button>
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
              <button className="bg-gray-900 text-white px-4 py-2 rounded" type="submit">Submit</button>

            </div>
            <div style={{ whiteSpace: 'pre-wrap' }} className="w-full h-32 bg-gray-900 text-gray-300 p-2" name="output_area">{output}</div>
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
