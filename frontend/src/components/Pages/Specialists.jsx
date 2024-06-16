import React, {useEffect, useState} from 'react';
import InfiniteScroll from 'react-infinite-scroll-component';
import axios from "axios";
import {BACKEND_API_URL} from "../../api";

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
    const [items, setItems] = useState([])
    const [index, setIndex] = useState(2);
    const [hasMore, setHasMore] = useState(true);
    useEffect(() => {
        axios
            .get(BACKEND_API_URL + '/api/specialist?page=1&size=10')
            .then((res) => {
                console.log(res.data);
                setItems(res.data.items);
            })
            .catch((err) => console.log(err));
    }, []);

    const fetchMoreData = () => {
        axios
            .get(BACKEND_API_URL + `/api/specialist?page=${index}&size=10`)
            .then((res) => {
                setItems((prevItems) => [...prevItems, ...res.data.results]);
                res.pages > 1 ? setHasMore(true) : setHasMore(false);
            })
            .catch((err) => console.log(err));

        setIndex((prevIndex) => prevIndex + 1);
    };

    return (
        <div className="container mx-auto px-4 py-8">
            <InfiniteScroll
                dataLength={items.length}
                next={fetchMoreData}
                hasMore={hasMore}
                loader={<div key={0}>Загрузка...</div>}
            >
                <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
                    {items.map((specialist, index) => (
                        <div key={index} className="bg-white rounded-lg shadow-md p-4">
                            <img
                                src={specialist.profile_picture ? specialist.profile_picture : "https://placehold.co/600x400"}
                                alt={specialist.first_name}
                                className="w-full h-auto mb-2 rounded-lg"
                            />
                            <h2 className="text-lg font-semibold">{specialist.first_name} {specialist.last_name}</h2>
                            <p className="text-sm text-gray-600">Специализация: {specialist.speciality}</p>
                            <p className="text-sm text-gray-600">{specialist.bio}</p>
                            <p className="text-sm text-gray-600">Рейтинг: {specialist.sum_rating}</p>
                        </div>
                    ))}
                </div>
            </InfiniteScroll>
        </div>
    );
};

export default Specialists;