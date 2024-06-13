import React, { useState } from 'react';
import { Modal, Button } from 'flowbite-react';

const ScheduleManagement = () => {
  const [slots, setSlots] = useState([]);
  const [modalOpen, setModalOpen] = useState(false);
  const [currentSlot, setCurrentSlot] = useState({ date: '', time: '' });

  const handleAddSlot = () => {
    setSlots([...slots, currentSlot]);
    setCurrentSlot({ date: '', time: '' });
    setModalOpen(false);
  };

  const handleDeleteSlot = (index) => {
    const newSlots = slots.filter((_, i) => i !== index);
    setSlots(newSlots);
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h2 className="text-2xl font-bold mb-4">Управление расписанием</h2>
      <Button onClick={() => setModalOpen(true)} className="mb-4">Добавить слот</Button>
      <ul className="space-y-2">
        {slots.map((slot, index) => (
          <li key={index} className="flex justify-between items-center bg-gray-100 p-2 rounded-lg">
            <span>{slot.date} - {slot.time}</span>
            <Button color="failure" size="xs" onClick={() => handleDeleteSlot(index)}>Удалить</Button>
          </li>
        ))}
      </ul>

      <Modal show={modalOpen} onClose={() => setModalOpen(false)}>
        <Modal.Header>
          Добавить временной слот
        </Modal.Header>
        <Modal.Body>
          <div className="space-y-4">
            <input
              type="date"
              value={currentSlot.date}
              onChange={(e) => setCurrentSlot({ ...currentSlot, date: e.target.value })}
              className="border p-2 rounded w-full"
            />
            <input
              type="time"
              value={currentSlot.time}
              onChange={(e) => setCurrentSlot({ ...currentSlot, time: e.target.value })}
              className="border p-2 rounded w-full"
            />
          </div>
        </Modal.Body>
        <Modal.Footer>
          <Button onClick={handleAddSlot}>Добавить</Button>
        </Modal.Footer>
      </Modal>
    </div>
  );
};

export default ScheduleManagement;
