import React, {useState, useEffect} from 'react';
import {useNavigate} from 'react-router-dom';
import EditUserModal from "../Modals/EditUserModal";
import api from "../../api";

const UserProfile = () => {
    const [user, setUser] = useState(null);
    const [bookings, setBookings] = useState([]);
    const [bookingHistory, setBookingHistory] = useState([]);
    const [isModalOpen, setIsModalOpen] = useState(false);
    const history = useNavigate();

    useEffect(() => {
        // Функция для загрузки данных пользователя
        const fetchUserData = async () => {
            try {
                const response = await api.get('/api/', {
                    withCredentials: true
                });
                setUser(response.data);
            } catch (error) {
                console.error('Error fetching user data:', error);
                if (error.response && error.response.status === 404) {
                    history('/login');
                }
            }
        };

        // Функция для загрузки данных о бронированиях
        const fetchAppointments = async () => {
            try {
                const response = await api.get('/api/appointment', {
                    withCredentials: true
                });

                const currentDate = new Date();

                // Фильтрация актуальных бронирований (по дате)
                const activeBookings = response.data.filter(booking => {
                    const endTime = new Date(booking.slot_end_time);
                    return endTime >= currentDate && booking.user_first_name === user.first_name && booking.user_last_name === user.last_name && booking.is_confirmed;
                });

                // Фильтрация бронирований в истории (прошедшие по дате)
                const historyBookings = response.data.filter(booking => {
                    const endTime = new Date(booking.slot_end_time);
                    return endTime < currentDate && booking.user_first_name === user.first_name && booking.user_last_name === user.last_name && booking.is_confirmed;
                });

                setBookings(activeBookings);
                setBookingHistory(historyBookings);
            } catch (error) {
                console.error('Error fetching appointments:', error);
            }
        };

        // Вызов функций загрузки данных
        if (!user) {
            fetchUserData();
        }
        if (user) {
            fetchAppointments();
        }
    }, [history, user]);

    const handleSubmit = async (formData) => {
        try {
            const response = await api.patch('/api/update_user', formData, {
                withCredentials: true,
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });

            setUser(response.data);
            setIsModalOpen(false);
        } catch (error) {
            console.error('Error updating user data:', error);
            if (error.response && error.response.status === 404) {
                history('/login');
            }
        }
    };

    const openModal = () => {
        setIsModalOpen(true);
    };

    const closeModal = () => {
        setIsModalOpen(false);
    };

    if (!user) {
        return <div>Loading...</div>;
    }

    return (
        <div className="min-h-screen flex items-center justify-center">
            <div className="bg-white w-full max-w-4xl rounded-lg shadow-lg overflow-hidden">
                <div className="px-6 py-8 md:flex md:items-center md:justify-between">
                    <div className="md:flex md:items-center">
                        <div className="md:flex-shrink-0">
                            <img
                                className="h-24 w-24 rounded-full object-cover mx-auto md:mx-0 md:mr-4"
                                src={user.profile_picture || "https://randomuser.me/api/portraits/men/1.jpg"}
                                alt="User avatar"
                            />
                        </div>
                        <div className="mt-4 md:mt-0">
                            <h1 className="text-2xl font-bold text-gray-800">{`${user.first_name} ${user.last_name}`}</h1>
                            <p className="text-sm text-gray-600">{user.email}</p>
                        </div>
                    </div>
                    <div className="mt-4 md:mt-0">
                        <button
                            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                            onClick={openModal}
                        >
                            Редактировать профиль
                        </button>
                    </div>
                </div>

                <div className="border-t border-gray-200 px-6 py-4">
                    <div className="mb-8">
                        <h2 className="text-xl font-semibold text-gray-800">Текущие брони</h2>
                        <div className="mt-4">
                            {bookings.length > 0 ? (
                                <div className="overflow-x-auto">
                                    <table className="table-auto w-full border-collapse">
                                        <thead>
                                        <tr className="bg-gray-100">
                                            <th className="px-4 py-2 text-left text-sm font-semibold text-gray-600 uppercase border-b">Время
                                                начала
                                            </th>
                                            <th className="px-4 py-2 text-left text-sm font-semibold text-gray-600 uppercase border-b">Время
                                                окончания
                                            </th>
                                            <th className="px-4 py-2 text-left text-sm font-semibold text-gray-600 uppercase border-b">Специалист</th>
                                            <th className="px-4 py-2 text-left text-sm font-semibold text-gray-600 uppercase border-b">Статус</th>
                                        </tr>
                                        </thead>
                                        <tbody>
                                        {bookings.map(booking => (
                                            <tr key={booking.id} className="border-b">
                                                <td className="px-4 py-3 text-sm text-gray-600">{new Date(booking.slot_start_time).toLocaleString()}</td>
                                                <td className="px-4 py-3 text-sm text-gray-600">{new Date(booking.slot_end_time).toLocaleString()}</td>
                                                <td className="px-4 py-3 text-sm text-gray-600">{`${booking.specialist_first_name} ${booking.specialist_last_name}`}</td>
                                                <td className="px-4 py-3 text-sm text-gray-600">Подтверждено</td>
                                            </tr>
                                        ))}
                                        </tbody>
                                    </table>
                                </div>
                            ) : (
                                <p className="text-sm text-gray-600">У вас нет текущих активных бронирований.</p>
                            )}
                        </div>
                    </div>

                    <div>
                        <h2 className="text-xl font-semibold text-gray-800">История бронирований</h2>
                        <div className="mt-4">
                            {bookingHistory.length > 0 ? (
                                <div className="overflow-x-auto">
                                    <table className="table-auto w-full border-collapse">
                                        <thead>
                                        <tr className="bg-gray-100">
                                            <th className="px-4 py-2 text-left text-sm font-semibold text-gray-600 uppercase border-b">Время
                                                начала
                                            </th>
                                            <th className="px-4 py-2 text-left text-sm font-semibold text-gray-600 uppercase border-b">Время
                                                окончания
                                            </th>
                                            <th className="px-4 py-2 text-left text-sm font-semibold text-gray-600 uppercase border-b">Специалист</th>
                                            <th className="px-4 py-2 text-left text-sm font-semibold text-gray-600 uppercase border-b">Статус</th>
                                        </tr>
                                        </thead>
                                        <tbody>
                                        {bookingHistory.map(historyItem => (
                                            <tr key={historyItem.id} className="border-b">
                                                <td className="px-4 py-3 text-sm text-gray-600">{new Date(historyItem.slot_start_time).toLocaleString()}</td>
                                                <td className="px-4 py-3 text-sm text-gray-600">{new Date(historyItem.slot_end_time).toLocaleString()}</td>
                                                <td className="px-4 py-3 text-sm text-gray-600">{`${historyItem.specialist_first_name} ${historyItem.specialist_last_name}`}</td>
                                                <td className="px-4 py-3 text-sm text-gray-600">Подтверждено</td>
                                            </tr>
                                        ))}
                                        </tbody>
                                    </table>
                                </div>
                            ) : (
                                <p className="text-sm text-gray-600">У вас нет подтвержденных бронирований в
                                    истории.</p>
                            )}
                        </div>
                    </div>
                </div>
            </div>

            {isModalOpen && (
                <EditUserModal
                    user={user}
                    handleSubmit={handleSubmit}
                    handleClose={closeModal}
                />
            )}
        </div>
    );
};

export default UserProfile;
