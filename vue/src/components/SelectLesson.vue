<script setup>
    import { onMounted } from 'vue'

    import TheHeader from '../components/TheHeader.vue'
    import TheMain from '../components/TheMain.vue'
    
    // Функция переключения класса в select__student
    const selectStudent = () => {
        document.querySelector('.select__student').classList.toggle('selected');

        // Вызываем функцию изменения размеров родительского контейнера
        adjustParentSize();
    }

    // Функция изменения размеров родительского контейнера
    function adjustParentSize() {
        const selectContainer = document.querySelector('.select')
        const studentContainer = document.querySelector('.select__student')
        const lessonContainer = document.querySelector('.select__lesson')

        let maxHeight = 0

        // Проверяем, какой контейнер открыт
        if (studentContainer.classList.contains('selected')) {
            maxHeight = lessonContainer.offsetHeight
        } else {
            maxHeight = studentContainer.offsetHeight
        }

        // Устанавливаем размеры родителя
        selectContainer.style.height = `${maxHeight}px`
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
            <div class="select__student">
                <button class="btn" @click="selectStudent">Далее</button>
            </div>
            
            <div class="select__lesson">
                <button class="btn" @click="selectStudent">Назад</button>
            </div>
        </div>
    </TheMain>
</template>

<style scoped lang="scss">
    .select {
        position: relative;

        overflow: hidden;

        transition: height 0.2s ease-in-out;

        &__student, &__lesson {
            width: 100%;

            position: absolute;
            top: 0;

            transition: left 0.2s ease-in-out;
        }

        &__student {
            height: 100px;

            left: 0;
            background-color: red;

            &.selected {
                left: calc(-100% - var(--padding));

                & + .select__lesson {
                    left: 0;
                }
            }
        }

        &__lesson {
            height: 150px;

            left: calc(100% + var(--padding));

            background-color: blue;
        }
    }
</style>