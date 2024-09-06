<script>
	import poaching from '$lib/images/poaching.png';
	import causes from '$lib/images/causes2.png';
	import bulb from '$lib/images/bulb.png';
	import arrow from '$lib/images/arrow.png';
	import feature from '$lib/images/feature.png';
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
					<a href="/detection" class="btn"> Live Detection </a> 
				</div>
				<div class="border2">
					<a href="/about" class="btn"> Learn More </a>
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

	<div class="history mt-5 mb-5 p-4">
		<h1 class="fw-bold mt-2"> The <span style="color: #00FFCC">HISTORY</span> of <span style="color: #00FFCC">POACHING</span></h1>
		<!-- <p class=""> Poaching, or the illegal hunting of animals, can be seen all over the world, and a multitude of animals are targeted, including, but not limited to, rhinos and elephants. There are many different reasons as to why these animals are hunted, some being for their meat, horns, fur, bones, or even for entertainment purposes. In the case of rhinos and elephants, they are both hunted for their horns and tusks, as people often created medicines and ivory out of the animals’ body parts. Poaching has been around since the middle ages, when lawmakers started creating rules and regulations to protect the wildlife in the area. In North Africa specifically, poaching started in the 14th century, and was the main cause of the extinction of elephants about 1,000 years ago within the area. Poaching is not limited to only land animals, but also sea life. Many sea animals, including sharks, turtles, and many other fish species are poached daily, harming the ecosystems they are part of, and also the plant life surrounding them, such as coral reefs. Poaching has countless harmful effects on the earth, yet not enough is done to protect the wildlife that keeps our planet healthy and beautiful. Help and awareness is spread throughout the world, however poaching is still at large in many areas of the world.</p> -->
		<div class="container mt-5">
			<div class="row">
				<div class="col-md-4">
					<h2>Overview</h2>
					<p>Poaching, or the illegal hunting of animals, can be seen all over the world, and a multitude of animals are targeted, including, but not limited to, rhinos and elephants. There are many different reasons as to why these animals are hunted, some being for their meat, horns, fur, bones, or even for entertainment purposes.</p>
				</div>
				<div class="col-md-4">
					<h2>Historical Impact</h2>
					<p>In the case of rhinos and elephants, they are both hunted for their horns and tusks, as people often created medicines and ivory out of the animals’ body parts. Poaching has been around since the middle ages, when lawmakers started creating rules and regulations to protect the wildlife in the area. In North Africa specifically, poaching started in the 14th century, and was the main cause of the extinction of elephants about 1,000 years ago within the area.</p>
				</div>
				<div class="col-md-4">
					<h2>Effects on Marine Life</h2>
					<p>Poaching is not limited to only land animals, but also sea life. Many sea animals, including sharks, turtles, and many other fish species are poached daily, harming the ecosystems they are part of, and also the plant life surrounding them, such as coral reefs. Poaching has countless harmful effects on the earth, yet not enough is done to protect the wildlife that keeps our planet healthy and beautiful. Help and awareness is spread throughout the world, however poaching is still at large in many areas of the world.</p>
				</div>
			</div>
		</div>
	</div>
	<div class="feature m-5 p-5">
		<img src={feature} alt="background" class="img-fluid" />
	</div>
	<div class="causes position-relative">
		<div class="phrase position-absolute text-center p-3">
			<h2 class="fw-bold"> Why does this <span style="color: #00FFCC">matter</span>?</h2>
			<p> Seize the moment—ensure future generations experience what we cherish today. </p>
		</div>
		<img src={causes} alt="background" class="img-fluid"/>
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

	.row {
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
		color: var(--prim) !important; 
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

	.causes{
		width: 100%;
		height: auto;
		padding: 0;
		margin: 0;
	}

	.phrase {
		top: 55%;
		left: 50%;
		transform: translate(-50%, -50%);
	}

	.img-fluid {
		width: 100%;
		height: auto;
		display: block;
	}
</style>
