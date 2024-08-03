<script setup>
    import { inject, onMounted, defineEmits, ref } from 'vue'
    import axios from 'axios'

    const apiEndpoint = import.meta.env.VITE_PRIVATE_API_ENDPOINT

    const props = defineProps({
        changeSlide: Function,
    })

    const emit = defineEmits()

    const students = ref([]);

    const selectedStudent = inject('selectedStudent')

    onMounted(async () => {
        await fetchStudentsData();
    });
    
    // Получаем данные о студентах
    const fetchStudentsData = async () => {
        try {
            const response = await axios.get(`${apiEndpoint}/students/`);
            console.log(response.data);
            students.value = response.data;

            // Вызываем событие, когда данные загружены
            emit('students-loaded');
        } catch (error) {
            console.error('Failed to fetch students data:', error);
        }
    };

    const selectStudent = (student) => {
        selectedStudent.value = student;
        props.changeSlide();
    };
</script>

<template>
    <div class="wrapper">
        <div class="student item" v-for="student in students" :key="student.id">
            <p class="student-name" @click.prevent="selectStudent(student)">
                {{ student.first_name }} {{ student.last_name }}
            </p>
        </div>
    </div>
</template>

<style scoped>
    .item {
        cursor: pointer;

        transition: transform 0.3s ease-in-out;

        &::after {
            content: '';

            display: block;
            width: 100%;
            height: 1px;

            margin-top: 10px;

            background-color: var(--light-gray);
        }
    }

    .item:hover {
        transform: translateY(-3px);
    }
</style>