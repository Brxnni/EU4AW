<script>
	
	import BorderContainer from "./components/BorderContainer.svelte";
	import TextCheckbox from "./components/TextCheckbox.svelte";

	function capFirstLetter(name){
		let words = name.split("_");
		words.forEach(function (word, index){
			words[index] = word.charAt(0).toUpperCase() +
			word.slice(1).toLowerCase()
		});
		return words.join(" ");
	}

	let dlcNames = [
		"conquest_of_paradise",
		"wealth_of_nations",
		"res_publica",
		"art_of_war",
		"el_dorado",
		"common_sense",
		"the_cossacks",
		"mare_nostrum",
		"rights_of_man",
		"mandate_of_heaven",
		"third_rome",
		"cradle_of_civilization",
		"rule_britannia",
		"dharma",
		"golden_century",
		"emperor",
		"leviathan",
		"origins",
		"lions_of_the_north"
	];
	let availableDLCs = {};

</script>

<style>

	.outer-container {
		text-align: center;
		max-width: 100%;
		white-space: nowrap;
		margin: auto;
	}
	
	.inline {
		display: inline-block;
		vertical-align: top;
		width: 49%;
	}

	.left {
		text-align: left;
	}

	p { margin: 0 0 10px 0; }

</style>

<main>
	<h1>EU4, Best Game in whole World</h1>

	<h2>Settings</h2>
	<div class="outer-container">

		<!-- DLC selection -->
		<div class="inline"><BorderContainer>
		
			<p>Select all DLCs you have available:</p>

			<!-- This is why I love svelte -->
			<div class="left">
				{#each dlcNames as dlc}
					<TextCheckbox text={capFirstLetter(dlc)} iconURL={`/dlc_icons/${dlc}.png`}/>
				{/each}
			</div>

		</BorderContainer></div>

		<!-- Difficulty selection -->
		<div class="inline"><BorderContainer> Difficulty selection goes here... </BorderContainer></div>

	</div>

</main>
