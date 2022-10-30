<script>

	import Checkbox from "./Checkbox.svelte";

	export let checked = false;
	export let iconURL;
	export let text;

</script>

<style>

	div { user-select: none; }
	span { user-select: text; }

	img {
		margin-bottom: -6px;
		height: 1.2em;
		pointer-events: none;
	}

</style>

<div>
	<Checkbox checked={checked}/>
	{#if iconURL} <img src={iconURL} alt=""> {/if}
	<span>{text}</span>
</div>
