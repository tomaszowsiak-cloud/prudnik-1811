import json, zipfile, numpy as np, os, sys
OUT=sys.argv[1] if len(sys.argv)>1 else '..'
os.makedirs(OUT,exist_ok=True)
LAT0,LON0=50.3215,17.5806; KY=111250; KX=111320*np.cos(np.radians(LAT0))
d11=json.load(open('../dane/plan1811.json')); d90=json.load(open('../dane/plan1890.json')); d08=json.load(open('../dane/plan1908.json')); d13=json.load(open('../dane/plan1913.json'))
plans=[
 dict(id="1811",img="plan1811.jpg",src_file='../plan1811.jpg',w=4476,h=3304,head="Plan von der Stadt Neustadt, 1811",
  meta="Pomiar: maj–sierpień 1811, konduktor Scheuerwasser młodszy; kopia: marzec 1835 (kopista Treeger lub Freeger). Podziałka: 150 prętów reńskich ≈ 565 m.",
  source="Archiwum Państwowe w Opolu, zespół Rejencja Opolska (nr 1191), seria Mapy i plany IX, sygn. 81.",
  scaleNote="Skala z podziałki planu: ok. 0,75 m/piksel. Zgodność z dopasowaniem świadczy, że punkty są dobrze rozpoznane.",
  points=d11['points'],labels=d11['labels']),
 dict(id="1890",img="plan1890.jpg",src_file='../plan1890.jpg',w=4000,h=3450,head="Plan von Neustadt in Ober-Schlesien, 1890",
  meta="Rysował geometra Weymann, 1890. Skala 1:8000, podziałka w metrach.",
  source="Polona (Biblioteka Narodowa), polona.pl/item-view/9b189dde-cd14-41d8-885f-6ac1b62f0c5c",
  scaleNote="Skala z podziałki planu (1:8000): ok. 0,91 m/piksel. Różnica rzędu 2% wynika najpewniej z kurczenia się papieru.",
  points=d90['points'],labels=d90['labels']),
 dict(id="1908",img="plan1908.jpg",src_file='../plan1908.jpg',w=1839,h=1846,head="Neustadt O/S, 1908",
  meta="Plan turystyczny z przewodnika wydawnictwa Woerl's Reisebücherverlag (Lipsk). Bez podziałki; plan uproszczony, ale z dokładnie rozmieszczonymi obiektami.",
  source="Polona (Biblioteka Narodowa), polona.pl/item-view/52c71138-9151-42d5-ab13-cb1dde0e522a",
  scaleNote="Plan nie ma podziałki. Skala z dopasowania: ok. 1,30 m/piksel.",
  points=d08['points'],labels=d08['labels']),
 dict(id="1913",img="plan1913.jpg",src_file='../plan1913.jpg',w=2576,h=2434,head="Plan von Neustadt in Oberschlesien, 1913",
  meta="Plan Miejskiego Urzędu Budowlanego (Stadtbauamt), podpisany przez miejskiego budowniczego, Prudnik, 3 grudnia 1913. Skala oryginału 1:2500. Na planie zaznaczono działki (kolorem czerwonym i zielonym) oraz oczyszczalnię ścieków.",
  source="do uzupełnienia",
  scaleNote="Skala oryginału 1:2500; skan jest pomniejszony. Skala z dopasowania: ok. 0,79 m/piksel.",
  points=d13['points'],labels=d13['labels'])]
data={"plans":[{k:v for k,v in p.items() if k!='src_file'} for p in plans],"water":d11['water']}
html=open('template.html').read().replace('__DATA__',json.dumps(data,ensure_ascii=False))
open(f'{OUT}/index.html','w').write(html)
def fitp(P):
    R=[];r=[]
    for p in P: R+=[[p['u'],p['v'],1,0],[-p['v'],p['u'],0,1]]; r+=[(p['lon']-LON0)*KX,(p['lat']-LAT0)*KY]
    a,b,tx,ty=np.linalg.lstsq(np.array(R),np.array(r),rcond=None)[0]
    c=np.array([a,b,tx]); d=np.array([b,-a,ty])
    res=[np.hypot(c@[p['u'],p['v'],1]-(p['lon']-LON0)*KX, d@[p['u'],p['v'],1]-(p['lat']-LAT0)*KY) for p in P]
    return (lambda u,v:(LAT0+(d@[u,v,1])/KY, LON0+(c@[u,v,1])/KX)), res, np.hypot(a,b)
crs='#CRS: GEOGCRS["WGS 84",DATUM["World Geodetic System 1984",ELLIPSOID["WGS 84",6378137,298.257223563]],CS[ellipsoidal,2],AXIS["latitude",north],AXIS["longitude",east],ANGLEUNIT["degree",0.0174532925199433],ID["EPSG",4326]]'
kml='<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2"><Document><name>Dawne plany Prudnika</name>'
F={}
for p in plans:
    f,res,s=fitp(p['points']); F[p['id']]=f
    print(p['id'],'RMS %.1f m'%np.sqrt(np.mean(np.square(res))),'skala %.3f m/px'%s,[round(x,1) for x in res])
    W,H=p['w'],p['h']
    q=[f(0,H),f(W,H),f(W,0),f(0,0)]
    kml+=f'<Folder><name>Plan {p["id"]}</name><GroundOverlay><name>{p["head"]}</name><visibility>{1 if p["id"]=="1811" else 0}</visibility><color>b3ffffff</color><Icon><href>{p["img"]}</href></Icon><gx:LatLonQuad><coordinates>'+' '.join(f'{lo:.7f},{la:.7f},0' for la,lo in q)+'</coordinates></gx:LatLonQuad></GroundOverlay>'
    for l in p['labels']:
        if 'u' in l: la,lo=f(l['u'],l['v']); kml+=f'<Placemark><name>{p["id"]} · {l["n"]}. {l["pl"]}</name><Point><coordinates>{lo:.7f},{la:.7f},0</coordinates></Point></Placemark>'
    kml+='</Folder>'
    open(f'{OUT}/{p["img"]}.points','w').write(crs+'\nmapX,mapY,sourceX,sourceY,enable,dX,dY,residual\n'+''.join(f"{q['lon']},{q['lat']},{q['u']},{-q['v']},1,0,0,0\n" for q in p['points']))
    os.system(f'cp {p["src_file"]} {OUT}/{p["img"]}')
f=F['1811']; Wt=d11['water']
kml+='<Style id="rura"><LineStyle><color>ffc44f0b</color><width>4</width></LineStyle></Style><Folder><name>Wodociąg 1811</name>'
for r in Wt['rury']:
    kml+='<Placemark><name>%s</name><styleUrl>#rura</styleUrl><LineString><coordinates>%s</coordinates></LineString></Placemark>'%(r['pl'],' '.join('%.7f,%.7f,0'%(f(u,v)[1],f(u,v)[0]) for u,v in r['pts']))
for z in Wt['zdroje']+[Wt['czerpadlo'],Wt['wieza']]:
    la,lo=f(z['u'],z['v']); kml+='<Placemark><name>%s</name><Point><coordinates>%.7f,%.7f,0</coordinates></Point></Placemark>'%(z['pl'],lo,la)
kml+='</Folder></Document></kml>'
with zipfile.ZipFile(f'{OUT}/prudnik-plany.kmz','w',zipfile.ZIP_DEFLATED) as z:
    z.writestr('doc.kml',kml)
    for p in plans: z.write(p['src_file'],p['img'])
w=[l for l in d90['labels'] if l['n']==27][0]; la,lo=F['1890'](w['u'],w['v'])
print('Wasserhebewerk 1890:',round(la,5),round(lo,5)); c=Wt['czerpadlo']; la2,lo2=f(c['u'],c['v'])
print('czerpadlo 1811:',round(la2,5),round(lo2,5),'odl. m',round(np.hypot((lo-lo2)*KX,(la-la2)*KY)))
