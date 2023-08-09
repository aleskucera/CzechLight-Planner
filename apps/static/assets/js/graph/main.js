function createGraph(graphData, graphElement, [width, height] = [400, 300]) {
    d3.select(graphElement).selectAll("*").remove();
    const simulation = graphSimulation(graphData, [width, height])
    const {link, node, nodeText} = svgElements(graphData, graphElement);

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
}

function graphSimulation(graphData, [width, height] = [400, 300]) {
    const simulation = d3.forceSimulation(graphData.nodes)
        .force("link", d3.forceLink(graphData.links).id(d => d.id))
        .force("charge", d3.forceManyBody().strength(-50))
        .force("center", d3.forceCenter(width / 2, height / 2));

    // Warm up the simulation to stabilize the positions
    for (let i = 0; i < 100; i++) {
        simulation.tick();
    }

    return simulation;
}

function svgElements(graphData, svgId) {
    const svg = d3.select(svgId);

    const link = svg.append("g")
        .selectAll("line")
        .data(graphData.links)
        .enter()
        .append("line")
        .attr("stroke-width", d => (d.selected ? 3.5 : 2))
        .attr("stroke", d => (d.selected ? "#1dd3b0" : getLinkColor(d.type)));

    const node = svg.append("g")
        .selectAll("circle")
        .data(graphData.nodes)
        .enter()
        .append("circle")
        .attr("r", 10)
        .attr("fill", d => getNodeColor(d.type))
        .attr("opacity", 0.9);

    const nodeText = svg.append("g")
        .selectAll("text")
        .data(graphData.nodes)
        .enter()
        .append("text")
        .text(d => d.id)
        .attr("class", "node-text");

    return {link, node, nodeText};
}

function getNodeColor(type) {
    switch (type) {
        case "line_degree":
            return "#27187e";
        case "add_drop":
            return "#758bfd";
        case "termination_point":
            return "#aeb8fe";
        default:
            return "gray";
    }
}

function getLinkColor(type) {
    switch (type) {
        case "line":
            return "#f7b538";
        case "intra":
            return "#c32f27";
        case "client":
            return "#780116";
        default:
            return "gray";
    }
}