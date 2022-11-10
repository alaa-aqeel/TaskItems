import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from "@/plugins/axios.js"


export const useItemsStore = defineStore('items', () => {

  



  return { count, doubleCount, increment }
})
