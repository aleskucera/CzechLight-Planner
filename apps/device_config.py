device_types = [
    ('line_degree', 'Line Degree ROADM'),
    ('passive_add_drop', 'Passive Add/Drop ROADM'),
    ('coherent_add_drop', 'Coherent Add/Drop ROADM'),
    ('wss_add_drop', 'WSS-based Add/Drop ROADM'),
    ('alien_wavelength_add_drop', 'Alien Wavelength Add/Drop ROADM'),
    ('client', 'Client'),
]
# Add line, add, then add types
# client separately, automatically
# intra client manually
# separate devices and termination points
# find path, manage termination points

# termination point 1, termination point 2
# TD filtration destination

# Nodes. ROADM?

# subtype

# optical connection, (TP1, TP2), path, paths found, simulation result

# Node management
device_ports = {
    'line_degree': {
        'line': 1,
        'intra': 9,
        'client': None
    },
    'passive_add_drop': {
        'line': None,
        'intra': 8,
        'client': 8
    },
    'coherent_add_drop': {
        'line': None,
        'intra': 8,
        'client': 8
    },
    'wss_add_drop': {
        'line': None,
        'intra': 8,
        'client': 20
    },
    'alien_wavelength_add_drop': {
        'line': None,
        'intra': 8,
        'client': 20
    },
    'client': {
        'line': None,
        'intra': None,
        'client': 1
    }
}
