import React from 'react';
import {FaUserPlus, FaSignInAlt} from 'react-icons/fa';


const MainPage = () => {
    return (
        <div className="min-h-screen flex flex-col">
            <header className="relative bg-cover bg-center py-20"
                    style={{backgroundImage: 'url(/path/to/new-background-image.jpg)'}}>
                <div className="absolute inset-0 bg-black opacity-50"></div>
                <div className="relative z-10">
                    <h1 className="text-5xl font-bold text-white text-center drop-shadow-lg">
                        Приложение для бронирования встреч
                    </h1>
                </div>
            </header>
            <main className="flex-grow bg-gray-100">
                <section className="py-20 text-center">
                    <div className="container mx-auto">
                        <p className="text-lg mb-8 text-gray-800 max-w-lg mx-auto">
                            Удобный сервис для бронирования встреч и управления вашими делами. Планируйте и организуйте
                            свои
                            встречи легко и эффективно.
                        </p>
                        <div className="flex justify-center space-x-4">
                            <a href="/register"
                               className="bg-blue-500 text-white px-6 py-3 rounded-lg shadow-lg hover:bg-blue-600 flex items-center space-x-2 transition duration-300">
                                <FaUserPlus/>
                                <span>Регистрация</span>
                            </a>
                            <a href="/login"
                               className="bg-gray-800 text-white px-6 py-3 rounded-lg shadow-lg hover:bg-gray-700 flex items-center space-x-2 transition duration-300">
                                <FaSignInAlt/>
                                <span>Вход</span>
                            </a>
                        </div>
                    </div>
                </section>

                <section className="bg-gray-100 py-16">
                    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                        <h2 className="text-3xl font-semibold text-gray-800 text-center mb-8">Основные возможности</h2>
                        <div className="space-y-16">
                            <div className="flex flex-col lg:flex-row items-center">
                                <img src="https://via.placeholder.com/600x400" alt="Простое бронирование"
                                     className="w-full lg:w-1/2 rounded-lg shadow-lg mb-8 lg:mb-0 lg:mr-8"/>
                                <div className="lg:w-1/2 text-center lg:text-left">
                                    <h3 className="text-2xl font-semibold text-gray-800">Простое бронирование</h3>
                                    <p className="mt-4 text-gray-600">Легко бронируйте встречи с помощью нашего
                                        интуитивно
                                        понятного интерфейса.</p>
                                </div>
                            </div>
                            <div className="flex flex-col lg:flex-row-reverse items-center">
                                <img src="https://via.placeholder.com/600x400" alt="Управление расписанием"
                                     className="w-full lg:w-1/2 rounded-lg shadow-lg mb-8 lg:mb-0 lg:ml-8"/>
                                <div className="lg:w-1/2 text-center lg:text-left">
                                    <h3 className="text-2xl font-semibold text-gray-800">Управление расписанием</h3>
                                    <p className="mt-4 text-gray-600">Организуйте своё расписание и никогда не
                                        пропустите
                                        важные встречи.</p>
                                </div>
                            </div>
                            <div className="flex flex-col lg:flex-row items-center">

                                <img src="https://via.placeholder.com/600x400" alt="Напоминания"
                                     className="w-full lg:w-1/2 rounded-lg shadow-lg mb-8 lg:mb-0 lg:mr-8"/>
                                <div className="lg:w-1/2 text-center lg:text-left">
                                    <h3 className="text-2xl font-semibold text-gray-800">Напоминания</h3>
                                    <p className="mt-4 text-gray-600">Получайте напоминания о предстоящих встречах и
                                        событиях.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </main>
            <footer className="bg-gray-900 text-white w-full py-4 text-center">
                <p>&copy; 2024 Приложение для бронирования встреч. Все права защищены.</p>
            </footer>
        </div>
    );
};

export default MainPage;
