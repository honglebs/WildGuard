<script>
	import Counter from './Counter.svelte';
	import welcome from '$lib/images/svelte-welcome.webp';
	import welcome_fallback from '$lib/images/svelte-welcome.png';
	import poaching from '$lib/images/poaching.png';
	import causesBG from '$lib/images/causes.png';
	import causes from '$lib/images/causes2.png';
</script>

<svelte:head>
	<title>WildGuard</title>
	<meta name="description" content="WildGuard demo app" />
</svelte:head>

<section>
	<div class="row">
		<div class="column">
			<h1 class="tagline"> Wildlife </h1>
			<h1><span>Poaching Detection</span></h1>
			<h1>System</h1>

			<div class="buttons">
				<a href="/"> Live Detection </a> 
				<a href="/"> Learn More </a>
			</div>
		</div>
		<div class="column">
			<div class="bento">
				<picture> 
					<img src={poaching} alt="poaching" />
				</picture>
				<div class="sideBox">
					<div class="funfact">
						<p> Fun Fact! </p>
						<p> The word "poach" comes from the Middle English word pocchen, which means "bagged" or "enclosed in a bag"</p>
	
					</div>
	
					<div class="stats">
						<h1> 100 + </h1>
						<p>poaching throughtout the year</p>
					</div>
				</div>
			</div>
		</div>
	</div>

	<div class="causes">
		<!-- <picture>  -->
			<img src={causes} alt="background" />
		<!-- </picture> -->
	</div>
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		margin: 0;
		padding: 0;
	}

	.row, .sideBox {
		display: flex;
		flex-direction: row;
		width: 100%;
		margin: 0;
		padding: 0;
	}

	.column {
		display: flex;
		flex-direction: column;
		flex: 1;
		position: relative;
	}

	.column h1 {
		font-size: 4em;
		text-align: left;
		font-weight: bold;
		margin: 0;
		position: relative;
		z-index: 1;
	}

	.column h1 span{
		color: var(--highlights);
	}

	.column:hover::after {
		opacity: 1;
	}

	.bento {
		width: 80%; /* adjust the width as needed */
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.sideBox {
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		gap: 20px;
	}

	.funfact, .stats {
		width: 22vw;
		flex: 1;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		background-color: var(--icon);
		padding: 10px;
		/* margin: 10px; */
		border-radius: 10px;
	}

	.stats{
		background-color: var(--sec);
	}

	.funfact p{
		color: var(--sec);
		text-align: center;
	}

	.stats p {
		color: var(--text);
		text-align: center;
	}

	.stats h1 {
		font-size: 2em;
		margin-bottom: 10px;
		color: var(--highlights);
	}

	.funfact{
		background-color: var(--icon);
	}

	.funfact p{
		color: var(--sec);
	}
	

</style>
