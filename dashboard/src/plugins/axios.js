import axios from "axios"
import store from "@/store"
import router from "@/router";
// import router from "@/router";

const instance = axios.create({
    baseURL: process.env.VUE_APP_BASE_API_URL+'/api/v1/admin',
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