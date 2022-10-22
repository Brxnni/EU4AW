<script>

	export let onClick;

	import button_normal_end from "./../assets/button_normal_end.png";
	import button_normal_middle from "./../assets/button_normal_middle.png";
	import button_hover_end from "./../assets/button_hover_end.png";
	import button_hover_middle from "./../assets/button_hover_middle.png";

</script>

<style>
	* { user-select: none; }

	div {
		display: inline-block;
		/* Set font-size to 0 so that there is no weird
		   space between the inline-block elements */
		font-size: 0;
		height: 58px;
	}

	div.beginning {
		width: 29px;
		height: 58px;
	}

	div.end {
		width: 29px;
		height: 58px;
		transform: scaleX(-1);
	}

	div.middle {
		position: relative;
		min-width: 139px;
		width: fit-content;
		
		/* This makes it so that the div doesn't go down when <span> is added */
		vertical-align: top;
		text-align: center;
		

		background-repeat: repeat-x;
	}
	
	div div.beginning { background-image: url("./../assets/button_normal_end.png"); }
	div div.middle { background-image: url("./../assets/button_normal_middle.png"); }
	div div.end { background-image: url("./../assets/button_normal_end.png"); }

	div:hover div.beginning { background-image: url("./../assets/button_hover_end.png"); }
	div:hover div.middle { background-image: url("./../assets/button_hover_middle.png"); }
	div:hover div.end { background-image: url("./../assets/button_hover_end.png"); }

	div:hover {
		cursor: pointer;
	}

	span {
		display: block;
		margin-top: 0.8em;
		line-height: 100%;
		min-width: 139px;
		width: fit-content;
		
		padding: 0 20px 0 20px;
		font-size: 22px;
		white-space: nowrap;

		z-index: 2;
	}

</style>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div class="button" on:click={onClick}>

	<div class="beginning"></div>
	<div class="middle"><span><slot/></span></div>
	<div class="end"></div>

</div>