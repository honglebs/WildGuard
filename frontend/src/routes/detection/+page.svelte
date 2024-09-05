<script>
    import { onMount } from 'svelte';
    import L from 'leaflet';

    let poachingRisk = null;
    let map;
   
    /**
   * @type {string | null}
   */
    let error = null; 
    export const ssr = false;


    // // Fetch poaching risk data from the backend
    // async function fetchPoachingRisk() {
    //     try {
    //         const response = await fetch('/api/poaching-risk/');
    //         if (!response.ok) {
    //             throw new Error('Network response was not ok');
    //         }
    //         const data = await response.json();
    //         poachingRisk = data.poaching_risk;
    //     } catch (err) {
    //         // error = err.message;
    //     }
    // }

    // // Fetch the data when the component is mounted
    // onMount(() => {
    //     fetchPoachingRisk();
    // });

    // // Fetch map data from the backend
    // async function fetchMapData() {
    //     try {
    //         const response = await fetch('/api/map-data/');
    //         if (!response.ok) {
    //             throw new Error('Network response was not ok');
    //         }
    //         const data = await response.json();
    //         return data;
    //     } catch (err) {
    //         error = err instanceof Error ? err.message : 'Unknown error occurred';
    //         console.error(err);
    //     }
    // }

    // // Initialize the map when the component is mounted
    // onMount(async () => {
    //     const mapData = await fetchMapData();

    //     if (mapData && !error) {
    //         // Initialize Leaflet map
    //         map = L.map('map').setView([0, 15], 5);

    //         // Add tile layer from GEE
    //         L.tileLayer(mapData.tile_url, {
    //             attribution: 'Map data © Google Earth Engine',
    //             maxZoom: 18,
    //             tileSize: 256,
    //             zoomOffset: 0,
    //         }).addTo(map);
    //     }
    // });


    // Fetch map data from the backend
    async function fetchMapData() {
        try {
            const response = await fetch('/api/map-data/');
            if (!response.ok) {
                throw new Error('Failed to load map data.');
            }
            const data = await response.json();
            return data;
        } catch (err) {
            if (err instanceof Error) {
                error = err.message;  // If err is an instance of Error, use the message
            } else {
                error = 'An unknown error occurred';  // Handle other types of thrown values
            }
            console.error(err);
        }
    }

    // Initialize the map when the component is mounted
    onMount(async () => {
        if (typeof window !== 'undefined') {  // Only run on the client
            const L = await import('leaflet');  // Dynamically import Leaflet

            const mapData = await fetchMapData();

            if (mapData && !error) {
                // Initialize Leaflet map
                map = L.map('map').setView([0, 15], 5);

                // Add tile layer from GEE
                L.tileLayer(mapData.tile_url, {
                    attribution: 'Map data © Google Earth Engine',
                    maxZoom: 18,
                    tileSize: 256,
                    zoomOffset: 0,
                }).addTo(map);
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
