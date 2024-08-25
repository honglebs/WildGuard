<script>
	import Header from './Header.svelte';
	import '../app.css';
</script>

<div class="app">
	<Header />

	<main class="container mb-4">
		<slot />
	</main>

	<footer class="text-white py-2 py-md-3 d-flex justify-content-between align-items-center">
		<p class="credit mb-0">© 2024 by <span>WilGuard Group</span> | All Rights Reserved</p>
		<p class="credit2 mb-0">BAHA TEAM | Animal Hacks 2024</p>
	</footer>
</div>


<style>
	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}

	/* main {
		flex: 1;
		display: flex;
		flex-direction: column;
		padding: 1rem;
		width: 100%;
		max-width: 85vw;
		margin: 0 100px;
		box-sizing: border-box;
	} */

	footer {
		background-color: var(--sec);
	}

	.credit, .credit2{
		margin: 0 2em;
	}
</style>
