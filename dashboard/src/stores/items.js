import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from "@/plugins/axios.js"


export const useItemsStore = defineStore('items', {
  state: () => ({
      items: [],
      nextPage: null,
      prevPage: null,
      count: 0,
      totalPage: 0,
      columns: [
        {text: "#", name: "id"},
        {text: "Image", name: "image"},
        {text: "Name", name: "name"},
        {text: "Expired At", name: "expired_at"},
      ],
      current: {}
  }),
  actions: {
    async getAll(page = 1, expired = '', search = "") {
      this.item = []
      return await axios.get(`items?page=${page}&expired=${expired}&search=${search}`)
            .then(resp => {
              console.log(resp)
              this.items = resp.data.results
              this.nextPage = resp.data.next
              this.prevPage = resp.data.previous
              this.count = resp.data.count
              this.totalPage = resp.data.total_page
            })
    },
    async create(fd) {

      return await axios.post("items/", fd)
              .then( resp=> {
                this.items.push(resp.data)
                return resp 
              })
    },
    async update(id, fd) {

      return await axios.put(`items/${id}/`, fd)
                .then( resp=> {
                  this.item = this.items.map(it => it.id == id ? resp.data : it) 
                })
    },
    async delete(id) {

      return await axios.delete(`items/${id}/`)
                .then( ()=> {
                    this.items = this.items.filter(it => it.id != id)
                })
    }
  }
})
