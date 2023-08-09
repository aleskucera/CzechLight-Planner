function drawClusteredNodes(map, nodeData) {
    const sourceId = 'node-circles-source';
    const layerIdClusters = 'clusters';
    const layerIdClusterCount = 'cluster-count';
    const layerIdUnclusteredPoint = 'unclustered-point';
    const coordinates = nodeData.map((node) => [node.longitude, node.latitude]);

    // Remove the existing layers if they exist
    if (map.getLayer(layerIdClusters)) {
        map.removeLayer(layerIdClusters);
    }

    if (map.getLayer(layerIdClusterCount)) {
        map.removeLayer(layerIdClusterCount);
    }

    if (map.getLayer(layerIdUnclusteredPoint)) {
        map.removeLayer(layerIdUnclusteredPoint);
    }

    if (map.getSource(sourceId)) {
        map.removeSource(sourceId);
    }

    // Add a new source for the devices' points
    map.addSource(sourceId, {
        type: 'geojson',
        data: {
            type: 'FeatureCollection',
            features: coordinates.map((coords) => ({
                type: 'Feature',
                geometry: {
                    type: 'Point',
                    coordinates: coords,
                },
            })),
        },
        cluster: true,
        clusterMaxZoom: 14,
        clusterRadius: 50,
    });

    map.addLayer({
        id: layerIdClusters,
        type: 'circle',
        source: sourceId,
        filter: ['has', 'point_count'],
        paint: {
            'circle-color': [
                'step',
                ['get', 'point_count'],
                '#51bbd6',
                100,
                '#f1f075',
                750,
                '#f28cb1',
            ],
            'circle-radius': [
                'step',
                ['get', 'point_count'],
                20,
                100,
                30,
                750,
                40,
            ],
        },
    });

    map.addLayer({
        id: layerIdClusterCount,
        type: 'symbol',
        source: sourceId,
        filter: ['has', 'point_count'],
        layout: {
            'text-field': ['get', 'point_count_abbreviated'],
            'text-font': ['DIN Offc Pro Medium', 'Arial Unicode MS Bold'],
            'text-size': 12,
        },
    });

    map.addLayer({
        id: layerIdUnclusteredPoint,
        type: 'circle',
        source: sourceId,
        filter: ['!', ['has', 'point_count']],
        paint: {
            'circle-color': '#11b4da',
            'circle-radius': 4,
            'circle-stroke-width': 1,
            'circle-stroke-color': '#fff',
        },
    });
}

function drawLinks(map, linkData, color = '#000000', lineWidth = 2) {
    const sourceId = 'device-lines-source';
    const layerIdDLines = 'device-lines';

    const lineFeatures = [];
    for (const link of linkData) {
        lineFeatures.push({
            type: 'Feature',
            geometry: {
                type: 'LineString',
                coordinates: [link['source_coords'], link['target_coords']],
            },
            properties: {
                selected: link['selected'],
            }
        });
    }

    if (map.getLayer(layerIdDLines)) {
        map.removeLayer(layerIdDLines);
    }

    if (map.getSource(sourceId)) {
        map.removeSource(sourceId);
    }

    map.addSource(sourceId, {
        type: 'geojson',
        data: {
            type: 'FeatureCollection',
            features: lineFeatures,
        },
    });

    map.addLayer({
        id: layerIdDLines,
        type: 'line',
        source: sourceId,
        paint: {
            'line-color': [
                'case',
                ['boolean', ['get', 'selected'], false],
                '#00FF00', // Green color for selected links
                color, // Default color for non-selected links
            ],
            'line-width': lineWidth, // Adjust the width of the lines as needed
        },
    });
}