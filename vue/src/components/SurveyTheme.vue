<script setup>
	import Question from './Question.vue'

	const props = defineProps({
		subject: String,
		type: String,
		questions: Object
	})
</script>

<template>
	<div class="subject">
		<h3 class="subject__title">{{ subject }}</h3>

		<div class="subject__questions">
			<Question
				v-for="(question, index) in questions"
				:key="index"
				:title="question.text"
				:answer="question.answer"
				:type="type"
				:id="question.id"
			/>
		</div>
	</div>
</template>

<style scoped lang="scss">
.subject {
	padding: 20px;

	&__title {
		font-size: 16px;
		font-weight: 500;
		background-color: var(--extra-light-gray);
	}

	&__questions {
		display: grid;
		grid-template-columns: 1fr auto;
		align-items: center;
		justify-content: space-between;
		gap: 20px;
		padding-top: 20px;
	}
}
</style>
