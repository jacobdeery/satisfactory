recipes = {
    'supercomputer': {
        'building': 'manufacturer',
        'rate': 1.875,
        'inputs': {
            'computer': 2,
            'ai_limiter': 3.75,
            'high_speed_connector': 5.625,
            'plastic': 52.5
        }
    },
    'computer': {
        'building': 'manufacturer',
        'rate': 2.5,
        'inputs': {
            'circuit_board': 25,
            'cable': 22.5,
            'plastic': 45,
            'screw': 130
        }
    },
    'high_speed_connector': {
        'building': 'manufacturer',
        'rate': 3.75,
        'inputs': {
            'quickwire': 210,
            'cable': 37.5,
            'circuit_board': 3.75
        }
    },
    'ai_limiter': {
        'building': 'assembler',
        'rate': 5,
        'inputs': {
            'copper_sheet': 25,
            'quickwire': 100
        }
    },
    'circuit_board': {
        'building': 'assembler',
        'rate': 7.5,
        'inputs': {
            'copper_sheet': 15,
            'plastic': 4
        }
    },
    'copper_sheet': {
        'building': 'constructor',
        'rate': 10,
        'inputs': {
            'copper_ingot': 20
        }
    },
    'copper_ingot': {
        'building': 'refinery',
        'rate': 37.5,
        'inputs': {
            'copper_ore': 15,
            'water': 10
        }
    },
    'cable': {
        'building': 'constructor',
        'rate': 30,
        'inputs': {
            'wire': 60
        }
    },
    'wire': {
        'building': 'constructor',
        'rate': 30,
        'inputs': {
            'copper_ingot': 15
        }
    },
    'quickwire': {
        'building': 'constructor',
        'rate': 60,
        'inputs': {
            'caterium_ingot': 12
        }
    },
    'caterium_ingot': {
        'building': 'smelter',
        'rate': 15,
        'inputs': {
            'caterium_ore': 45
        }
    }
}
