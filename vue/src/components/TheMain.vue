<script setup></script>

<template>
  <main class="main">
    <slot />
  </main>
</template>

<style scoped lang="scss">
.main {
  border: var(--border);
  border-radius: 20px;
  padding: 20px;
  margin-top: 20px;
}
</style>
