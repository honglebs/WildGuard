<script>
    import { onMount } from 'svelte';
    let poachingRisk = null;
    let error = null;

    // Fetch poaching risk data from the backend
    async function fetchPoachingRisk() {
        try {
            const response = await fetch('/api/poaching-risk/');
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const data = await response.json();
            poachingRisk = data.poaching_risk;
        } catch (err) {
            // error = err.message;
        }
    }

    // Fetch the data when the component is mounted
    onMount(() => {
        fetchPoachingRisk();
    });
</script>

<svelte:head>
    <title>Live Detection</title>
</svelte:head>

<div class="container d-flex align-items-center">
    <p>Live Detection</p>
    <!-- {#if poachingRisk}
        <pre>{JSON.stringify(poachingRisk, null, 2)}</pre>
    {:else if error}
        <p>Error: {error}</p>
    {:else}
        <p>Loading...</p>
    {/if} -->
</div>

<style>
    
</style>
