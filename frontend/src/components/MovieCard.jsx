import React from 'react';

export default function MovieCard({ movie }) {
  return (
    <div className="card m-2" style={{ width: '200px' }}>
      <img src={movie.poster} className="card-img-top" alt={movie.title} />
      <div className="card-body">
        <h5 className="card-title">{movie.title}</h5>
        <p>⭐ {movie.rating?.toFixed(1)}</p>
        <a
          className="btn btn-outline-secondary btn-sm"
          href={`https://www.imdb.com/title/${movie.imdb_id}`}
          target="_blank"
          rel="noreferrer"
        >
          IMDb
        </a>
      </div>
    </div>
  );
}
