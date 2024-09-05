<script setup>
	import { ref, onMounted } from 'vue'

	import axios from 'axios'

	import Qualitie from './Qualitie.vue'

	const apiEndpoint = import.meta.env.VITE_PRIVATE_API_ENDPOINT

	const attitudes = ref([])

	const fetchLearningAttitudes = async () => {
		try {
			const response = await axios.get(apiEndpoint + '/learning-attitudes/')
			attitudes.value = response.data
		} catch (error) {
			console.error('Failed to fetch learning attitudes:', error)
		}
	}

	onMounted(fetchLearningAttitudes)
</script>

<template>
	<div class="personal-qualities">
		<Qualitie
			v-for="attitude in attitudes"
			:key="attitude.id"
			:title="attitude.name"
			:id="attitude.id"
		/>
	</div>
</template>

<style scoped>
	.personal-qualities {
		margin-bottom: 20px;
	}
</style>
