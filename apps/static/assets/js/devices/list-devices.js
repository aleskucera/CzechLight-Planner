// custom.js
mapboxgl.accessToken = 'pk.eyJ1IjoiYWxlc2t1Y2VyYSIsImEiOiJjbGc5OG0wd3MxNWI2M3NvOTIyMDJwdGV4In0.pLzkwEwCdgexkT_ai7yP8Q';

function initMap(devices) {
    console.log("Initializing map...");

    // Create a new map centered on the first device's address
    var map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/aleskucera/clg9at7fl001d01pe1mwrkvgl',
        center: [15.251112431996722, 49.78450556341959], // Center of Czech Republic
        zoom: 6
    });

    // Wait for the map style to finish loading before adding markers
    map.on('load', function () {
        console.log("Map initialized. Adding markers...");

        // Loop through the devices and add a marker for each one
        devices.forEach(function (device) {
            console.log("Adding marker for device " + device.id + "...");
            var marker = new mapboxgl.Marker()
                .setLngLat([device.longitude, device.latitude])
                .setPopup(new mapboxgl.Popup({
                    offset: 25
                }).setHTML('<h4>' + device.name + '</h4>'))
                .addTo(map);
            console.log("Marker added for device " + device.id + ".");

            // Connect this marker to the previous marker with a line
            if (prevMarker) {
                var line = {
                    "type": "FeatureCollection",
                    "features": [
                        {
                            "type": "Feature",
                            "geometry": {
                                "type": "LineString",
                                "coordinates": [
                                    [prevMarker._lngLat.lng, prevMarker._lngLat.lat],
                                    [marker._lngLat.lng, marker._lngLat.lat]
                                ]
                            },
                            "properties": {}
                        }
                    ]
                };
                map.addLayer({
                    "id": "route" + device.id,
                    "type": "line",
                    "source": {
                        "type": "geojson",
                        "data": line
                    },
                    "layout": {
                        "line-join": "round",
                        "line-cap": "round"
                    },
                    "paint": {
                        "line-color": "#FF0000",
                        "line-width": 2
                    }
                });
            }

            // Keep track of the previous marker
            var prevMarker = marker;
        });

        console.log("All markers and lines added.");
    });
}

function updateDeviceStatusIcon(deviceId, isOnline) {
    const icon = document.querySelector(`.device-status[data-device-id="${deviceId}"]`);
    if (icon) {
        icon.classList.remove('text-c-red', 'text-c-green');
        icon.classList.add(isOnline ? 'text-c-green' : 'text-c-red');
    }
}

async function fetchDeviceStatus(deviceId) {
    const response = await fetch(`/api/devices/${deviceId}/`);
    const data = await response.json();
    return data.online;
}

window.addEventListener('load', async () => {
    console.log('Page loaded. Starting device status update loop...');

    while (true) {
        // Loop through all device status icons and update them
        const icons = document.querySelectorAll('.device-status');
        for (const icon of icons) {
            const deviceId = icon.dataset.deviceId;
            const isOnline = await fetchDeviceStatus(deviceId);
            updateDeviceStatusIcon(deviceId, isOnline);
        }
        console.log('Device status updated.');

        // Wait for 30 seconds before updating again
        await new Promise(resolve => setTimeout(resolve, 30000));
    }
});

// Call the initMap function when the page has finished loading
window.onload = function () {
    // Pass the 'devices' data from the Django template to the JavaScript function
    initMap(devicesData);
};
