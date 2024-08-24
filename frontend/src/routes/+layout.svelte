<script>
	import Header from './Header.svelte';
	import '../app.css';
</script>

<div class="app">
	<Header />

	<main>
		<slot />
	</main>

	<footer>
		<!-- <p>visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to learn SvelteKit</p> -->
		<p class="credit">&copy; <span id="currentYear"></span> by <span>WilGuard Group</span> | All Rights Reserved</p>
		<p class="credit2">BAHA TEAM | Animal Hacks 2024</p>
	</footer>
</div>

<style>
	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}

	main {
		flex: 1;
		display: flex;
		flex-direction: column;
		padding: 1rem;
		width: 100%;
		max-width: 85vw;
		margin: 0 100px;
		box-sizing: border-box;
	}

	footer {
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: center;
		padding: .5em;
		background-color: var(--sec);
	}

	.credit, .credit2{
		margin: 0 2em;
	}

	@media (min-width: 480px) {
		footer {
			padding: 12px 0;
		}
	}
</style>
