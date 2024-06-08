import { api } from 'src/boot/axios'
import { formDataGenerator } from 'src/utils/request'


export const loginUser = async (form: any) => {
    const formData = formDataGenerator(form)
    return await api.post('/login', formData).then((response) => {
        if (response.status == 200) {
            const { user } = response.data
            return user
        } else {
            return false
        }
    }
    ).catch((error) => {
        return false
        console.log(error)
    })
}

export const logoutUser = async () => {
    return await api.post('/logout').then((response) => {
        if (response.status == 200) {
            localStorage.removeItem('token')
            localStorage.removeItem('refreshToken')
            return true
        }
        return false
    }
    ).catch((error) => {
        return false
        console.log(error)
    }
    )
}


export const registerUser = async (form: any) => {
    const formData = formDataGenerator(form)
    return await api.post('/registeration/new_user', formData).then((response) => {
        if (response.status == 200) {
            return true
        }
        return false
    }
    ).catch((error) => {
        console.log(error)
        return false
    })
}
