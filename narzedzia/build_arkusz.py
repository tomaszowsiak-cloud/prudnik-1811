import json, numpy as np, sys, os, shutil
OUT=sys.argv[1] if len(sys.argv)>1 else '..'
D11=sys.argv[2] if len(sys.argv)>2 else '../dane/plan1811.json'; DG=sys.argv[3] if len(sys.argv)>3 else '../dane/plangarnizon.json'; META=sys.argv[4] if len(sys.argv)>4 else '../dane/arkusz5671.json'
LAT0,LON0=50.3215,17.5806;KY=111250;KX=111320*np.cos(np.radians(LAT0))
def fitp(P):
    R=[];r=[]
    for p in P: R+=[[p['u'],p['v'],1,0],[-p['v'],p['u'],0,1]]; r+=[(p['lon']-LON0)*KX,(p['lat']-LAT0)*KY]
    a,b,tx,ty=np.linalg.lstsq(np.array(R),np.array(r),rcond=None)[0]
    return lambda u,v:[round(LAT0+(b*u-a*v+ty)/KY,6), round(LON0+(a*u+b*v+tx)/KX,6)]
d11=json.load(open(D11)); K59=json.load(open('../dane/kanal1959.json')); dg=json.load(open(DG)); meta=json.load(open(META))
f=fit=fitp(d11['points']); W=d11['water']
water={"lines":[{"pl":r['pl'],"pts":[f(u,v) for u,v in r['pts']]} for r in W['rury']],
       "points":[{"pl":z['pl'],"lat":f(z['u'],z['v'])[0],"lon":f(z['u'],z['v'])[1],"big":k!='z'} for k,z in [('c',W['czerpadlo']),('w',W['wieza'])]+[('z',z) for z in W['zdroje']]]}
plac=[{"pl":p['pl'],"opis":p['opis'],"pts":p['pts']} for p in dg['extra']['polys']]
TBD="do uzupełnienia"
sheets=[
 {"id":"1884","tag":"1884","label":"1884","img":"arkusz1884.jpg","meta":"Messtischblatt 3301 „Neustadt (in Oberschlesien)”. Pomiar Królewskiej Pruskiej Służby Topograficznej (Landes-Aufnahme) z 1883, wydanie 1884. Długości geograficzne od południka Ferro.","source":"Instytut Geografii Uniwersytetu Pedagogicznego w Krakowie, skan 400 dpi (Mapster, igrek.amzp.pl/details.php?id=16506)."},
 {"id":"1930","tag":"1930","label":"1930","img":"arkusz1930.jpg","meta":"Na stopce: „Herausgegeben von der Preußischen Landesaufnahme 1884 · Reichsamt für Landesaufnahme · Einzelne Nachträge 1930”, czyli wydanie z 1884 z pojedynczymi uzupełnieniami z 1930, bez nowego pomiaru. Do uzupełnień należą m.in. oczyszczalnia, stacja pomp i koszary.","source":"Egzemplarz z pieczęcią Technische Hochschule Danzig, Geographisches Seminar. Ten sam stan wydania mają w Mapsterze egzemplarze z Archiwum Map Zachodniej Polski (id 5272) i z Biblioteki Cyfrowej Uniwersytetu Wrocławskiego, sygn. 6541-III.C./3301, datowany przez bibliotekę „1935?” (id 11772860)."},
 {"id":"1943","tag":"1943","label":"1943","img":"arkusz1943.jpg","meta":"Topographische Karte 1:25 000, arkusz 5671 „Neustadt O.S.”, „Ausgabe 1943”, „Nur für den Dienstgebrauch”. Na stopce stan aktualizacji: pomiar 1883 (Borchmann), sprostowany przez Reichsamt für Landesaufnahme w 1937 (Wirth), nazwy według stanu z 1.04.1938, ostatnie uzupełnienia H.V.A. II 1939. To jedyne wydanie z prawdziwą rewizją treści.","source":"Wydział Geografii i Studiów Regionalnych Uniwersytetu Warszawskiego (Mapster, igrek.amzp.pl/details.php?id=11780596)."},
 {"id":"1959","tag":"1959 (kanalizacja)","label":"1959 – plan sieci kanalizacyjnej","img":"kanal1959.jpg","bounds":K59['bounds'],"meta":"„Plan sytuacyjny sieci kanalizacyjnej m. Prudnika”, 1:2500, z inwentaryzacji sieci w 1959 roku (w rogu opis „Inwent. sieci kan. m. Prudnika” i podpisy, odczyt niepewny). Kolektory z numerami studzienek, średnicami (Φ 0,15–0,75 m) i spadkami, wyloty do rzeki Prudnik, płuczki automatyczne. Ten plan nie jest arkuszem 5671: nałożono go osobno, dopasowując narysowany na nim bieg rzeki do rzeki na arkuszu z 1930 roku (średnio ok. 12 m odchyłki); plan jest sklejony z fotografii, więc lokalnie może się rozjeżdżać o 20–30 m.","source":"Fotografie planu od Tomka Owsiaka; miejsce przechowywania do uzupełnienia."},
 {"id":"1953","tag":"1953 (USA)","label":"1953 (wyd. amerykańskie)","img":"arkusz1953.jpg","meta":"Kopia Army Map Service (USA), seria M841, skopiowana w 1951 z arkusza z 1943 i wydrukowana w 1953, z dodaną siatką UTM. Treść jak w 1943. Na marginesie dopisek: „The entire area covered by this map is under Polish Administration” (cały obszar tej mapy jest pod administracją polską).","source":"Brigham Young University Library, Map Collection (pieczęć BYU i sygnatura „Map File G6080 s25 .G4” na skanie); kolekcja „Germany Maps”, contentdm.lib.byu.edu."}]
poi=[
 {"name":"Rynek i stare miasto","lat":50.3212,"lon":17.5803,"zoom":16,"pair":["1884","esri"],"text":"Układ ulic w obrębie dawnych murów niemal się nie zmienił. Zmienia się za to wszystko dookoła."},
 {"name":"Zakłady Fränkla","lat":50.32715,"lon":17.5722,"zoom":16,"pair":["1884","1930"],"text":"W 1884 fabryka stoi tylko po wschodniej stronie drogi do Nysy. W 1930 po zachodniej stronie jest już duży nowy kompleks hal."},
 {"name":"Koszary","lat":50.31636,"lon":17.56711,"zoom":15.75,"pair":["1884","1930"],"text":"W 1884 w tym miejscu są pola. W 1930 stoi tu cały kompleks koszar (opis „Kas.”) z placami."},
 {"name":"Oczyszczalnia ścieków","lat":50.3129,"lon":17.5765,"zoom":16,"pair":["1884","1930"],"text":"W 1884 nic tu nie ma. W 1930 i 1943 jest napis „Kläranl.” dokładnie w miejscu oczyszczalni z planu z 1913 roku, a obok poletka osadowe i stawy."},
 {"name":"Stacja pomp z 1894","lat":50.31121,"lon":17.56851,"zoom":16.5,"pair":["1884","1930"],"text":"Na arkuszu z 1930 napis „Wasserhebew.” (stacja pomp) przy drodze na południe, za Heiligbrunnen, dopisany jako uzupełnienie do wydania z 1884. W 1884 jeszcze jej nie ma. Budynek tuż nad napisem to najpewniej sama stacja."},
 {"name":"Rzeźnia miejska","lat":50.3156,"lon":17.5886,"zoom":16.5,"pair":["1884","1930"],"text":"W 1930 nad Prudnikiem stoi rzeźnia („Schlachth.”), zgodnie z planem z 1908 roku (nr 38). W 1884 jest tu jeszcze łąka."},
 {"name":"Plac ćwiczeń i strzelnice","lat":50.3411,"lon":17.5785,"zoom":15,"pair":["1884","1943"],"plac":True,"text":"Na arkuszu z 1930 napis „Exerzier-Platz” pokrywa się z obrysem placu nr 68 z planu garnizonu. W 1943 obok są strzelnice („Schießstde.”)."}]
data={"sheets":sheets,"bounds":meta['bounds'],"show":["1884","1930","1943","esri"],"start":["1884","esri"],"poi":poi,"sewer":{"img":"kanal1959_siec.png","bounds":K59["bounds"]},"plac":plac,"water":water}
os.makedirs(OUT,exist_ok=True)
open(f'{OUT}/arkusz.html','w').write(open('template_arkusz.html').read().replace('__DATA__',json.dumps(data,ensure_ascii=False)))
for s in sheets+[{"img":"kanal1959_siec.png"}]:
    src=f'../{s["img"]}'
    if os.path.exists(src) and os.path.abspath(src)!=os.path.abspath(f'{OUT}/{s["img"]}'): shutil.copy(src,f'{OUT}/{s["img"]}')
print('ok')
