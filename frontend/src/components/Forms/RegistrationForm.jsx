import React from 'react';

const RegistrationForm = () => {
    const handleYandexLogin = () => {
        window.location.href = 'https://oauth.yandex.ru/authorize?response_type=code&client_id=ВАШ_CLIENT_ID';
    };

    return (
        <div className="flex items-center justify-center min-h-screen bg-gradient-to-b from-white to-blue-400">
            <div className="bg-white p-8 rounded-lg shadow-md w-full max-w-md">
                <h2 className="text-3xl font-bold mb-6 text-gray-900 text-center">Регистрация</h2>
                <form className="space-y-4">
                    <div className="grid grid-cols-2 gap-4">
                        <div>
                            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="firstName">
                                Имя
                            </label>
                            <input
                                type="text"
                                id="firstName"
                                placeholder="Введите ваше имя"
                                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                            />
                        </div>
                        <div>
                            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="lastName">
                                Фамилия
                            </label>
                            <input
                                type="text"
                                id="lastName"
                                placeholder="Введите вашу фамилию"
                                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                            />
                        </div>
                    </div>
                    <div>
                        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="email">
                            Email
                        </label>
                        <input
                            type="email"
                            id="email"
                            placeholder="Введите ваш email"
                            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                        />
                    </div>
                    <div>
                        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="password">
                            Пароль
                        </label>
                        <input
                            type="password"
                            id="password"
                            placeholder="Введите ваш пароль"
                            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                        />
                    </div>
                    <div>
                        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="confirm-password">
                            Повторите пароль
                        </label>
                        <input
                            type="password"
                            id="confirm-password"
                            placeholder="Повторите ваш пароль"
                            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                        />
                    </div>
                    <div>
                        <button
                            type="submit"
                            className="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                        >
                            Зарегистрироваться
                        </button>
                    </div>
                </form>
                <div className="mt-4 text-center">
                    <p className="text-sm text-gray-600">Уже есть аккаунт? <a href="#"
                                                                              className="font-medium text-indigo-600 hover:text-indigo-500">Войдите</a>
                    </p>
                    <p className="text-sm text-gray-600">или</p>
                </div>
                <div className="mt-6 text-center">
                    <button
                        onClick={handleYandexLogin}
                        className="w-full bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                    >
                        Войти через Яндекс
                    </button>
                </div>
            </div>
        </div>
    );
};

export default RegistrationForm;