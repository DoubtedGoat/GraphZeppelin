import random;
import pprint;
import numpy as np;
np.set_printoptions(threshold=np.nan)
np.core.arrayprint._line_width=120

class Voronoi:
    def test(self, width, height, nRegions):
        grid = self.emptyGrid(width, height);
        points = self.makePoints(grid, nRegions);
        grid = self.voronoiDemarcation(grid, points);
        for index in range(len(points)):
            point = points[index];
            grid[point[0]][point[1]] = index + 1;
        return grid;

    def emptyGrid(self, width, height):
        grid = [[-1 for y in range(width)] for x in range(height)];
        return grid;

    def makePoints(self, grid, nPoints):
        yMax = len(grid[0]);
        xMax = len(grid);
        points = [];
        for pointNum in range(nPoints):
            yVal = random.choice(range(yMax));
            xVal = random.choice(range(xMax));
            points.append([xVal, yVal]);
        return points;

    def voronoiDemarcation(self, grid, points):
        yMax = len(grid[0]);
        xMax = len(grid);
        for y in range(yMax):
            for x in range(xMax):
                distances = list(map(lambda curPoint: self.manhattanDistance([x,y], curPoint), points));
                region = np.argmin(distances) + 1;
                grid[x][y] = region;
        return grid;

    def manhattanDistance(self, pointA, pointB):
        return abs(pointA[0] - pointB[0]) + abs(pointA[1] - pointB[1]);
