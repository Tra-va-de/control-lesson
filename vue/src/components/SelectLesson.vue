<script setup>
    import { onMounted, nextTick, ref } from 'vue'

    import TheHeader from '../components/TheHeader.vue'
    import TheMain from '../components/TheMain.vue'

    import StudentsList from './StudentsList.vue'
    import LessonsList from './LessonsList.vue'

    const studentIsSelected = ref(false)

    // Функция, которая будет вызываться при загрузке студентов
    const handleStudentsLoaded = () => {
        // console.log('Students loaded:');
        nextTick(() => {
            adjustParentSize();
        });
    }

    // Функция переключения класса в select__student
    const changeSlide = () => {
        document.querySelector('.select__students').classList.toggle('selected');

        // Вызываем функцию изменения размеров родительского контейнера
        adjustParentSize();
    }

    // Функция изменения размеров родительского контейнера
    function adjustParentSize() {
        const selectContainer = document.querySelector('.select')
        const studentContainer = document.querySelector('.select__students')
        const lessonContainer = document.querySelector('.select__lessons')

        let maxHeight = 0

        if (studentContainer) {
            // Проверяем, какой контейнер открыт
            if (studentContainer.classList.contains('selected')) {
                maxHeight = lessonContainer.offsetHeight
                studentIsSelected.value = true
            } else {
                maxHeight = studentContainer.offsetHeight
                studentIsSelected.value = false
            }
            
            // Устанавливаем размеры родителя
            selectContainer.style.height = `${maxHeight}px`
        }
    }

    // Также можно вызывать функцию при изменении размеров окна
    window.onresize = adjustParentSize;

    onMounted(() => {
        adjustParentSize();
    })
</script>

<template>
    <TheHeader>
        <div class="header-content">
            <button v-if="studentIsSelected" class="back-btn" @click="changeSlide">↶</button>
            <h1 class="header-title">{{ studentIsSelected ? 'Выбор урока' : 'Выбор студента' }}</h1>
        </div>
    </TheHeader>

    <TheMain>
        <div class="select">
            <div class="select__students">
                <StudentsList :changeSlide="changeSlide" @students-loaded="handleStudentsLoaded" />
            </div>
            
            <div class="select__lessons">
                <LessonsList @click="adjustParentSize" />
            </div>
        </div>
    </TheMain>
</template>

<style scoped lang="scss">
    .header-content {
        display: flex;
        align-items: center;
        gap: var(--padding);
    }

    .back-btn {
        font-size: 18px;
        font-weight: 700;

        width: 35px;
        padding: 5px 2px 2px;
        aspect-ratio: 1;

        border: var(--border);
        border-width: 2px;
        border-radius: 50%;
        outline: none;

        color: var(--white);
        background-color: transparent;

        transition: background-color 0.2s ease-in-out,
                    scale 0.2s ease-in-out;

        &:hover {
            background-color: rgba(255, 255, 255, 0.1);
            scale: 1.1;
        }
    }

    .select {
        position: relative;

        overflow: hidden;

        transition: height 0.2s ease-in-out;

        &__students, &__lessons {
            width: 100%;

            position: absolute;
            top: 0;

            transition: left 0.2s ease-in-out;
        }

        &__students {
            left: 0;

            &.selected {
                left: calc(-100% - var(--padding));

                & + .select__lessons {
                    left: 0;
                }
            }
        }

        &__lessons {
            left: calc(100% + var(--padding));
        }
    }
</style>