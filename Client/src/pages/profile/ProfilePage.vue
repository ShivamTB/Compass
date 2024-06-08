<template>
    <q-page>
        <div class="background-photo">
            <div class="default-background shadow-5">
                <q-img src="src/assets/bg.png" style="height: 300px;"></q-img>
            </div>

        </div>
        <div class="profile-container" style="margin-top:-150px">
            <div class="profile-photo text-center">
                <div class="user-image column items-center">
                    <q-avatar class="shadow-5 cursor-pointer mavatar" @click="uploadDoc" size="250px">

                        <img v-if="user_details.photo" :src="`${photoBaseUrl}${user_details.photo}`"
                            style="border:5px solid white;">
                        <img v-else src="https://cdn.quasar.dev/img/boy-avatar.png" style="border:5px solid white;">
                    </q-avatar>
                    <input type="file" name="photo" id="" style="visibility: hidden;" ref="file" :onchange="uploadFIle">
                </div>
            </div>
        </div>
        <div class="flex justify-center">
            <q-card bordered clas style="width: 70%;" dark>
                <q-card-section class="text-h6 ">
                    <div class="text-h6 text-center">{{ user_details.first_name }} {{ user_details.last_name }}</div>
                </q-card-section>
                <q-card-section class="q-pa-sm q-mb-lg">

                    <q-list class="row">
                        <q-item class="col-lg-6 col-md-6 col-sm-6 col-xs-6">
                            <q-item-section>
                                <q-input dark color="white" outlined disable v-model="user_details.user_name"
                                    label="User Name" />
                            </q-item-section>
                        </q-item>
                        <q-item class="col-lg-6 col-md-6 col-sm-6 col-xs-6">
                            <q-item-section>
                                <q-input dark color="white" outlined disable v-model="user_details.email"
                                    label="Email Address" />

                            </q-item-section>
                        </q-item>
                        <q-item class="col-lg-6 col-md-6 col-sm-6 col-xs-6">
                            <q-item-section>
                                <q-input dark color="white" outlined disable v-model="user_details.referral_id"
                                    prefix="R-" label="Referral ID" />
                            </q-item-section>
                        </q-item>
                        <q-item class="col-lg-6 col-md-6 col-sm-6 col-xs-6">
                            <q-item-section>
                                <q-input dark color="white" outlined disable v-model="user_details.count"
                                    label="Total Referral" />
                            </q-item-section>
                        </q-item>

                    </q-list>



                </q-card-section>
                <q-separator />
                <div class="q-mt-lg q-pa-sm" v-if="photos?.length">
                    <div class="row q-col-gutter-md">
                        <div class="col-4" v-for="photo in photos" :key="photo">
                            <q-img :src="`${photoBaseUrl}${photo}`" :ratio="16 / 9" />
                        </div>
                    </div>
                </div>
            </q-card>

        </div>
    </q-page>
</template>

<script setup lang="ts">
import { addUserPhoto, getUserPhotos, getUserProfile } from 'src/services/user.service';
import { onMounted, ref } from 'vue';

const photoBaseUrl = 'http://192.168.101.195:8000/registeration/'


const user_details = ref({
    user_name: null,
    email: null,
    first_name: null,
    last_name: null,
    photo: null,
    referral_id: null,
    count: null

})

// const hoverFlag = ref(false)

const file: any = ref(null)

const photos = ref([])

onMounted(() => {
    getUserDetails()
    getPhotos()
})

const getUserDetails = async () => {
    const user = await getUserProfile()

    user_details.value = {
        user_name: user.username,
        email: user.email,
        first_name: user.first_name,
        last_name: user.last_name,
        photo: user.photo,
        count: user.count,
        referral_id: user.referral_id
    }
}

const getPhotos = async () => {
    const pts = await getUserPhotos()
    photos.value = pts
}

const uploadDoc: any = () => {
    console.log(file?.value?.click?.());

}

const uploadFIle = async (e: any) => {
    const file = e.target.files[0]

    const formData = new FormData()
    formData.append('photo', file)
    const isUploaded = await addUserPhoto(formData)
    if (isUploaded) {
        getPhotos()
    }

}
</script>

<style scoped>
.mavatar img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    overflow: hidden;
}
</style>