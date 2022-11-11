<template>
    <nav class="bg-white px-2 sm:px-4 py-2.5 rounded border-b border-gray-200">
        <div class="container flex flex-wrap justify-between items-center mx-auto">
            <a href="https://flowbite.com/" class="flex items-center">
                <span class="self-center text-xl font-semibold whitespace-nowrap dark:text-white">
                    Task 
                </span>
            </a>

            <div class="hidden w-full md:block md:w-auto" id="navbar-default">
                <ul class="flex flex-col p-4 mt-4 bg-gray-50 rounded-lg border border-gray-100 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">
                    <li>
                        <RouterLink 
                            :to="{name: 'home'}" 
                            class="block py-2 pr-4 pl-3 text-white hover:text-blue-500 bg-gray-700 rounded md:bg-transparent md:text-gray-700 md:p-0" 
                            >
                            Home
                        </RouterLink>
                    </li>

                    <li>
                        <RouterLink 
                            :to="{name: 'items'}" 
                            class="block py-2 pr-4 pl-3 hover:text-blue-500 text-white bg-gray-700 rounded md:bg-transparent md:text-gray-700 md:p-0" 
                            >
                            Items
                        </RouterLink>
                    </li>

                </ul>
            </div>
            <div class="flex md:order-2 items-center justify-center gap-1">
                <h1 class="font-medium">
                    {{ store.user.username }}
                </h1>
                <button 
                    type="button" 
                    @click="logout"
                    class="text-red-700 hover:text-red-800 focus:ring-4 focus:outline-none  font-medium rounded-lg text-sm px-2 py-2.5 text-center mr-3 md:mr-0 ">
                    Logout
                </button>
            </div>
        </div>
    </nav>
</template>


<script setup>
import { RouterLink, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/auth';

const store = useUserStore()
const router = useRouter()

const logout = () => {
    store.logout()
    router.push({name: "login"})
}

</script>
