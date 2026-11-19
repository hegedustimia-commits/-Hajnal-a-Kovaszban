# Mérés és Search Console bekötése

Az oldalon jelenleg nincs Google Analytics mérés. A `public/sitemap.xml` és `public/robots.txt` készen van. A hozzájárulási modul a `projektanyagok/weboldal/consent.js` fájlban van előkészítve. Amíg a GA4-azonosító üres, nem tölt be Google-kódot és nem jelenít meg sütisávot.

## Search Console

1. A [Google Search Console](https://search.google.com/search-console/) felületén vegyél fel **URL-előtag** tulajdont ezzel a címmel: `https://hajnal-a-kovaszban.netlify.app/`.
2. Válaszd a **HTML-címke** igazolást. A kapott `google-site-verification` címkét küldd el, hogy az oldal `<head>` részébe beilleszthessem. Az igazolásig ne kattints az Ellenőrzés gombra.
3. A címke élesítése után indítsd el az igazolást, majd a **Webhelytérképek** résznél add meg: `https://hajnal-a-kovaszban.netlify.app/sitemap.xml`.

## Google Analytics 4 és hozzájárulás

1. Hozz létre GA4-tulajdont és webes adatfolyamot a fenti webcímhez. Az **Adminisztrálás → Adatfolyamok → Web** résznél másold ki a `G-` kezdetű mérési azonosítót.
2. Az azonosító beillesztése előtt egészítsük ki az adatkezelési tájékoztatót a tényleges üzemeltető, a Google Analytics szolgáltató, a kezelt adatok és a megőrzési idő adataival.
3. Az azonosító a `projektanyagok/weboldal/consent.js` fájl `GA4_MEASUREMENT_ID` változójába kerül. Az oldal újraépítése és élesítése után a látogató elfogadási döntéséig nem töltődik be a Google Analytics szkript. Az elutasítás nem indít mérést; a választás később a láblécben módosítható.

Az igazolás és az adatfolyam létrehozása Google-fiókbeli tulajdonosi művelet. A két azonosító birtokában a technikai bekötés befejezhető és élesben tesztelhető.
