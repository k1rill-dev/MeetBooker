import React, {useState, useEffect} from 'react';
import {Modal, Button} from 'flowbite-react';
import axios from 'axios';
import api from "../../api";
import {useNavigate} from "react-router-dom";

const InfoAbout = ({user, specialist}) => {
    const [info, setInfo] = useState(user);
    const [modalOpen, setModalOpen] = useState(false);
    const nav = useNavigate();
    const [tempInfo, setTempInfo] = useState({
        first_name: user.first_name || '',
        last_name: user.last_name || '',
        email: user.email || '',
        bio: specialist.bio || '',
        speciality: specialist.speciality || ''
    });
    const [profileImage, setProfileImage] = useState(null);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        setTempInfo({
            first_name: user.first_name || '',
            last_name: user.last_name || '',
            email: user.email || '',
            bio: specialist.bio || '',
            speciality: specialist.speciality || ''
        });
    }, [specialist]);

    const handleSave = async () => {
        setLoading(true);
        try {
            const formData = new FormData();
            formData.append('first_name', tempInfo.first_name);
            formData.append('last_name', tempInfo.last_name);
            formData.append('email', tempInfo.email);
            if (profileImage) {
                formData.append('file', profileImage);
            }

            const userResponse = await api.patch('/api/update_user', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                },
                withCredentials: true
            });

            const specialistResponse = await api.patch('/api/specialist', {
                bio: tempInfo.bio,
                speciality: tempInfo.speciality,
                user_id: user.id
            }, {
                headers: {
                    'Content-Type': 'application/json'
                },
                withCredentials: true
            });

            setInfo(tempInfo);
            setModalOpen(false);
        } catch (error) {
            console.error('Error updating information:', error);
        } finally {
            setLoading(false);
        }
    };

    const handleFileChange = (e) => {
        const file = e.target.files[0];
        setProfileImage(file);
    };

    return (
        <div className="bg-white p-6 rounded-lg shadow-md">
            <h2 className="text-2xl font-bold mb-4">Информация о тебе</h2>
            <p><strong>ФИО:</strong> {tempInfo.first_name} {tempInfo.last_name}</p>
            <p><strong>Биография:</strong> {tempInfo.bio}</p>
            <p><strong>Специальность:</strong> {tempInfo.speciality}</p>
            <p><strong>Email:</strong> {tempInfo.email}</p>
            <Button onClick={() => setModalOpen(true)} className="mt-4">Редактировать</Button>
            <Button onClick={() => nav('/logout')} className="mt-4">Выйти из аккаунта</Button>

            <Modal show={modalOpen} onClose={() => setModalOpen(false)}>
                <Modal.Header>
                    Редактировать информацию
                </Modal.Header>
                <Modal.Body>
                    <div className="space-y-4">
                        <input
                            type="text"
                            value={tempInfo.first_name}
                            onChange={(e) => setTempInfo({...tempInfo, first_name: e.target.value})}
                            className="border p-2 rounded w-full"
                            placeholder="ФИО"
                        />
                        <input
                            type="text"
                            value={tempInfo.last_name}
                            onChange={(e) => setTempInfo({...tempInfo, last_name: e.target.value})}
                            className="border p-2 rounded w-full"
                            placeholder="ФИО"
                        />
                        <textarea
                            value={tempInfo.bio}
                            onChange={(e) => setTempInfo({...tempInfo, bio: e.target.value})}
                            className="border p-2 rounded w-full"
                            placeholder="Биография"
                        />
                        <input
                            type="text"
                            value={tempInfo.speciality}
                            onChange={(e) => setTempInfo({...tempInfo, speciality: e.target.value})}
                            className="border p-2 rounded w-full"
                            placeholder="Специальность"
                        />
                        <input
                            type="email"
                            value={tempInfo.email}
                            onChange={(e) => setTempInfo({...tempInfo, email: e.target.value})}
                            className="border p-2 rounded w-full"
                            placeholder="Email"
                        />
                        <input
                            type="file"
                            onChange={handleFileChange}
                            className="border p-2 rounded w-full"
                            accept="image/*"
                        />
                    </div>
                </Modal.Body>
                <Modal.Footer>
                    <Button onClick={handleSave} disabled={loading}>{loading ? 'Сохранение...' : 'Сохранить'}</Button>
                </Modal.Footer>
            </Modal>
        </div>
    );
};

export default InfoAbout;
