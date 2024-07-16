<script setup>
import { ref } from 'vue';

const props = defineProps({
  name: String,
  lessonsLassed: Number,
  initialDate: String
})

const formatDate = (date) => {
  const d = new Date(date);
  const day = String(d.getDate()).padStart(2, '0');
  const month = String(d.getMonth() + 1).padStart(2, '0');
  const year = d.getFullYear();

  return `${day}.${month}.${year}`;
}

const date = ref(props.initialDate);
const isHovered = ref(false);

const updateDate = () => {
  // Выводим новую дату в формате "дд.мм.гггг"
  date.value = formatDate(new Date());
};
</script>

<template>
  <header class="header">
    <h1 class="header__lesson-name">Контрольный урок 1</h1>
    <ul class="header__student-info">
      <li class="header__student-name">Ученик: {{ name }}</li>
      <li class="header__lessons-liassed">Уроков пройдено: {{ lessonsLassed }}</li>
      <li class="header__date-of-lesson"
          @mouseenter="isHovered = true" 
          @mouseleave="isHovered = false"
          v-auto-animate>
        <p class="header__date">Дата: {{ date }}</p>
        <button v-if="isHovered" @click="updateDate" class="header__update-date-btn">
          ✓
        </button>
      </li>
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

    display: flex;
    align-items: center;
    column-gap: 10px;
  }

  &__update-date-btn {
    background-color: green;
    color: white;

    border: none;
    border-radius: 50%;
    
    width: 24px;
    height: 24px;
    
    cursor: pointer;
    font-size: 14px;
  }
}
</style>
