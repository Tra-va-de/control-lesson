<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  title: String,
  studentPoints: Number,
  maximumPoints: Number
})

const width = ref((props.studentPoints / props.maximumPoints) * 100)

watch(
  () => props.studentPoints,
  () => {
    width.value = (props.studentPoints / props.maximumPoints) * 100
  }
)
watch(
  () => props.maximumPoints,
  () => {
    width.value = (props.studentPoints / props.maximumPoints) * 100
  }
)
</script>

<template>
  <div class="success">
    <h2 class="success__title">{{ title }}</h2>

    <p class="success__points">{{ studentPoints }}/{{ maximumPoints }} {{ width.toFixed(2) }}%</p>

    <div class="success__line">
      <div class="success__line-green"></div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.success {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 10px;

  margin-bottom: 20px;

  &__title {
    margin-bottom: 5px;
    font-size: 15px;
    font-weight: 400;
  }

  &__line {
    width: 100%;
    height: 5px;

    border-radius: 45px;
    background-color: var(--light-gray);

    position: relative;

    overflow: hidden;

    &-green {
      width: calc(v-bind(width) * 1%);
      height: 100%;

      background-color: var(--green);

      position: absolute;
      top: 0;
      left: 0;

      transition: width 0.5s ease-in-out;
    }
  }
}
</style>
