<script setup>
	import { ref, inject, onMounted } from 'vue'

	import axios from 'axios'

	const apiEndpoint = import.meta.env.VITE_PRIVATE_API_ENDPOINT

	const props = defineProps({
		count: Number,
		qualityId: Number
	})

	const selectedStudent = inject('selectedStudent')

	const stars = ref(Array(props.count).fill(false))
	let rating = ref(-1)

	const toggleStar = async (index, isClicked = false) => {
		stars.value = stars.value.map((_, i) => i <= index)
		
		if (isClicked) {
			rating.value = index

			try {
				await axios.post(apiEndpoint + '/student-learning-attitudes/create-or-update/', {
					student_id: selectedStudent.value.id,
					learning_attitude_id: props.qualityId,
					rating: index + 1
				})
			} catch (error) {
				console.error('Failed to save rating:', error)
			}
		}
	}

	const fetchRating = async () => {
		try {
			const response = await axios.get(
				import.meta.env.VITE_PRIVATE_API_ENDPOINT + 
				'/student-learning-attitudes/student-and-learning-attitude/' + 
				selectedStudent.value.id + '/' + props.qualityId
			)
			if (response.data && Object.keys(response.data).length !== 0) {
				// Обновляем значение рейтинга
				rating.value = response.data.rating - 1

				// Отображаем звезды
				stars.value = stars.value.map((_, i) => i <= rating.value)
			}
		} catch (error) {
			console.error('Failed to fetch rating:', error)
		}
	}

	onMounted(fetchRating)

	// watch(rating, () => {
	// 	toggleStar(rating.value, true)
	// })
</script>

<template>
	<div>
		<span
			v-for="(star, index) in stars"
			:key="index"
			:class="['material-symbols-outlined', 'star', { 'gold-star': star }]"
			@click="toggleStar(index, true)"
			@mouseover="toggleStar(index)"
			@mouseout="toggleStar(rating)"
		>
			star
		</span>
	</div>
</template>

<style scoped>
	.material-symbols-outlined {
		font-variation-settings:
			'FILL' 1,
			'wght' 300,
			'GRAD' 0,
			'opsz' 48;
	}

	.star {
		color: var(--light-gray);
		margin: -2px;
		cursor: pointer;

		transition: color 0.2s ease-in-out;
	}

	.gold-star {
		color: rgb(255 193 7);
	}
</style>
