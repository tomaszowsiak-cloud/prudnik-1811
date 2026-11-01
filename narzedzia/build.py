import json, base64, zipfile, numpy as np
D=json.load(open('data.json')); W,H=2238,1652
LAT0,LON0=50.3215,17.5806; KY=111250; KX=111320*np.cos(np.radians(LAT0))
img=open('../plan1811.jpg','rb').read()
html=open('template.html').read().replace('__IMG__','data:image/jpeg;base64,'+base64.b64encode(img).decode()).replace('__W__',str(W)).replace('__H__',str(H)).replace('__DATA__',json.dumps(D,ensure_ascii=False))
open('../prudnik-1811-nakladka.html','w').write(html)
# affine fit
P=D['points']; A=np.array([[p['u'],p['v'],1] for p in P],float)
E=np.array([(p['lon']-LON0)*KX for p in P]); N=np.array([(p['lat']-LAT0)*KY for p in P])
R=[];r=[]
for (u,v,_),e,n in zip(A,E,N): R+= [[u,v,1,0],[-v,u,0,1]]; r+=[e,n]
a,bb,tx,ty=np.linalg.lstsq(np.array(R),np.array(r),rcond=None)[0]
c=np.array([a,bb,tx]); d=np.array([bb,-a,ty])
res=np.hypot(A@c-E,A@d-N)
for p,r in zip(P,res): print(f"{p['name']:40s} {r:5.1f} m")
print('RMS',np.sqrt((res**2).mean()).round(1),'skala',np.hypot(c[0],d[0]).round(3),np.hypot(c[1],d[1]).round(3),'azymut gory',np.degrees(np.arctan2(-c[1],-d[1])).round(1))
f=lambda u,v:(LAT0+(d@[u,v,1])/KY, LON0+(c@[u,v,1])/KX)
# KML LatLonQuad: corners counter-clockwise starting lower-left
corners=[f(0,H),f(W,H),f(W,0),f(0,0)]
coords=' '.join(f'{lo:.7f},{la:.7f},0' for la,lo in corners)
kml=f'''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2"><Document><name>Prudnik 1811</name>
<GroundOverlay><name>Plan miasta Prudnika (Neustadt) 1811</name><color>b3ffffff</color><Icon><href>plan1811.jpg</href></Icon>
<gx:LatLonQuad><coordinates>{coords}</coordinates></gx:LatLonQuad></GroundOverlay>
''' + ''.join(f'<Placemark><name>{p["name"]}</name><Point><coordinates>{p["lon"]},{p["lat"]},0</coordinates></Point></Placemark>\n' for p in P) + '</Document></kml>'
with zipfile.ZipFile('../prudnik-1811.kmz','w',zipfile.ZIP_DEFLATED) as z:
    z.writestr('doc.kml',kml); z.write('../plan1811.jpg','plan1811.jpg')
crs='#CRS: GEOGCRS["WGS 84",DATUM["World Geodetic System 1984",ELLIPSOID["WGS 84",6378137,298.257223563]],CS[ellipsoidal,2],AXIS["latitude",north],AXIS["longitude",east],ANGLEUNIT["degree",0.0174532925199433],ID["EPSG",4326]]'
open('../plan1811.jpg.points','w').write(crs+'\nmapX,mapY,sourceX,sourceY,enable,dX,dY,residual\n'+''.join(f"{p['lon']},{p['lat']},{p['u']},{-p['v']},1,0,0,0\n" for p in P))
# podgląd: plan po przekształceniu + punkty
from PIL import Image, ImageDraw
im=Image.open('../plan1811.jpg').convert('RGB'); dr=ImageDraw.Draw(im)
for p,cc in zip(P,zip(c,d)):
    pass
