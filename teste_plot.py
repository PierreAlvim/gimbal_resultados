import pyqtgraph as pg
import numpy as np


def find_ind(x: np.array, y: np.array, x0: float):
    # get indexes
    # best guess to linear time
    dx = (x[-1]-x[0])/x.size
    i0 = int((x0-x[0])/dx)

    # out of bounds
    if i0 >= y.size or i0 < 0:
        return 0

    while x[i0] < x0:
        i0 += 1
    #x[i0] > x_
    # x0 esta entre x[i0] e x_
    if x[i0]-x[i0-1] != 0:
        a = (x0 - x[i0 - 1])/(x[i0] - x[i0-1])
        return y[i0-1] + a * (y[i0] - y[i0-1])
    else:
        return y[i0-1]



app = pg.mkQApp("plotter")

x = np.linspace(-2*np.pi, 2*np.pi, 10)
y = np.sin(x)


# pg.setConfigOption('background', color=(15,15,15))
# pg.setConfigOption('foreground', 'k')
p = pg.mkPen(width=2, color=(200, 80, 80))
p2 = pg.mkPen(width=0.5, color=(128, 128, 128))
w = pg.GraphicsLayoutWidget(show=True)
pl = w.addPlot(row=0, col=0, title='sine')
label = pg.LabelItem(justify='left')
w.addItem(label, row=1, col=0)
# w.addItem(label)
pl.plot(x, y, name="teste", pen=p)
# p = pg.CurvePoint()


vLine = pg.InfiniteLine(angle=90, movable=True, pen=p2)
def update(line):
    x_1 = line.value()
    y_1 = find_ind(x, y, x_1)
    label.setText("x<sub>1</sub> = %.4f<br>y<sub>1</sub> = %.4f" % (x_1, y_1))
vLine.sigPositionChanged.connect(update)


pl.addItem(vLine, ignoreBounds=True)
w.show()

pg.exec()
