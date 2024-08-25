<script>
	import baha from '$lib/images/baha.png';
</script>

<svelte:head>
	<title>About</title>
	<meta name="description" content="About this app" />
</svelte:head>

<div class="container d-flex align-items-center">
	<div class="row w-100">
		<div class="col-md-6 text-start">
			<img src={baha} alt="team" />
		</div>
		

		<div class="col-md-6">
			<p class="mb-0">About</p>
			<h1 class="mb-3 text-start">Wild<span style="color: #00FFCC">Guard</span></h1>
			<p class="linebreak mb-3"> The Wildlife Poaching Detection System aims to detect and prevent poaching activities by leveraging satellite imagery and machine learning. The system will serve organizations and individuals dedicated to stopping poaching, focusing on regions where poaching is prevalent.</p>

			<p class="text-end mb-0"> by <span style="color: #00FFCC"> BAHA </span> Team</p>
		</div>
	</div>
</div>


