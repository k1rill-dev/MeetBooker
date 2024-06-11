import React, { useState } from 'react';
import Modal from 'react-modal';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';
import { Button } from 'flowbite-react';
import './SpecialistProfile.css';

Modal.setAppElement('#root');

const SpecialistProfile = () => {
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [selectedDate, setSelectedDate] = useState(new Date());
    const [selectedTime, setSelectedTime] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const handleModalToggle = () => {
        setIsModalOpen(!isModalOpen);
    };

    const onDateChange = (date) => {
        setSelectedDate(date);
        setSelectedTime('');
        setErrorMessage('');
    };

    const onTimeChange = (event) => {
        setSelectedTime(event.target.value);
    };

    const schedule = {
        '2024-06-12': ['10:00', '14:00', '16:00'],
        '2024-06-13': ['09:00', '12:00', '15:00'],
    };

    const formatDate = (date) => {
        return date.toISOString().split('T')[0];
    };

    const formattedSelectedDate = formatDate(selectedDate);
    const availableTimes = schedule[formattedSelectedDate] || [];

    const tileContent = ({ date, view }) => {
        const formattedDate = formatDate(date);
        if (view === 'month' && schedule[formattedDate]) {
            return (
                <ul className="text-xs text-center">
                    {schedule[formattedDate].map((time, index) => (
                        <li key={index}>{time}</li>
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

    return (
        <div className="container mx-auto">
            <div className="grid md:grid-cols-2 gap-8 p-6 bg-gray-100 rounded-lg shadow-lg">
                <div className="p-6 border-b md:border-b-0 md:border-r border-gray-200">
                    <img
                        src="https://via.placeholder.com/150"
                        alt="Иван Иванов"
                        className="w-24 h-24 rounded-full border-4 border-blue-500 mb-4 mx-auto"
                    />
                    <h2 className="text-3xl font-bold mb-2 text-center">Иван Иванов</h2>
                    <p className="text-lg text-gray-700 mb-4 text-center">Специалист по программированию</p>
                </div>
                <div className="p-6 flex flex-col justify-between">
                    <p className="text-gray-700 mb-4">
                        Иван Иванов - специалист с многолетним опытом в программировании. Занимается разработкой
                        веб-приложений, баз данных и многим другим.
                    </p>
                    <Button
                        className="bg-blue-500 text-white px-6 py-3 rounded-lg hover:bg-blue-600 transition duration-300 ease-in-out self-center"
                        onClick={handleModalToggle}
                    >
                        Забронировать время
                    </Button>
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
                                        {availableTimes.map((time, index) => (
                                            <option key={index} value={time}>
                                                {time}
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
            </div>
        </div>
    );
};

export default SpecialistProfile;
