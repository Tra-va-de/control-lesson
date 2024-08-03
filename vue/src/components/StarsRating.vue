<script setup>
	import { ref } from 'vue'

	const props = defineProps({
		count: Number
	})

	const stars = ref(Array(props.count).fill(false))
	let rating = -1

	const toggleStar = (index, isClicked) => {
		stars.value = stars.value.map((star, i) => i <= index)
		if (isClicked) rating = index
	}
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
