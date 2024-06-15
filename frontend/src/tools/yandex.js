import axios from "axios";
import {BACKEND_API_URL} from "../api";


export const handleYandexLogin = async () => {
    let response = await axios.get(BACKEND_API_URL + "/api/login/yandex", {
        headers: {
            'Content-Type': 'application/json',
            Accept: 'application/json'
        }
    }).then(r => r.data)
    window.location.href = response.auth_url;
};