<script>
    export const ssr = false;
    import { onMount } from 'svelte';

    let map;  // Store the Leaflet map instance
    let error = null;  // Track errors

    // Fetch map data from the backend
    async function fetchMapData() {
        try {
            const response = await fetch('http://127.0.0.1:8000/api/map-data/');
            
            console.log('Response status:', response.status);  // Log the status code

            if (!response.ok) {
                throw new Error(`Failed to load map data from the backend. Status code: ${response.status}`);
            }

            const data = await response.json();
            console.log("Map Data Fetched:", data);  // Log fetched data for debugging
            return data;
        } catch (err) {
            error = err instanceof Error ? err.message : 'An unknown error occurred while fetching map data.';
            console.error("Error while fetching map data:", err);  // Log error
            return null;  // Return null on error
        }
    }

    // Initialize the Leaflet map once the component mounts
    onMount(async () => {
        if (typeof window !== 'undefined') {  // Only run on the client side
            try {
                const L = await import('leaflet');  // Dynamically import Leaflet

                const mapData = await fetchMapData();  // Fetch map data

                if (mapData && !error) {
                    map = L.map('map').setView([0, 15], 5);

                    // Add a tile layer to the map using the data from the backend
                    L.tileLayer(mapData.tile_url, {
                        attribution: 'Map data © Google Earth Engine',
                        maxZoom: 18,
                        tileSize: 256,
                        zoomOffset: 0,
                    }).addTo(map);
                }
            } catch (err) {
                error = 'Error initializing map';  // Handle any initialization errors
                console.error("Map Initialization Error:", err);
            }
        }
    });
</script>


<svelte:head>
    <title>Live Detection</title>
</svelte:head>

<div class="container d-flex align-items-center">
    <p>Live Detection</p>
    <div id="map" style="width: 100%; height: 600px;"></div>
    {#if error}
        <p>Error: {error}</p>
    {/if}
</div>

<style>
    #map {
        width: 100%;
        height: 600px;
    }
</style>
