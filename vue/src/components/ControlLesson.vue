<script setup>
	import { ref, provide, onMounted } from 'vue'
	import axios from 'axios'

	import TheHeader from '../components/TheHeader.vue'
	import LessonHeaderContent from '../components/LessonHeaderContent.vue'
	import TheMain from '../components/TheMain.vue'
	import Summary from '../components/Summary.vue'
	import TheSidenav from '../components/TheSidenav.vue'

	const apiEndpoint = import.meta.env.VITE_PRIVATE_API_ENDPOINT

	const selectedLesson = ref(null);
	const selectedStudent = ref(null);

	provide('selectedStudent', selectedStudent)

	const handleLessonSelected = (lessonId) => {
		selectedLesson.value = lessonId;
	};

	const handleStudentSelected = (data) => {
		selectedStudent.value = data;
	}

	const fetchStudentData = async () => {
		try {
			const response = await axios.get(`${apiEndpoint}/students/3`);
			handleStudentSelected(response.data);
			console.log(response.data);
		} catch (error) {
			console.error('Failed to fetch student data:', error);
		}
	};

	onMounted(fetchStudentData);
</script>

<template>
	<TheSidenav :onLessonSelected="handleLessonSelected" />

	<TheHeader>
		<LessonHeaderContent
			:lessonId="selectedLesson ? selectedLesson : 1"
			:student-name="selectedStudent ? `${selectedStudent.first_name} ${selectedStudent.last_name}` : ''"
			:lessonsLassed="2" 
			initialDate="01.01.2022" 
		/>
	</TheHeader>

	<TheMain v-if="selectedStudent && selectedLesson">
		<Summary :lessonId="selectedLesson" />
	</TheMain>
</template>

<style scoped></style>
