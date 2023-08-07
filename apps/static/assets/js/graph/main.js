function graphSimulation(graphData, [width, height] = [400, 300]) {
    // Create a D3 force simulation
    const simulation = d3
        .forceSimulation(graphData.nodes)
        .force("link", d3.forceLink(graphData.links).id(d => d.id))
        .force("charge", d3.forceManyBody().strength(-100))
        .force("center", d3.forceCenter(width / 2, height / 2));

    // // Warm up the simulation to stabilize the positions
    // for (let i = 0; i < 100; i++) {
    //     simulation.tick();
    // }

    return simulation;
}

function svgElements(graphData, svgId) {
    // Create SVG element for the graph
    const svg = d3.select(svgId)
        .attr("width", "100%")
        .attr("height", 500);

    // Create SVG elements for links
    const link = svg.append("g")
        .selectAll("line")
        .data(graphData.links)
        .enter()
        .append("line")
        .attr("stroke", d => (d.selected ? "green" : getLinkColor(d.type)));

    // Create SVG elements for nodes
    const node = svg.append("g")
        .selectAll("circle")
        .data(graphData.nodes)
        .enter()
        .append("circle")
        .attr("r", 10)
        .attr("fill", d => getNodeColor(d.type))
        .attr("opacity", 0.8); // Set the opacity value here (e.g., 0.8 for 80% opacity)

    // Add text elements for node names with shadow effect
    const nodeText = svg.append("g")
        .selectAll("text")
        .data(graphData.nodes)
        .enter()
        .append("text")
        .text(d => d.id)
        .attr("class", "node-text"); // Apply a class for the node text elements

    // Apply D3.js drag behavior directly to nodes
    node.call(
        d3.drag()
            .on("start", dragStart)
            .on("drag", dragging)
            .on("end", dragEnd)
    );

    return {svg, link, node, nodeText};
}

function getChargeStrength(node) {
    // Adjust the charge strength based on node type
    switch (node.type) {
        case "line_degree":
            return -200; // Adjust the charge strength for line_degree nodes as needed
        case "add_drop":
            return -150; // Adjust the charge strength for add_drop nodes as needed
        case "termination_point":
            return -100; // Adjust the charge strength for termination_point nodes as needed
        default:
            return -100; // Default charge strength for unknown node types
    }
}

function getCollisionRadius(node) {
    // Adjust the collision radius based on node type
    switch (node.type) {
        case "line_degree":
            return 15; // Adjust the collision radius for line_degree nodes as needed
        case "add_drop":
            return 12; // Adjust the collision radius for add_drop nodes as needed
        case "termination_point":
            return 10; // Adjust the collision radius for termination_point nodes as needed
        default:
            return 10; // Default collision radius for unknown node types
    }
}


function getNodeColor(type) {
    switch (type) {
        case "line_degree":
            return "blue";
        case "add_drop":
            return "red";
        case "termination_point":
            return "green";
        default:
            return "gray";
    }
}

function getLinkColor(type) {
    switch (type) {
        case "line":
            return "black";
        case "intra":
            return "orange";
        case "client":
            return "purple";
        default:
            return "gray";
    }
}

// Function to get the link distance based on the link type
function getLinkDistance(linkType) {
    switch (linkType) {
        case "line":
            return 150; // Adjust the distance for line links as needed
        case "intra":
            return 25; // Adjust the distance for intra links as needed
        case "client":
            return 50; // Adjust the distance for client links as needed
        default:
            return 100; // Default distance for unknown link types
    }
}


// Show tooltip function
function showTooltip(event, d) {
    tooltip.transition()
        .duration(200)
        .style("opacity", 0.9);
    tooltip.html(d.id) // Show the node name in the tooltip
        .style("left", (event.pageX) + "px")
        .style("top", (event.pageY - 28) + "px");
}

// Hide tooltip function
function hideTooltip() {
    tooltip.transition()
        .duration(500)
        .style("opacity", 0);
}

// Functions for drag events
function dragStart(event, d) {
    if (!event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
}

function dragging(event, d) {
    d.fx = event.x;
    d.fy = event.y;
}

function dragEnd(event, d) {
    if (!event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
}

// Function to handle node click event
function onNodeClick(event, d) {
    // Perform actions when a node is clicked
    console.log("Node clicked:", d.id);
    // Add your custom logic here, for example, display more information or open a modal.
}