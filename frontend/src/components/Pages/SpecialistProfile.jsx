import React, {useEffect, useState} from 'react';
import Modal from 'react-modal';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';
import {Button} from 'flowbite-react';
import './SpecialistProfile.css';
import SpecialistCard from '../Cards/SpecialistCard';
import {useParams} from 'react-router-dom';
import axios from 'axios';
import {BACKEND_API_URL} from '../../api';
import ReactStars from 'react-rating-stars-component';

Modal.setAppElement('#root');

const SpecialistProfile = () => {
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [selectedDate, setSelectedDate] = useState(new Date());
    const [selectedTime, setSelectedTime] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const [rating, setRating] = useState(0);
    const [userRating, setUserRating] = useState(0);
    const [rightSideItems, setRightSideItems] = useState([])

    const params = useParams();
    const id = params.id;
    const [items, setItems] = useState({});
    const [schedule, setSchedule] = useState({});

    const handleModalToggle = () => {
        setIsModalOpen(!isModalOpen);
    };

    useEffect(() => {
        axios
            .get(`${BACKEND_API_URL}/api/specialist/${id}`)
            .then((res) => {
                setItems(res.data);
                setRating(res.data.rating || 0); // Assuming the rating is part of the specialist data
            })
            .catch((err) => console.log(err));
    }, [id]);
    useEffect(() => {
        axios
            .get(`${BACKEND_API_URL}/api/specialist?page=1&size=4`)
            .then((res) => {
                console.log(res.data.items)
                setRightSideItems(res.data.items);
            })
            .catch((err) => console.log(err));
    }, []);
    useEffect(() => {
        axios
            .get(`${BACKEND_API_URL}/api/schedule/${id}`)
            .then((res) => {
                const newSchedule = res.data.reduce((acc, slot) => {
                    const date = slot.start_time.split('T')[0];
                    if (!acc[date]) {
                        acc[date] = [];
                    }
                    acc[date].push({
                        start_time: slot.start_time.split('T')[1].slice(0, 5),
                        end_time: slot.end_time.split('T')[1].slice(0, 5),
                        is_booked: slot.is_booked
                    });
                    return acc;
                }, {});
                setSchedule(newSchedule);
            })
            .catch((err) => console.log(err));
    }, [id]);

    const onDateChange = (date) => {
        setSelectedDate(date);
        setSelectedTime('');
        setErrorMessage('');
    };

    const onTimeChange = (event) => {
        setSelectedTime(event.target.value);
    };

    const formatDate = (date) => {
        return date.toISOString().split('T')[0];
    };

    const formattedSelectedDate = formatDate(selectedDate);
    const availableTimes = schedule[formattedSelectedDate] || [];

    const tileContent = ({date, view}) => {
        const formattedDate = formatDate(date);
        if (view === 'month' && schedule[formattedDate]) {
            return (
                <ul className="text-xs text-center list-none p-0">
                    {schedule[formattedDate].map((slot, index) => (
                        <li
                            key={index}
                            className={`${
                                slot.is_booked ? 'text-red-500' : 'text-green-500'
                            }`}
                        >
                            {slot.start_time} - {slot.end_time}
                        </li>
                    ))}
                </ul>
            );
        }
        return null;
    };

    const handleBooking = () => {
        if (selectedTime) {
            // Perform booking action
            alert(`Booking confirmed for ${selectedTime} on ${formattedSelectedDate}`);
            handleModalToggle();
        } else {
            setErrorMessage('Please select a time slot');
        }
    };

    const ratingChanged = (newRating) => {
        setUserRating(newRating);

        axios
            .post(`${BACKEND_API_URL}/api/rate/${id}`, {rating: newRating})
            .then((res) => {
                setRating(res.data.new_rating); // Assuming the new average rating is returned
            })
            .catch((err) => console.log(err));
    };

    return (
        <div className="container mx-auto">
            <div className="grid md:grid-cols-2 gap-8 p-6 bg-gray-100 rounded-lg shadow-lg">
                <div className="p-6 border-b md:border-b-0 md:border-r border-gray-200">
                    <div className="flex flex-col items-center">
                        <img
                            src={items.profile_picture || "https://via.placeholder.com/150"}
                            alt="Иван Иванов"
                            className="w-24 h-24 rounded-full border-4 border-blue-500 mb-4"
                        />
                        <h2 className="text-3xl font-bold mb-2 text-center">
                            {items.first_name} {items.last_name}
                        </h2>
                        <p className="text-lg text-gray-700 mb-4 text-center">{items.speciality}</p>
                        <p className="text-gray-700 mb-4 text-center">{items.bio}</p>
                        <div className="text-center mb-4">
                            <h3 className="text-xl font-bold">Рейтинг: {items.sum_rating}</h3>
                            <ReactStars
                                count={5}
                                onChange={ratingChanged}
                                size={40}
                                activeColor="#ffd700"
                                value={rating}
                            />
                            <p>Ваш рейтинг: {userRating}</p>
                        </div>
                        <Button
                            className="bg-blue-500 text-white px-6 py-3 rounded-lg hover:bg-blue-600 transition duration-300 ease-in-out"
                            onClick={handleModalToggle}
                        >
                            Забронировать время
                        </Button>
                    </div>
                    <Modal
                        isOpen={isModalOpen}
                        onRequestClose={handleModalToggle}
                        contentLabel="Выберите время для бронирования"
                        className="modal"
                        overlayClassName="modal-overlay"
                    >
                        <div className="p-6">
                            <h2 className="text-2xl mb-4 text-center">Выберите время для бронирования</h2>
                            <Calendar
                                onChange={onDateChange}
                                value={selectedDate}
                                className="rounded-lg shadow-lg"
                                tileContent={tileContent}
                            />
                            {availableTimes.length > 0 && (
                                <div className="mt-4">
                                    <label
                                        className="block text-gray-700 text-base font-bold mb-2"
                                        htmlFor="time-select"
                                    >
                                        Выберите время:
                                    </label>
                                    <select
                                        id="time-select"
                                        value={selectedTime}
                                        onChange={onTimeChange}
                                        className="block w-full bg-white border border-gray-300 px-4 py-3 rounded-lg shadow-sm focus:outline-none focus:border-blue-500"
                                    >
                                        <option value="">-- Выберите время --</option>
                                        {availableTimes.filter(slot => !slot.is_booked).map((slot, index) => (
                                            <option key={index} value={slot.start_time}>
                                                {slot.start_time} - {slot.end_time}
                                            </option>
                                        ))}
                                    </select>
                                    {errorMessage && (
                                        <p className="text-red-500 text-sm mt-2">{errorMessage}</p>
                                    )}
                                </div>
                            )}
                            <div className="flex justify-center mt-6">
                                <Button
                                    className="bg-gray-500 text-white px-6 py-3 rounded-lg mr-4 hover:bg-gray-600 transition duration-300 ease-in-out"
                                    onClick={handleModalToggle}
                                >
                                    Закрыть
                                </Button>
                                <Button
                                    className="bg-blue-500 text-white px-6 py-3 rounded-lg hover:bg-blue-600 transition duration-300 ease-in-out"
                                    onClick={handleBooking}
                                >
                                    Забронировать
                                </Button>
                            </div>
                        </div>
                    </Modal>
                </div>
                <div className="p-6">
                    {rightSideItems.map((item, index) => (
                        <SpecialistCard
                            name={item.first_name}
                            expertise={item.speciality}
                            description={item.bio}
                            rating={item.sum_rating}
                            id={item.spec_id}
                            picture={item.profile_picture}
                        />
                    ))}
                </div>
            </div>
        </div>
    );
};

export default SpecialistProfile;
