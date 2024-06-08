<template>
    <div>
        <q-img src="src/assets/logo.png" spinner-color="white" style="min-height: 100px; min-width:300px" />

        <h5 class="text-h5 text-center q-mt-md text-white">June 6-8, Space42, Abu Dhabi</h5>
        <q-btn class="full-width fredoka" :to="{ name: 'login' }" color="primary" label="Login" rounded></q-btn>
        <q-btn class="full-width fredoka q-mt-lg" :to="{ name: 'register' }" color="secondary" label="Register"
            rounded></q-btn>

    </div>
</template>

<script setup>

</script>

<style lang="scss" scoped></style>