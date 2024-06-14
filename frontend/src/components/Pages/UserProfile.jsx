import React, {useState} from 'react';
import EditUserModal from "../Modals/EditUserModal";

const UserProfile = () => {
    const [user, setUser] = useState({
        name: 'John Doe',
        email: 'john.doe@example.com',
        bookings: [
            {id: 1, date: '2024-06-15', status: 'Confirmed'},
            {id: 2, date: '2024-06-17', status: 'Pending'},
        ],
        bookingHistory: [
            {id: 3, date: '2024-06-10', status: 'Completed'},
            {id: 4, date: '2024-05-25', status: 'Completed'},
        ],
    });

    const [isModalOpen, setIsModalOpen] = useState(false);

    const handleSubmit = (e) => {
        e.preventDefault();
        // Simulate API call to update user data
        // In a real app, this would be replaced with an actual API call
        console.log('Updated user:', user);
        setIsModalOpen(false);
    };

    const openModal = () => {
        setIsModalOpen(true);
    };

    const closeModal = () => {
        setIsModalOpen(false);
    };

    return (
        <div className="min-h-screen flex items-center justify-center">
            <div className="bg-white w-full max-w-4xl rounded-lg shadow-lg overflow-hidden">
                <div className="px-6 py-8 md:flex md:items-center md:justify-between">
                    <div className="md:flex md:items-center">
                        <div className="md:flex-shrink-0">
                            <img
                                className="h-24 w-24 rounded-full object-cover mx-auto md:mx-0 md:mr-4"
                                src="https://randomuser.me/api/portraits/men/1.jpg"
                                alt="User avatar"
                            />
                        </div>
                        <div className="mt-4 md:mt-0">
                            <h1 className="text-2xl font-bold text-gray-800">{user.name}</h1>
                            <p className="text-sm text-gray-600">{user.email}</p>
                        </div>
                    </div>
                    <div className="mt-4 md:mt-0">
                        <button
                            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                            onClick={openModal}
                        >
                            Edit Profile
                        </button>
                    </div>
                </div>

                <div className="border-t border-gray-200 px-6 py-4">
                    <div className="border-t border-gray-200 px-6 py-4">
                        <div className="mb-8">
                            <h2 className="text-xl font-semibold text-gray-800">Bookings</h2>
                            <div className="mt-4">
                                {user.bookings.length > 0 ? (
                                    <div className="overflow-x-auto">
                                        <table className="table-auto w-full border-collapse">
                                            <thead>
                                            <tr className="bg-gray-100">
                                                <th className="px-4 py-2 text-left text-sm font-semibold text-gray-600 uppercase border-b">Date</th>
                                                <th className="px-4 py-2 text-left text-sm font-semibold text-gray-600 uppercase border-b">Status</th>
                                            </tr>
                                            </thead>
                                            <tbody>
                                            {user.bookings.map((booking) => (
                                                <tr key={booking.id} className="border-b">
                                                    <td className="px-4 py-3 text-sm text-gray-600">{booking.date}</td>
                                                    <td className="px-4 py-3 text-sm text-gray-600">{booking.status}</td>
                                                </tr>
                                            ))}
                                            </tbody>
                                        </table>
                                    </div>
                                ) : (
                                    <p className="text-sm text-gray-600">No bookings found.</p>
                                )}
                            </div>
                        </div>

                        <div>
                            <h2 className="text-xl font-semibold text-gray-800">Booking History</h2>
                            <div className="mt-4">
                                {user.bookingHistory.length > 0 ? (
                                    <div className="overflow-x-auto">
                                        <table className="table-auto w-full border-collapse">
                                            <thead>
                                            <tr className="bg-gray-100">
                                                <th className="px-4 py-2 text-left text-sm font-semibold text-gray-600 uppercase border-b">Date</th>
                                                <th className="px-4 py-2 text-left text-sm font-semibold text-gray-600 uppercase border-b">Status</th>
                                            </tr>
                                            </thead>
                                            <tbody>
                                            {user.bookingHistory.map((historyItem) => (
                                                <tr key={historyItem.id} className="border-b">
                                                    <td className="px-4 py-3 text-sm text-gray-600">{historyItem.date}</td>
                                                    <td className="px-4 py-3 text-sm text-gray-600">{historyItem.status}</td>
                                                </tr>
                                            ))}
                                            </tbody>
                                        </table>
                                    </div>
                                ) : (
                                    <p className="text-sm text-gray-600">No booking history found.</p>
                                )}
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            {isModalOpen && (
                <EditUserModal
                    user={user}
                    setUser={setUser}
                    handleSubmit={handleSubmit}
                    handleClose={closeModal}
                />
            )}
        </div>
    );
};

export default UserProfile;
