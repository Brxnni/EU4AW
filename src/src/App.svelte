<script>
	
	import { onMount } from "svelte";

	import BorderContainer from "./components/BorderContainer.svelte";
	import TextCheckbox from "./components/TextCheckbox.svelte";
	import Splitter from "./components/Splitter.svelte";
	import Button from "./components/Button.svelte";
	import Footer from "./components/Footer.svelte";
	import Result from "./components/Result.svelte";

	function capFirstLetter(name){
		let words = name.split("_");
		words.forEach(function (word, index){
			words[index] = word.charAt(0).toUpperCase() +
			word.slice(1).toLowerCase()
		});
		return words.join(" ");
	}

	let difficultyNames = [
		"very_easy",
		"easy",
		"medium",
		"hard",
		"very_hard",
		"insane"
	]

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

	let userDLCs = {};
	let userDiffs = {};

	let result;

	onMount(() => {
		console.log(userDLCs, userDiffs);
	});


</script>

<style>

	main {
		text-align: center;
	}

	/* These headings will be replaced by custom components later anyway */
	h1 {
		text-align: center;
		margin: 0;
	}

	.outer-container {
		max-width: 100%;
		margin: 0 auto 30px auto;
		user-select: none;
	}
	
	.inline {
		display: inline-block;
		vertical-align: top;
		min-width: fit-content;
		width: 49%;
		max-width: fit-content;
		margin: 10px;
		user-select: auto;
	}

	.left {
		text-align: left;
	}

	p { margin: 0 0 10px 0; }

</style>

<main>

	<h1>The EU4 Achievement Wheel</h1>
	<Splitter direction="up" />

	<div class="outer-container">

		<!-- DLC selection -->
		<div class="inline"><BorderContainer>
		
			<p>Select all DLCs you have available:</p>
			<!-- This is why I love svelte -->
			<div class="left">
				{#each dlcNames as dlc}
					<TextCheckbox
						bind:this={userDLCs[dlc]}
						text={capFirstLetter(dlc)}
						iconURL={`./dlc_icons/${dlc}.png`}
					/>
				{/each}
			</div>

		</BorderContainer></div>

		<!-- Difficulty selection -->
		<div class="inline"><BorderContainer> 
			
			<p>Select all difficulties that are acceptable:</p>
			<div class="left">
				{#each difficultyNames as diff, i}
					<TextCheckbox
						bind:this={userDiffs[diff]}
						checked
						text={capFirstLetter(diff)}
						iconURL={`./diff_icons/diff_${i}.png`}
					/>
				{/each}
			</div>

		</BorderContainer></div>

	</div>

	<Button onClick={() => {result.roll()}}>Roll!</Button>
	<Result bind:this={result} />
	<Splitter direction="down" />
	<Footer />

</main>
