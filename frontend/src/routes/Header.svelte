<script>
	import { page } from '$app/stores';
	import logo from '$lib/images/svelte-logo.svg';
	// import github from '$lib/images/github.svg';
</script>

<header>
	<div class="corner">
		<a href="https://kit.svelte.dev">
			<img src={logo} alt="SvelteKit" />
		</a>
		<a href="/">
			Wild <span> Guard </span>
		</a>
	</div>

	<nav>
		<!-- <svg viewBox="0 0 2 3" aria-hidden="true">
			<path d="M0,0 L1,2 C1.5,3 1.5,3 2,3 L2,0 Z" />
		</svg> -->
		<ul>
			<!-- <li aria-current={$page.url.pathname === '/' ? 'page' : undefined}>
				<a href="/">Wild<span>Guard</span></a>
			</li> -->
			<li aria-current={$page.url.pathname === '/sverdle' ? 'page' : undefined}>
				<a href="/sverdle">Live Detection</a>
			</li>
			<li aria-current={$page.url.pathname.startsWith('/about') ? 'page' : undefined}>
				<a href="/about">About Us</a>
			</li>
		</ul>
		<!-- <svg viewBox="0 0 2 3" aria-hidden="true">
			<path d="M0,0 L0,3 C0.5,3 0.5,3 1,2 L2,0 Z" />
		</svg> -->
	</nav>
</header>

<style>
	header {
		display: flex;
		justify-content: space-between;
		padding: 2em 3em;
	}

	.corner {
		display: flex;
		justify-content: space-between;
		/* width: 5em; */
		font-size: var(--heading);
		/* height: 3em; */
	}

	.corner a {
		display: flex;
		align-items: center;
		justify-content: center;
		font-weight: bold;
		width: 100%;
		height: 100%;
	}

	.corner a:hover{
		text-decoration: none;
	}

	.corner a span{
		color: var(--highlights);
	}

	.corner img {
		width: 2em;
		height: 2em;
		object-fit: contain;
	}

	nav {
		display: flex;
		justify-content: center;
		/* --background: rgba(255, 255, 255, 0.7); */
	}

	ul {
		position: relative;
		padding: 0;
		margin: 0;
		height: 3em;
		display: flex;
		justify-content: center;
		align-items: center;
		list-style: none;
		/* background-size: contain; */
	}

	li {
		position: relative;
		font-size: var(--heading);
		height: 100%;
	}

	li[aria-current='page']::before {
		--size: 6px;
		content: '';
		width: 0;
		height: 0;
		position: absolute;
		top: 0;
		left: calc(50% - var(--size));
		border: var(--size) solid transparent;
		border-top: var(--size) solid var(--color-theme-1);
	}

	nav a {
		display: flex;
		height: 100%;
		align-items: center;
		padding: 0 1rem;
		color: var(--text);
		/* font-weight: 700; */
		/* font-size: 0.8rem; */
		font-size: var(--subparagraph);
		/* text-transform: uppercase; */
		/* letter-spacing: 0.1em; */
		text-decoration: none;
		transition: color 0.2s linear;
	}

	nav a:hover{
		color: var(--highlights);
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
