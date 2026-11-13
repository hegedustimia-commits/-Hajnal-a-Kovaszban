# Hajnal Kovászos Pékség – arculati javaslat A: Hajnali pékség

Állapot: első egyeztetési változat. A brief meleg, reggeli fényes, enyhén retró hangulatát követi.

Ez az eredeti irány. Alternatívák: [retró](design-system-retro.md) és [mediterrán](design-system-mediterran.md). A tortaképek válogatása: [fotóválogatás](tortafotok-valogatas.md).

## Vizuális alapötlet

„Hajnali pékség”: papírszerű világos felület, kenyérhéj és kávé színei, kevés mélyvörös kiemelés. A fényképek és a tipográfia adják a karaktert; díszítésből kevés kell.

## Színek

| Szerep | Név | Kód | Használat |
|---|---|---|---|
| Háttér | Liszt | `#F7F2E8` | Oldal fő háttere |
| Kártya | Tejszín | `#FFFDF8` | Kártyák, űrlap |
| Fő szöveg | Kávé | `#2F241D` | Törzsszöveg, címsor |
| Elsődleges gomb | Kenyérhéj | `#874622` | CTA, aktív állapot |
| Gombszöveg | Meleg fehér | `#FFF9F1` | Kenyérhéj gombon |
| Másodlagos kiemelés | Téglavörös | `#A34E35` | Apró címkék, részletek |
| Elválasztó | Zab | `#D9C8B1` | Vonalak, finom keretek |

A főszöveg világos alapon sötét. Szöveget ne tegyünk közvetlenül forgalmas fotóra; ha mégis, legyen mögötte egységes sötét fedőréteg.

## Tipográfia

- **Címsor:** Fraunces, tartalék: Georgia, serif. Barátságos, enyhén régies karakter.
- **Törzsszöveg és navigáció:** DM Sans, tartalék: Arial, sans-serif. Jól olvasható mobilon is.
- **Méretirány:** törzsszöveg legalább 16–18 px, főcím mobilon kb. 40 px, asztalon 64–72 px. Sorhossz legfeljebb kb. 65–70 karakter.
- **Szöveghang:** tegező, közvetlen, konkrét. Rövid mondatok; nincs üres luxusnyelv.

## Logó

Egyszerű szöveges jel: **HAJNAL** nagy, karakteres serif betűvel; alatta kisebb sorban **KOVÁSZOS PÉKSÉG · PÉCS**. Opcionális kis napkorong vagy kelő nap félkör a szó mellé. Egyszínű változatban is működjön.

## Elrendezési elvek

- Tágas, levegős felületek, váltakozó kép és szöveg szakaszok.
- Kerekítés visszafogottan: 8–12 px; a fotóknál lehet lágyabb ív.
- A CTA egységes, nagy érintési felülettel (legalább 44 px magas).
- Mobilon egy oszlop; a rendelési CTA és a nyitvatartás könnyen megtalálható.
- Animáció csak finom hover és fókusz visszajelzésre. A mozgáscsökkentési beállítást tiszteletben kell tartani.

## Képirány a meglévő mappából

- **Főoldali hero:** `képek/pexels-aygnedalya-296473942-24245229.jpg` – nagyon közeli kenyérfotó, meleg tónus. Sötétebb, erős kép; jó, ha a szöveg külön világos panelre kerül.
- **Készítés / rólunk:** `képek/pexels-klaus-nielsen-6287298.jpg` – lisztes kéz és tészta, emberi folyamatot mutat.
- **Kínálat részlet:** `képek/pexels-valeriya-10038679.jpg` – felszeletelt kenyér, puha reggeli hangulat.
- **Tartalék termékfotó:** `képek/pexels-insideportugal-11570660.jpg` – erős kenyérközeli, de sötétebb és kontrasztosabb. Inkább kisebb blokkba.
- A többi képet az építési fázisban kategóriánként válogatjuk; az összes nagy felbontású fotót nem célszerű betölteni. A kiválasztottakat webes méretre kell optimalizálni, és ellenőrizni kell a stock fotók felhasználási feltételeit.
- **Torta:** `képek/pexels-polina-tankilevitch-4110003.jpg` a torta-előrendelés kiemelt képe; az emberi jelenet és a meleg tónus illik az alapirányhoz. A részletes értékelés külön fájlban van.
- A videó opcionális. Automatikus lejátszás nélkül, önálló tartalmi értékkel használható, ha illik a kiválasztott irányhoz.

## UI elemek

Gomb: kenyérhéj háttér, meleg fehér felirat; jól látható fókuszkeret. Másodlagos link: aláhúzott, sötét szöveg. Kártya: világos felület, vékony zab színű keret. Űrlapmező: fehér alap, sötét címke, egyértelmű hibajelzés. A nyitvatartás külön, könnyen pásztázható blokk.

## Kerülendő

Hűvös fine dining összhatás, túl sok animáció, erőltetett vintage textúra, minden kép egyszerre való használata, olvashatatlan szöveg a fotón.
