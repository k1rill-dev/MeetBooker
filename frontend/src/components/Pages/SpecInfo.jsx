import React, {useEffect, useState} from 'react';
import AppointmentsManagement from "../SpecialistInfo/AppointmentsManagement";
import ScheduleManagement from "../SpecialistInfo/ScheduleManagement";
import InfoAbout from "../SpecialistInfo/InfoAbout";
import getCookie from "../../tools/getCookie";
import api from "../../api";

const SpecInfo = () => {
    const [user, setUser] = useState({});
    const [specData, setSpecData] = useState({});

    useEffect(() => {
        const fetchData = async () => {
            try {
                const isLogin = getCookie('login');
                if (isLogin) {
                    const userDataResponse = await api.get('/api/', {withCredentials: true});
                    setUser(userDataResponse.data);

                    const specDataResponse = await api.get('/api/specialist-by-user-id', {withCredentials: true});
                    setSpecData(specDataResponse.data);
                }
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };
        fetchData();
    }, []);

    return (
        <div className="container mx-auto p-4 space-y-6">
            <h1 className="text-3xl font-bold mb-4 text-center">Личный кабинет специалиста</h1>
            <InfoAbout user={user} specialist={specData}/>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <ScheduleManagement user={user} specialist={specData}/>
                <AppointmentsManagement user={user} specialist={specData}/>
            </div>
        </div>
    );

};

export default SpecInfo;