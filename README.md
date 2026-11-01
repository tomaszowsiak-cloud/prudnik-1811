# Dawne plany Prudnika na dzisiejszej mapie

Historyczne plany Prudnika (niem. Neustadt in Oberschlesien) nałożone na współczesną mapę. Na stronie można przełączać plany, zmieniać przezroczystość, porównywać je z mapą OpenStreetMap, ortofotomapą Geoportalu i zdjęciami satelitarnymi oraz poprawiać punkty kontrolne.

**Strona:** https://tomaszowsiak-cloud.github.io/prudnik-1811/

| Plan | Autor | Skala | Źródło | Średni błąd dopasowania |
|---|---|---|---|---|
| 1811 | konduktor Scheuerwasser młodszy, kopia z 1835 r. | 150 prętów reńskich ≈ 565 m | Archiwum Państwowe w Opolu, zespół Rejencja Opolska (nr 1191), seria Mapy i plany IX, sygn. 81 | ok. 20 m |
| 1890 | geometra Weymann | 1:8000 | [Polona (Biblioteka Narodowa)](https://polona.pl/item-view/9b189dde-cd14-41d8-885f-6ac1b62f0c5c?page=0) | ok. 9 m |
| 1908 | Woerl's Reisebücherverlag, Lipsk (plan z przewodnika) | bez podziałki | [Polona (Biblioteka Narodowa)](https://polona.pl/item-view/52c71138-9151-42d5-ab13-cb1dde0e522a?page=3) | ok. 7 m (na 5 punktach) |
| 1913 | Miejski Urząd Budowlany (Stadtbauamt), 3 grudnia 1913 | 1:2500 | do uzupełnienia | ok. 4 m (na 5 punktach) |
| ok. 1900–1914 (data nieznana) | plan garnizonu *Neustadt mit Umgebung* | 1:5000, wstawka 1:25 000 | [Archiwum Państwowe we Wrocławiu, sygn. 82/329/0/-/10](https://polska-org.pl/11454549,foto.html?idEntity=521918) | ok. 12 m (przez plan 1890) |

## Co jest w repozytorium

| Plik | Zawartość |
|---|---|
| `index.html` | Strona z nakładkami i przełącznikiem planów |
| `plan1811.jpg` | Skan planu z 1811 r., pomniejszony do 4476 × 3304 pikseli i przycięty do ramki |
| `plan1890.jpg` | Skan planu z 1890 r., pomniejszony do 4000 × 3450 pikseli |
| `plan1908.jpg` | Plan z 1908 r., przycięty do ramki mapy |
| `plan1913.jpg` | Plan z 1913 r. |
| `plangarnizon.jpg` | Plan garnizonu, data nieznana |
| `prudnik-plany.kmz` | Wszystkie plany i wodociąg 1811 do Google Earth |
| `plan1811.jpg.points`, `plan1890.jpg.points`, `plan1908.jpg.points`, `plan1913.jpg.points`, `plangarnizon.jpg.points` | Punkty kontrolne do wtyczki Georeferencer w QGIS |
| `dane/` | Punkty kontrolne, położenia numerów z legend i wodociąg 1811 (JSON) |
| `narzedzia/` | Szablon strony i skrypt, który buduje z niego `index.html`, plik KMZ i pliki punktów |

## Plan z 1811 roku

*Plan von der Stadt Neustadt und deren Vorstaedte*, pomierzony w maju–sierpniu 1811 r., skopiowany w marcu 1835 r. (kopista Treeger lub Freeger, odczyt niepewny).

- Dopasowanie przez podobieństwo na 6 punktach kontrolnych, średni błąd ok. 20 m.
- Skala z dopasowania 0,74 m/piksel, z podziałki ok. 0,75 m/piksel.
- Góra planu jest obrócona o ok. 20° na wschód względem północy.
- Punkty kontrolne: ratusz, kościół św. Michała, Wieża Woka, kościół bonifratrów, Wieża Bramy Dolnej, arsenał (Wieża Katowska).

### Wodociąg 1811

Osobna warstwa na stronie i w pliku KMZ pokazuje miejski wodociąg zaznaczony na planie. Przebieg odczytał Tomasz Owsiak:

- **czerpadło** (nr 6, początek kunsztu wodnego) w północno-wschodnim narożniku miasta, przy jazie na rzece; ok. 50,32221° N, 17,58355° E,
- **wieża wodna** przy arsenale (nr 19), w miejscu dzisiejszej Wieży Katowskiej; ok. 50,32181° N, 17,58287° E,
- **rurociąg** (nr 21) z wieży wzdłuż północnej części miasta, z odgałęzieniami do rynku i dalej na południe, łącznie ok. 940 m,
- **osiem zdrojów miejskich** (nr 20) w zachodniej części miasta, wokół rynku i przy jatkach.

Położenie obiektów ma dokładność ok. ±20–30 m, wynikającą z dopasowania planu.

### Legenda planu 1811

| Nr | Obiekt | Oryginał |
|---|---|---|
| 1 | Ruina zamku i wozownia | Die Ruine des Schlosses u. Wagenremise |
| 2 | Skład soli | Die Salz-Niederlage |
| 3 | Szopa sikawek strażackich (odczyt niepewny) | Das Spritzen-Häusel |
| 4 | Słodownia | Das Maltz-Haus |
| 5 | Browary | Brau-Häuser |
| 6 | Kunszt wodny – czerpadło | Die Wasser-Kunst |
| 7 | Ratusz | Das Rathhaus |
| 8 | Szkoła, seminarium | Schulen, Seminarium |
| 9 | Jatki mięsne | Die Fleischbänke |
| 10 | Kościół parafialny | Die Pfarr-Kirche |
| 11 | Ujeżdżalnia | Die Reitbahn |
| 12 | Budynki parafialne | Die zur Pfarre gehörigen Gebäude |
| 13 | Dawny klasztor i kościół kapucynów | Ehemaliges Kapuziner-Kloster u. Kirche |
| 14 | Kościół bonifratrów | Barmherzigen-Kirche |
| 15 | Cegielnia miejska | Die Stadt-Ziegeley |
| 16 | Dom strzelecki | Das Schützen-Haus |
| 17 | Rynek | Der Ring |
| 18 | Targ świński (Schwarzvieh = trzoda chlewna) | Der Schwarz-Vieh-Markt |
| 19 | Arsenał (przy nim wieża wodna) | Das Zeug-Haus |
| 20 | Zdroje miejskie | Die Wasser-Reservoirs |
| 21 | Rurociąg z kunsztu | Die Röhrleitung aus der Kunst |

Objaśnienie kolorów i znaków (*Explication der Farben*): budynki mieszczańskie (*Bürger Gebäude*), budynki publiczne (*Publique Gebäude*), ogrody (*Gärten*), cmentarze (*Kirchhöfe*), łąki (*Wiesen*), zarośla (*Strauchwerk*), pola (*Acker*). Znaki krzyżyków, kresek i kwadracików na działkach oznaczają okręg miejski (*Bezirk*): zamkowy (*Schloß*), górny (*Ober*), rynkowy (*Markt*) i dolny (*Nieder*). Linie pomarańczowa i różowa to granice Przedmieścia Górnego i Dolnego.

Odczyt legendy z odręcznego pisma jest roboczy. W kilku miejscach różni się od tłumaczenia przygotowanego przez Gemini. Przy nr 4, 5, 15 i 19 przyjęto odczyt zgodny z położeniem obiektów na planie: słodownia i browary obok siebie, cegielnia przy dołach gliny, arsenał w narożnym bastionie. Podziałka to 150 prętów (nie 100), co potwierdza dopasowanie do współczesnej mapy.

## Plan z 1890 roku

*Plan von Neustadt in Ober-Schlesien*, rysował geometra Weymann, 1890. Plan pomierzony nowocześnie, w skali 1:8000, z podziałką metryczną i zaznaczoną koleją.

- Dopasowanie przez podobieństwo na 7 punktach kontrolnych, średni błąd ok. 9 m.
- Skala z dopasowania 0,895 m/piksel, z podziałki ok. 0,91 m/piksel (różnica ok. 2%, najpewniej kurczenie się papieru).
- Góra planu jest niemal dokładnie na północ (odchylenie ok. 1°).
- Punkty kontrolne: ratusz, kościół św. Michała, Wieża Woka, kościół bonifratrów, Wieża Bramy Dolnej, Wieża Katowska, areszt przy ul. Kościuszki 7 (na planie więzienie powiatowe, nr 16).

### Kunszt wodny w 1890 a czerpadło z 1811

W legendzie planu 1890 pod nr 27 (domy nr 515 i 516) jest *Wasserhebewerk*. Nie jest to jeszcze stacja pomp, tylko kunszt wodny, czyli następca czerpadła z 1811 r. Stoi nad Prudnikiem przy jazie, ok. 50,32224° N, 17,58331° E, niespełna 20 m od czerpadła z planu 1811, czyli w granicach dokładności obu dopasowań. Widać też kanał biegnący od jazu wzdłuż ulicy. Pierwsza prawdziwa stacja pomp w Prudniku pochodzi z 1894 r.

### Legenda planu 1890 (*Nachweisung öffentlicher Gebäude*)

| Nr | Obiekt | Oryginał | Nr domu |
|---|---|---|---|
| 1 | Sąd rejonowy, ratusz | Amtsgericht, Rathhaus | 1 |
| 2 | Przytułek, szpital dla kobiet (położenie przybliżone, z planu 1908) | Siechenhaus, Frauenhospital | 80 |
| 3 | Katolicka szkoła elementarna dla dziewcząt | Kath. Elementarschule (Mädchen) | 87 |
| 4 | Kościół parafialny (św. Michała) | Kath. Pfarrkirche | 88 |
| 5 | Gimnazjum i szkoła elementarna | Gymnasium u. Elementarschule | 89 |
| 6 | Plebania katolicka | Kath. Pfarrei | 90 |
| 7 | Przytułek św. Łazarza (dla mężczyzn) (położenie przeniesione z planu 1908, przybliżone) | Siechenhaus „St. Lazarus” (Männer) | 154 |
| 8 | Królewski Główny Urząd Celny (położenie przeniesione z planu 1908, przybliżone) | Königl. Haupt-Zollamt | 167 |
| 9 | Biura magistratu (Herrenhaus) | Magistrats-Büreaus (Herrenhaus) | 168 |
| 10 | Więzienie miejskie | Stadtgefängniss | 199 |
| 11 | Szopa sikawek strażackich | Spritzenschuppen | 213 |
| 12 | Zbrojownia (arsenał) | Zeughaus | 214 (nie zlokalizowano) |
| 13 | Stajnie garnizonowe i ujeżdżalnia (na terenie zamku) | Garnisonställe u. Reitbahn | 215, 216 |
| 14 | Kościół ewangelicki | Evang. Kirche | 236 |
| 15 | Starostwo powiatowe | Kreisverwaltung | 237 |
| 16 | Więzienie powiatowe (dziś areszt, ul. Kościuszki 7) | Kreis-Gefängniss | 239 |
| 17 | Koszary garnizonu, stajnie i ujeżdżalnia | Garnison-Kaserne, Ställe u. Reitbahn | 238, 270 |
| 18 | Sala gimnastyczna | Turnhalle | 271 |
| 19 | Poczta cesarska | Kaiserliche Post | – |
| 20 | Synagoga | Synagoge | 274 |
| 21 | Gazownia | Gas-Anstalt | 339 |
| 22 | Konwent bonifratrów (klasztor) | Convent der barmh. Brüder (Kloster) | 389 |
| 23 | Lazaret garnizonowy | Garnison-Lazareth | 392 |
| 24 | Szkoła symultanna (międzywyznaniowa) | Schulgebäude (simultan) | 395 |
| 25 | Szpital (położenie przeniesione z planu 1908, przybliżone) | Krankenhaus | 451 |
| 26 | Sierociniec Fundacji św. Anny | Waisenhaus „St. Anna Stift” | 457 |
| 27 | Kunszt wodny przy jazie na Prudniku, w miejscu czerpadła z 1811 r. | Wasserhebewerk | 515, 516 |

Położenie obiektów nr 2, 7, 8 i 25 przeniesiono z planu 1908, więc jest przybliżone. Nr 9 i 14 po przeniesieniu sprawdzono na planie: trafiają w dom nr 168 i w budynek kościoła. Zbrojowni (nr 12) nie zlokalizowano.

## Plan z 1908 roku

*Neustadt O/S*, plan z przewodnika turystycznego wydawnictwa Woerl's Reisebücherverlag z Lipska. Plan jest uproszczony i nie ma podziałki, ale obiekty są rozmieszczone dokładnie.

- Dopasowanie przez podobieństwo na 5 punktach kontrolnych, średni błąd ok. 7 m. Przy tak małej liczbie punktów błąd na obrzeżach planu może być większy.
- Punkty kontrolne: ratusz, Wieża Woka (nr 13, *Schloßhofturm*), kościół św. Michała, Wieża Bramy Dolnej (nr 37, *Niedertorturm*), areszt przy ul. Kościuszki 7 (nr 16).

### Oczyszczalnia ścieków z 1908 roku

Na planie jest **oczyszczalnia ścieków** (*Kläranlage*, nr 39), na południe od miasta, nad Prudnikiem, poniżej Dolnego Młyna (*Ndr. Mühle*). Według dopasowania leży ok. 50,3136° N, 17,5770° E (±20 m).

### Stacja pomp w 1908 roku

Stacja pomp wodociągowych (*Wasserhebewerk*, nr 27) leży poza ramką planu. Numer 27 jest wydrukowany pod dolną krawędzią, w kolumnie B, poniżej okolic Heilbrunnen. To pierwsza prawdziwa stacja pomp w Prudniku, z 1894 r. Zastąpiła kunszt wodny przy jazie, widoczny jeszcze na planie z 1890 r.

### Legenda planu 1908 (*Erklärung zum Plan von Neustadt O.-Schl.*)

| Nr | Obiekt | Oryginał |
|---|---|---|
| 1 | Sąd rejonowy, ratusz | Amtsgericht-Rathaus |
| 2 | Przytułek, szpital dla kobiet | Siechenhaus-Frauenhospital |
| 3 | Katolicka szkoła elementarna dla dziewcząt | Kath. Elementarschule (Mädchen) |
| 4 | Kościół parafialny (św. Michała) | Kath. Pfarrkirche |
| 5 | Katolicka szkoła elementarna | Kath. Elementarschule |
| 6 | Plebania katolicka | Kath. Pfarrei |
| 7 | Przytułek św. Łazarza dla mężczyzn | Siechenhaus St. Lazarus f. Männer |
| 8 | Królewski Główny Urząd Celny | Kgl. Hauptzollamt |
| 9 | Biura magistratu | Magistrat-Bureaus-Stadthaus |
| 10 | Więzienie miejskie | Stadtgefängnis |
| 11 | Szopa sikawek strażackich | Spritzenschuppen |
| 12 | Zbrojownia | Zeughaus |
| 13 | Wieża zamkowa (Wieża Woka) | Schloßhofturm |
| 14 | Kościół ewangelicki | Evang. Kirche |
| 15 | Starostwo powiatowe | Kreisverwaltung |
| 16 | Więzienie powiatowe (dziś areszt) | Kreisgefängnis |
| 17 | Ujeżdżalnia | Reitbahn |
| 18 | Sala gimnastyczna | Turnhalle |
| 19 | Poczta cesarska | Kaiserl. Post |
| 20 | Synagoga | Synagoge |
| 21 | Gazownia | Gasanstalt |
| 22 | Konwent bonifratrów (klasztor) | Convent d. barmh. Brüder (Kloster) |
| 23 | Lazaret garnizonowy | Garnison-Lazaret |
| 24 | Szkoła ewangelicka (symultanna) | Evgl. Schulgebäude (Simultan) |
| 25 | Szpital miejski | Städtisches Krankenhaus |
| 26 | Sierociniec Fundacji św. Anny | Waisenhaus St. Anna-Stift |
| 27 | Stacja pomp wodociągowych z 1894 r. (poza ramką planu, na południu) | Wasserhebewerk |
| 28 | Wojskowy urząd prowiantowy (magazyny) | Proviantamt |
| 29 | Koszary garnizonu | Garnison-Kaserne |
| 30 | Pomocniczy skład artylerii | Artillerie-Nebendepot |
| 31 | Kasyno oficerskie | Offizier-Kasino |
| 32 | Łaźnia miejska | Städt. Badeanstalt |
| 33 | Katolicki dom czeladzi | Kath. Gesellenhaus |
| 34 | Królewskie Gimnazjum Katolickie | Kgl. Kath. Gymnasium |
| 35 | Nowy kościół ewangelicki | Neue Evangel. Kirche |
| 36 | Szpital Fundacji Maxa i Hedwig Pinkusów | Krankenhaus (Max u. Hedwig Pinkus-Stiftung) |
| 37 | Wieża Bramy Dolnej | Niedertorturm |
| 38 | Rzeźnia z chłodnią | Schlachthaus mit Kühlanlage |
| 39 | Oczyszczalnia ścieków | Kläranlage |

## Plan z 1913 roku

*Plan von Neustadt in Oberschlesien*, sporządzony przez Miejski Urząd Budowlany (*Stadtbauamt*) i podpisany przez miejskiego budowniczego, Prudnik, 3 grudnia 1913. Skala oryginału 1:2500. Plan obejmuje głównie południowo-zachodnią część miasta. Kolorem czerwonym i zielonym zaznaczono na nim działki.

- Dopasowanie przez podobieństwo na 5 punktach kontrolnych, średni błąd ok. 4 m.
- Góra planu jest obrócona o ok. 17° względem północy.
- Punkty kontrolne: ratusz, Wieża Woka, kościół św. Michała, Wieża Bramy Dolnej, areszt przy ul. Kościuszki 7.

### Oczyszczalnia ścieków na planie 1913

Oczyszczalnia (*Kläranlage*) jest narysowana szczegółowo: dwa okrągłe zbiorniki, element w kształcie wachlarza i podłużny basen. Dalej na południowy zachód są rowy osadowe (*Schlammgräben*). Według dopasowania oczyszczalnia leży ok. 50,3129° N, 17,5765° E, a rowy osadowe ok. 50,3112° N, 17,5739° E.

Na planie 1908 oczyszczalnia wypada ok. 80 m dalej. Oba plany dopasowano na punktach w centrum miasta, a oczyszczalnia leży ok. 1 km na południe od nich, więc błąd na obrzeżu jest dużo większy niż średni. Dokładniejszy jest plan 1913.

### Obiekty opisane na planie 1913

| Nr | Obiekt | Oryginał |
|---|---|---|
| 1 | Oczyszczalnia ścieków | Kläranlage |
| 2 | Rowy (poletka) osadowe oczyszczalni | Schlammgräben |
| 3 | Cmentarz symultanny (międzywyznaniowy) | Simultan-Friedhof |
| 4 | Park miejski | Stadtpark |
| 5 | Pomnik wojenny | Kriegerdenkmal |
| 6 | Szpital miejski | Städtisches Krankenhaus |
| 7 | Fabryki S. Fränkla | S. Fränkel'sche Fabriken |
| 8 | Koszary | Kaserne |
| 9 | Wielka Łąka | Die große Wiese |
| 10 | Rynek z ratuszem | Ring |

Numeracja w tej tabeli jest robocza: plan 1913 ma własne numery działek i budynków, ale bez legendy.

## Plan garnizonu (data nieznana, ok. 1900–1914)

*Neustadt mit Umgebung* – plan miasta w skali 1:5000 z wstawką okolic w skali 1:25 000. Kolorami zaznaczono obiekty wojskowe, a legendy w rogach je wymieniają:

- **zarząd garnizonu** (*Garnison-Verwaltung*, nr 1–46, niebieski): koszary baterii, stajnie, ujeżdżalnie, kuźnie, warsztat rusznikarza, latryny i doły na popiół i śmieci,
- **urząd prowiantowy** (*Proviant-Amt*, nr 47–52, żółty): magazyn zboża, budynek mieszkalny, waga, stodoła,
- **skład artylerii** (*Artillerie-Depot*, nr 53–59d, czerwony kreskowany): wozownie, magazyny pocisków i zapalników, magazyny prochu, warsztat amunicyjny,
- **lazaret** (*Lazareth*, nr 62–66, czerwony): budynek główny, kostnica, kotłownia,
- na wstawce: **duży plac ćwiczeń** (*Großer Exerzierplatz*, nr 68) przy Buchelsdorf (Dębowcu).

**Źródło:** Archiwum Państwowe we Wrocławiu, sygn. 82/329/0/-/10, teka *Situations-Pläne der größeren Garnison-Städte im Bezirk des VI. Armee-Corps* (plany sytuacyjne większych miast garnizonowych w okręgu VI Korpusu Armii), wydawnictwo Brehmer & Minuth. Skan: [polska-org.pl](https://polska-org.pl/11454549,foto.html?idEntity=521918).

Część wpisów poprawiono odręcznie, m.in. dopisano budynek socjalny (*Wohlfahrtsgebäude*) i powierzchnię placu ćwiczeń.

**Datowanie.** Plan nie ma daty. Na planie z 1890 r. koszary są jeszcze w mieście przy Wiesener Straße, a duży kompleks koszarowy na południowym zachodzie pojawia się dopiero na planach z 1908 i 1913 r. Plan garnizonu powstał więc najpewniej po 1890 r., a przed I wojną światową. To oszacowanie z zawartości planu, a nie z dokumentu.

**Dopasowanie.** Plan jest obrócony o ok. 33° względem północy. Dopasowano go przez ratusz, kościół św. Michała i trzy punkty wspólne z planem 1890 (zbiornik gazowni, most przy Bramie Dolnej, studnia na Rynku). Średni błąd ok. 12 m, ale sumuje się z błędem planu 1890.
