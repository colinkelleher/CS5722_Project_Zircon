

import os
from typing import Tuple

import tcod

from definitions import ROOT_DIR

# Screen size, in tiles
screen_width = 90
screen_height = 70

# Load the font, a 32 by 8 tile font with libtcod's old character layout.
path_to_tilesheet = os.path.join(ROOT_DIR, 'resources/dejavu10x10_gs_tc.png')
tileset = tcod.tileset.load_tilesheet(path_to_tilesheet, 32, 8, tcod.tileset.CHARMAP_TCOD)

# Map size
max_rooms = 30
room_min_size = 7
room_max_size = 20
map_width = 90
map_height = 60

# Colors
bg_color_player: Tuple = (0, 0, 0)
bg_color_floor: Tuple = (200, 200, 200)
bg_color_wall: Tuple = (100, 100, 100)
bg_color_item: Tuple = (200, 200, 200)

fg_color_player: Tuple = (255, 255, 255)
fg_color_floor: Tuple = (0, 0, 0)
fg_color_wall: Tuple = (0, 0, 0)
fg_color_item: Tuple = (20, 148, 20)
fg_color_item_damaged: Tuple = (255, 0, 0)

