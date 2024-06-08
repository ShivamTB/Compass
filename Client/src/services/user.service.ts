import { api } from 'src/boot/axios';

export const getUserProfile = async () => {
    return await api.get('/registeration/get_profile_data').then(response => {
        if (response.status == 200) {
            const user = response.data;
            return user;
        } else {
            return false;
        }
    }).catch(error => {
        console.log(error);
        return false;
    });
};


export const getUserPhotos = async () => {
    return await api.get('/registeration/get_user_photos').then(response => {
        if (response.status == 200) {
            const { photos } = response.data;
            return photos;
        } else {
            return false;
        }
    }).catch(error => {
        console.log(error);
        return false;
    });
}


export const addUserPhoto = async (form: any) => {
    return await api.post('/registeration/add_user_photo', form).then((response) => {
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