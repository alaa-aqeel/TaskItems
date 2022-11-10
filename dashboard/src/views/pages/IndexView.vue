
<template>
    <div>
  
      <Navbar />
  
      <div class="container mx-auto m-10 p-6 ">
  
        <RouterView />
  
      </div>
    </div>
  </template>
  
  
  
  <script setup>
  import { RouterLink, RouterView } from 'vue-router'
  import  Navbar from '@/components/Navbar.vue'
  
  
  
  </script>
  
  