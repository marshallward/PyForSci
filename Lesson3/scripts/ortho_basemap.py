from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

m = Basemap(projection='ortho',lon_0=-105,
            lat_0=40,resolution='l')
m.drawcoastlines()
m.fillcontinents(color='coral',
                 lake_color='aqua')
m.drawparallels(np.arange(-90.,120.,30.))
m.drawmeridians(np.arange(0.,420.,60.))
m.drawmapboundary(fill_color='aqua')
plt.show()
