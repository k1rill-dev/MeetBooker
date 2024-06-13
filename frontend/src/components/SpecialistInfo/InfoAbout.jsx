import React, { useState } from 'react';
import { Modal, Button } from 'flowbite-react';

const InfoAbout = () => {
  const [info, setInfo] = useState({
    fullName: 'Иван Иванов',
    bio: 'Опытный специалист в области психологии.',
    specialty: 'Психолог',
    email: 'ivanov@example.com',
  });

  const [modalOpen, setModalOpen] = useState(false);
  const [tempInfo, setTempInfo] = useState(info);

  const handleSave = () => {
    setInfo(tempInfo);
    setModalOpen(false);
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h2 className="text-2xl font-bold mb-4">Информация о тебе</h2>
      <p><strong>ФИО:</strong> {info.fullName}</p>
      <p><strong>Биография:</strong> {info.bio}</p>
      <p><strong>Специальность:</strong> {info.specialty}</p>
      <p><strong>Email:</strong> {info.email}</p>
      <Button onClick={() => setModalOpen(true)} className="mt-4">Редактировать</Button>

      <Modal show={modalOpen} onClose={() => setModalOpen(false)}>
        <Modal.Header>
          Редактировать информацию
        </Modal.Header>
        <Modal.Body>
          <div className="space-y-4">
            <input
              type="text"
              value={tempInfo.fullName}
              onChange={(e) => setTempInfo({ ...tempInfo, fullName: e.target.value })}
              className="border p-2 rounded w-full"
              placeholder="ФИО"
            />
            <textarea
              value={tempInfo.bio}
              onChange={(e) => setTempInfo({ ...tempInfo, bio: e.target.value })}
              className="border p-2 rounded w-full"
              placeholder="Биография"
            />
            <input
              type="text"
              value={tempInfo.specialty}
              onChange={(e) => setTempInfo({ ...tempInfo, specialty: e.target.value })}
              className="border p-2 rounded w-full"
              placeholder="Специальность"
            />
            <input
              type="email"
              value={tempInfo.email}
              onChange={(e) => setTempInfo({ ...tempInfo, email: e.target.value })}
              className="border p-2 rounded w-full"
              placeholder="Email"
            />
          </div>
        </Modal.Body>
        <Modal.Footer>
          <Button onClick={handleSave}>Сохранить</Button>
        </Modal.Footer>
      </Modal>
    </div>
  );
};

export default InfoAbout;
