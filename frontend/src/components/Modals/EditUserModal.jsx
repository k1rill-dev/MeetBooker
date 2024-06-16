import React, { useState } from 'react';
import axios from 'axios';

const EditUserModal = ({ user, handleSubmit, handleClose }) => {
    const [updatedUser, setUpdatedUser] = useState({
        first_name: user.first_name,
        last_name: user.last_name,
        email: user.email,
        file: null, // Добавляем состояние для файла фотографии
    });

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setUpdatedUser({ ...updatedUser, [name]: value });
    };

    const handleFileChange = (e) => {
        setUpdatedUser({ ...updatedUser, file: e.target.files[0] });
    };

    const onSubmit = (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append('first_name', updatedUser.first_name);
        formData.append('last_name', updatedUser.last_name);
        formData.append('email', updatedUser.email);
        if (updatedUser.file) {
            formData.append('file', updatedUser.file);
        }

        handleSubmit(formData);
    };

    return (
        <div className="fixed inset-0 flex items-center justify-center z-50">
            <div className="absolute inset-0 bg-gray-900 opacity-50"></div>
            <div className="bg-white w-full max-w-lg p-6 rounded-lg shadow-lg z-50">
                <h2 className="text-2xl font-bold mb-4">Edit Profile</h2>
                <form onSubmit={onSubmit}>
                    <div className="mb-4">
                        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="first_name">
                            Имя
                        </label>
                        <input
                            type="text"
                            id="first_name"
                            name="first_name"
                            className="form-input w-full"
                            value={updatedUser.first_name}
                            onChange={handleInputChange}
                            required
                        />
                    </div>
                    <div className="mb-4">
                        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="last_name">
                            Фамилия
                        </label>
                        <input
                            type="text"
                            id="last_name"
                            name="last_name"
                            className="form-input w-full"
                            value={updatedUser.last_name}
                            onChange={handleInputChange}
                            required
                        />
                    </div>
                    <div className="mb-4">
                        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="email">
                            Email
                        </label>
                        <input
                            type="email"
                            id="email"
                            name="email"
                            className="form-input w-full"
                            value={updatedUser.email}
                            onChange={handleInputChange}
                            required
                        />
                    </div>
                    <div className="mb-4">
                        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="file">
                            Фото профиля
                        </label>
                        <input
                            type="file"
                            id="file"
                            name="file"
                            className="form-input w-full"
                            onChange={handleFileChange}
                        />
                        {updatedUser.file && (
                            <img
                                className="mt-2 rounded-lg"
                                src={URL.createObjectURL(updatedUser.file)}
                                alt="Preview"
                                style={{ maxWidth: '100px' }}
                            />
                        )}
                    </div>
                    <div className="flex justify-end">
                        <button
                            type="submit"
                            className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded mr-2 focus:outline-none focus:shadow-outline"
                        >
                            Сохранить
                        </button>
                        <button
                            type="button"
                            className="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                            onClick={handleClose}
                        >
                            Отмена
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
};

export default EditUserModal;
