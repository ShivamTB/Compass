<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar class="bg-black text-white">
        <q-toolbar-title>
          Compass
        </q-toolbar-title>
        <q-btn flat dense icon="sim_card" class="q-mr-xs" label="Market Place" />
        <q-btn flat dense icon="restaurant" label="Order Food" />
      </q-toolbar>
    </q-header>


    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
// import { ref } from 'vue';

defineOptions({
  name: 'MainLayout'
});

</script>
