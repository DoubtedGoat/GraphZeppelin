class TileType:
    posLookup = {"UpperLeft":0,
                  "Upper":1,
                  "UpperRight":2,
                  "Left":3,
                  "Center":4,
                  "Right":5,
                  "LowerLeft":6,
                  "Lower":7,
                  "LowerRight":8,
                  "InnerUpperLeft":9,
                  "InnerUpperRigh":10,
                  "InnerLowerLeft":11,
                  "InnerLowerRight":12};

    def __init__(self, tileset, tilenums):
        tiles = list(map(lambda x: tileset[x], tilenums))
        self.tiles = tiles;

    def TileAt(self, pos):
        tile = self.tiles[pos];
        return tile;
