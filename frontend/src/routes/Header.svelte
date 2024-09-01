<script>
	import { page } from '$app/stores';
	import logo from '$lib/images/logo.png';
</script>

<svelte:head>
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
</svelte:head>

<header class="d-flex justify-content-between align-items-center p-4">
	<div class="corner d-flex align-items-center gap-2">
		<a href="/">
			<img src={logo} alt="SvelteKit" style="width: 3em"/>
		</a>
		<a href="/" class="fw-bold text-decoration-none">
			Wild<span>Guard</span>
		</a>
	</div>

	<nav>
		<ul class="nav">
			<li class="nav-item">
				<a href="/wildhackle" class="nav-link" aria-current={$page.url.pathname === '/wildhackle' ? 'page' : undefined}>WildHackle</a>
			</li>
			<li class="nav-item">
				<a href="/detection" class="nav-link" aria-current={$page.url.pathname === '/detection' ? 'page' : undefined}>Live Detection</a>
			</li>
			<li class="nav-item">
				<a href="/about" class="nav-link" aria-current={$page.url.pathname.startsWith('/about') ? 'page' : undefined}>About Us</a>
			</li>
		</ul>
	</nav>
</header>

<style>
	header{
		padding: 2em;
	}

	.corner {
		font-size: var(--heading);
		gap: 10px;
	}

	.corner a span{
		color: var(--highlights);
	}

	.corner img {
		width: 2em;
		height: 2em;
		object-fit: contain;
	}

	ul {
		height: 3em;
	}

	li {
		position: relative;
		font-size: var(--heading);
		height: 100%;
	}

	/* li[aria-current='page']::before {
		--size: 6px;
		content: '';
		width: 0;
		height: 0;
		position: absolute;
		top: 0;
		left: calc(50% - var(--size));
		border: var(--size) solid transparent;
		border-top: var(--size) solid var(--color-theme-1);
	} */

	nav a {
		color: var(--text);
		font-size: var(--subparagraph);
		transition: color 0.2s linear;
		text-decoration: none;
	}

	nav a:hover{
		color: var(--highlights) !important;
	}

	nav a::after {
		color: var(--highlights);
		text-decoration: none;
		content: ''; 
		position: absolute; 
		top: 4px; 
		left: 0; 
		width: 0; 
		height: 3px; 
		background: var(--highlights);
		transform: scaleX(0); 
		transform-origin: bottom right; 
		transition: transform 0.3s ease; 
	}

	nav a:hover::after{
		width: 100%; 
		transform: scaleX(1);
		transform-origin: bottom left; 
	}
</style>
