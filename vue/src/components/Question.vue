<script setup>
import QuestionDropDown from './QuestionDropDown.vue'

defineProps({
  title: String,
  answer: String,
  type: String,
  state: Boolean
})

const options = [
  {
    name: 'cancel',
    text: 'не выполнено (0 баллов)',
    color: 'var(--red)',
    value: 0
  },
  {
    name: 'check_circle',
    text: 'выполнено частично (0.5 балла)',
    color: 'var(--yellow)',
    value: 0.5
  },
  {
    name: 'check_circle',
    text: 'выполнено полностью (1 балл)',
    color: 'var(--lime)',
    value: 1
  }
]
</script>

<template>
  <div class="question-info">
    <h3 class="question-title">{{ title }}</h3>
    <p class="question-answer">{{ answer }}</p>
  </div>

  <QuestionDropDown :options="options" :themeType="type" />
</template>

<style scoped lang="scss">
.question {
  &-title {
    font-size: 14px;
    font-weight: 500;
  }

  &-answer {
    font-size: 13px;
    font-weight: 400;
    color: var(--gray);
  }
}
</style>
