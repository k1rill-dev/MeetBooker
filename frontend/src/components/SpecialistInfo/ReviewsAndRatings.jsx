import React from 'react';

const ReviewsAndRatings = () => {
  const reviews = [
    { id: 1, name: 'John Doe', rating: 5, comment: 'Great service!' },
    { id: 2, name: 'Jane Smith', rating: 4, comment: 'Very professional.' },
  ];

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h2 className="text-2xl font-bold mb-4">Отзывы и рейтинги</h2>
      <ul className="space-y-4">
        {reviews.map(review => (
          <li key={review.id} className="bg-gray-100 p-4 rounded-lg">
            <p className="font-semibold">{review.name} ({review.rating} звёзд)</p>
            <p>{review.comment}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ReviewsAndRatings;
