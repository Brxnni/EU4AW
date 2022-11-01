<script>

	import Checkbox from "./Checkbox.svelte";
	import InlineImage from "./InlineImage.svelte";

	export let checked = false;
	export let iconURL;
	export let text;

</script>

<style>

	div { user-select: none; }
	span { user-select: text; }

</style>

<div>
	<Checkbox checked={checked}/>
	{#if iconURL} <InlineImage src={iconURL} /> {/if}
	<span>{text}</span>
</div>
