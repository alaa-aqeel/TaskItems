import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import './assets/main.css'

import { useUserStore } from '@/stores/auth';
import axios from "@/plugins/axios"


const app = createApp(App)


router.beforeEach((to, from, next)=>{
    const store = useUserStore()

    if(to.matched.some(record => record.meta.requiredAuth)) {
        if (store.getAccessToken()) {
            next()
            return
        }
        store.logout()
        next('/login')
    } else if(to.matched.some(record => record.meta.guest)) {
        if (store.getAccessToken()) {
            next({name: "home"})
            return
        }
        next()
    }
})


app.use(createPinia())
app.use(router)


axios.get("me")
    .then((resp)=> {
        const store = useUserStore()
        store.user = resp.data
    })
    .finally(()=> app.mount('#app'))

