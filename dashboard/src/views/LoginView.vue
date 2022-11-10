<template>
    <div class="container mx-auto flex items-center justify-center min-h-screen w-1/5">

        <div class="w-full">
            <h1 class="text-8xl text-gray-500 drop-shadow-xl">
                Login 
            </h1>
            <LoginForm />
        </div>

    </div>
</template>


<script setup>
import LoginForm from '@/components/forms/LoginForm.vue';

</script>