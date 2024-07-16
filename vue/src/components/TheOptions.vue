<script setup>
import Option from './Option.vue'
</script>

<template>
  <section class="options">
    <Option name="check_circle" text="выполнено полностью (1 балл)" color="var(--lime)" />
    <Option name="check_circle" text="выполнено частично (0.5 балла)" color="var(--yellow)" />
    <Option name="cancel" text="не выполнено (0 баллов)" color="var(--red)" />
  </section>
</template>

<style scoped>
.options {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 10px;
}
</style>
