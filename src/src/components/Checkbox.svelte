<script>

	import checkbox_unchecked from "./../assets/checkbox_unchecked.png";
	import checkbox_checked from "./../assets/checkbox_checked.png";

	export let checked = false;

	function click(){
		checked = !checked;
	}

</script>

<style>

	div {
		display: inline-block;
		width: 32px;
		height: 32px;
		margin: 0 0 -9px 0;
		background-image: url(./../assets/checkbox_unchecked.png);
		background-repeat: no-repeat;
		background-size: 100% 100%;
	}

	div:hover {
		filter: brightness(110%);
	}

	div.checked {
		background-image: url(./../assets/checkbox_checked.png);
	}

</style>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div class="{checked ? 'checked' : ''}" on:click={click}></div>