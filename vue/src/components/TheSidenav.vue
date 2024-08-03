<script setup>

</script>

<template>
    <div class="sidenav">
        <slot />
    </div>
</template>

<style scoped>
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
    }
</style>