# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 16:55:36 2017

@author: Jay
"""

import tmxlib;
import MapDrawer;

map = tmxlib.Map.open('newmap.tmx');
layer = map.layers['Ground'];
tileset = map.tilesets['Desert'];
drawer = MapDrawer.Drawer();
tileType = MapDrawer.TileType(tileset, [0,1,2,8,9,10,16,17,18])
drawer.draw_square(10, 10, 4, 8, layer, tileType)
map.save('generated.tmx');
