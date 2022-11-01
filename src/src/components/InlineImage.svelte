<script>

	export let src;
	export let alt = "";
	export let ariaHidden = false;

</script>

<style>
	div {
		display: inline-block;
	}
	
	img {
		margin-bottom: -6px;
		height: 1.2em;
	}
</style>

<div class="inlineimage">
	<img src={src} alt={alt} aria-hidden={ariaHidden ? "true" : "false"}>
</div>