# Dawne plany Prudnika na dzisiejszej mapie

Historyczne plany Prudnika (niem. Neustadt in Oberschlesien) nałożone na współczesną mapę. Na stronie można przełączać plany, zmieniać przezroczystość, porównywać je z mapą OpenStreetMap, zdjęciami satelitarnymi Esri i ortofotomapą Geoportalu oraz poprawiać punkty kontrolne.

**Strona:** https://tomaszowsiak-cloud.github.io/prudnik-1811/

**Arkusz 5671 (1884–1953):** https://tomaszowsiak-cloud.github.io/prudnik-1811/arkusz.html

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
| `arkusz.html` | Porównanie czterech wydań arkusza 5671 (kurtyna, przenikanie, pokaz) |
| `arkusz1884.jpg` … `arkusz1953.jpg` | Arkusze przeliczone do odwzorowania mapy internetowej (Web Mercator), przycięte do ramki |
| `plan1811.jpg` | Skan planu z 1811 r., pomniejszony do 4476 × 3304 pikseli i przycięty do ramki |
| `plan1890.jpg` | Skan planu z 1890 r., pomniejszony do 4000 × 3450 pikseli |
| `plan1908.jpg` | Plan z 1908 r., przycięty do ramki mapy |
| `plan1913.jpg` | Plan z 1913 r. |
| `plangarnizon.jpg` | Plan garnizonu (bez wstawki), data nieznana |
| `plangarnizon-okolice.jpg` | Wstawka okolic z planu garnizonu (1:25 000) |
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

### Legenda planu garnizonu

| Nr | Obiekt | Oryginał |
|---|---|---|
| | **Zarząd garnizonu (niebieski)** | |
| 1 | Budynek zarządu garnizonu | Garnison-Verwaltungs-Gebäude |
| 2 | Pralnia garnizonowa | Garnison-Waschanstalt |
| 3 | Stajnia dla chorych koni | Krankenstall |
| 4 | Warsztat rusznikarza | Waffenmeister-Werkstatt |
| 5 | Gnojownia | Düngerstätte |
| 6 | Szopa na działa | Geschützschuppen |
| 7 | Dół na popiół i śmieci | Asch- und Müllgrube |
| 8 | Budynek sztabu | Stabsgebäude |
| 9 | Budynek magazynu mundurowego (kwatermistrzowski) | Kammergebäude |
| 10 | Koszary 6. baterii | Batterie-Kaserne 6 |
| 11 | Latryna nr 4 z dołem na popiół i śmieci | Latrine 4 mit Asch- und Müllgrube |
| 12 | Koszary 5. baterii | Batterie-Kaserne 5 |
| 13 | Budynek gospodarczy | Wirthschaftsgebäude |
| 14 | Koszary 4. baterii | Batterie-Kaserne 4 |
| 14a | Szopa na działa (dopisek odręczny) | Geschützschuppen (dopisek odręczny) |
| 15 | Latryna nr 3 z dołem na popiół i śmieci | Latrine 3 mit Asch- und Müllgrube |
| 16 | Koszary 3. baterii | Batterie-Kaserne 3 |
| 17 | Latryna nr 2 z dołem na popiół i śmieci | Latrine 2 mit Asch- und Müllgrube |
| 18 | Koszary 2. baterii | Batterie-Kaserne 2 |
| 19 | Budynek gospodarczy | Wirthschaftsgebäude |
| 20 | Plac ćwiczeń w celowaniu | Richtübungsplatz |
| 21 | Szopa na działa | Geschützschuppen |
| 22 | Latryna nr 1 z dołem na popiół i śmieci | Latrine 1 mit Asch- und Müllgrube |
| 23 | Koszary 1. baterii | Batterie-Kaserne 1 |
| 24 | Tor do prezentacji koni | Vorführbahn |
| 25 | Kuźnia podkuwacza | Beschlagschmiede |
| 26 | Warsztat rusznikarza | Waffenmeister-Werkstatt |
| 27 | Ogród skokowy (do ćwiczeń jazdy) | Sprunggarten |
| 28 | Stajnia 1. baterii | Batterie-Stall 1 |
| 29 | Gnojownia nr 6 | Düngerstätte 6 |
| 30 | Ujeżdżalnia nr 1 | Reitbahn 1 |
| 31 | Stajnia 2. baterii | Batterie-Stall 2 |
| 32 | Stajnia 3. baterii | Batterie-Stall 3 |
| 33 | Stajnia 4. baterii | Batterie-Stall 4 |
| 34 | Gnojownia nr 5 z latryną stajenną | Düngerstätte 5 mit Stalllatrine |
| 35 | Gnojownia nr 4 | Düngerstätte 4 |
| 36 | Gnojownia nr 3 | Düngerstätte 3 |
| 37 | Gnojownia nr 2 | Düngerstätte 2 |
| 38 | Ujeżdżalnia nr 2 | Reitbahn 2 |
| 39 | Stajnia 5. baterii | Batterie-Stall 5 |
| 40 | Stajnia 6. baterii | Batterie-Stall 6 |
| 41 | Kuźnia podkuwacza | Beschlagschmiede |
| 42 | Tor do prezentacji koni | Vorführbahn |
| 43 | Gnojownia nr 1 z latryną stajenną | Düngerstätte 1 mit Stalllatrine |
| 44 | Dom mieszkalny dla rodzin | Familien-Wohnhaus |
| 45 | Dół na popiół i śmieci | Asch- und Müllgrube |
| 46 | Dom mieszkalny dla rodzin | Familien-Wohnhaus |
| 60 | Kasyno (stołówka) oficerska | Offizier-Speise-Anstalt |
| 61 | Dół na popiół i śmieci przy kasynie | Asch- und Müllgrube |
| | **Urząd prowiantowy (żółty)** | |
| 47 | Magazyn zboża | Körner-Magazin |
| 48 | Budynek mieszkań służbowych | Dienstwohngebäude |
| 49 | Dół na popiół i śmieci | Asch- und Müllgrube |
| 50 | Waga | Waage |
| 51 | Latryna | Latrine |
| 51a | Budynek socjalny (dopisek odręczny) | Wohlfahrtsgebäude (dopisek odręczny) |
| 52 | Stodoła | Scheune |
| | **Skład artylerii (czerwony kreskowany)** | |
| 53 | Wozownia nr 1 | Wagenhaus 1 |
| 54 | Wozownia nr 2 | Wagenhaus 2 |
| 55 | Magazyn pocisków i zapalników | Geschoss- und Zündungen-Magazin |
| 56 | Wozownia nr 3 | Wagenhaus 3 |
| 56a | Wozownia nr 4 (dopisek odręczny) | Wagenhaus 4 (dopisek odręczny) |
| 57 | Magazyn amunicji (nabojów) | Patronenhaus |
| 58 | Magazyn prochu na czas pokoju nr 1 | Friedenspulvermagazin 1 |
| 59 | Magazyn prochu na czas pokoju nr 2 | Friedenspulvermagazin 2 |
| 59a | Szopa do prac z amunicją | Munitions-Arbeitsschuppen |
| 59b | Latryna z magazynem oleju | Latrine mit Öllagerraum |
| 59c | Budynek mieszkań służbowych | Dienstwohngebäude |
| 59d | Budynek stajni | Stallgebäude |
| | **Lazaret (czerwony)** | |
| 62 | Latryna i budynek pomocniczy | Latrine und Nebengebäude |
| 63 | Budynek główny lazaretu | Lazarett-Hauptgebäude |
| 64 | Dół na popiół i śmieci | Asch- und Müllgrube |
| 65 | Kostnica | Leichenhaus |
| 66 | Szopa na węgiel | Kohlenschuppen |
| | **Inne obiekty** | |
| 67 | Strzelnica (bractwo kurkowe) | Schiessstand (Schützengilde) |
| 68 | Duży plac ćwiczeń (miejski), na wstawce przy Buchelsdorf (Dębowcu) | Grosser Exerzierplatz (Städtisch), 794 947 m² (dopisek) |
| 69 | Studnia (dopisek odręczny w miejsce skreślonej łaźni), na wstawce | Brunnen (dopisek; pierwotnie: Badeanstalt) |
| 70 | Mały plac ćwiczeń (dopisek odręczny w miejsce skreślonej prochowni) | Kleiner Exerzierplatz, 326… m² (dopisek; pierwotnie: Pulverhaus) |

Legenda planu dotyczy wyłącznie obiektów wojskowych. Dopisek „(Städtisch)” przy większości pozycji oznacza najpewniej, że budynki należały do miasta, a wojsko z nich korzystało. Numery 68 i 69 są na wstawce okolic w skali 1:25 000; wstawkę dopasowano osobno.

**Datowanie.** Plan nie ma daty. Na planie z 1890 r. koszary są jeszcze w mieście przy Wiesener Straße, a duży kompleks koszarowy na południowym zachodzie pojawia się dopiero na planach z 1908 i 1913 r. Plan garnizonu powstał więc najpewniej po 1890 r., a przed I wojną światową. To oszacowanie z zawartości planu, a nie z dokumentu.

**Wstawka okolic i plac ćwiczeń.** Wstawkę w skali 1:25 000 dopasowano osobno (jest zorientowana na północ), przez lazaret, urząd prowiantowy, cmentarz, Rynek i most przy Bramie Dolnej. Błąd wynosi ok. 20–60 m. Duży plac ćwiczeń (nr 68) leży na północ od miasta, w stronę Prężynki. Jego obrys odrysowano z wstawki i naniesiono na mapę jako wielokąt. Po przeniesieniu ma ok. 72.9 ha, a na planie dopisano ręcznie 794 947 m² (79,5 ha). Zgodność ok. 92% niezależnie potwierdza dopasowanie. Studnię (nr 69) naniesiono jako punkt. Plik `plangarnizon-okolice.jpg` to wycięta wstawka.

**Dopasowanie.** Plan jest obrócony o ok. 33° względem północy. Dopasowano go przez ratusz, kościół św. Michała i trzy punkty wspólne z planem 1890 (zbiornik gazowni, most przy Bramie Dolnej, studnia na Rynku). Średni błąd ok. 12 m, ale sumuje się z błędem planu 1890.

## Arkusz 5671 Neustadt O.S. (1884–1953)

Ten sam arkusz mapy topograficznej 1:25 000 (Messtischblatt 3301, później 5671) w czterech wydaniach:

| Wydanie | Opis | Źródło |
|---|---|---|
| 1884 | pierwsze wydanie, pomiar Królewskiej Pruskiej Służby Topograficznej z 1883; długości od południka Ferro | [Instytut Geografii UP w Krakowie](http://igrek.amzp.pl/details.php?id=16506), 400 dpi |
| 1930 | stopka: „Herausgegeben … 1884, Einzelne Nachträge 1930”, czyli wydanie z 1884 z pojedynczymi uzupełnieniami, bez nowego pomiaru | egzemplarz z pieczęcią TH Danzig, Geographisches Seminar; ten sam stan mają [AMZP](http://igrek.amzp.pl/details.php?id=5272) i [BUWr, sygn. 6541-III.C./3301](http://igrek.amzp.pl/details.php?id=11772860) (datowany „1935?”) |
| 1943 | „Ausgabe 1943”; stopka: pomiar 1883 (Borchmann), sprostowanie Reichsamt für Landesaufnahme 1937 (Wirth), nazwy wg stanu z 1.04.1938, ostatnie uzupełnienia H.V.A. II 1939 | [Wydział Geografii i Studiów Regionalnych UW](http://igrek.amzp.pl/details.php?id=11780596) |
| 1953 | kopia Army Map Service (USA), seria M841, skopiowana w 1951 z arkusza z 1943, wydruk 1953; dodana siatka UTM | Brigham Young University Library, Map Collection (pieczęć i sygnatura „Map File G6080 s25 .G4” na skanie), [kolekcja Germany Maps](https://contentdm.lib.byu.edu/digital/collection/GermanyMaps/search) |

Pełna lista skanów arkusza: [Mapster, arkusz 5671](http://igrek.amzp.pl/result.php?cmd=id&god=5671&cat=TK25).

**Historia wydań.** Prudnik nie dostał nowego pomiaru terenu: wszystkie wydania wychodzą z pomiaru z 1883. Wydanie z 1930 to arkusz z 1884 z punktowymi uzupełnieniami, wśród nich oczyszczalnia (*Kläranl.*), stacja pomp (*Wasserhebew.*) i koszary. Wydanie z 1943 ma już prawdziwe sprostowanie treści z 1937 i uzupełnienia z 1939.

**Dopasowanie.** Każdy arkusz dopasowano po czterech narożnikach ramki (17°30′–17°40′ E, 50°18′–50°24′ N w dawnym układzie niemieckim, elipsoida Bessela), przeliczonych na WGS 84. Kontrola na ratuszu, kościele św. Michała, Wieży Bramy Dolnej, Wieży Woka, areszcie i dworcu daje odchyłki rzędu 5–15 m na wszystkich wydaniach. Przeliczenie układu zgadza się z wartościami narożników podanymi na arkuszu amerykańskim (ED50) z dokładnością ok. 5 m.

**Strona** pozwala porównać dowolne dwa wydania albo wydanie z dzisiejszą ortofotomapą: kurtyną (przeciągana linia), przenikaniem albo w pokazie 1884 → 1930 → 1943 → dziś. Lista „Na co zwrócić uwagę” przenosi do miejsc, gdzie zmiana jest dobrze widoczna.

**Potwierdzenia z planów miasta:**
- napis *Kläranl.* (oczyszczalnia) na arkuszach z 1930 i 1943 leży dokładnie w miejscu oczyszczalni z planu z 1913,
- napis *Exerzier-Platz* na arkuszu z 1930 pokrywa się z obrysem placu ćwiczeń nr 68 z planu garnizonu; w 1943 obok są strzelnice,
- na arkuszu z 1930 jest stacja pomp (*Wasserhebew.*) na południe od miasta, za Heiligbrunnen, ok. 50,3112° N, 17,5685° E; na arkuszu z 1884 jej jeszcze nie ma,
- rzeźnia (*Schlachth.*) na arkuszu z 1930 zgadza się z planem z 1908 (nr 38).

## Plan sieci kanalizacyjnej z 1959 roku

*Plan sytuacyjny sieci kanalizacyjnej m. Prudnika*, 1:2500, z inwentaryzacji sieci w 1959 roku. Na planie są kolektory z numerami studzienek, średnicami (Φ 0,15–0,75 m) i spadkami, wyloty do rzeki Prudnik i płuczki automatyczne.

- Dopasowanie: sklejka planu przygotowana wcześniej miała przesunięcia na szwach (np. rzeka urywała się przy Bramie Dolnej o ok. 50 m), więc plan złożono od nowa z 8 zdjęć: zdjęcia dopasowano do siebie po tysiącach wspólnych punktów (średni błąd zszycia kilka metrów). Gotowy plan nałożono po biegu rzeki na arkusz z 1930 roku i poprawiono po skrzyżowaniach ulic na arkuszu z 1943 roku. Dokładność ok. 10–20 m.
- Na stronie arkusza 5671 plan jest do wyboru w porównaniu (*1959 – plan sieci kanalizacyjnej*), a sama sieć jako warstwa *Sieć kanalizacyjna z 1959 roku*, którą można nałożyć na dowolne wydanie arkusza albo na zdjęcia satelitarne.
- Pliki: `kanal1959.jpg` (plan przeliczony do odwzorowania mapy), `kanal1959_siec.png` (wyodrębniona sieć i rzeka, przezroczyste tło), `dane/kanal1959.json` (zasięg).
- Źródło: fotografie planu od Tomka Owsiaka; miejsce przechowywania do uzupełnienia.
