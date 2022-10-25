<script>
	
	import BorderContainer from "./components/BorderContainer.svelte";
	import Checkbox from "./components/Checkbox.svelte";
	import Button from "./components/Button.svelte";

</script>

<main>
	<h1>EU4, Best Game in whole World</h1>

	<p> Cool Checkbox: <Checkbox checked/> </p>
	<Button> Dynamic Button 😎 </Button>

	<BorderContainer>

		<p>I am inside a container, look at me!</p>
		<Button> I am also inside a container 😎 </Button>

	</BorderContainer>

</main>

<style>
</style>
