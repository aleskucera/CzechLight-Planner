const devicePorts = {
    'lineDegree': {
        'linePorts': 1,
        'intraPorts': 10,
        'clientPorts': null
    },
    'addDrop': {
        'linePorts': null,
        'intraPorts': 10,
        'clientPorts': 10
    },
    'client': {
        'linePorts': null,
        'intraPorts': null,
        'clientPorts': 1
    }
};

$(document).ready(function () {
    const selectedDeviceType = localStorage.getItem('selectedDeviceType');

    // Set the selected option based on the stored value or default to placeholder option
    if (selectedDeviceType) {
        $('#device-type').val(selectedDeviceType);
    } else {
        $('#device-type').val("placeholder");
    }

    // Function to show or hide connection containers based on the device type
    function showHideConnections(deviceType) {
        // Hide all connection containers
        $('#line-conn-container, #intra-conn-container, #client-conn-container').hide();

        // Show the relevant connection container based on the device type
        if (deviceType === 'lineDegree') {
            $('#line-conn-container').show();
            $('#intra-conn-container').show();
        } else if (deviceType === 'addDrop') {
            $('#intra-conn-container').show();
            $('#client-conn-container').show();
        } else if (deviceType === 'client') {
            $('#client-conn-container').show();
        }
    }

    // Function to update the port options based on the selected device type
    function updatePortOptions(deviceType) {
        // Get the device ports for the selected device type
        const ports = devicePorts[deviceType];

        // Update the line port options
        const linePortSelect = $('.line-port-number');
        linePortSelect.empty();


        if (ports.linePorts !== null) {

            if (ports.linePorts === 1) {
                $('#one-line-conn').show();
                $('#multiple-line-conn').hide();
                $('#add-line-connection').hide();
            } else {
                linePortSelect.append($('<option value="placeholder" disabled selected>Select Port Number</option>'));
                for (let i = 1; i <= ports.linePorts; i++) {
                    linePortSelect.append($('<option></option>').val(i).text(i));
                }
                $('#one-line-conn').hide();
                $('#multiple-line-conn').show();
                $('#add-line-connection').show();
            }
        }

        // Update the intra port options
        const intraPortSelect = $('.intra-port-number');
        intraPortSelect.empty();

        if (ports.intraPorts !== null) {
            if (ports.intraPorts === 1) {
                $('#one-intra-conn').show();
                $('#multiple-intra-conn').hide();
                $('#add-intra-connection').hide();
            } else {
                intraPortSelect.append($('<option value="placeholder" disabled selected>Select Port Number</option>'));
                for (let i = 1; i <= ports.intraPorts; i++) {
                    intraPortSelect.append($('<option></option>').val(i).text(i));
                }
                $('#one-intra-conn').hide();
                $('#multiple-intra-conn').show();
                $('#add-intra-connection').show();
            }
        }

        // Update the client port options
        const clientPortSelect = $('.client-port-number');
        clientPortSelect.empty();

        if (ports.clientPorts !== null) {
            if (ports.clientPorts === 1) {
                $('#one-client-conn').show();
                $('#multiple-client-conn').hide();
                $('#add-client-connection').hide();
            } else {
                clientPortSelect.append($('<option value="placeholder" disabled selected>Select Port Number</option>'));
                for (let i = 1; i <= ports.clientPorts; i++) {
                    clientPortSelect.append($('<option></option>').val(i).text(i));
                }
                $('#one-client-conn').hide();
                $('#multiple-client-conn').show();
                $('#add-client-connection').show();
            }
        }
    }

    // Event listener for device type change
    $('#device-type').on('change', function () {
        const deviceType = $(this).val();

        // Call the functions to show/hide connection containers and update port options
        showHideConnections(deviceType);
        updatePortOptions(deviceType);
    });

    // Event listener for adding a line port
    $('.add-line-conn').on('click', function () {
        const lineConnContainer = $('#multiple-line-conn');

        const linePortInput = $('<select class="form-control line-port-number" name="line_port"></select>');
        const deviceNameInput = $('<input type="text" class="form-control device-name" name="device_name">');

        // Populate line port options
        const deviceType = $('#device-type').val();
        const linePorts = devicePorts[deviceType]['linePorts'];
        for (let i = 1; i <= linePorts; i++) {
            linePortInput.append($('<option></option>').val(i).text(i));
        }

        lineConnContainer.append($('<div class="col-lg-4">').append($('<label class="line-port-label">Port Number:</label>')).append(linePortInput));
        lineConnContainer.append($('<div class="col-lg-8">').append($('<label for="device_name">Connected Device:</label>')).append(deviceNameInput));

    });

    // Event listener for adding an intra port
    $('.add-intra-conn').on('click', function () {
        const intraConnContainer = $('#multiple-intra-conn');

        const intraPortInput = $('<select class="form-control intra-port-number" name="intra_port"></select>');
        const deviceNameInput = $('<input type="text" class="form-control device-name" name="device_name">');

        // Populate intra port options
        const deviceType = $('#device-type').val();
        const intraPorts = devicePorts[deviceType]['intraPorts'];
        for (let i = 1; i <= intraPorts; i++) {
            intraPortInput.append($('<option></option>').val(i).text(i));
        }

        intraConnContainer.append($('<div class="col-lg-4">').append($('<label class="intra-port-label">Port Number:</label>')).append(intraPortInput));
        intraConnContainer.append($('<div class="col-lg-8">').append($('<label for="device_name">Connected Device:</label>')).append(deviceNameInput));

    });

    // Event listener for adding a client port
    $('.add-client-conn').on('click', function () {
        const clientConnContainer = $('#multiple-client-conn');

        const clientPortInput = $('<select class="form-control client-port-number" name="client_port"></select>');
        const deviceNameInput = $('<input type="text" class="form-control device-name" name="device_name">');

        // Populate client port options
        const deviceType = $('#device-type').val();
        const clientPorts = devicePorts[deviceType]['clientPorts'];
        for (let i = 1; i <= clientPorts; i++) {
            clientPortInput.append($('<option></option>').val(i).text(i));
        }

        clientConnContainer.append($('<div class="col-lg-4">').append($('<label class="client-port-label">Port Number:</label>')).append(clientPortInput));
        clientConnContainer.append($('<div class="col-lg-8">').append($('<label for="device_name">Connected Device:</label>')).append(deviceNameInput));
    });
});
