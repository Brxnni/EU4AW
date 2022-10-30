<script>

	export let checked = false;

	function click(){
		checked = !checked;
	}

</script>

<style>

	div {
		/* Inline */
		display: inline-block;

		/* This can be any size, but bigger than 32px looks blurry */
		width: 32px;
		aspect-ratio: 1/1;

		/* Adjust to text level */
		margin: 0 0 -9px 0;

		/* Checkbox image itself */
		background-image: url(./../checkbox/checkbox_unchecked.png);
		background-repeat: no-repeat;
		background-size: 100% 100%;

		/* Prevent accidentally selecting when repeatedly clicking checkbox */
		user-select: none;
	}

	div:hover {
		/* No seperate images for hover, just extra brightness */
		filter: brightness(120%);
	}

	div.checked {
		/* Change image on state change */
		background-image: url(./../checkbox/checkbox_checked.png);
	}

</style>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div class="{checked ? 'checked' : ''}" on:click={click}></div>
