<script setup>
defineProps({
  name: String,
  lessonsLassed: Number,
  date: String
})
</script>

<template>
  <header class="header">
    <h1 class="header__lesson-name">Контрольный урок 1</h1>
    <ul class="header__student-info">
      <li class="header__student-name">Ученик: {{ name }}</li>
      <li class="header__lessons-liassed">Уроков пройдено: {{ lessonsLassed }}</li>
      <li class="header__date-of-lesson">Дата: {{ date }}</li>
    </ul>
  </header>
</template>

<style scoped lang="scss">
.header {
  background-color: var(--bg-color);
  color: white;
  padding: 25px;
  border-radius: 20px;

  &__lesson-name {
    font-size: 22px;
    font-weight: 500;
    padding-bottom: 20px;
  }

  &__student-info li {
    font-size: 17px;
    line-height: 24px;
  }
}
</style>
