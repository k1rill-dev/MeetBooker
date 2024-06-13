import React from 'react';
import ReviewsAndRatings from "../SpecialistInfo/ReviewsAndRatings";
import AppointmentsManagement from "../SpecialistInfo/AppointmentsManagement";
import ScheduleManagement from "../SpecialistInfo/ScheduleManagement";
import InfoAbout from "../SpecialistInfo/InfoAbout";

const SpecInfo = () => {
  return (
    <div className="container mx-auto p-4 space-y-6">
      <h1 className="text-3xl font-bold mb-4 text-center">Личный кабинет специалиста</h1>
      <InfoAbout />
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <ScheduleManagement />
        <AppointmentsManagement />
      </div>
      <ReviewsAndRatings />
    </div>
  );

};

export default SpecInfo;