<script setup></script>

<template>
	<header class="header">
		<slot />
	</header>
</template>

<style scoped>
	.header {
		background-color: var(--bg-color);
		color: white;
		padding: 25px;
		border-radius: 20px;
	}
</style>
