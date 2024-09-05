<script setup>
	defineProps({
		name: String,
		text: String,
		color: String,
	})
</script>

<template>
	<div class="option">
		<span class="material-symbols-outlined outcome-options-variant-full icon">{{ name }}</span>
		<span>{{ text }}</span>
	</div>
</template>

<style scoped lang="scss">
	.option {
		display: flex;
		align-items: center;
		gap: 20px;

		.icon {
			color: v-bind(color);
		}
	}
</style>
