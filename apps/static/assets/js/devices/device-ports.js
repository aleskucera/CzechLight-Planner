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


// $(document).ready(function () {
//     const selectedDeviceType = localStorage.getItem('selectedDeviceType');
//
//     console.log("selectedDeviceType:", selectedDeviceType);
//
//     // Make the placeholder option in the device type select disabled
//     $('#device-type option[value="placeholder"]').prop('disabled', true);
//
//     // Set the selected option based on the stored value or default to placeholder option
//     if (selectedDeviceType) {
//         console.log("Setting selectedDeviceType:", selectedDeviceType);
//         $('#device-type').val(selectedDeviceType);
//     } else {
//         console.log("Setting default option");
//         $('#device-type').val("placeholder");
//     }
//
//     // Function to show or hide connection containers based on the device type
//     function showHideConnections(deviceType) {
//         // Hide all connection containers
//         $('#line-conn-container, #intra-conn-container, #client-conn-container').hide();
//
//         // Show the relevant connection container based on the device type
//         if (deviceType === 'LineDegree') {
//             $('#line-conn-container').show();
//             $('#intra-conn-container').show();
//         } else if (deviceType === 'AddDrop') {
//             $('#intra-conn-container').show();
//             $('#client-conn-container').show();
//         } else if (deviceType === 'Client') {
//             $('#client-conn-container').show();
//         }
//     }
//
//     // Function to update the port options based on the selected device type
//     function updatePortOptions(deviceType) {
//         // Get the device ports for the selected device type
//         const ports = devicePorts[deviceType];
//
//         // Update the line port options
//         const linePortSelect = $('.line-port-number');
//         linePortSelect.empty();
//
//
//         if (ports.linePorts !== null) {
//
//             if (ports.linePorts === 1) {
//                 $('#one-line-conn').show();
//                 $('#multiple-line-conn').hide();
//                 $('#add-line-connection').hide();
//             } else {
//                 linePortSelect.append($('<option value="placeholder" disabled selected>Select Port Number</option>'));
//                 for (let i = 1; i <= ports.linePorts; i++) {
//                     linePortSelect.append($('<option></option>').val(i).text(i));
//                 }
//                 $('#one-line-conn').hide();
//                 $('#multiple-line-conn').show();
//                 $('#add-line-connection').show();
//             }
//         }
//
//         // Update the intra port options
//         const intraPortSelect = $('.intra-port-number');
//         intraPortSelect.empty();
//
//         if (ports.intraPorts !== null) {
//             if (ports.intraPorts === 1) {
//                 $('#one-intra-conn').show();
//                 $('#multiple-intra-conn').hide();
//                 $('#add-intra-connection').hide();
//             } else {
//                 intraPortSelect.append($('<option value="placeholder" disabled selected>Select Port Number</option>'));
//                 for (let i = 1; i <= ports.intraPorts; i++) {
//                     intraPortSelect.append($('<option></option>').val(i).text(i));
//                 }
//                 $('#one-intra-conn').hide();
//                 $('#multiple-intra-conn').show();
//                 $('#add-intra-connection').show();
//             }
//         }
//
//         // Update the client port options
//         const clientPortSelect = $('.client-port-number');
//         clientPortSelect.empty();
//
//         if (ports.clientPorts !== null) {
//             if (ports.clientPorts === 1) {
//                 $('#one-client-conn').show();
//                 $('#multiple-client-conn').hide();
//                 $('#add-client-connection').hide();
//             } else {
//                 clientPortSelect.append($('<option value="placeholder" disabled selected>Select Port Number</option>'));
//                 for (let i = 1; i <= ports.clientPorts; i++) {
//                     clientPortSelect.append($('<option></option>').val(i).text(i));
//                 }
//                 $('#one-client-conn').hide();
//                 $('#multiple-client-conn').show();
//                 $('#add-client-connection').show();
//             }
//         }
//     }
//
//     // Event listener for device type change
//     $('#device-type').on('change', function () {
//
//         // Make the placeholder option disabled
//
//         const deviceType = $(this).val();
//
//         // Call the functions to show/hide connection containers and update port options
//         showHideConnections(deviceType);
//         updatePortOptions(deviceType);
//     });
//
//     // Event listener for adding a line port
//     $('.add-line-conn').on('click', function () {
//         const lineConnContainer = $('#multiple-line-conn');
//
//         const linePortInput = $('<select class="form-control line-port-number" name="line-port[]"></select>');
//         const deviceNameInput = $('<input type="text" class="form-control device-name" name="line-device-name[]">');
//
//         // Populate line port options
//         const deviceType = $('#device-type').val();
//         const linePorts = devicePorts[deviceType]['linePorts'];
//         for (let i = 1; i <= linePorts; i++) {
//             linePortInput.append($('<option></option>').val(i).text(i));
//         }
//
//         lineConnContainer.append($('<div class="col-lg-4">').append($('<label class="line-port-label">Port Number:</label>')).append(linePortInput));
//         lineConnContainer.append($('<div class="col-lg-8">').append($('<label for="line-device-name[]">Connected Device:</label>')).append(deviceNameInput));
//
//     });
//
//     // Event listener for adding an intra port
//     $('.add-intra-conn').on('click', function () {
//         const intraConnContainer = $('#multiple-intra-conn');
//
//         const intraPortInput = $('<select class="form-control intra-port-number" name="intra-port"></select>');
//         const deviceNameInput = $('<input type="text" class="form-control device-name" name="intra-device-name">');
//
//         // Populate intra port options
//         const deviceType = $('#device-type').val();
//         const intraPorts = devicePorts[deviceType]['intraPorts'];
//         for (let i = 1; i <= intraPorts; i++) {
//             intraPortInput.append($('<option></option>').val(i).text(i));
//         }
//
//         intraConnContainer.append($('<div class="col-lg-4">').append($('<label class="intra-port-label">Port Number:</label>')).append(intraPortInput));
//         intraConnContainer.append($('<div class="col-lg-8">').append($('<label for="intra-device-name">Connected Device:</label>')).append(deviceNameInput));
//
//     });
//
//     // Event listener for adding a client port
//     $('.add-client-conn').on('click', function () {
//         const clientConnContainer = $('#multiple-client-conn');
//
//         const clientPortInput = $('<select class="form-control client-port-number" name="client-port"></select>');
//         const deviceNameInput = $('<input type="text" class="form-control device-name" name="client-device-name">');
//
//         // Populate client port options
//         const deviceType = $('#device-type').val();
//         const clientPorts = devicePorts[deviceType]['clientPorts'];
//         for (let i = 1; i <= clientPorts; i++) {
//             clientPortInput.append($('<option></option>').val(i).text(i));
//         }
//
//         clientConnContainer.append($('<div class="col-lg-4">').append($('<label class="client-port-label">Port Number:</label>')).append(clientPortInput));
//         clientConnContainer.append($('<div class="col-lg-8">').append($('<label for="client-device-name">Connected Device:</label>')).append(deviceNameInput));
//     });
// });
