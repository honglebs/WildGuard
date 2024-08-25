<script>
	import poaching from '$lib/images/poaching.png';
	import causes from '$lib/images/causes2.png';
	import bulb from '$lib/images/bulb.png';
	import arrow from '$lib/images/arrow.png';
</script>

<svelte:head>
	<title>WildGuard</title>
	<meta name="description" content="WildGuard demo app" />
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
</svelte:head>

<section class="container-fluid">
	<div class="row">
		<div class="column col-md-6 d-flex flex-column align-items-start mt-5 pt-5">
			<h1 class="tagline"> Wildlife </h1>
			<h1><span>Poaching Detection</span></h1>
			<h1>System</h1>

			<div class="buttons d-flex gap-3 my-3">
				<div class="border1">
					<a href="/" class="btn"> Live Detection </a> 
				</div>
				<div class="border2">
					<a href="/" class="btn"> Learn More </a>
				</div>
			</div>
		</div>
		<div class="column col-md-6 d-flex flex-column align-items-center">
			<div class="bento">
				<picture> 
					<img src={poaching} alt="poaching" />
				</picture>
				<div class="d-flex flex-row justify-content-between gap-3 mt-3">
					<div class="funfact d-flex flex-column align-items-center justify-content-center p-3 rounded">
						<div class="top d-flex align-items-center gap-2 mb-2">
							<p> Fun Fact!</p>
							<img src={bulb} alt="bulb"/>
						</div>
						<p> The word "poach" comes from the Middle English word pocchen, which means "bagged" or "enclosed in a bag"</p>
					</div>
	
					<div class="stats">
						<img src={arrow} alt="arrow" class="arrow"/>
						<h1> 100 + </h1>
						<p>poaching throughtout the year</p>
					</div>
				</div>
			</div>
		</div>
	</div>

	<div class="history m-5 p-4">
		<h1 class="fw-bold"> The <span style="color: #00FFCC">HISTORY</span> of <span style="color: #00FFCC">POACHING</span></h1>
	</div>
	<div class="causes">
		<!-- <picture>  -->
			<img src={causes} alt="background" />
		<!-- </picture> -->
	</div>
</section>

<style>
	/* section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		margin: 0;
		padding: 0;
	} */

	.row, .sideBox {
		display: flex;
		flex-direction: row;
		width: 100%;
		margin: 0;
		padding: 0;
	}

	.column {
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

	.buttons {
		width: 30vw;
	}

	.border1, .border2 {
		flex: 1;
		background: linear-gradient(to right, var(--highlights), var(--icon)); 
		padding: 3px; 
		border-radius: 8px; 
	}

	.btn {
		display: block; 
		background: var(--sec);
		padding: .75em;
		border-radius: 8px; 
		text-align: center;
		text-decoration: none; 
		color: var(--text); 
	}

	.btn:hover {
		color: var(--prim); 
		background-color: var(--icon);
		text-decoration: none;
		font-weight: 500;
	}

	.border1:hover, .border2:hover{
		background: linear-gradient(to right, var(--sec), var(--prim))
	}

	.funfact, .stats {
		width: 10vw;
		flex: 1;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		background-color: var(--icon);
		padding: 5px;
		border-radius: 10px;
	}

	.stats{
		background-color: var(--sec);
		position: relative;
	}

	.funfact p{
		color: var(--sec);
		text-align: center;
		margin: 0;
	}

	.stats p {
		color: var(--text);
		text-align: center;
		margin: 0;
	}

	.stats h1 {
		font-size: 3em;
		margin-bottom: 10px;
		color: var(--highlights);
		transition: transform 0.3s ease, color 0.3s ease;
	}

	.stats h1:hover {
		transform: scale(1.2);
	}

	.funfact{
		background-color: var(--icon);
	}

	.funfact p{
		color: var(--sec);
	}

	.top{
		/* display: flex; */
		flex-direction: row;
		justify-content: space-between;
		gap: 5em;
		width: 90%;
	}

	.top p{
		background-color: var(--sec);
		padding: .5em;
		color: var(--text);
		border-radius: 8px;
		align-items: center;
		margin: 0.8rem 0;
	}

	.top img{
		width: auto;
		height: 45px;
	}


	.stats img.arrow {
		position: absolute; 
		top: .8rem;             
		right: .8rem;          
		height: 45px;      
		margin: 5px;      
	}
</style>
