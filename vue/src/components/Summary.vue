<script setup>
import { provide, ref, onMounted, watch } from 'vue'
import axios from 'axios'

import SuccessLine from './SuccessLine.vue'
import ThePersonalQualities from './ThePersonalQualities.vue'
import TheOptions from './TheOptions.vue'
import Survey from './Survey.vue'

const apiEndpoint = import.meta.env.VITE_PRIVATE_API_ENDPOINT

const theoryQuestionsArray = ref([])
const practiceQuestionsArray = ref([])

const theoryStudentPoints = ref(0)
const practiceStudentPoints = ref(0)

const theoryQuestionsCount = ref(0)
const practiceQuestionsCount = ref(0)

provide('theoryStudentPoints', theoryStudentPoints)
provide('practiceStudentPoints', practiceStudentPoints)

const theorySubjectsAndQuestions = ref([])
const practiceSubjectsAndQuestions = ref([])

const generateSubjectsAndQuestions = (subjects, questionsArray) => {
  const subjectsAndQuestions = []

  for (let i = 0; i < subjects.length; i++) {
    const subject = subjects[i]
    const questions = []

    for (const question of questionsArray.value) {
      if (subject.id === question.subject_id) {
        questions.push({
          text: question.text,
          answer: question.answer
        })
      }
    }

    subjectsAndQuestions.push({
      subject: subject.name,
      questions: questions
    })
  }

  return subjectsAndQuestions
}

onMounted(async () => {
  // Получаем урок
  try {
    // Номер урока
    const lesson = 1

    // Получаем все темы теории и практики
    const theorySubjects = await axios.get(apiEndpoint + '/subjects/lesson/' + lesson + '/category/1')
    const practiceSubjects = await axios.get(apiEndpoint + '/subjects/lesson/' + lesson + '/category/2')

    // Перебираем все темы теории и получаем общий список вопросов
    for (const subject of theorySubjects.data) {
      const questions = await axios.get(apiEndpoint + '/questions/subject/' + subject.id)
      theoryQuestionsArray.value.push(...questions.data)
    }

    // // Перебираем все темы практики и получаем общий список вопросов
    for (const subject of practiceSubjects.data) {
      const questions = await axios.get(apiEndpoint + '/questions/subject/' + subject.id)
      practiceQuestionsArray.value.push(...questions.data)
    }

    // Связываем вопросы с темой в общий объект
    theorySubjectsAndQuestions.value = generateSubjectsAndQuestions(theorySubjects.data, theoryQuestionsArray)
    practiceSubjectsAndQuestions.value = generateSubjectsAndQuestions(
      practiceSubjects.data,
      practiceQuestionsArray
    )
  } catch (error) {
    console.log(error)
  }
})

// Получаем количество вопросов в каждом разделе
watch(
  () => theoryQuestionsArray.value.length,
  () => {
    theoryQuestionsCount.value = theoryQuestionsArray.value.length
  }
)
watch(
  () => practiceQuestionsArray.value.length,
  () => {
    practiceQuestionsCount.value = practiceQuestionsArray.value.length
  }
)
</script>

<template>
  <section class="summary">
    <SuccessLine
      title="Теория"
      :studentPoints="theoryStudentPoints"
      :maximumPoints="theoryQuestionsCount"
    />
    <SuccessLine
      title="Практика"
      :studentPoints="practiceStudentPoints"
      :maximumPoints="practiceQuestionsCount"
    />

    <ThePersonalQualities />

    <TheOptions />

    <Survey title="Теория" type="theory" :questionsArray="theorySubjectsAndQuestions" />
    <Survey title="Практика" type="practice" :questionsArray="practiceSubjectsAndQuestions" />
  </section>
</template>

<style scoped></style>
