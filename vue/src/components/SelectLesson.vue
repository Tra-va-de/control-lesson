<script setup>
    import { onMounted, nextTick } from 'vue'

    import TheHeader from '../components/TheHeader.vue'
    import TheMain from '../components/TheMain.vue'

    import StudentsList from './StudentsList.vue'
    import LessonsList from './LessonsList.vue'

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
            } else {
                maxHeight = studentContainer.offsetHeight
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
        <h1>Выбор урока</h1>
    </TheHeader>

    <TheMain>
        <div class="select">
            <div class="select__students">
                <StudentsList :changeSlide="changeSlide" @students-loaded="handleStudentsLoaded" />
            </div>
            
            <div class="select__lessons">
                <button class="btn" @click="changeSlide">Назад</button>
                <LessonsList @click="adjustParentSize" />
            </div>
        </div>
    </TheMain>
</template>

<style scoped lang="scss">
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