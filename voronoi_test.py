import Voronoi;
import numpy as np;
from PIL import Image;
from PIL import ImageColor;

#https://gist.github.com/ollieglass/f6ddd781eeae1d24e391265432297538
colormap = ['#FF6EC7',
            '#F2F3F4',
            '#222222',
            '#F3C300',
            '#875692',
            '#F38400',
            '#A1CAF1',
            '#BE0032',
            '#C2B280',
            '#848482',
            '#008856',
            '#E68FAC',
            '#0067A5',
            '#F99379',
            '#604E97',
            '#F6A600',
            '#B3446C',
            '#DCD300',
            '#882D17',
            '#8DB600',
            '#654522',
            '#E25822',
            '#2B3D26'];

vor = Voronoi.Voronoi();
width = 1000;
height = 1000;
nPoints = 22;
grid = vor.test(width, height, nPoints);

rgb = np.uint8(np.array([[ImageColor.getrgb(colormap[index]) for index in row] for row in grid]));
img = Image.fromarray(rgb);
img.save('voronoi.png');
