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
		"third_rome",
		"wealth_of_nations",
		"art_of_war",
		"common_sense",
		"conquest_of_paradise",
		"cradle_of_civilization",
		"dharma",
		"el_dorado",
		"emperor",
		"golden_century",
		"leviathan",
		"lions_of_the_north",
		"mandate_of_heaven",
		"mare_nostrum",
		"origins",
		"res_publica",
		"rights_of_man",
		"rule_britannia",
		"the_cossacks"
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
			{#each dlcNames as dlc}
				<TextCheckbox text={capFirstLetter(dlc)} iconURL={`/dlc_icons/${dlc}.png`}/>
			{/each}

		</BorderContainer></div>

		<!-- Difficulty selection -->
		<div class="inline"><BorderContainer> Difficulty selection goes here... </BorderContainer></div>

	</div>

</main>
