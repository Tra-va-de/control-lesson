<script setup>
	import { ref, inject, onMounted, watch } from 'vue'

	import axios from 'axios'

	const props = defineProps({
		count: Number,
		qualityId: Number
	})

	const selectedStudent = inject('selectedStudent')

	const stars = ref(Array(props.count).fill(false))
	let rating = ref(-1)

	const toggleStar = (index, isClicked) => {
		stars.value = stars.value.map((_, i) => i <= index)
		if (isClicked) rating.value = index
	}

	const fetchRating = async () => {
		try {
			const response = await axios.get(
				import.meta.env.VITE_PRIVATE_API_ENDPOINT + 
				'/student-learning-attitudes/student-and-learning-attitude/' + 
				selectedStudent.value.id + '/' + props.qualityId
			)
			if (response.data && Object.keys(response.data).length !== 0) rating.value = response.data.rating - 1
		} catch (error) {
			console.error('Failed to fetch rating:', error)
		}
	}

	onMounted(fetchRating)

	watch(rating, () => {
		toggleStar(rating.value, true)
	})
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
