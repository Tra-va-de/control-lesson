<script setup>
	import { ref, onMounted, reactive, inject } from 'vue'
	import axios from 'axios'

	const apiEndpoint = import.meta.env.VITE_PRIVATE_API_ENDPOINT

	const selectedLesson = inject('selectedLesson')

	const disciplines = ref([])
	const levels = ref([])
	const lessons = ref([])

	const expandedDisciplines = reactive({})
	const expandedLevels = reactive({})

	onMounted(async () => {
		await fetchDisciplines()
		await fetchLevels()
		await fetchLessons()
	})

	const fetchDisciplines = async () => {
		const response = await axios.get(apiEndpoint + '/disciplines/')
		disciplines.value = response.data
	}

	const fetchLevels = async () => {
		const response = await axios.get(apiEndpoint + '/lesson-levels/')
		levels.value = response.data
	}

	const fetchLessons = async () => {
		const response = await axios.get(apiEndpoint + '/lessons/')
		lessons.value = response.data
	}

	const getLevelsByDiscipline = (disciplineId) => {
		const lessonLevels = lessons.value
			.filter((lesson) => lesson.discipline_id === disciplineId)
			.map((lesson) => lesson.lesson_level_id)
		return levels.value.filter((level) => lessonLevels.includes(level.id))
	}

	const getLessonsByDisciplineAndLevel = (disciplineId, levelId) => {
		return lessons.value.filter(
			(lesson) => lesson.discipline_id === disciplineId && lesson.lesson_level_id === levelId
		)
	}

	const toggleDiscipline = (disciplineId) => {
		expandedDisciplines[disciplineId] = !expandedDisciplines[disciplineId]
	}

	const toggleLevel = (disciplineId, levelId) => {
		const key = `${disciplineId}-${levelId}`
		expandedLevels[key] = !expandedLevels[key]

		toggleDiscipline(disciplineId)
	}

	const isExpanded = (disciplineId) => {
		return expandedDisciplines[disciplineId] || false
	}

	const isLevelExpanded = (disciplineId, levelId) => {
		const key = `${disciplineId}-${levelId}`
		return expandedLevels[key] || false
	}

	const selectLesson = (lessonId) => {
		selectedLesson.value = lessonId

		// Сохраняем выбранный урок в локальное хранилище
		localStorage.setItem(
			'selectedLesson',
			JSON.stringify({ value: lessonId, timestamp: Date.now() })
		)
	}
</script>

<template>
	<div class="wrapper">
		<div
			class="discipline item"
			v-for="discipline in disciplines"
			:key="discipline.id"
			@click="toggleDiscipline(discipline.id)"
		>
			<h3 class="discipline-title">
				{{ discipline.name }}
				<span class="toggle-icon">{{ isExpanded(discipline.id) ? '-' : '+' }}</span>
			</h3>
			<div class="levels" v-if="isExpanded(discipline.id)">
				<div
					class="level item"
					v-for="level in getLevelsByDiscipline(discipline.id)"
					:key="level.id"
					@click="toggleLevel(discipline.id, level.id)"
				>
					<h4 class="level-title">
						{{ level.name }}
						<span class="toggle-icon">{{
							isLevelExpanded(discipline.id, level.id) ? '-' : '+'
						}}</span>
					</h4>
					<div class="lessons" v-if="isLevelExpanded(discipline.id, level.id)">
						<ul class="lesson-list">
							<li
								class="lesson item"
								v-for="lesson in getLessonsByDisciplineAndLevel(
									discipline.id,
									level.id
								)"
								:key="lesson.id"
								@click.stop="selectLesson(lesson.id)"
							>
								<p class="lesson-name">{{ lesson.name }}</p>
							</li>
						</ul>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped lang="scss">
	.item {
		transition: transform 0.3s ease-in-out;

		&:hover {
			transform: translateY(-3px);
		}
	}

	.item .item {
		margin-left: 20px;
	}

	.discipline-title,
	.level-title,
	.lesson-name {
		display: block;
		margin-bottom: 10px;
		font-weight: 400;
		font-size: 14px;
		cursor: pointer;
		white-space: nowrap;

		&::after {
			content: '';

			display: block;
			width: 100%;
			height: 1px;

			margin-top: 10px;

			background-color: var(--light-gray);
		}
	}
</style>
