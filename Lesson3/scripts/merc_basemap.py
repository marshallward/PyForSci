from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
m = Basemap(projection='merc',llcrnrlat=-80,
            urcrnrlat=80, llcrnrlon=-180,
            urcrnrlon=180,lat_ts=20,
            resolution='c')
m.drawcoastlines()
m.fillcontinents(color='coral',
                 lake_color='aqua')
m.drawparallels(np.arange(-90.,91.,30.))
m.drawmeridians(np.arange(-180.,181.,60.))
m.drawmapboundary(fill_color='aqua')
plt.show()
