import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from "@/plugins/axios.js"


export const useAccsessTokenStore = defineStore('login', {
    state: () => ({
        user: {}
    }),
    actions: {

        async login(fd) {
            return await axios.post("login/", fd) 
                .then( resp=>{
                    
                    this.setAccessToken(resp.data.access)
                    return resp
                })
        },
        setAccessToken(accessToken) {

            localStorage.setItem("access_token", accessToken)
        }
    }


})
