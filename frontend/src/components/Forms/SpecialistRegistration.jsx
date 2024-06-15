import React from 'react';
import {Textarea} from "flowbite-react";

const SpecialistRegistration = ({handlePreviousStep, userId, setSpeciality, setBio, handleSendSpecialistData}) => {
    return (
        <>
            <form onSubmit={(event) => handleSendSpecialistData(event)} className="space-y-4">
                <div>
                    <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="speciality">
                        Специальность
                    </label>
                    <input
                        onChange={(event) => setSpeciality(event.target.value)}
                        type="text"
                        id="speciality"
                        placeholder="Ваша специальность"
                        className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    />
                </div>
                <div>
                    <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="bio">
                        О себе
                    </label>
                    <Textarea
                        onChange={(event) => setBio(event.target.value)}
                        className={"shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"}
                        id="bio" placeholder="Расскажите нам о себе" required rows={4}/>
                </div>
                <div>
                    <button
                        type="submit"
                        className="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                    >
                        Отправить на проверку
                    </button>
                    <div className={"mt-4"}></div>
                    <button
                        type="submit"
                        onClick={() => handlePreviousStep()}
                        className="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                    >
                        Не все заполнили? Вернуться обратно
                    </button>
                </div>
            </form>
        </>
    );
};

export default SpecialistRegistration;