<script setup>
	// import { inject, onMounted } from 'vue'
	// import axios from 'axios'

	import { inject } from 'vue'

	import TheHeader from '../components/TheHeader.vue'
	import LessonHeaderContent from '../components/LessonHeaderContent.vue'
	import TheMain from '../components/TheMain.vue'
	import Summary from '../components/Summary.vue'
	import TheSidenav from '../components/TheSidenav.vue'
	import LessonsList from '../components/LessonsList.vue'

	// const apiEndpoint = import.meta.env.VITE_PRIVATE_API_ENDPOINT

	const selectedStudent = inject('selectedStudent');
	const selectedLesson = inject('selectedLesson');

	// const handleStudentSelected = (data) => {
	// 	selectedStudent.value = data;
	// }

	// const fetchStudentData = async () => {
	// 	try {
	// 		const studentId = selectedStudent.value;
	// 		const response = await axios.get(`${apiEndpoint}/students/${studentId}`);
	// 		handleStudentSelected(response.data);
	// 		console.log(response.data);
	// 	} catch (error) {
	// 		console.error('Failed to fetch student data:', error);
	// 	}
	// };

	// onMounted(fetchStudentData);
</script>

<template>
	<TheSidenav>
		<LessonsList />
	</TheSidenav>

	<TheHeader>
		<LessonHeaderContent
			:lessonId="selectedLesson ? selectedLesson : 1"
			:student-name="selectedStudent ? `${selectedStudent.first_name} ${selectedStudent.last_name}` : ''"
			:lessonsLassed="2" 
			initialDate="01.01.2022" 
		/>
	</TheHeader>

	<TheMain v-if="selectedStudent && selectedLesson">
		<Summary />
	</TheMain>
</template>

<style scoped></style>
