<script>
	import BorderContainer from "./BorderContainer.svelte";
</script>

<style>

	div.footer {
		max-width: fit-content;
		display: inline-block;
	}

	ul {
		list-style-type: none;
		padding: 5px;
		margin: 5px;
	}

	a {
		color: inherit;
	}

</style>

<div class="footer">
	<BorderContainer>

		<ul>
			<li>Made with <s>&#128149;</s> Code by		<a target="_blank" rel="noreferrer" href="https://github.com/Brxnni">							Brxnni</a> @ LemmyTech</li>
			<li>Credits:								<a target="_blank" rel="noreferrer" href="https://github.com/Brxnni/EU4AW/blob/main/CREDITS.md">	Unimplemented</a></li>
			<li>Code can be found						<a target="_blank" rel="noreferrer" href="https://github.com/Brxnni/EU4AW">						here</a></li>
			<li>Found an issue? Report it 				<a target="_blank" rel="noreferrer" href="https://github.com/Brxnni/EU4AW/issues/new">			here</a></li>
		</ul>

	</BorderContainer>
</div>
