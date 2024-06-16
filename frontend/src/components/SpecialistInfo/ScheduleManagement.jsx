import React, {useState, useEffect} from 'react';
import {Modal, Button} from 'flowbite-react';
import api from '../../api';

const ScheduleManagement = ({specialist}) => {
    const [slots, setSlots] = useState([]);
    const [modalOpen, setModalOpen] = useState(false);
    const [currentSlot, setCurrentSlot] = useState({
        end_time: '',
        start_time: '',
        is_booked: false,
        specialist_id: specialist.spec_id
    });

    const handleAddSlot = async () => {
        try {
            const response = await api.post('/api/schedule', currentSlot, {withCredentials: true});

            const newSlot = {
                id: response.data.uuid, // предположим, что UUID возвращается как response.data.uuid
                start_time: currentSlot.start_time,
                end_time: currentSlot.end_time,
                is_booked: false,
                specialist_id: specialist.spec_id
            };

            setSlots([...slots, newSlot]);

            setCurrentSlot({
                end_time: '',
                start_time: '',
                is_booked: false,
                specialist_id: specialist.spec_id
            });

            setModalOpen(false);
        } catch (error) {
            console.error('Error adding slot:', error);
        }
    };

    const handleDeleteSlot = async (index, slotId) => {
        try {
            await api.delete(`/api/schedule/${slotId}`, {withCredentials: true});
            const newSlots = slots.filter((_, i) => i !== index);
            setSlots(newSlots);
        } catch (error) {
            console.error('Error deleting slot:', error);
        }
    };

    useEffect(() => {
        const fetchSchedule = async () => {
            try {
                const response = await api.get(`/api/schedule/${specialist.spec_id}`, {withCredentials: true});
                setSlots(response.data);
            } catch (error) {
                console.error('Error fetching schedule:', error);
            }
        };
        fetchSchedule();

    }, [specialist.spec_id]);

    if (slots.length === 0) {
        return <div>Loading...</div>;
    }

    return (
        <div className="bg-white p-6 rounded-lg shadow-md">
            <h2 className="text-2xl font-bold mb-4">Управление расписанием</h2>
            <Button onClick={() => setModalOpen(true)} className="mb-4">Добавить слот</Button>
            <ul className="space-y-2">
                {slots.map((slot, index) => (
                    <li key={index} className="flex justify-between items-center bg-gray-100 p-2 rounded-lg">
                        <span>{new Date(slot.start_time).toLocaleString()} - {new Date(slot.end_time).toLocaleString()}</span>
                        <Button color="failure" size="xs"
                                onClick={() => handleDeleteSlot(index, slot.id)}>Удалить</Button>
                    </li>
                ))}
            </ul>

            <Modal show={modalOpen} onClose={() => setModalOpen(false)}>
                <Modal.Header>
                    Добавить временной слот
                </Modal.Header>
                <Modal.Body>
                    <div className="space-y-4">
                        <div className="flex flex-col">
                            <label htmlFor="datetime-local-input" className="mb-2">Дата и время начала:</label>
                            <input
                                id="datetime-local-input"
                                type="datetime-local"
                                value={currentSlot.start_time}
                                onChange={(e) => setCurrentSlot({...currentSlot, start_time: e.target.value})}
                                className="border p-2 rounded w-full"
                            />
                            <label htmlFor="datetime-local-input" className="mb-2">Дата и время конца:</label>
                            <input
                                id="datetime-local-input"
                                type="datetime-local"
                                value={currentSlot.end_time}
                                onChange={(e) => setCurrentSlot({...currentSlot, end_time: e.target.value})}
                                className="border p-2 rounded w-full"
                            />
                        </div>
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
