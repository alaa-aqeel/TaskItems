import axios from "axios"

const instance = axios.create({
    baseURL: import.meta.env.VITE_BASE_URL+'/api/',
    headers: {
      "Accept": "application/json",
      "Content-Type": "application/json"
    }
});

instance.defaults.headers.common['Authorization'] = "Bearer "+localStorage.getItem("access_token");


instance.interceptors.response.use(
  function (response) {
    // Success
    instance.defaults.headers.common['Authorization'] = "Bearer "+localStorage.getItem("access_token");
    return response;
  }, 
  function (error) {
    
    return Promise.reject(error);
  });

export default instance;