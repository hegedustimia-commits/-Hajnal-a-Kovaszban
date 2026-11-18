# Hajnal Kovászos Pékség – arculati javaslat D: Hajnali retró

Állapot: egyeztetési változat, 2026. november 12. Az [A: Hajnali pékség](design-system.md) és a [B: Retró pékség](design-system-retro.md) ötvözete, a meglévő [UX-tervhez](ux-terv.md).

## Alapötlet

A pékség reggeli fénye és természetes anyagai adják az alapot. Egy könnyen felismerhető, régi pékségi papírcímkékre emlékeztető grafikai rendszer ad karaktert. Az összhatás otthonos és mai: a retró a részletekben jelenik meg, a tartalom és az előrendelés végig könnyen használható marad.

**Kulcskép:** a frissen sült kenyér mellett egy krémszínű, meggypiros szegélyű papírcímke, rajta a Hajnal neve és egy kelő nap jele.

## Színrendszer

| Szerep | Név | Kód | Használat |
|---|---|---|---|
| Fő háttér | Liszt | `#F7F2E8` | Oldal fő háttere, az A irányból |
| Kártya és űrlap | Meleg krém | `#FFF9EE` | Olvasható tartalmi felületek |
| Fő szöveg | Kávé | `#2F241D` | Címsor, törzsszöveg |
| Elsődleges CTA | Kenyérhéj | `#874622` | Előrendelés gomb, az A irányból |
| CTA felirat | Meleg fehér | `#FFF9F1` | Gombszöveg |
| Karakteres akcentus | Meggypiros | `#9B3E3A` | Papírcímkék széle, kis jelölések |
| Másodlagos akcentus | Olíva | `#5F6A45` | Workshop vagy szezonális címke |
| Vonal és keret | Zab | `#D9C8B1` | Elválasztók, kártyakeretek |

A meggypiros kis felületeken szerepeljen, legfeljebb a vizuális hangsúly 10–15%-ában. Az előrendelési gomb maradjon következetesen kenyérhéj színű, hogy a fő akció mindig azonosítható legyen.

## Tipográfia

- **Címsor és szójel:** Fraunces, 650–750 súly. Puha, kissé régies formái adják a retró karaktert, de nem uralják túl az oldalt.
- **Törzsszöveg és navigáció:** DM Sans, 400–600 súly, legalább 16 px. Tartalék: Arial.
- **Kis címke és számozás:** DM Sans félkövér, nagybetűvel, kissé növelt betűközzel. Csak rövid feliratokra, például „MA A PULTBAN” vagy „ELŐRENDELHETŐ”.
- **Méretirány:** H1 mobilon 40–44 px, asztalon 64–72 px; H2 mobilon 30–34 px; törzsszöveg 17–18 px. A tényleges tördelést a kész oldalon ellenőrizni kell.

## Logó és felismerhető motívum

**HAJNAL** szójel Fraunces betűvel, alatta kis **KOVÁSZOS PÉKSÉG · PÉCS** sor. A szójel bal oldalán egy félkörből felkelő nap három rövid sugárral. A nap félköre visszatérhet a kategóriacímkék sarkán és a láblécben, de ne legyen minden szakaszban.

**Címkerendszer:** enyhén lekerekített téglalap, vékony meggypiros keret, krémszínű háttér. Egyetlen ilyen címke a hero képen vagy mellette már elég karaktert ad. Termékkártyákon a „kovászos”, „előrendelhető” és „hétvégi” jelölések ugyanebben a formában készülnek.

## Elrendezési szabályok

- **Hero:** szöveg világos felületen, mellette vagy alatta nagy, közeli kenyérfotó. A papírcímke a fotó szélén jelenik meg, nem takarja a terméket.
- **Kínálat:** világos kártyák vékony kerettel és nagy fotóval. A fő kategóriák három jól elkülönülő blokkban jelennek meg.
- **Előrendelés:** a meleg arculatból megtartott, egyszerű űrlap. A címkék csak a szakaszcímeknél jelennek meg, az űrlapmezőkön nem.
- **Rólunk:** lisztes kéz és tészta fotója, rövid Marci–Lili történet. Egy kiemelt, kézzel írt jegyzetet idéző sor lehet, de valódi kézírásos font nélkül.
- **Workshop:** olívazöld kis jelölés választja el a fő előrendelési úttól.
- **Kapcsolat:** a nyitvatartás árjegyzékszerű, de nagy, jól pásztázható sorokban. A cím és az útvonal gomb azonnal látható.
- **Mobil:** egy oszlop, korán megjelenő előrendelési CTA és nyitvatartás. A díszítő címkék nem szűkíthetik a tartalmi szélességet.

## Képválasztás

- **Hero:** `képek/pexels-aygnedalya-296473942-24245229.jpg` közeli kenyérfotó. A kenyér formája erős, a címke mellett jól megjegyezhető nyitókép lehet.
- **Rólunk:** `képek/pexels-klaus-nielsen-6287298.jpg`, lisztes kéz és tészta.
- **Kínálat:** `képek/pexels-valeriya-10038679.jpg`, meleg reggeli tónus.
- **Torta-előrendelés:** `képek/pexels-polina-tankilevitch-4110003.jpg`, málnás csokoládétorta emberi jelenettel. Második képként `képek/pexels-marta-dzedyshko-1042863-6341564.jpg` használható. A gyümölcsös tart fotója csak akkor kerüljön be, ha ilyen tétel is szerepel a kínálatban.

## Komponensek

| Elem | Megjelenés | Viselkedés |
|---|---|
| Elsődleges gomb | Kenyérhéj háttér, meleg fehér szöveg, 8 px sarok | Hover és fókusz jól látható; felirat igével: „Előrendelek” |
| Másodlagos link | Kávé szín, aláhúzás | Egyértelmű fókuszállapot |
| Papírcímke | Krém háttér, vékony meggypiros keret | Rövid információ, nem gombnak álcázva |
| Termékkártya | Krém háttér, zab keret, nagy fotó | Egész felület helyett külön, érthető link |
| Űrlapmező | Fehér vagy krém háttér, sötét címke | Kötelező mező és hiba szövegesen is jelölve |

## Mitől lesz megjegyezhető

1. Az egyszerű kelő nap jel és a HAJNAL szójel együtt könnyen felismerhető.
2. A meggypiros szegélyű papírcímke visszatérő, de ritkán használt elem.
3. A közeli kenyérfotók és a személyes készítési képek a brief valódi hangulatát hordozzák.
4. A fő CTA mindig ugyanazt a színt és helyet követi, ezért a karakter nem rontja a használhatóságot.

## Kerülendő

Sok különböző retró minta, kockás háttér az egész oldalon, kézírásos törzsszöveg, meggypiros CTA mindenhol, díszítő elem a formmezőkben, erős animáció.
