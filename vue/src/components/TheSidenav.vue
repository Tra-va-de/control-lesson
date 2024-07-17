<script setup>
    import { ref, onMounted, reactive } from 'vue';
    import axios from 'axios';

    const apiEndpoint = import.meta.env.VITE_PRIVATE_API_ENDPOINT

    const props = defineProps({
        onLessonSelected: {
            type: Function,
            required: true
        }
    });

    const disciplines = ref([]);
    const levels = ref([]);
    const lessons = ref([]);

    const expandedDisciplines = reactive({});
    const expandedLevels = reactive({});

    onMounted(async () => {
        await fetchDisciplines();
        await fetchLevels();
        await fetchLessons();
    });

    const fetchDisciplines = async () => {
        const response = await axios.get(apiEndpoint + '/disciplines');
        disciplines.value = response.data;
    };

    const fetchLevels = async () => {
        const response = await axios.get(apiEndpoint + '/lesson-levels');
        levels.value = response.data;
    };

    const fetchLessons = async () => {
        const response = await axios.get(apiEndpoint + '/lessons');
        lessons.value = response.data;
    };

    const getLevelsByDiscipline = (disciplineId) => {
        const lessonLevels = lessons.value
            .filter(lesson => lesson.discipline_id === disciplineId)
            .map(lesson => lesson.lesson_level_id);
        return levels.value.filter(level => lessonLevels.includes(level.id));
    };

    const getLessonsByDisciplineAndLevel = (disciplineId, levelId) => {
        return lessons.value.filter(lesson => lesson.discipline_id === disciplineId && lesson.lesson_level_id === levelId);
    };

    const toggleDiscipline = (disciplineId) => {
        expandedDisciplines[disciplineId] = !expandedDisciplines[disciplineId];
    };

    const toggleLevel = (disciplineId, levelId) => {
        const key = `${disciplineId}-${levelId}`;
        expandedLevels[key] = !expandedLevels[key];
    };

    const isExpanded = (disciplineId) => {
        return expandedDisciplines[disciplineId] || false;
    };

    const isLevelExpanded = (disciplineId, levelId) => {
        const key = `${disciplineId}-${levelId}`;
        return expandedLevels[key] || false;
    };

    const selectLesson = (lessonId) => {
        props.onLessonSelected(lessonId);
    };
</script>

<template>
    <div class="sidenav">
        <div class="sidenav__discipline sidenav__item" v-for="discipline in disciplines" :key="discipline.id" v-auto-animate>
            <h3 class="sidenav__discipline-title" @click="toggleDiscipline(discipline.id)">
                {{ discipline.name }}
                <span class="toggle-icon">{{ isExpanded(discipline.id) ? '-' : '+' }}</span>
            </h3>
            <div class="sidenav__levels" v-if="isExpanded(discipline.id)">
                <div class="sidenav__level sidenav__item" v-for="level in getLevelsByDiscipline(discipline.id)" :key="level.id" v-auto-animate>
                    <h4 class="sidenav__level-title" @click="toggleLevel(discipline.id, level.id)">
                        {{ level.name }}
                        <span class="sidenav__toggle-icon">{{ isLevelExpanded(discipline.id, level.id) ? '-' : '+' }}</span>
                    </h4>
                    <div class="sidenav__lessons sidenav__item" v-if="isLevelExpanded(discipline.id, level.id)">
                        <ul class="sidenav__lesson-list">
                            <li class="sidenav__lesson" v-for="lesson in getLessonsByDisciplineAndLevel(discipline.id, level.id)" :key="lesson.id">
                                <p class="sidenav__lesson-name" @click.prevent="selectLesson(lesson.id)">{{ lesson.name }}</p>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
<style scoped lang="scss">
  .sidenav {
    background-color: var(--extra-light-gray);
    box-sizing: border-box !important;

    width: 0;
    height: 100dvh;
    padding: 20px;

    border: var(--border);
    border-radius: 0 20px 20px 0;
    user-select: none;

    position: fixed;
    top: 0;
    left: 0;
    overflow: hidden;

    opacity: 0;
    
    transition: width 0.3s ease-in-out, opacity 0.3s ease-in-out;
    
    &:hover {
        width: 300px;
        opacity: 1;
    }

    &__item{
        transition: transform 0.3s ease-in-out;

        &:hover {
            transform: translateY(-3px);
        }
    }

    &__item  &__item {
        margin-left: 20px;
    }

    &__discipline-title,
    &__level-title,
    &__lesson-name {
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
  }
</style>