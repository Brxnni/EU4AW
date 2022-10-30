<script>

	export let direction = "up";

</script>

<style>

	* {
		user-select: none;
	}

	/* Inline styles */
	div {
		display: inline-block;
		/* Set font-size to 0 so that there is no weird
		   space between the inline-block elements */
		font-size: 0;
		height: 43px;
		
		/* Make sure backgrounds work when bigger */
		background-repeat: no-repeat;
		background-size: 100% 100%;
		
		white-space: nowrap;
	}
	
	div.splitter {
		display: block;
		height: 43px;
		width: 100%;
		margin: 10px 0 10px 0;
	}

	/* Remove some margin from correct side, depending on the direction */
	div.splitter.up { margin-top: -20px; }
	div.splitter.down { margin-bottom: 5px; }

	div.beginning {
		width: 43px;
		height: 100%;
	}

	div.end {
		width: 43px;
		height: 100%;
		transform: scaleX(-1);
	}

	div.middle {
		/* Fit entire length that isn't taken by start and end */
		width: calc(100% - 2*43px);
		/* Texture height */
		height: 14px;
		
		background-repeat: repeat-x;
		background-size: 100% 14px;
	}

	div.down div.middle {
		/* Make line connect properly */
		vertical-align: top;
	}

	div div.beginning { 		background-image: url("./../splitter/splitter_end.png"); }
	div div.middle { 			background-image: url("./../splitter/splitter_middle.png"); }
	div div.end { 				background-image: url("./../splitter/splitter_end.png"); }

	/* Apparently using scaleY overwrites the scaleX value to 1 (which is stupid) so it needs to be defined again */
	div.down div.beginning { transform: scale(1, -1) }
	div.down div.end { transform: scale(-1, -1) }

</style>

<div class="splitter {direction}">
	<div class="beginning"></div>
	<div class="middle"></div>
	<div class="end"></div>
</div>