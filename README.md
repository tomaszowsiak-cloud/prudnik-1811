# Prudnik 1811 na dzisiejszej mapie

Plan miasta Prudnika (*Plan von der Stadt Neustadt und deren Vorstaedte*) pomierzony w maju–sierpniu 1811 r. przez konduktora Scheuerwassera, skopiowany w marcu 1835 r. przez Treegera, nałożony na współczesną mapę.

**Strona:** https://tomaszowsiak-cloud.github.io/prudnik-1811/

## Co jest w repozytorium

| Plik | Zawartość |
|---|---|
| `index.html` | Strona z nakładką: suwak przezroczystości, podkłady (OpenStreetMap, ortofotomapa Geoportalu, zdjęcia satelitarne), numery obiektów z legendy z tłumaczeniem, edycja punktów kontrolnych |
| `plan1811.jpg` | Skan planu |
| `prudnik-1811.kmz` | Nakładka do Google Earth |
| `plan1811.jpg.points` | Punkty kontrolne do wtyczki Georeferencer w QGIS |
| `punkty-kontrolne.json` | Punkty kontrolne i położenia numerów z legendy na skanie |
| `narzedzia/` | Szablon strony i skrypt, który z niego buduje `index.html` i plik KMZ |

## Dopasowanie

- Przekształcenie przez podobieństwo (przesunięcie, obrót, skala) na 6 punktach kontrolnych.
- Średni błąd ok. 20 m.
- Skala z dopasowania: 1,48 m/piksel. Skala z podziałki planu (150 prętów reńskich ≈ 565 m): ok. 1,50 m/piksel.
- Góra planu jest obrócona o ok. 20° na wschód względem północy.

Punkty kontrolne: ratusz, kościół św. Michała, Wieża Woka, kościół bonifratrów, Wieża Bramy Dolnej, arsenał (Wieża Katowska). Współrzędne: rejestr zabytków (zabytek.pl), odtur.pl, Wikimedia Commons.

## Wodociąg 1811

Osobna warstwa na stronie i w pliku KMZ pokazuje miejski wodociąg zaznaczony na planie:

- **kunszt wodny** (nr 6, *Die Wasser-Kunst*) w północnej części starego miasta, ok. 85 m na północ od ratusza; współrzędne ok. 50,32225° N, 17,58100° E (±20–30 m),
- **rurociąg** (nr 21) z kunsztu na południe do rynku, z rozgałęzieniem na zachodnią i wschodnią stronę,
- **zbiorniki wody** (nr 20) wokół rynku i w sąsiednich kwartałach.

Przebieg rur odczytano z bladych niebieskich linii na planie, więc jest przybliżony.

## Legenda planu

| Nr | Obiekt | Oryginał |
|---|---|---|
| 1 | Ruina zamku | Die Ruine des Schlosses |
| 2 | Skład soli | Die Salz-Niederlage |
| 3 | Szopa sikawek strażackich | Das Spritzen-Häusel |
| 4 | Słodownia | Das Maltz-Haus |
| 5 | Browary | Brau-Häuser |
| 6 | Urządzenie wodociągowe | Die Wasser-Kunst |
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
| 18 | Targ bydła | Der Schwarz-Vieh-Markt |
| 19 | Arsenał | Das Zeug-Haus |
| 20 | Zbiorniki wody | Die Wasser-Reservoirs |
| 21 | Rurociąg z urządzenia wodociągowego | Die Röhrleitung aus der Kunst |

Odczyt legendy z odręcznego pisma jest roboczy i wymaga weryfikacji.
