<script setup>
	import { ref, provide, onMounted } from 'vue'

	import SelectLesson from '@/components/SelectLesson.vue'
	import ControlLesson from '@/components/ControlLesson.vue'

	const selectedStudent = ref(null)
	const selectedLesson = ref(null)

	provide('selectedStudent', selectedStudent)
	provide('selectedLesson', selectedLesson)

	// Функция для получения сохраненных данных
	const getSelection = (selectionName) => {
		// Пытаемся получить сохраненные данные
		const selection = JSON.parse(localStorage.getItem(selectionName))
		if (selection) {
			const currentTime = new Date().getTime()
			// Проверяем, не истек ли час (3600000 мс)
			if (currentTime - selection.timestamp < 3600000) {
				return selection.value // Возвращаем сохраненные данные, если они актуальны
			} else {
				localStorage.removeItem(selectionName) // Удаляем устаревшие данные
			}
		}
		return null // Данные не найдены или устарели
	}

	onMounted(() => {
		selectedStudent.value = getSelection('selectedStudent')
		selectedLesson.value = getSelection('selectedLesson')
	})
</script>

<template>
	<SelectLesson v-if="!selectedStudent || !selectedLesson" />

	<ControlLesson v-else />
</template>

<style scoped></style>
