import React, { useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import SearchBar from './components/SearchBar';
import MovieCarousel from './components/MovieCarousel';

function App() {
  const [recommendations, setRecommendations] = useState([]);

  const fetchRecommendations = async (movieTitle) => {
    try {
      const res = await axios.post('/recommend', { movie: movieTitle });
      setRecommendations(res.data.recommendations);
    } catch (error) {
      console.error('Failed to fetch recommendations:', error);
    }
  };

  return (
    <div className="container mt-5">
      <h1 className="mb-4">Movie Recommender</h1>
      <SearchBar onSearch={fetchRecommendations} />
      {recommendations.length > 0 && (
        <MovieCarousel movies={recommendations} />
      )}
    </div>
  );
}
 
export default App;