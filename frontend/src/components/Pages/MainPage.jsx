import React from 'react';
import {useNavigate} from "react-router-dom";


const MainPage = () => {
    const nav = useNavigate()
    return (
        <div>
            <section className="bg-blue-900 text-white py-20">
                <div className="container mx-auto px-4 flex flex-col items-center">
                    <h1 className="text-4xl md:text-6xl font-bold mb-6 text-center">Нужна помощь?</h1>
                    <p className="text-lg mb-8 text-center max-w-lg">Забронируй встречу с сертифицированным
                        специалистом</p>
                    <button
                        onClick={() => nav('/register')}
                        className="bg-white text-blue-900 py-2 px-6 rounded-full shadow-lg font-semibold text-lg hover:bg-gray-200 transition duration-300">
                        Регистрация
                    </button>
                    <button
                        onClick={() => nav('/specialists')}
                        className="mt-4 bg-white text-blue-900 py-2 px-6 rounded-full shadow-lg font-semibold text-lg hover:bg-gray-200 transition duration-300">
                        Наши специалисты
                    </button>
                </div>
            </section>
            <section className="py-20">
                <div className="container mx-auto px-4">
                    <h2 className="text-3xl font-bold mb-10 text-center">Как это работает?</h2>
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-12">
                        <div className="text-center">
                            <div
                                className="bg-blue-900 text-white rounded-full p-4 mx-auto mb-6 w-16 h-16 flex items-center justify-center">
                                <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                                     xmlns="http://www.w3.org/2000/svg">
                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2"
                                          d="M13 10V3L4 14h7v7l9-11h-7z"></path>
                                </svg>
                            </div>
                            <h3 className="text-xl font-semibold mb-4">Находи специалистов</h3>
                            <p>Найди нужного тебе специалиста</p>
                        </div>
                        <div className="text-center">
                            <div
                                className="bg-blue-900 text-white rounded-full p-4 mx-auto mb-6 w-16 h-16 flex items-center justify-center">
                                <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                                     xmlns="http://www.w3.org/2000/svg">
                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2"
                                          d="M8 14l4 4 4-4m-4-5v9"></path>
                                </svg>
                            </div>
                            <h3 className="text-xl font-semibold mb-4">Бронируй встречи</h3>
                            <p>Планируй встречи в удобное время.</p>
                        </div>
                        <div className="text-center">
                            <div
                                className="bg-blue-900 text-white rounded-full p-4 mx-auto mb-6 w-16 h-16 flex items-center justify-center">
                                <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                                     xmlns="http://www.w3.org/2000/svg">
                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2"
                                          d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
                                </svg>
                            </div>
                            <h3 className="text-xl font-semibold mb-4">Управляй расписанием</h3>
                            <p>Специалисты сами выбирают себе расписание.</p>
                        </div>
                    </div>
                </div>
            </section>
            <section className="py-20 bg-gray-100">
                <div className="container mx-auto px-4">
                    <h2 className="text-3xl font-bold mb-10 text-center">Что говорят наши пользователи?</h2>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-12">
                        <div className="bg-white p-6 rounded-lg shadow-lg">
                            <p className="text-lg mb-4">"ЭТО ПРОСТО ИМБА!!"</p>
                            <p className="text-gray-600">John Doe, CEO Company A</p>
                        </div>
                        <div className="bg-white p-6 rounded-lg shadow-lg">
                            <p className="text-lg mb-4">"Ну это полная конфетка, заходите срочно."</p>
                            <p className="text-gray-600">Jane Smith, CTO at Company B</p>
                        </div>
                    </div>
                </div>
            </section>

        </div>
    );
};

export default MainPage;
