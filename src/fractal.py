import itertools
import numpy as np

def mandelbrot(xo: float|int = 2.47/2, yo: float|int = 0, res: int = 200, maxiter: int = 1000, zoom: int|float = 1) -> np.ndarray:
    """Return an array representation of the mandelbrot set fractal."""
    xrange = 2.47 / zoom
    yrange = 2.24 / zoom
    xmin = xo - xrange/2
    xmax = xo + xrange/2
    ymin = yo - yrange/2
    ymax = yo + yrange/2
    
    rx = int(2.47 * res)
    ry = int(2.24 * res)
    
    X = np.linspace(xmin, xmax, rx)
    Y = np.linspace(ymin, ymax, ry)
    image = np.empty((len(Y), len(X)))
    for (j,y), (i,x) in itertools.product(enumerate(Y), enumerate(X)):
        c = complex(x, y)
        z = 0
        iter = 0
        while iter < maxiter and (z*z.conjugate()).real < 4:
            z = z**2 + c
            iter += 1
        image[-(j-1),i] = iter
    return image