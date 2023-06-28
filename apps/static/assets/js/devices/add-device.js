// Place your JavaScript code here

mapboxgl.accessToken = 'pk.eyJ1IjoiYWxlc2t1Y2VyYSIsImEiOiJjbGc5OG0wd3MxNWI2M3NvOTIyMDJwdGV4In0.pLzkwEwCdgexkT_ai7yP8Q';

var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/aleskucera/clg9at7fl001d01pe1mwrkvgl',
    center: [15.251112431996722, 49.78450556341959], // Center of Czech Republic
    zoom: 6
});

var geocoder = new MapboxGeocoder({
    accessToken: mapboxgl.accessToken,
    mapboxgl: mapboxgl,
    marker: false,
    language: 'cs',
    placeholder: 'Enter your address'
});

// Add geocoder to the address field
document.getElementById('geocoder').appendChild(geocoder.onAdd(map));
document.querySelector('.mapboxgl-ctrl-geocoder input').classList.add('form-control');

// Listen for result event on geocoder
geocoder.on('result', function (event) {
    // Get selected address
    var selectedAddress = event.result.place_name;

    // Set selected address in input field
    document.getElementById('geocoder').value = selectedAddress;

    // Get latitude and longitude of selected address
    var lngLat = event.result.center;

    // Set latitude and longitude values in hidden input fields
    document.getElementById('latitude').value = lngLat[1];
    document.getElementById('longitude').value = lngLat[0];
});

// Hide coordinates field by default
document.getElementById('coordinates_field').style.display = 'none';

// Listen for checkbox change event
document.getElementById('use_coordinates').addEventListener('change', function () {
    // If checkbox is checked, show coordinates field
    if (this.checked) {
        document.getElementById('address_field').style.display = 'none';
        document.getElementById('coordinates_field').style.display = 'block';
    } else { // Otherwise, hide coordinates field
        document.getElementById('coordinates_field').style.display = 'none';
        document.getElementById('address_field').style.display = 'block';
    }
});

document.addEventListener("DOMContentLoaded", function () {
    var form = document.querySelector("#device-form");
    form.addEventListener("keydown", function (event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            return false;
        }
    });
});
