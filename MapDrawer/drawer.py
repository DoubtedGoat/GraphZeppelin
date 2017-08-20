class Drawer:
    def __init__(self):
        return

    def draw_square(self, x_start, y_start, x_length, y_length, layer, tileType):
        def coord(start, length, val):
            if (val - start == 0):
                pos = 0;
            elif (val - start == (length-1)):
                pos = 2;
            else:
                pos = 1;
            return pos;

        for x in range(x_start, x_start + x_length):
            for y in range(y_start, y_start + y_length):
                layer[x,y] = tileType.TileAt(coord(x_start, x_length, x) + (coord(y_start, y_length, y)*3))
