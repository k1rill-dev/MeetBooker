import React from 'react';

const EditUserModal = ({ user, setUser, handleSubmit, handleClose }) => {
  return (
    <div className="fixed inset-0 flex items-center justify-center z-50">
      <div className="absolute inset-0 bg-gray-900 opacity-50"></div>
      <div className="bg-white w-full max-w-lg p-6 rounded-lg shadow-lg z-50">
        <h2 className="text-2xl font-bold mb-4">Edit Profile</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="name">
              Name
            </label>
            <input
              type="text"
              id="name"
              className="form-input w-full"
              value={user.name}
              onChange={(e) => setUser({ ...user, name: e.target.value })}
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
              className="form-input w-full"
              value={user.email}
              onChange={(e) => setUser({ ...user, email: e.target.value })}
              required
            />
          </div>
          <div className="flex justify-end">
            <button
              type="submit"
              className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded mr-2 focus:outline-none focus:shadow-outline"
            >
              Save Changes
            </button>
            <button
              type="button"
              className="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
              onClick={handleClose}
            >
              Cancel
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default EditUserModal;
