<template>
    <q-card class="q-ma-xl">
        <div class="row">
            <div class="col-0 col-sm-5 bg-secondary rounded-left-borders xs-hide">
                <div class="row full-width q-px-xl q-pb-xl full-height flex flex-center">
                    <div class="">
                        <div class="text-h4 text-uppercase text-white fredoka" style="min-width: 220px">Welcome!
                        </div>
                        <div class="text-white q-my-sm text-subtitle1">Enter your details to get started!
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-12 col-sm-7">
                <div class="row q-pa-sm-sm q-pa-md">
                    <div class="col-12">
                        <q-card-section>
                            <div class="q-mb-xl">
                                <div class="flex justify-center">
                                    <div class="text-h4 text-uppercase q-my-none text-weight-bold text-primary fredoka">
                                        Registration Form</div>
                                </div>
                            </div>
                            <q-form ref="form" class="q-gutter-md" @submit="submit">
                                <q-input v-model="user.username" label="User Name" name="User Name" />
                                <q-input v-model="user.first_name" label="First Name" name="First Name" />
                                <q-input v-model="user.last_name" label="Last Name" name="Last Name" />
                                <q-input v-model="user.email" label="Email" name="Email" />
                                <q-input v-model="user.password" label="Password" name="password" type="password" />
                                <q-input v-model="user.referral" label="Referral" name="Referral" prefix="R-" />
                                <div>
                                    <q-btn class="full-width fredoka" color="primary" label="Register" rounded
                                        type="submit"></q-btn>
                                    <div class="q-mt-lg">
                                        <div class="q-mt-sm">
                                            Already have an account?
                                            <router-link class="text-primary" to="/login">Login</router-link>
                                        </div>
                                    </div>
                                </div>
                            </q-form>
                        </q-card-section>
                    </div>
                </div>
            </div>
        </div>
    </q-card>
</template>

<script setup>
import { registerUser } from 'src/services/auth.service';
import { notifySuccess } from 'src/utils/notify';
import { ref } from 'vue'
import { useRouter } from 'vue-router';


const router = useRouter()

const user = ref({
    username: null,
    last_name: null,
    first_name: null,
    email: null,
    password: null,
    referral: null
})

// const form = ref({})

const submit = async () => {
    const isRegistered = await registerUser(user.value);
    if (isRegistered) {
        notifySuccess('User registered successfully');
        router.push({ path: '/login' })
    }
}
</script>