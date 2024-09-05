<script setup>
	import SurveyTheme from './SurveyTheme.vue'

	defineProps({
		title: String,
		type: String,
		questionsArray: Array,
	})
</script>

<template>
	<section class="survey">
		<h2 class="survey__title">{{ title }}</h2>

		<SurveyTheme
			v-for="(questions, index) in questionsArray"
			:key="index"
			:subject="questions.subject"
			:type="type"
			:questions="questions.questions"
		/>
	</section>
</template>

<style scoped lang="scss">
	.survey {
		border: var(--border);
		border-radius: 20px;
		margin-top: 20px;

		&__title {
			font-size: 20px;
			font-weight: 500;
			border-bottom: var(--border);
			padding: 20px 20px 15px;
		}
	}
</style>
