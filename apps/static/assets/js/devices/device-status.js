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
