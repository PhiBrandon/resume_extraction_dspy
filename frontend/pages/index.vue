<script setup="ts">

let resume = ref("")
let returned = ref(null)
async function sendResume(e) {
    let data = await $fetch('api/parseResume', {
        method: 'POST',
        body: { resume: resume }
    })
    if (data) {
        returned.value = data
    }
}

</script>

<template>
    <div class="flex flex-col items-center w-full mt-12">
        <form class="min-w-full space-y-2 flex flex-col items-center" @submit.prevent="sendResume">
            <textarea class="textarea textarea-bordered textarea-lg w-96" placeholder="Resume" v-model="resume"></textarea>
            <button class="btn min-w-96 bg-slate-500">Extract Information</button>
        </form>
        <div class="flex flex-col max-w-lg text-center space-y-4 mt-4" v-if="returned">
            <h1 class="border-b-2">Education</h1>
            <div class="flex flex-col " v-for="education in returned.education">
                <p class=" rounded-md  p-2">{{ education }} </p>
            </div>
            <h1 class="border-b-2">Job Titles</h1>
            <div class="flex flex-col " v-for="job_title in returned.job_titles">
                <p class="  rounded-md  p-2">{{ job_title }} </p>
            </div>
            <h1 class="border-b-2">Certifications</h1>
            <div class="flex flex-col " v-for="certs in returned.certifications">
                <p class="  rounded-md  p-2">{{ certs }} </p>
            </div>

        </div>

    </div>
</template>