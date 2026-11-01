# Dawne plany Prudnika na dzisiejszej mapie

Historyczne plany Prudnika (niem. Neustadt in Oberschlesien) nałożone na współczesną mapę. Na stronie można przełączać plany, zmieniać przezroczystość, porównywać je z mapą OpenStreetMap, ortofotomapą Geoportalu i zdjęciami satelitarnymi oraz poprawiać punkty kontrolne.

**Strona:** https://tomaszowsiak-cloud.github.io/prudnik-1811/

| Plan | Autor | Skala | Źródło | Średni błąd dopasowania |
|---|---|---|---|---|
| 1811 | konduktor Scheuerwasser młodszy, kopia z 1835 r. | 150 prętów reńskich ≈ 565 m | Archiwum Państwowe w Opolu, zespół Rejencja Opolska (nr 1191), seria Mapy i plany IX, sygn. 81 | ok. 20 m |
| 1890 | geometra Weymann | 1:8000 | [Polona (Biblioteka Narodowa)](https://polona.pl/item-view/9b189dde-cd14-41d8-885f-6ac1b62f0c5c?page=0) | ok. 9 m |

## Co jest w repozytorium

| Plik | Zawartość |
|---|---|
| `index.html` | Strona z nakładkami i przełącznikiem planów |
| `plan1811.jpg` | Skan planu z 1811 r., pomniejszony do 4476 × 3304 pikseli i przycięty do ramki |
| `plan1890.jpg` | Skan planu z 1890 r., pomniejszony do 4000 × 3450 pikseli |
| `prudnik-plany.kmz` | Oba plany i wodociąg 1811 do Google Earth |
| `plan1811.jpg.points`, `plan1890.jpg.points` | Punkty kontrolne do wtyczki Georeferencer w QGIS |
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

### Stacja pomp z 1890 a czerpadło z 1811

Stacja pomp wodociągowych (*Wasserhebewerk*, nr 27, domy nr 515 i 516) stoi nad Prudnikiem przy jazie, ok. 50,32224° N, 17,58331° E. To niespełna 20 m od czerpadła z planu 1811, czyli w granicach dokładności obu dopasowań. Na planie 1890 widać też kanał biegnący od jazu wzdłuż ulicy.

### Legenda planu 1890 (*Nachweisung öffentlicher Gebäude*)

| Nr | Obiekt | Oryginał | Nr domu |
|---|---|---|---|
| 1 | Sąd rejonowy, ratusz | Amtsgericht, Rathhaus | 1 |
| 2 | Przytułek, szpital dla kobiet | Siechenhaus, Frauenhospital | 80 (nie zlokalizowano) |
| 3 | Katolicka szkoła elementarna dla dziewcząt | Kath. Elementarschule (Mädchen) | 87 |
| 4 | Kościół parafialny (św. Michała) | Kath. Pfarrkirche | 88 |
| 5 | Gimnazjum i szkoła elementarna | Gymnasium u. Elementarschule | 89 |
| 6 | Plebania katolicka | Kath. Pfarrei | 90 |
| 7 | Przytułek św. Łazarza (dla mężczyzn) | Siechenhaus „St. Lazarus” (Männer) | 154 (nie zlokalizowano) |
| 8 | Królewski Główny Urząd Celny | Königl. Haupt-Zollamt | 167 (nie zlokalizowano) |
| 9 | Biura magistratu (Herrenhaus) | Magistrats-Büreaus (Herrenhaus) | 168 (nie zlokalizowano) |
| 10 | Więzienie miejskie | Stadtgefängniss | 199 |
| 11 | Szopa sikawek strażackich | Spritzenschuppen | 213 |
| 12 | Zbrojownia (arsenał) | Zeughaus | 214 (nie zlokalizowano) |
| 13 | Stajnie garnizonowe i ujeżdżalnia (na terenie zamku) | Garnisonställe u. Reitbahn | 215, 216 |
| 14 | Kościół ewangelicki | Evang. Kirche | 236 (nie zlokalizowano) |
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
| 25 | Szpital | Krankenhaus | 451 (nie zlokalizowano) |
| 26 | Sierociniec Fundacji św. Anny | Waisenhaus „St. Anna Stift” | 457 |
| 27 | Stacja pomp wodociągowych (przy jazie na Prudniku) | Wasserhebewerk | 515, 516 |

Pozycje oznaczone „nie zlokalizowano” są w legendzie, ale ich numerów domów nie odnaleziono jeszcze na planie.
