import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from "@/plugins/axios.js"


export const useItemsStore = defineStore('items', {
  state: () => ({
      items: [],
      canNext: null,
      canPrev: null,
      count: null,
      columns: [
        {text: "#", name: "id"},
        {text: "Image", name: "image"},
        {text: "Name", name: "name"},
        {text: "Expired At", name: "expired_at"},
      ],
      current: {}
  }),
  actions: {
    async getAll() {
      return await axios.get("items")
            .then(resp => {
              this.items = resp.data.results
              this.canNext = !!resp.data.next
              this.canPrev = !!resp.data.Prev
              this.count = resp.data.count
            })
    },
    async create(fd) {

      return await axios.post("items/", fd)
    },
    async update(id, fd) {

      return await axios.put(`items/${id}/`, fd)
    },
    async delete(id) {

      return await axios.delete(`items/${id}/`)
    }
  }
})
