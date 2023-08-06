$(document).ready(function () {
    const selectedDeviceType = localStorage.getItem('selectedDeviceType');
    const $deviceType = $('#device-type'); // Assign the selected element to a variable

    // Function to disable the placeholder option in the device type select
    function disablePlaceholderOption() {
        $deviceType.find('option[value="placeholder"]').prop('disabled', true);
    }

    // Function to set the selected option based on the stored value or default to placeholder option
    function setSelectedDeviceType() {
        if (selectedDeviceType) {
            $deviceType.val(selectedDeviceType);
        } else {
            $deviceType.val("placeholder");
        }
    }

    // Function to show or hide connection containers based on the device type
    function showHideConnections(deviceType) {
        const $connectionContainers = $('.connection-container'); // Assign the selected elements to a variable
        $connectionContainers.hide();

        if (deviceType.includes('line')) {
            console.log('Showing line connection container');
            $('#line-conn-container').show();
            $('#intra-conn-container').show();
        } else if (deviceType.includes('add')) {
            console.log('Showing add/drop connection container');
            $('#intra-conn-container').show();
            $('#client-conn-container').show();
        } else if (deviceType.includes('client')) {
            console.log('Showing client connection container');
            $('#client-conn-container').show();
        } else {
            console.log('Device type not recognized');
        }
    }

    // Function to update the port options based on the selected device type
    function updatePortOptions(deviceType) {
        const ports = devicePorts[deviceType];
        const $portSelects = $('.port-select'); // Assign the selected elements to a variable
        $portSelects.empty();

        for (let portType in ports) {
            if (ports[portType] !== null) {
                const $portSelect = $(`.${portType}-port-number`);

                if (ports[portType] === 1) {
                    console.log(`Showing single ${portType} connection`);
                    $(`#one-${portType}-conn`).show();
                    $(`#multiple-${portType}-conn`).hide();
                    $(`#add-${portType}-connection`).hide();
                } else {
                    console.log(`Showing multiple ${portType} connections`);
                    $portSelect.append($('<option value="placeholder" disabled selected>Select Port Number</option>'));
                    for (let i = 1; i <= ports[portType]; i++) {
                        $portSelect.append($('<option></option>').val(i).text(i));
                    }
                    $(`#one-${portType}-conn`).hide();
                    $(`#multiple-${portType}-conn`).show();
                    $(`#add-${portType}-connection`).show();
                }
            }
        }
    }

    // Event listener for device type change
    $deviceType.on('change', function () {
        const deviceType = $(this).val();
        console.log('Selected device type:', deviceType);
        showHideConnections(deviceType);
        updatePortOptions(deviceType);
    });

    // Event listener for adding a connection
    $('.add-conn').on('click', function () {
        const $connContainer = $(this).closest('.connections-container').find('.multi-connection');
        const connType = $(this).data('conn-type');
        console.log('Adding', connType, 'connection');

        const portInput = $('<select class="form-control port-select" name="port"></select>');
        const deviceNameInput = $('<input type="text" class="form-control device-name" name="device-name">');

        const deviceType = $deviceType.val();
        const ports = devicePorts[deviceType][connType];

        portInput.append($('<option value="placeholder" disabled selected>Select Port Number</option>'));
        for (let i = 1; i <= ports; i++) {
            portInput.append($('<option></option>').val(i).text(i));
        }

        $connContainer.append($('<div class="col-lg-4">').append($('<label class="port-label">Port Number:</label>')).append(portInput));
        $connContainer.append($('<div class="col-lg-8">').append($('<label for="device-name">Connected Device:</label>')).append(deviceNameInput));
    });

    // Call the functions to disable the placeholder option and set the selected device type
    disablePlaceholderOption();
    setSelectedDeviceType();
});


