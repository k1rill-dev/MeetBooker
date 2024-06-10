import React from 'react';

const specialists = [
    {
        name: 'Иван Иванов',
        specialization: 'Врач-терапевт',
        location: 'Москва',
        // Другие свойства специалиста
    },
    {
        name: 'Мария Петрова',
        specialization: 'Стоматолог',
        location: 'Санкт-Петербург',
        // Другие свойства специалиста
    }, {
        name: 'Мария Петрова',
        specialization: 'Стоматолог',
        location: 'Санкт-Петербург',
        // Другие свойства специалиста
    }, {
        name: 'Мария Петрова',
        specialization: 'Стоматолог',
        location: 'Санкт-Петербург',
        // Другие свойства специалиста
    }, {
        name: 'Мария Петрова',
        specialization: 'Стоматолог',
        location: 'Санкт-Петербург',
        // Другие свойства специалиста
    }, {
        name: 'Мария Петрова',
        specialization: 'Стоматолог',
        location: 'Санкт-Петербург',
        // Другие свойства специалиста
    }, {
        name: 'Мария Петрова',
        specialization: 'Стоматолог',
        location: 'Санкт-Петербург',
        // Другие свойства специалиста
    }, {
        name: 'Мария Петрова',
        specialization: 'Стоматолог',
        location: 'Санкт-Петербург',
        // Другие свойства специалиста
    }, {
        name: 'Мария Петрова',
        specialization: 'Стоматолог',
        location: 'Санкт-Петербург',
        // Другие свойства специалиста
    }, {
        name: 'Мария Петрова',
        specialization: 'Стоматолог',
        location: 'Санкт-Петербург',
        // Другие свойства специалиста
    }, {
        name: 'Мария Петрова',
        specialization: 'Стоматолог',
        location: 'Санкт-Петербург',
        // Другие свойства специалиста
    }, {
        name: 'Мария Петрова',
        specialization: 'Стоматолог',
        location: 'Санкт-Петербург',
        // Другие свойства специалиста
    }, {
        name: 'Мария Петрова',
        specialization: 'Стоматолог',
        location: 'Санкт-Петербург',
        // Другие свойства специалиста
    }, {
        name: 'Мария Петрова',
        specialization: 'Стоматолог',
        location: 'Санкт-Петербург',
        // Другие свойства специалиста
    }, {
        name: 'Мария Петрова',
        specialization: 'Стоматолог',
        location: 'Санкт-Петербург',
        // Другие свойства специалиста
    }, {
        name: 'Мария Петрова',
        specialization: 'Стоматолог',
        location: 'Санкт-Петербург',
        // Другие свойства специалиста
    },
    // Другие специалисты
];

const Specialists = () => {
    return (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
            {specialists.map((specialist, index) => (
                <div key={index} className="bg-white rounded-lg shadow-md p-4">
                    <img
                        src="https://placehold.co/600x400"
                        alt={specialist.name}
                        className="w-full h-auto mb-2 rounded-lg"
                    />
                    <h2 className="text-lg font-semibold">{specialist.name}</h2>
                    <p className="text-sm text-gray-600">{specialist.specialization}</p>
                    <p className="text-sm text-gray-600">{specialist.location}</p>
                    {/* Другие детали специалиста */}
                </div>
            ))}
        </div>
    );
};

export default Specialists;