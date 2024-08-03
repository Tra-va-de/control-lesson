<script setup>
	import { ref, inject, onMounted } from 'vue'
	import axios from 'axios'

	import Option from './Option.vue'

	const apiEndpoint = import.meta.env.VITE_PRIVATE_API_ENDPOINT

	const props = defineProps({
		options: Array,
		themeType: String,
		questionId: Number
	})

	const selectedOption = ref(0)
	const isDropDownVisible = ref(false)

	const selectOption = async (option) => {
		if (props.themeType == 'theory') {
			theoryStudentPoints.value += option.value - selectedOption.value
		} else if (props.themeType === 'practice') {
			practiceStudentPoints.value += option.value - selectedOption.value
		}

		selectedOption.value = option.value
		isDropDownVisible.value = false

		await axios.post(apiEndpoint + '/student-answers/create-or-update/', {
			student_id: selectedStudent.value.id,
			question_id: props.questionId,
			answer: option.value
		})
	}

	const theoryStudentPoints = inject('theoryStudentPoints')
	const practiceStudentPoints = inject('practiceStudentPoints')

	const selectedStudent = inject('selectedStudent')

	const fetchStudentAnswer = async () => {
		try {
			const response = await axios.get(
				apiEndpoint + '/student-answers/student-and-question/' + selectedStudent.value.id + '/' + props.questionId
			)
			selectedOption.value = response.data.answer

			if (props.themeType == 'theory') {
				theoryStudentPoints.value += selectedOption.value
			} else if (props.themeType === 'practice') {
				practiceStudentPoints.value += selectedOption.value
			}
		} catch (error) {
			console.error('Failed to fetch student answer:', error)
		}
	}

	onMounted(fetchStudentAnswer)
</script>

<template>
	<div class="drop-down-wrapper" :class="{ open: isDropDownVisible }" v-auto-animate>
		<div class="drop-down-selected" @click="isDropDownVisible = !isDropDownVisible">
			<div class="selected-option" v-for="(option, index) in options" :key="index">
				<Option
					v-if="option.value === selectedOption"
					:name="option.name"
					:text="option.text"
					:color="option.color"
				/>
			</div>
		</div>

		<div class="option-wrapper" v-if="isDropDownVisible">
			<div
				class="option"
				v-for="(option, index) in options"
				:key="index"
				@click="selectOption(option)"
			>
				<Option :name="option.name" :text="option.text" :color="option.color"></Option>
			</div>
		</div>
	</div>
</template>

<style scoped lang="scss">
	.drop-down-wrapper {
		border-radius: 5px;
		overflow: hidden;

		&.open {
			border: var(--border);
		}
	}

	.drop-down-selected {
		padding: 5px;

		&:hover {
			cursor: pointer;
			background-color: var(--light-gray);
		}
	}

	.option-wrapper {
		padding-top: 10px;

		border-top: var(--border);

		display: flex;
		flex-direction: column;
		gap: 10px;

		background-color: white;

		& > * {
			padding: 5px;

			&:hover {
				cursor: pointer;
				background-color: var(--light-gray);
			}
		}
	}
</style>
