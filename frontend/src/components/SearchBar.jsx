import React, { useState } from 'react';

export default function SearchBar({ onSearch }) {
  const [input, setInput] = useState('');

  return (
    <div className="mb-4">
      <input
        className="form-control"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Enter a movie..."
      />
      <button className="btn btn-primary mt-2" onClick={() => onSearch(input)}>
        Recommend
      </button>
    </div>
  );
}
