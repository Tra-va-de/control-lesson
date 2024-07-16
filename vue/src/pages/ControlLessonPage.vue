<script setup>
import TheHeader from '../components/TheHeader.vue'
import TheMain from '../components/TheMain.vue'
import Summary from '../components/Summary.vue'
</script>

<template>
  <TheHeader name="Тестовый ученик" :lessonsLassed="2" date="01/01/2022" />
  <TheMain>
    <Summary />
  </TheMain>
</template>

<style scoped></style>
