// Function to create and initialize the map
function createMap(containerId, center = [15.251112431996722, 49.78450556341959], zoom = 6) {
    mapboxgl.accessToken = 'pk.eyJ1IjoiYWxlc2t1Y2VyYSIsImEiOiJjbGc5OG0wd3MxNWI2M3NvOTIyMDJwdGV4In0.pLzkwEwCdgexkT_ai7yP8Q';

    // Create map
    const map = new mapboxgl.Map({
        container: containerId,
        style: 'mapbox://styles/aleskucera/clg9at7fl001d01pe1mwrkvgl',
        center: center,
        zoom: zoom
    });

    return map;
}