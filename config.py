

import os

import tcod

from definitions import ROOT_DIR

# Screen size, in tiles
screen_width = 90
screen_height = 70

# Load the font, a 32 by 8 tile font with libtcod's old character layout.
path_to_tilesheet = os.path.join(ROOT_DIR, 'resources\\dejavu10x10_gs_tc.png')
tileset = tcod.tileset.load_tilesheet(path_to_tilesheet, 32, 8, tcod.tileset.CHARMAP_TCOD)

# Map size
max_rooms = 30
room_min_size = 7
room_max_size = 20
map_width = 80
map_height = 80

