<script>
	import baha from '$lib/images/baha.png';
</script>

<svelte:head>
	<title>About</title>
	<meta name="description" content="About this app" />
</svelte:head>

<div class="wrapper container d-flex align-items-center">
	<div class="row w-100">
		<div class="col-md-6 text-start">
			<img src={baha} alt="team" />
		</div>
		

		<div class="col-md-6">
			<p class="mb-0">About</p>
			<h1 class="mb-3 text-start">Wild<span style="color: #00FFCC">Guard</span></h1>
			<p class="linebreak mb-3 "> The Wildlife Poaching Detection System aims to detect and prevent poaching activities by leveraging satellite imagery and machine learning. The system will serve organizations and individuals dedicated to stopping poaching, focusing on regions where poaching is prevalent.</p>

			<p class="linebreak mb-3"> Our mission is driven by a profound concern for the future of wildlife, particularly elephants. We were inspired by the troubling reality that many young people today encounter elephants only through photographs and videos, rather than as vibrant, living creatures in their natural habitats. Faced with the escalating threat of poaching, we envisioned a future where these majestic animals thrive in the wild rather than being relegated to static images.</p>

			<p class="linebreak mb-3">WildGuard is a cutting-edge web application created to combat wildlife poaching on a global scale. By leveraging advanced technologies, we monitor and detect poaching activities in real-time. Our platform integrates Google Earth Engine to deliver up-to-date geospatial data and satellite imagery, while our custom machine learning model—developed using a specialized dataset from Roboflow—analyzes and identifies potential poaching incidents. This powerful combination of tools equips conservationists and law enforcement agencies with critical resources to safeguard wildlife and combat the dire threat of poaching effectively.</p>

			<p class="text-end mb-0"> by <span style="color: #00FFCC"> BAHA </span> Team</p>
		</div>
	</div>
</div>

<style>
	.wrapper{
		overflow: hidden;
	}
</style>

