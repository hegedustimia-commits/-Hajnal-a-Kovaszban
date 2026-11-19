# Mérés és Search Console bekötése

Az oldal Search Console-igazolása és a webhelytérkép beküldése kész. A GA4-mérési azonosító `G-K5SDZEJNFE`; a hozzájárulási modul a `projektanyagok/weboldal/consent.js` fájlban tölti be a mérőkódot, kizárólag az elfogadás után.

## Search Console

A tulajdon igazolása a webhely gyökerében lévő `googlebba6e953c72f0733.html` fájllal sikerült. A beküldött webhelytérkép: `https://hajnal-a-kovaszban.netlify.app/sitemap.xml`.

## Google Analytics 4 és hozzájárulás

Az azonosító bekerült a `projektanyagok/weboldal/consent.js` fájl `GA4_MEASUREMENT_ID` változójába. A látogató elfogadási döntéséig nem töltődik be a Google Analytics szkript. Az elutasítás nem indít mérést; a választás később a láblécben módosítható.

A fiktív vizsgademó adatkezelési tájékoztatója továbbra is minta. Valós üzemeltetéshez a tényleges adatkezelő és a GA4-adatok megőrzési ideje pontosítandó.
