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

    // Create a row for the graph and the map
    const row = document.createElement("div");
    row.classList.add("row");
    tabContent.appendChild(row);

    // Create a column for the graph
    const graphColumn = document.createElement("div");
    graphColumn.classList.add("col-md-6");
    graphColumn.setAttribute("id", `graph-${pathNumber}-column`);
    row.appendChild(graphColumn);

    // Create a column for the map
    const mapColumn = document.createElement("div");
    mapColumn.classList.add("col-md-6");
    mapColumn.setAttribute("id", `map-${pathNumber}-column`);
    row.appendChild(mapColumn);

    // Create elements for the graph
    const graphElement = document.createElementNS('http://www.w3.org/2000/svg', 'svg')
    graphElement.setAttribute("id", `graph-${pathNumber}`);
    graphElement.setAttribute("width", "100%");
    graphElement.setAttribute("height", "500");
    graphElement.setAttribute("class", "graph");
    graphColumn.appendChild(graphElement);

    // Create elements for the map
    const mapElement = document.createElement("div");
    mapElement.setAttribute("id", `map-${pathNumber}`);
    mapElement.setAttribute("style", "width: 100%; height: 500px;");
    mapElement.setAttribute("class", "map");
    mapColumn.appendChild(mapElement);

    // Add button for submitting the path
    const submitButton = document.createElement("button");
    submitButton.setAttribute("id", `submit-${pathNumber}`);
    submitButton.setAttribute("type", "button");
    submitButton.setAttribute("class", "btn btn-primary");
    submitButton.textContent = "Choose this path";
    tabContent.appendChild(submitButton);

    return tabContent;
}

function updateTabsAndContent(paths) {
    const tabContainer = document.getElementById("myTab");
    const tabContentContainer = document.getElementById("myTabContent");
    tabContainer.innerHTML = "";
    tabContentContainer.innerHTML = "";

    let width = 0;
    let height = 0;

    for (const pathNumber in paths) {
        if (paths.hasOwnProperty(pathNumber)) {
            const isActive = pathNumber === '1';
            const tab = createTab(pathNumber, isActive);
            const tabContent = createTabContent(pathNumber, isActive);

            tabContainer.appendChild(tab);
            tabContentContainer.appendChild(tabContent);

            // Create a graph for the current path
            const graphData = paths[pathNumber]['graph_data'];
            const graphElement = document.getElementById(`graph-${pathNumber}`);

            if (isActive) {
                width = document.getElementById(`graph-${pathNumber}-column`).clientWidth;
                height = document.getElementById(`graph-${pathNumber}-column`).clientHeight;
            }
            createGraph(graphData, graphElement, [width, height]);

            // Create a map for the current path
            const mapData = paths[pathNumber]['map_data'];
            const map = createMap(`map-${pathNumber}`, [15.251112431996722, 49.78450556341959], 6);

            map.on('load', () => {
                drawLinks(map, mapData['links'], '#6e6f73', 3);
                drawClusteredNodes(map, mapData['nodes']);
            });

            // Add event listener for the submit button
            const submitButton = document.getElementById(`submit-${pathNumber}`);
            submitButton.addEventListener("click", () => {
                console.log(`Path ${pathNumber} was chosen`);
                console.log(paths[pathNumber]);
            });
        }
    }
}
