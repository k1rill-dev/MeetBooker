import React, {useState, useEffect} from 'react';
import {Button} from 'flowbite-react';
import api from '../../api';

const AppointmentsManagement = ({user, specialist}) => {
    const [appointments, setAppointments] = useState([]);

    useEffect(() => {
        const fetchAppointments = async () => {
            try {
                const response = await api.get('/api/spec-appointment', {withCredentials: true});
                console.log(response.data)
                setAppointments(response.data);
            } catch (error) {
                console.error('Error fetching appointments:', error);
            }
        };
        fetchAppointments();
    }, []);

    const handleConfirm = async (id) => {
        try {
            await api.patch(`/api/appointment/${id}`, {is_confirmed: true}, {withCredentials: true});
            setAppointments(appointments.map(app => app.id === id ? {...app, status: true} : app));
        } catch (error) {
            console.error('Error confirming appointment:', error);
        }
    };

    const handleCancel = async (id) => {
        try {
            await api.patch(`/api/appointment/${id}`, {is_confirmed: false}, {withCredentials: true});
            setAppointments(appointments.map(app => app.id === id ? {...app, is_confirmed: false} : app));
        } catch (error) {
            console.error('Error cancelling appointment:', error);
        }
    };
    if(appointments.length < 0){
        return(
            <div>loading</div>
        )
    }
    return (
        <div className="bg-white p-6 rounded-lg shadow-md">
            <h2 className="text-2xl font-bold mb-4">Управление встречами</h2>
            <ul className="space-y-4">
                {appointments.map(app => (
                    <li key={app.id} className="bg-gray-100 p-4 rounded-lg flex justify-between items-center">
                        <div>
                            <p className="font-semibold">{app.name}</p>
                            <p>{app.slot_start_time} - {app.slot_end_time}</p>
                            <p className={`font-semibold ${app.is_confirmed === true ? 'text-green-500' : app.status === false ? 'text-red-500' : 'text-yellow-500'}`}>
                                {app.is_confirmed ? <a>Подтверждено</a> : <a>Не подтверждено</a>}
                            </p>
                        </div>
                        <div className="flex space-x-2">
                            <Button color="success" size="xs" onClick={() => handleConfirm(app.id)}>Подтвердить</Button>
                            <Button color="failure" size="xs" onClick={() => handleCancel(app.id)}>Отменить</Button>
                        </div>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default AppointmentsManagement;
