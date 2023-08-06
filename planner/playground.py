def remove_duplicate_links(links):
    unique_links = {}
    for link in links:
        src, dst = sorted([link['source'], link['target']])
        key = (src, dst)
        if key not in unique_links:
            unique_links[key] = {
                'source': src,
                'target': dst,
                'source_coords': link['source_coords'],
                'target_coords': link['target_coords'],
                'type': link['type']
            }

    return list(unique_links.values())


# Example usage
original_list = [
    {
        'source': 'Device1',
        'target': 'Device2',
        'source_coords': [34.123, -118.456],
        'target_coords': [34.567, -118.789],
        'type': 'link_type_1'
    },
    {
        'source': 'Device2',
        'target': 'Device1',
        'source_coords': [34.567, -118.789],
        'target_coords': [34.123, -118.456],
        'type': 'link_type_1'
    },
    {
        'source': 'Device3',
        'target': 'Device4',
        'source_coords': [40.123, -73.456],
        'target_coords': [40.567, -73.789],
        'type': 'link_type_2'
    },
    {
        'source': 'Device4',
        'target': 'Device3',
        'source_coords': [40.567, -73.789],
        'target_coords': [40.123, -73.456],
        'type': 'link_type_2'
    },
]

unique_list = remove_duplicate_links(original_list)
print(unique_list)
