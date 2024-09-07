<script>
    export const ssr = false;
    import { onMount } from 'svelte';

    let map;
    let error = null;

    async function fetchMapData() {
        try {
            const response = await fetch('/api/map-data/', {
                method: 'GET',
                credentials: 'include',
            });

            if (response.status === 403 || response.status === 401) {
                window.location.href = '/api/start-auth/';
                return null;
            }

            if (!response.ok) {
                throw new Error(`Error fetching data: ${response.status} ${response.statusText}`);
            }

            return await response.json();
        } catch (error) {
            console.error("Error while fetching map data:", error.message);
            error = `Error fetching map data: ${error.message}`;
            return null;
        }
    }

    onMount(async () => {
        if (typeof window !== 'undefined') {
            try {
                const L = await import('leaflet');

                const mapData = await fetchMapData();

                if (mapData) {
                    map = L.map('map').setView([0, 15], 5);
                    L.tileLayer(mapData.tile_url, {
                        attribution: 'Map data © Google Earth Engine',
                        maxZoom: 18,
                    }).addTo(map);
                } else {
                    error = 'Failed to fetch map data. Please try refreshing the page.';
                }
            } catch (err) {
                error = `Error initializing map: ${err.message || 'Unknown error'}`;
                console.error("Map Initialization Error:", err);
            }
        }
    });
</script>

<div class="container align-items-center">
    <h1> 🔴 Live <span style="color:var(--highlights)"> Detection</span></h1>
    <div id="map" style="width: 100%; height: 600px;"></div>
    
    {#if error}
    <p>Error: {error}</p>
    {/if} 
</div>