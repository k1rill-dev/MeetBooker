import axios from 'axios';

export const BACKEND_API_URL = "http://localhost:8000";

const api = axios.create({
    baseURL: BACKEND_API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
    withCredentials: true,
});

const refreshAccessToken = async () => {
    try {
        const response = await api.post('/api/rotate');
        return response.data;
    } catch (error) {
        console.error('Ошибка обновления токена', error);
        throw error;
    }
};

api.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config;
        if (error.response.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;
            try {
                await refreshAccessToken();
                return api(originalRequest);
            } catch (error) {
                console.error('Не удалось обновить токен', error);
                return Promise.reject(error);
            }
        }
        return Promise.reject(error);
    }
);

export default api;
