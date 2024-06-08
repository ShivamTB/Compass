import { defineStore } from 'pinia'
import { loginUser, logoutUser } from 'src/services/auth.service';


export const useAuthStore = defineStore('users', {
    state: () => ({
        userData: null,
        // ...
    }),

    actions: {
        async loginUser(form: any) {
            const user: any = await loginUser(form)
            if (user) {
                this.userData = user
                return true
            }
            return false
        },
        async logoutUser() {
            await logoutUser()
            this.userData = null
        }
    },
})