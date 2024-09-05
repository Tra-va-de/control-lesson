<script setup>
	import { inject } from 'vue'

	import TheHeader from '../components/TheHeader.vue'
	import LessonHeaderContent from '../components/LessonHeaderContent.vue'
	import TheMain from '../components/TheMain.vue'
	import Summary from '../components/Summary.vue'
	import TheSidenav from '../components/TheSidenav.vue'
	import LessonsList from '../components/LessonsList.vue'

	const selectedStudent = inject('selectedStudent')
	const selectedLesson = inject('selectedLesson')
</script>

<template>
	<TheSidenav>
		<LessonsList />
	</TheSidenav>

	<TheHeader>
		<LessonHeaderContent
			:lessonId="selectedLesson"
			:student-name="`${selectedStudent.first_name} ${selectedStudent.last_name}`"
			:lessonsLassed="2"
			initialDate="01.01.2022"
		/>
	</TheHeader>

	<TheMain v-if="selectedStudent && selectedLesson">
		<Summary />
	</TheMain>
</template>

<style scoped></style>
