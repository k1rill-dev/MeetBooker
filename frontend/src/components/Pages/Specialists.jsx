import React, {useState} from 'react';

const specialists = [
    {
        name: 'Иван Иванов',
        specialization: 'Врач-терапевт',
        location: 'Москва',
        rating: 4.5,
        photo: 'ivan.jpg',
        // Другие свойства специалиста
    },
    {
        name: 'Мария Петрова',
        specialization: 'Стоматолог',
        location: 'Санкт-Петербург',
        rating: 4.8,
        photo: 'maria.jpg',
        // Другие свойства специалиста
    },
    {
        name: 'Александр Сидоров',
        specialization: 'Хирург',
        location: 'Новосибирск',
        rating: 4.2,
        photo: 'alexander.jpg',
    },
];


const Specialists = () => {
    const [filters, setFilters] = useState({
        name: '',
        specialization: '',
        minRating: 0
    });

    const handleChange = (e) => {
        const {name, value} = e.target;
        setFilters({
            ...filters,
            [name]: name === 'minRating' ? parseFloat(value.replace(/[^\d.]/g, '')) : value
        });
    };

    const filteredSpecialists = specialists.filter(specialist => {
        return (
            specialist.name.toLowerCase().includes(filters.name.toLowerCase()) &&
            specialist.specialization.toLowerCase().includes(filters.specialization.toLowerCase()) &&
            specialist.rating >= filters.minRating
        );
    });

    return (
        <div className="container mx-auto px-4 py-8">
            <div className="mb-4">
                <input
                    type="text"
                    placeholder="Фильтр по имени"
                    className="border border-gray-300 rounded-lg px-4 py-2 mr-2"
                    name="name"
                    value={filters.name}
                    onChange={handleChange}
                />
                <input
                    type="text"
                    placeholder="Фильтр по специализации"
                    className="border border-gray-300 rounded-lg px-4 py-2 mr-2"
                    name="specialization"
                    value={filters.specialization}
                    onChange={handleChange}
                />
                <input
                    type="text"
                    placeholder="Минимальный рейтинг"
                    className="border border-gray-300 rounded-lg px-4 py-2 mr-2"
                    name="minRating"
                    value={filters.minRating}
                    onChange={handleChange}
                />
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
                {filteredSpecialists.map((specialist, index) => (
                    <div key={index} className="bg-white rounded-lg shadow-md p-4">
                        <img
                            src="https://placehold.co/600x400"
                            alt={specialist.name}
                            className="w-full h-auto mb-2 rounded-lg"
                        />
                        <h2 className="text-lg font-semibold">{specialist.name}</h2>
                        <p className="text-sm text-gray-600">{specialist.specialization}</p>
                        <p className="text-sm text-gray-600">{specialist.location}</p>
                        <p className="text-sm text-gray-600">Рейтинг: {specialist.rating}</p>
                        {/* Другие детали специалиста */}
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Specialists;