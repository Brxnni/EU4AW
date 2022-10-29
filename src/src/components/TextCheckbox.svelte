<script>

	import Checkbox from "./Checkbox.svelte";

	export let checked;
	export let iconURL;
	export let text;

</script>

<style>

	img {
		margin-bottom: -6px;
		height: 1.2em;
	}

</style>

<div>
	<Checkbox checked={checked}/>
	{#if iconURL} <img src={iconURL} alt=""> {/if}
	<span>{text}</span>
</div>