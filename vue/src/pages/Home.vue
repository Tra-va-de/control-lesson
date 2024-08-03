<script setup>
    import { ref, provide } from 'vue'

    import SelectLesson from '@/components/SelectLesson.vue'
    import ControlLesson from '@/components/ControlLesson.vue';

	const selectedStudent = ref(null);
    const selectedLesson = ref(null);
    
    provide('selectedStudent', selectedStudent)
    provide('selectedLesson', selectedLesson)
</script>

<template>
    <SelectLesson v-if="!selectedStudent || !selectedLesson"/>
    
    <ControlLesson v-else/>
</template>

<style scoped>

</style>