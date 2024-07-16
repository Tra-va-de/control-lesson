<script setup>
import StarsRating from './StarsRating.vue'

defineProps({
  title: String
})
</script>

<template>
  <div class="qualitie">
    <p>{{ title }}</p>

    <StarsRating :count="5" />
  </div>
</template>

<style scoped lang="scss">
.qualitie {
  margin-bottom: 7px;
}
</style>
