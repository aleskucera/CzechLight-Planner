// function createTabContent(pathNumber, pathContent, isActive = false) {
//     const tabContent = document.createElement("div");
//     tabContent.classList.add("tab-pane", "fade");
//     tabContent.setAttribute("id", `path-${pathNumber}`);
//     tabContent.setAttribute("role", "tabpanel");
//     tabContent.setAttribute("aria-labelledby", `path-${pathNumber}-tab`);
//     if (isActive) {
//         tabContent.classList.add("show", "active");
//     }
//     // Create elements for the graph and map
//     const graphElement = document.createElement("svg");
//     graphElement.setAttribute("id", `graph-${pathNumber}`);
//     graphElement.setAttribute("width", "100%");
//     graphElement.setAttribute("height", "500");
//     const mapElement = document.createElement("div");
//     mapElement.setAttribute("id", `map-${pathNumber}`);
//     mapElement.style.width = "100%";
//     mapElement.style.height = "500px";
//
//     // Append the graph and map elements to the tab content
//     tabContent.appendChild(graphElement);
//     tabContent.appendChild(mapElement);
//
//     // Set the initial content for the tab
//     tabContent.innerHTML += `<p class="mb-0">${pathContent}</p>`;
//
//     return tabContent;
// }

function createTab(pathNumber, isActive = false) {
    const tab = document.createElement("li");
    tab.classList.add("nav-item");
    const tabLink = document.createElement("a");
    tabLink.classList.add("nav-link");
    if (isActive) {
        tabLink.classList.add("active");
    }
    tabLink.setAttribute("id", `path-${pathNumber}-tab`);
    tabLink.setAttribute("data-toggle", "tab");
    tabLink.setAttribute("href", `#path-${pathNumber}`);
    tabLink.setAttribute("role", "tab");
    tabLink.setAttribute("aria-controls", `path-${pathNumber}`);
    tabLink.setAttribute("aria-selected", isActive ? "true" : "false");
    tabLink.textContent = `Path ${pathNumber}`;
    tab.appendChild(tabLink);
    return tab;
}

function createTabContent(pathNumber, isActive = false) {
    const tabContent = document.createElement("div");
    tabContent.classList.add("tab-pane", "fade");
    tabContent.setAttribute("id", `path-${pathNumber}`);
    tabContent.setAttribute("role", "tabpanel");
    tabContent.setAttribute("aria-labelledby", `path-${pathNumber}-tab`);
    if (isActive) {
        tabContent.classList.add("show", "active");
    }

    // Create elements for the graph
    const graphElement = document.createElementNS('http://www.w3.org/2000/svg', 'svg')
    graphElement.setAttribute("id", `graph-${pathNumber}`);
    graphElement.setAttribute("width", "100%");
    graphElement.setAttribute("height", "500");

    // Append the graph element to the tab content
    tabContent.appendChild(graphElement);

    return tabContent;
}

function updateTabsAndContent(paths) {
    const tabContainer = document.getElementById("myTab");
    const tabContentContainer = document.getElementById("myTabContent");
    tabContainer.innerHTML = "";
    tabContentContainer.innerHTML = "";

    const width = tabContentContainer.clientWidth;
    const height = 500;

    for (const pathNumber in paths) {
        if (paths.hasOwnProperty(pathNumber)) {
            const isActive = pathNumber === '1'; // Set the first path as active by default
            const tabContent = createTabContent(pathNumber, isActive);
            const tab = createTab(pathNumber, isActive);
            tabContainer.appendChild(tab);
            tabContentContainer.appendChild(tabContent);

            // Create separate graphs for each path
            const graphData = paths[pathNumber]['graph_data'];

            // Update the graph for the current path and store the simulation
            const graphElement = document.getElementById(`graph-${pathNumber}`);
            createSimulation(graphData, graphElement, [width, height]);
        }
    }
}

function updateGraph(graphData, graphElement, [width, height] = [400, 300]) {
    // Clear the existing graph, if any
    d3.select(graphElement).selectAll("*").remove();

    // Create a new simulation for the current graph
    const simulation = graphSimulation(graphData, [width, height]);

    // Create SVG elements for the current graph
    const {svg, link, node, nodeText} = svgElements(graphData, graphElement);

    // Set up tick event for the simulation
    simulation.on("tick", () => {
        link
            .attr("x1", d => d.source.x)
            .attr("y1", d => d.source.y)
            .attr("x2", d => d.target.x)
            .attr("y2", d => d.target.y);

        node
            .attr("cx", d => d.x)
            .attr("cy", d => d.y);

        // Update the text position for node names
        nodeText
            .attr("x", d => d.x + 12) // Adjust the 'x' position as needed
            .attr("y", d => d.y + 5); // Adjust the 'y' position as needed
    });
}

function updateTabs2(graphData) {
    // Create elements for the graph
    const tabContent1 = document.getElementById("path-1");
    const graphElement1 = document.createElementNS('http://www.w3.org/2000/svg', 'svg')
    graphElement1.setAttribute("id", "graph-1");
    graphElement1.setAttribute("width", "100%");
    graphElement1.setAttribute("height", "500");

    // Append the graph element to the tab content
    tabContent1.appendChild(graphElement1);

    // const graphElement1 = document.getElementById("graph-1");
    const simulation1 = createSimulation(graphData, graphElement1);

    const graphElement2 = document.getElementById("graph-2");
    const simulation2 = createSimulation(graphData, graphElement2);
}

function createSimulation(graphData, graphElement, [width, height] = [400, 300]) {
    // Clear the existing graph, if any
    d3.select(graphElement).selectAll("*").remove();

    // Create a new simulation for the current graph
    const simulation = d3.forceSimulation(graphData.nodes)
        .force("link", d3.forceLink(graphData.links).id(d => d.id))
        .force("charge", d3.forceManyBody().strength(-50))
        .force("center", d3.forceCenter(width / 2, height / 2));


    // Create SVG elements for the current graph
    const svg = d3.select(graphElement);
    const link = svg.append("g")
        .selectAll("line")
        .data(graphData.links)
        .enter()
        .append("line")
        .style("stroke", "black");
    const node = svg.append("g")
        .selectAll("circle")
        .data(graphData.nodes)
        .enter()
        .append("circle")
        .attr("r", 10)
        .attr("fill", "blue")
        .attr("opacity", 0.8);
    const nodeText = svg.append("g")
        .selectAll("text")
        .data(graphData.nodes)
        .enter()
        .append("text")
        .attr("class", "node-text")
        .text(d => d.id);

    // Set up tick event for the simulation
    simulation.on("tick", () => {
        link
            .attr("x1", d => d.source.x)
            .attr("y1", d => d.source.y)
            .attr("x2", d => d.target.x)
            .attr("y2", d => d.target.y);

        node
            .attr("cx", d => d.x)
            .attr("cy", d => d.y);

        nodeText
            .attr("x", d => d.x + 12)
            .attr("y", d => d.y + 5);
    });

    return simulation;
}