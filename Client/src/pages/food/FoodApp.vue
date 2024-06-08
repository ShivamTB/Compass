<template>
    <q-page padding>
        <div class="row q-col-gutter-md">
            <div class="col-3" v-for="restaurant in restaurants" :key="restaurant.id">
                <q-card class="my-card" flat bordered>
                    <q-img v-if="restaurant.image" :src="`${photoBaseUrl}${restaurant.image}`" />
                    <q-img v-else src="https://cdn.quasar.dev/img/chicken-salad.jpg" />
                    <q-card-section>
                        <q-btn fab color="primary" icon="place" class="absolute"
                            style="top: 0; right: 12px; transform: translateY(-50%);" />

                        <div class="row no-wrap items-center">
                            <div class="col text-h6 ellipsis">
                                {{ restaurant.name }}
                            </div>
                            <!-- <div class="col-auto text-grey text-caption q-pt-md row no-wrap items-center">
                                <q-icon name="place" />
                                250 ft
                            </div> -->
                        </div>

                        <!-- <q-rating v-model="stars" :max="5" size="32px" /> -->
                    </q-card-section>

                    <q-card-section class="q-pt-none">
                        <div class="text-subtitle1">
                            $・{{ restaurant.cuisine }}
                        </div>
                        <div class="text-caption text-grey">
                            {{ restaurant.description }}
                        </div>
                    </q-card-section>

                    <q-separator />

                    <q-card-actions>
                        <q-btn flat round icon="event" />
                        <q-btn flat color="primary">
                            View Menu
                        </q-btn>
                    </q-card-actions>
                </q-card>
            </div>
        </div>

    </q-page>
</template>

<script setup lang="ts">
import { getRestaurants } from 'src/services/food.service';
import { onMounted, ref } from 'vue';

const restaurants: any = ref([]);

const photoBaseUrl = 'http://192.168.101.195:8000/fooddelivery/'


onMounted(() => {
    loadRestaurants();
});

const loadRestaurants = async () => {
    const restaurant = await getRestaurants();
    restaurants.value = restaurant;
}

</script>

<style scoped></style>