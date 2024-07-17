<script setup>
	import { ref } from 'vue'

	import TheHeader from '../components/TheHeader.vue'
	import TheMain from '../components/TheMain.vue'
	import Summary from '../components/Summary.vue'
	import TheSidenav from '../components/TheSidenav.vue'

	const selectedLesson = ref(null);

	const handleLessonSelected = (lessonId) => {
		selectedLesson.value = lessonId;
	};
</script>

<template>
  <TheSidenav :onLessonSelected="handleLessonSelected" />

  <TheHeader 
	:lessonId="selectedLesson"
    studentName="Тестовый ученик" 
    :lessonsLassed="2" 
    initialDate="01.01.2022" />

  <TheMain>
    <Summary :lessonId="selectedLesson" />
  </TheMain>
</template>

<style scoped></style>
