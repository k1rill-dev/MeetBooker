import React, { useState } from 'react';
import { Button } from 'flowbite-react';

const AppointmentsManagement = () => {
  const [appointments, setAppointments] = useState([
    { id: 1, name: 'John Doe', date: '2023-06-15', time: '10:00', status: 'Pending' },
    { id: 2, name: 'Jane Smith', date: '2023-06-16', time: '11:00', status: 'Pending' },
  ]);

  const handleConfirm = (id) => {
    setAppointments(appointments.map(app => app.id === id ? { ...app, status: 'Confirmed' } : app));
  };

  const handleCancel = (id) => {
    setAppointments(appointments.map(app => app.id === id ? { ...app, status: 'Cancelled' } : app));
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h2 className="text-2xl font-bold mb-4">Управление встречами</h2>
      <ul className="space-y-4">
        {appointments.map(app => (
          <li key={app.id} className="bg-gray-100 p-4 rounded-lg flex justify-between items-center">
            <div>
              <p className="font-semibold">{app.name}</p>
              <p>{app.date} - {app.time}</p>
              <p className={`font-semibold ${app.status === 'Confirmed' ? 'text-green-500' : app.status === 'Cancelled' ? 'text-red-500' : 'text-yellow-500'}`}>
                Статус: {app.status}
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
