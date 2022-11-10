import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from "@/plugins/axios.js"


export const useUserStore = defineStore('user', {
    state: () => ({
        user: {},
        isAuthenticated: false
    }),
    actions: {
        async profile() {

            return await axios.get("me/")
                .then((resp)=>{
                    this.user = resp.data
                    return resp
                })
        },
        async login(fd) {
            return await axios.post("login/", fd) 
                .then( resp=>{
                    
                    this.setAccessToken(resp.data.access)
                    this.isAuthenticated = true
                    return resp
                })
        },
        logout(){
            localStorage.removeItem("access_token")
            this.isAuthenticated = false
        },
        setAccessToken(accessToken) {

            localStorage.setItem("access_token", accessToken)
        },
        getAccessToken() {

            return localStorage.getItem("access_token")
        }
    }
})
