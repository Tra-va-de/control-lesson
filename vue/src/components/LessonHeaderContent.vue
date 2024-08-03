<script setup>
	import { ref, watch } from 'vue';
	import axios from 'axios'
	
	const apiEndpoint = import.meta.env.VITE_PRIVATE_API_ENDPOINT;

	const props = defineProps({
		lessonId: Number,
		studentName: String,
		lessonsLassed: Number,
		initialDate: String
	})

	const lessonName = ref('');

	const fetchLessonName = async (lessonId) => {
		try {
			const lessonDetails = await axios.get(
				`${apiEndpoint}/lessons/${lessonId}`
			)
			const disciplineDetails = await axios.get(
				`${apiEndpoint}/disciplines/${lessonDetails.data.discipline_id}`
			)
			const levelDetails = await axios.get(
				`${apiEndpoint}/lesson-levels/${lessonDetails.data.lesson_level_id}`
			)

			lessonName.value = `${disciplineDetails.data.name}. ${levelDetails.data.name} уровень. ${lessonDetails.data.name}`
		} catch (error) {
			console.log(error)
		}
	}

	watch(
		() => props.lessonId,
		async (newLessonId) => {
			if (newLessonId) {
				await fetchLessonName(newLessonId);
			}
		},
		{ immediate: true }
	);

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
	<h1 class="lesson-name">{{ lessonName }}</h1>

	<ul class="student-info">
		<li class="student-name">Ученик: {{ studentName }}</li>
		<li class="lessons-liassed">Уроков пройдено: {{ lessonsLassed }}</li>
		<li class="date-of-lesson"
			@mouseenter="isHovered = true" 
			@mouseleave="isHovered = false">
			<p class="date" v-auto-animate>Дата: {{ date }}</p>
			<button v-if="isHovered" @click="updateDate" class="update-date-btn">
				✓
			</button>
		</li>
	</ul>
</template>

<style scoped lang="scss">
	.lesson-name {
		font-size: 22px;
		font-weight: 500;
		padding-bottom: 20px;
	}

	.student-info li {
		font-size: 17px;
		line-height: 24px;

		display: flex;
		align-items: center;
		column-gap: 10px;
	}

	.update-date-btn {
		background-color: green;
		color: white;

		border: none;
		border-radius: 50%;
		
		width: 24px;
		height: 24px;
		
		cursor: pointer;
		font-size: 14px;
	}
</style>
