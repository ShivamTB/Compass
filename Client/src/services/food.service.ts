import { api } from 'src/boot/axios';


export const getRestaurants = async () => {
    return await api.get('/fooddelivery/get_restaurants').then(response => {
        if (response.status == 200) {
            const { restaurants } = response.data;
            return restaurants;
        } else {
            return false;
        }
    }).catch(error => {
        console.log(error);
        return false;
    });
}