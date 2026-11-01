import numpy as np, cv2, json, math
from pyproj import Transformer
cv2.setNumThreads(4)
C={'a1884':[(706,1072),(6932,1077),(706,6820),(6932,6821)],
   'a1930':[(331,930),(6512,943),(316,6746),(6505,6756)],
   'a1943':[(557,867),(6803,890),(531,6754),(6783,6774)],
   'a1953':[(354,310),(5494,315),(345,5161),(5513,5167)]}
L0,L1,P0,P1=17.5,17+40/60,50.3,50.4
toW=Transformer.from_crs("EPSG:4314","EPSG:4326",always_xy=True)
toD=Transformer.from_crs("EPSG:4326","EPSG:4314",always_xy=True)
R=6378137.0
merc=lambda lon,lat:(math.radians(lon)*R, math.log(math.tan(math.pi/4+math.radians(lat)/2))*R)
# WGS corners of DHDN frame
cw=[toW.transform(lo,la) for lo,la in [(L0,P1),(L1,P1),(L0,P0),(L1,P0)]]
west=max(cw[0][0],cw[2][0]); east=min(cw[1][0],cw[3][0]); north=min(cw[0][1],cw[1][1]); south=max(cw[2][1],cw[3][1])
x0,y1=merc(west,north); x1,y0=merc(east,south)
W=4800; H=int(round(W*(y1-y0)/(x1-x0)))
xs=x0+(np.arange(W)+0.5)*(x1-x0)/W; ys=y1-(np.arange(H)+0.5)*(y1-y0)/H
lon=np.degrees(xs/R); lat=np.degrees(2*np.arctan(np.exp(ys/R))-np.pi/2)
LON,LAT=np.meshgrid(lon,lat)
dlon,dlat=toD.transform(LON.ravel(),LAT.ravel()); dlon=dlon.reshape(LON.shape); dlat=dlat.reshape(LON.shape)
s=(dlon-L0)/(L1-L0); t=(P1-dlat)/(P1-P0)
meta={'bounds':[[south,west],[north,east]],'w':W,'h':H}
for n,c in C.items():
    c=np.array(c,float)
    px=(1-s)*(1-t)*c[0,0]+s*(1-t)*c[1,0]+(1-s)*t*c[2,0]+s*t*c[3,0]
    py=(1-s)*(1-t)*c[0,1]+s*(1-t)*c[1,1]+(1-s)*t*c[2,1]+s*t*c[3,1]
    im=cv2.imread(n+'.jpg')
    # prefilter to avoid aliasing (~1.3x downsample)
    im=cv2.GaussianBlur(im,(0,0),0.6)
    out=cv2.remap(im,px.astype(np.float32),py.astype(np.float32),cv2.INTER_AREA if False else cv2.INTER_LINEAR,borderValue=(245,245,245))
    cv2.imwrite(f'../arkusz{n[1:]}.jpg',out,[cv2.IMWRITE_JPEG_QUALITY,80,cv2.IMWRITE_JPEG_PROGRESSIVE,1])
    print(n,'ok')
json.dump(meta,open('meta.json','w')); print(meta)
