<template>
    <form class="w-full" @submit.prevent="submit" ref="form" enctype="multipart/form-data">

        <div class="grid gap-6 mb-6 grid-cols-1">
            <div>
                <label for="name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                    Name
                </label>
                <input 
                    type="text" 
                    name="name" 
                    id="name" 
                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" 
                    placeholder="name" 
                    v-model="currentItem.name"
                    required>
                <p v-if="errors.name" class="mt-2 text-sm text-red-600 dark:text-red-500">
                    {{ errors.name[0] }}
                </p>
            </div>

            <div>
                <label for="expired_at" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                    Expiredion Date
                </label>
                
                <input 
                    type="date" 
                    name="expired_at"
                    v-model="currentItem.expired_at" 
                    id="expired_at" 
                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" 
                    placeholder="date" 
                    required>
                    <p v-if="errors.expired_at" class="mt-2 text-sm text-red-600 dark:text-red-500">
                        {{ errors.expired_at[0] }}
                    </p>
            </div>

            <div class="flex w-full flex-col">
                <label for="dropzone-file" class="flex flex-col justify-center items-center w-full h-64 bg-gray-50 rounded-lg border-2 border-gray-300 border-dashed cursor-pointer dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
                    <div class="flex flex-col justify-center items-center pt-5 pb-6" >
                        <img ref="image" :src="currentItem.image" class="w-80">
                        <div class="p-2 text-center">
                            <p class="mb-2 text-sm text-gray-500 dark:text-gray-400"><span class="font-semibold">Click to upload</span></p>
                            <p class="text-xs text-gray-500 dark:text-gray-400">SVG, PNG, JPG or GIF </p>
                        </div>
                    </div>
                    <input id="dropzone-file" @change="onChangeFile" type="file" class="hidden" name="image" accept="image/*" />
                </label>
                <p v-if="errors.image" class="mt-2 text-sm  px-2 text-start text-red-600 dark:text-red-500">
                    {{ errors.image[0] }}
                </p>
            </div> 


            <div>
                <Button
                    type="submit" 
                    colors="text-white bg-blue-700 hover:bg-blue-800 focus:ring-blue-300"
                    :loading="isLoading"
                >
                    Save
                </Button> 
            </div>
        </div>

    </form>
</template>


<script setup>
import { ref, defineProps } from 'vue';
import Button from "@/components/Button.vue";
import { useItemsStore } from "@/stores/items.js"

const props = defineProps({
    currentItem: Object
})

const store = useItemsStore()
const image = ref(null)
const form = ref(null)
const isLoading = ref(false)
const errors = ref({})

const onChangeFile = (event) => {

    image.value.src = URL.createObjectURL(event.target.files[0]);
}


const submit = () => {

    errors.value = {}
    isLoading.value = true
    let fd = new FormData(form.value)
    console.log(fd.get("image"))
    if ( !fd.get("image") ) {
        fd.remove("image")
    }
    let response = props.currentItem.id 
            ? store.update(props.currentItem.id, fd)  
            : store.create(fd)

    response
        .then(()=> alert("Successfuly save item"))
        .catch((error)=> errors.value = error.response.data)
        .finally(()=> isLoading.value = false)

}

</script>