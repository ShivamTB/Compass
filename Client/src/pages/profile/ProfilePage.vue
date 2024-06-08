<template>
    <q-page padding>
        <div class="flex justify-center">
            <q-card bordered clas style="width: 60%;" dark>
                <q-card-section class="text-h6 ">
                    <div class="text-h6">User Profile</div>
                </q-card-section>
                <q-card-section class="q-pa-sm">
                    <q-list class="row">
                        <q-item class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                            <q-item-section side>
                                <q-avatar size="100px">
                                    <img v-if="user_details.photo" :src="`${photoBaseUrl}${user_details.photo}`">
                                    <img v-else src="https://cdn.quasar.dev/img/boy-avatar.png">
                                </q-avatar>

                            </q-item-section>
                            <q-item-section>
                                <q-btn label="Add Photo" class="text-capitalize" rounded color="info"
                                    style="max-width: 120px"></q-btn>
                            </q-item-section>
                        </q-item>
                        <q-item class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                            <q-item-section>
                                <q-input dark color="white" outlined disable v-model="user_details.user_name"
                                    label="User Name" />
                            </q-item-section>
                        </q-item>
                        <q-item class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                            <q-item-section>
                                <q-input dark color="white" outlined disable v-model="user_details.email"
                                    label="Email Address" />
                            </q-item-section>
                        </q-item>
                        <q-item class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                            <q-item-section>
                                <q-input dark color="white" outlined disable v-model="user_details.first_name"
                                    label="First Name" />
                            </q-item-section>
                        </q-item>
                        <q-item class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                            <q-item-section>
                                <q-input dark color="white" outlined disable v-model="user_details.last_name"
                                    label="Last Name" />
                            </q-item-section>
                        </q-item>

                    </q-list>
                </q-card-section>
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
import { getUserPhotos, getUserProfile } from 'src/services/user.service';
import { onMounted, ref } from 'vue';

const photoBaseUrl = 'http://192.168.101.195:8000/registeration/'


const user_details = ref({
    user_name: null,
    email: null,
    first_name: null,
    last_name: null,
    photo: null

})

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
        photo: user.photo
    }
}

const getPhotos = async () => {
    const pts = await getUserPhotos()
    photos.value = pts
}

</script>

<style scoped></style>