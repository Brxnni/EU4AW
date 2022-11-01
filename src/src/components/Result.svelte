<script>

	import BorderContainer from "./BorderContainer.svelte";
	import InlineImage from "./InlineImage.svelte";

	let visible = true;

	let logoSrc = "./achievements_icons/achievement_full_house.png";
	let achName = "Full House";
	let achDifficulty = "Very Easy";
	let achDesc = "Have 3 Vassals and 2 Marches at the same time.";
	let achDLCs = ["art_of_war"];
	let achCustomNation = false;

	function capFirstLetter(name){
		let words = name.split("_");
		words.forEach(function (word, index){
			words[index] = word.charAt(0).toUpperCase() +
			word.slice(1).toLowerCase()
		});
		return words.join(" ");
	}

	export function roll(){
		console.log("ROLL!");
		visible = true;
	}

</script>

<style>

	/* ALL of this code starting here needs to be refactored, but it is good enough for now
	   as this is only a template anyway */
	div.result {
		max-width: fit-content;
		margin: 0 auto 0 auto;
	}

	div.result:not(.visible) {
		display: none;
	}

	/* I am now learning CSS grid, let's see how it goes */
	/* Update: Eh, it's alright, just a LOT of code needed to do what you want. Looks very cool though! */
	div.grid {
		display: grid;
		grid-template-columns: 50px min-content min-content;
		grid-template-rows: min-content min-content min-content;
	}

	div.grid div {
		padding: 15px;
	}

	div.icon {
		grid-column-start: 1;
		grid-column-end: 1;
		grid-row-start: 1;
		grid-row-end: 1;
		padding: 0 !important;

		position: relative;
	}

	div.icon img {
		width: 100%;
		position: absolute;
		top: 50%;
		left: 50%;
		aspect-ratio: 1/1;
		transform: translate(-50%, -50%);
	}

	div.title {
		grid-column-start: 2;
		grid-column-end: span 2;
	}

	div.title span.name { font-size: 1.5rem; white-space: nowrap; }
	div.title span.difficulty { font-size: 0.75rem; white-space: nowrap; }

	div.description {
		grid-column-start: 2;
		grid-column-end: span 2;

		grid-row-start: 2;
		color: lightgray;
		font-style: italic;
	}

	div.dlcs {
		grid-column-start: 2;
		grid-row-start: 3;
	}

	div.dlcs ul li {
		white-space: nowrap;
	}

	div.misc {
		grid-column-start: 3;
		grid-row-start: 3;
	}

	div.misc span.customnation {
		white-space: nowrap;
		line-height: 100%;
	}

</style>

<div class="result {visible ? 'visible' : ''}"><BorderContainer>

	<div class="grid">

		<div class="icon"><img src="{logoSrc}" alt="achievement icon"></div>

		<div class="title">
			<span class="name"> {achName} </span> <br/>
			<span class="difficulty"> {achDifficulty} </span>
		</div>

		<div class="description"> {achDesc} </div>

		<div class="dlcs">

			<span>Required DLCs:</span>
			<ul>
				{#each achDLCs as dlc}
					<li>
						<InlineImage src={`./dlc_icons/${dlc}.png`} ariaHidden={true} />
						{capFirstLetter(dlc)}
					</li>
				{/each}
			</ul>

		</div>

		<div class="misc">

			<span class="customnation">
				<InlineImage src={achCustomNation ? "./other/yes.png" : "./other/no.png"} ariaHidden={true} />
				{achCustomNation ? "Possible" : "Not possible"} with Custom Nation
			</span>

		</div>

	</div>



</BorderContainer></div>