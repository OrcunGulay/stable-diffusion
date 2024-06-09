import React, { useState } from 'react';
import './App.css';

function App() {
  const [prompt, setPrompt] = useState('');
  const [imageBase64, setImageBase64] = useState('');

  const handleGenerateImage = () => {
    fetch(`https://cc3c-159-146-26-91.ngrok-free.app/generate-image?prompt=${encodeURIComponent(prompt)}`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        setImageBase64(data.image_base64);
      })
      .catch(error => {
        console.error('Error generating image:', error);
      });
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Image Generator</h1>
        <div>
          <input
            type="text"
            placeholder="Enter prompt"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
          />
          <button onClick={handleGenerateImage}>Generate</button>
        </div>
      </header>

      {imageBase64 && (
        <div className="App-image-container">
          <img src={`data:image/png;base64,${imageBase64}`} alt="Generated image" />
        </div>
      )}
    </div>
  );
}

export default App;
