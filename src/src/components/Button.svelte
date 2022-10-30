<script>

	export let onClick = () => {};

</script>

<style>

	/* Prevent selecting button text */
	* { user-select: none; }

	/* Inline */
	div {
		display: inline-block;
		/* Set font-size to 0 so that there is no weird
		   space between the inline-block elements */
		font-size: 0;
		height: 58px;
		max-width: 80% !important;

		/* Make sure backgrounds work when bigger */
		background-repeat: no-repeat;
		background-size: 100% 100%;

		white-space: nowrap;
	}

	div.button {
		height: 58px;
	}

	div.beginning {
		width: 29px;
		height: 100%;
	}

	div.end {
		width: 29px;
		height: 100%;
		transform: scaleX(-1);
	}

	div.middle {
		/* Make sure its wide enough for text */
		width: fit-content;
		/* Full height */
		height: 100%;
		
		/* This makes it so that the div doesn't go down when <span> is added */
		vertical-align: top;
		text-align: center;
		
		/* Make sure background div is under the text */
		z-index: 0;

		/* Repeat background (almost unnoticable, need to improve on that) */
		background-repeat: repeat-x;
		background-size: 139px 58px;
	}
	
	/* Different images with normal and on hover */
	div div.beginning { 		background-image: url("./../button/button_normal_end.png"); }
	div div.middle { 			background-image: url("./../button/button_normal_middle.png"); }
	div div.end { 				background-image: url("./../button/button_normal_end.png"); }

	div:hover div { filter: brightness(130%); }

	/* Change cursor on hover for better ✨ UX ✨ */
	div:hover {
		cursor: pointer;
	}

	span {
		/* Align exactly in the center */
		display: block;
		margin-top: 0.8em;
		line-height: 100%;
		
		/* Min-width is 139px, gets bigger with content */
		min-width: 139px;
		width: fit-content;
		max-width: calc(100%);
		
		padding: 0 30px 0 30px;

		/* Reset font-size from 0 to normal size */
		font-size: 1rem;

		/* Force into one line */
		text-overflow: ellipsis;
		overflow: hidden;
		white-space: nowrap;
	}

</style>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div class="button" on:click={onClick}>

	<div class="beginning"></div>
	<div class="middle"><span><slot/></span></div>
	<div class="end"></div>

</div>