# Hajnal weboldal – három főoldali terv

A `index.html` fájlt közvetlenül megnyitva a három korábbi terv összehasonlító oldala látszik. A változatok külön is megnyithatók:

1. `tervek/01-szerkesztosegi/index.html` – nyugodt, kétsávos nyitórész, nagy kenyérfotóval.
2. `tervek/02-plakat/index.html` – retró plakát jellegű tipográfia, pecsét és képpár.
3. `tervek/03-mozaik/index.html` – képes mozaik, hangsúlyos reggeli és nyitvatartás.

Mindhárom a választott D, „Hajnali retró” arculat színeit és motívumait használja. A képek a `build_variants.py` által előállított, optimalizált WebP-fájlok. A fejlesztési források a projekt `képek/` mappájában vannak.

## Kiválasztott változat és teljes oldal

A **2. retró plakát** tervet választottuk. Az ebből készült statikus weboldal a projektgyökér `public/` mappájában van. Nyitó fájl: `public/index.html`. A többi oldal: `kinalat.html`, `elorendeles.html`, `rolunk.html`, `workshop.html`, `kapcsolat.html`. Két külön köszönőoldal tartozik az űrlapokhoz.

Az előrendelő és kapcsolatfelvételi űrlap Netlify Forms jelölést kapott. Helyi `file://` megnyitáskor próbamódban marad, nem küld adatot. Az éles Netlify telepítés után űrlapbeküldést és célba érkezést is tesztelni kell. A fiktív címhez élő térképes útvonal nem tartozik.

A Rólunk oldalról letölthető receptfüzet a `public/assets/hajnal-kovaszos-receptek.pdf` fájlban van. A borító a választott plakátos arculathoz igazodik.

A böngészős ellenőrzés képei az `ellenorzes/teljes-oldal/` mappában vannak. A `build_site.py` a kiválasztott tervből újraépíti a teljes oldalt, a `check_links.py` a helyi hivatkozásokat ellenőrzi.

Az új weboldal megtekintéséhez a projektgyökér `public/index.html` fájlt nyisd meg a böngészőben.
