import axios from "axios";

const api = axios.create({
    baseURL: process.env.NEXT_PUBLIC_API,
    headers: {
        "Content-Type": "application/json",
    },
    timeout: 10000,
});

api.interceptors.request.use(
    (config) => {
        console.log(
            `[API] ${config.method?.toUpperCase()} ${config.url}`
        );
        return config;
    },
    (error) => Promise.reject(error)
);

api.interceptors.response.use(
    (response) => response,
    (error) => {
        console.error(error.response?.data);

        return Promise.reject(error);
    }
);

export default api;