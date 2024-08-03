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
		padding: var(--padding);
		margin-top: var(--padding);
	}
</style>
