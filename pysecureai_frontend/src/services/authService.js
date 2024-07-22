import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL;

const register = async (username, email, password) => {
    await axios.post(`${API_URL}/auth/register`, {
        username,
        email,
        password,
    });
};

const login = async (username, password) => {
    const response = await axios.post(`${API_URL}/auth/login`, {
        username,
        password,
    });
    localStorage.setItem('user', JSON.stringify(response.data));
};

const authService = {
    register,
    login,
};

export default authService;
