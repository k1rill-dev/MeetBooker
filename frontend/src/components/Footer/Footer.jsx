import React from 'react';

const Footer = () => {
    return (
        <div className="bg-white shadow-md mt-8">
            <div className="bg-gray-100 border-t border-gray-200 mt-4 py-4 px-4 text-gray-800 text-center">
                &copy; {new Date().getFullYear()} MeetBooker. Все права защищены.
            </div>
        </div>


    );
};

export default Footer;