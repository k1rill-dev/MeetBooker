import React, {useEffect, useState} from 'react';

const Header = () => {
    const [isOpen, setIsOpen] = useState(false);
    const toggleMenu = () => {
        setIsOpen(!isOpen);
    };

    const closeMenu = () => {
        setIsOpen(false);
    };
    useEffect(() => {

    }, []);

    return (
        <div className="bg-white shadow-md">
            <div className="container mx-auto px-4 py-4 flex justify-between items-center">
                <div className="text-gray-800 text-xl font-bold flex items-center">
                    <svg className="h-6 w-6 mr-2" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M12 0C5.373 0 0 5.372 0 12c0 2.815 1.003 5.403 2.678 7.438L12 24l9.322-4.562C22.996 17.403 24 14.814 24 12c0-6.628-5.373-12-12-12zM5 12c0-1.939.532-3.747 1.45-5.291l7.841 7.842V12H5zm7 7.991L6.009 11H19l-5 5v4.991zM12 6.009L16.991 11H7.008L12 6.009z"
                            fill="currentColor"/>
                    </svg>
                    MeetBooker
                </div>
                <nav className="hidden md:flex md:items-center md:space-x-4 md:flex-1 md:justify-center">
                    <a href="/"
                       className="text-gray-800 hover:text-gray-600 transition duration-300 ease-in-out">Главная</a>
                    <a href="/concerts"
                       className="text-gray-800 hover:text-gray-600 transition duration-300 ease-in-out">что эт</a>
                </nav>
                <div className="flex items-center">
                    <nav className="hidden md:flex md:items-center md:space-x-4">
                        <a href='/login'>Войти в аккаунт</a>
                    </nav>
                    <div className="md:hidden">
                        <button onClick={toggleMenu} className="text-gray-800 focus:outline-none">
                            <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2}
                                      d="M4 6h16M4 12h16m-7 6h7"/>
                            </svg>
                        </button>
                    </div>
                </div>
            </div>
            <nav
                className={`fixed top-0 right-0 h-full w-full md:hidden z-20 transition-transform ${isOpen ? 'translate-x-0' : 'translate-x-full'} bg-gray-100 shadow-lg p-4`}>
                <button onClick={closeMenu} className="absolute top-0 right-0 m-4 text-gray-800 focus:outline-none">
                    <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12"/>
                    </svg>
                </button>
                <div className="py-2 flex flex-col items-center">
                    <a href="/"
                       className="text-gray-800 hover:text-gray-600 transition duration-300 ease-in-out block py-2">Главная</a>
                    <a href="/concerts"
                       className="text-gray-800 hover:text-gray-600 transition duration-300 ease-in-out block py-2">Что эт</a>
                    <div className="flex items-center mt-4">
                        <a href='/login'>Войти в аккаунт</a>
                    </div>
                </div>
            </nav>
        </div>
    );
}

export default Header;