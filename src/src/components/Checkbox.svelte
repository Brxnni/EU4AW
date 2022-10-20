<script>

	import checkbox_unchecked from "./../assets/checkbox_unchecked.png";
	import checkbox_checked from "./../assets/checkbox_checked.png";

	export let state = false;

	function click(){
		state = !state;
	}

</script>

<style>

	div {
		width: 32px;
		height: 32px;
		margin: 3px;
		background-image: url(./../assets/checkbox_unchecked.png);
	}

	div:hover {
		filter: brightness(110%);
	}

	div.checked {
		background-image: url(./../assets/checkbox_checked.png);
	}

</style>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div class="{state ? 'checked' : ''}" on:click={click}></div>