import React from 'react';
import {Button} from "flowbite-react";

const SpecialistCard = ({name, expertise, description, rating, id, picture}) => {
    return (
        <div className="bg-white rounded-lg shadow-lg p-6 mb-4">
            <div className="flex items-center mb-4">
                <img
                    src={picture || "https://via.placeholder.com/150"}
                    alt={name}
                    className="w-16 h-16 rounded-full border-2 border-blue-500 mr-4"
                />
                <div>
                    <h2 className="text-xl font-bold mb-1">{name}</h2>
                    <p className="text-gray-700">{expertise}</p>
                </div>
            </div>
            <p className="text-gray-700">{description}</p>
            <p className="text-gray-700">Рейтинг: {rating}</p>
            <Button href={"/specialist/" + id}>Страница специалиста</Button>
        </div>
    );
};

export default SpecialistCard;
