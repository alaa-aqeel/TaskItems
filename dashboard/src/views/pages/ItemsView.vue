<template>
    <div>

        <div>

            <Modal 
                title="Item form"
                :show="showModal" 
                @close="onCloseModal"
            >
                <ItemForm
                    :currentItem="currentItem"
                ></ItemForm>
            </Modal>
        </div>

        <div class="mx-4">
            <h1 class="text-2xl border-l-4 drop-shadow-sm font-medium text-gray-700  px-1 border-blue-600">
                Items
            </h1>

            <div class="py-4">
                <button @click="showModal=true" type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 ">
                    Create
                </button>
            </div>
        </div>

        <div class="p-2 rounded-xl border">
            <div class="overflow-x-auto relative  shadow rounded-xl p-4">
                <table class="w-full text-sm text-left text-gray-500">
                    <thead class="text-xs text-gray-700 uppercase bg-gray-100 ">
                        <tr>
                            <th v-for="col in store.columns" :key="col.name" scope="col" class="py-3 px-6" >
                                {{ col.text }}
                            </th>
                            <th scope="col" class="py-3 px-6" >
                                Actions
                            </th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr 
                            class="bg-white  dark:bg-gray-800 dark:border-gray-700"
                            v-for="item in store.items" :key="item.id" 
                        >
                            <th 
                                v-for="col in store.columns" :key="col.name"
                                scope="row" 
                                class="py-4 px-6 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                            >
                                <img v-if="col.name == 'image'" :src="item[col.name]" alt="" class="w-20">
                                <span v-else> {{ item[col.name] }} </span>
                            </th>
                           
                            <td class="py-4 px-6">
                                <div>
                                    <button 
                                        @click="onClickEdit(item)"
                                        type="button" 
                                        class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center mr-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                                    >
                                        Edit
                                    </button>


                                    <Button
                                        @click="onClickDelete(item)"
                                        colors="text-white bg-red-700 hover:bg-red-800 focus:ring-red-300"
                                        :loading="btnDeleteLoading == item.id"
                                    >
                                        Del
                                    </Button>                                    
                                </div>
                            </td>
                        </tr>
                    </tbody>
                    
                </table>
            </div>
            
            <div class="flex flex-col items-start px-12 py-6">
                <div class="inline-flex mt-2 xs:mt-0">
                    <!-- Buttons -->
                    <button @click="prevPage" class="inline-flex items-center py-2 px-4 text-sm font-medium text-white bg-gray-800 rounded-l hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
                        <svg aria-hidden="true" class="mr-2 w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7.707 14.707a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l2.293 2.293a1 1 0 010 1.414z" clip-rule="evenodd"></path></svg>
                        Prev
                    </button>
                    <button @click="nextPage" class="inline-flex items-center py-2 px-4 text-sm font-medium text-white bg-gray-800 rounded-r border-0 border-l border-gray-700 hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
                        Next
                        <svg aria-hidden="true" class="ml-2 w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>


<script setup> 
import { useItemsStore } from "@/stores/items.js"
import { onMounted, ref } from "vue";
import Button from "@/components/Button.vue";
import Modal from "@/components/Modal.vue";
import ItemForm from "@/components/forms/ItemForm.vue";

const store = useItemsStore()
const btnDeleteLoading = ref(-1)
const showModal = ref(false)
const currentItem = ref({})

onMounted(()=>{
    
    store.getAll();
})

const prevPage = () => {}
const nextPage = () => {}

const onCloseModal = () =>{
    currentItem.value = {}
    showModal.value = false
}

const onClickEdit = (item) => {
    currentItem.value = item 
    showModal.value = true
}

const onClickDelete = (item) => {
    btnDeleteLoading.value = item.id 

    confirm(`You are sure delete item ${item.id}`) 
    && store.delete(item.id)
        .then( resp=> {

            alert("Successufly delete item ")
        })
        .finally(()=> btnDeleteLoading.value = -1)
}

</script>