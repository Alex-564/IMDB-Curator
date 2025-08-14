import React from 'react';
import MovieCard from './MovieCard';

export default function MovieCarousel({ movies }) {
  return (
    <div
      className="movie-carousel"
      style={{
        display: 'flex',
        overflowX: 'auto',
        gap: '1rem',
        padding: '1rem 0',
        scrollSnapType: 'x mandatory',
      }}
    >
      {movies.map((movie, index) => (
        <div
          key={index}
          style={{
            flex: '0 0 auto',
            scrollSnapAlign: 'start',
          }}
        >
          <MovieCard movie={movie} />
        </div>
      ))}
    </div>
  );
}