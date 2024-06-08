<template>
    <q-card class="q-ma-xl">
        <div class="row">
            <div class="col-0 col-sm-5 welcome-bg rounded-left-borders xs-hide">
                <div class="row full-width q-px-xl q-pb-xl full-height flex flex-center">
                    <div class="">
                        <div class="text-h4 text-uppercase text-white fredoka" style="min-width: 220px">Welcome!
                        </div>
                        <div class="text-white q-my-sm text-subtitle1">Please sign in to your account to get
                            started!
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
                                        Login</div>
                                </div>
                            </div>

                            <q-form ref="form" class="q-gutter-md" @submit="login">
                                <q-input v-model="user.username" label="Username" name="Username" />

                                <q-input v-model="user.password" label="Password" name="password" type="password" />

                                <div>
                                    <q-btn class="full-width fredoka" color="primary" label="Login" rounded
                                        type="submit"></q-btn>

                                    <div class="q-mt-lg">
                                        <div class="q-mt-sm">
                                            Don't have an account yet?
                                            <router-link class="text-primary" to="/register">Register</router-link>
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
import { notifyError, notifySuccess } from 'src/utils/notify';
import { ref } from 'vue'
import { useAuthStore } from '../../stores/authentication.store'
import { useRouter } from 'vue-router'

const user = ref({
    username: null,
    password: null
})


const router = useRouter()

const login = async () => {
    const authStore = useAuthStore()
    const isLoggedIn = await authStore.loginUser(user.value)
    if (isLoggedIn) {
        notifySuccess('Login Successful')
        router.push({ path: '/' })
    }
    else {
        notifyError('Login Failed. Please try again.')
    }
}

</script>

<style scoped>
.welcome-bg {
    background-color: #b0116b;
}
</style>