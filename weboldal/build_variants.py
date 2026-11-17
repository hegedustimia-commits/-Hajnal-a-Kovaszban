"""Create three static homepage design studies for Hajnal."""

from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / "képek"
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)

photos = {
    "bread": "pexels-aygnedalya-296473942-24245229.jpg",
    "slice": "pexels-valeriya-10038679.jpg",
    "hands": "pexels-klaus-nielsen-6287298.jpg",
    "pastry": "pexels-nikolai-nakorkeshko-2161421035-37471143.jpg",
    "breakfast": "pexels-yunustug-33059871.jpg",
    "cake": "pexels-polina-tankilevitch-4110003.jpg",
    "coffee": "pexels-nati-87264186-25949444.jpg",
    "baker_oven": "pexels-yasin-onus-520099596-36445126.jpg",
    "dough_hands": "pexels-klaus-nielsen-6294400.jpg",
    "workshop_dough": "pexels-travel-with-lenses-734723610-30918876.jpg",
}

for key, filename in photos.items():
    dest = ASSETS / f"{key}.webp"
    with Image.open(SOURCE / filename) as original:
        original = ImageOps.exif_transpose(original).convert("RGB")
        original.thumbnail((1500, 1500), Image.Resampling.LANCZOS)
        original.save(dest, "WEBP", quality=82, method=6)

sun = '<span class="sunmark" aria-hidden="true"><span></span></span>'

def header(active=""):
    return f'''<a class="skip" href="#tartalom">Ugrás a tartalomra</a>
    <div class="topline"><span>Pécs belvárosában</span><strong>K–Szo 7:00–14:00</strong><span>V–H zárva</span></div>
    <header class="site-header"><a class="brand" href="#top" aria-label="Hajnal – főoldal">{sun}<span><b>HAJNAL</b><small>KOVÁSZOS PÉKSÉG · PÉCS</small></span></a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="main-nav">Menü <span aria-hidden="true">☰</span></button>
      <nav id="main-nav" aria-label="Fő navigáció"><a href="#kinalat">Kínálat</a><a href="#rolunk">Rólunk</a><a href="#workshop">Workshop</a><a href="#kapcsolat">Kapcsolat</a><a class="nav-cta" href="#elorendeles">Előrendelés <span aria-hidden="true">↗</span></a></nav>
    </header>'''

def footer():
    return '''<footer class="footer"><div class="footer-inner"><div><span class="footer-kicker">Várunk reggel.</span><h2>Hajnal</h2><p>Kovászos pékség és reggeliző Pécsen.</p></div><div><h3>Nyitvatartás</h3><p>Kedd–szombat · 7:00–14:00<br>Vasárnap–hétfő · zárva</p></div><div><h3>Itt találsz</h3><p>Hajnalzug utca 2.<br>A Kovász köz sarkán, Pécs</p><small>Fiktív cím · vizsgaprojekt</small></div></div><div class="foot-bottom"><span>© Hajnal Kovászos Pékség</span><span>Fiktív vizsgaprojekt</span></div></footer>'''

def common_sections():
    return '''<section class="section offerings" id="kinalat"><div class="section-head"><span class="eyebrow">01 / MA A PULTBAN</span><h2>Amit reggelente Marci kisüt és Lili kínál a pultnál</h2><p>Kenyér a hétköznapokra, péksütemény a reggeli mellé, torta az ünnepre.</p></div><div class="offering-grid">
      <article class="offer-card"><div class="offer-photo"><img src="../assets/slice.webp" alt="Felszeletelt kovászos kenyér" loading="lazy"></div><div class="offer-body"><span class="stamp">KOVÁSZOS</span><h3>Kenyerek</h3><p>Ropogós héj, puha bélzet, minden reggel frissen.</p><a href="#elorendeles">Egész kenyeret rendelnék <span aria-hidden="true">↗</span></a></div></article>
      <article class="offer-card"><div class="offer-photo"><img src="../assets/pastry.webp" alt="Frissen sült péksütemények" loading="lazy"></div><div class="offer-body"><span class="stamp">REGGELI</span><h3>Péksütemények</h3><p>Valami jó a kávé mellé, amíg tart a napi sütés.</p><a href="#kapcsolat">Mikor találok nyitva? <span aria-hidden="true">↗</span></a></div></article>
      <article class="offer-card"><div class="offer-photo"><img src="../assets/cake.webp" alt="Málnás csokoládétorta" loading="lazy"></div><div class="offer-body"><span class="stamp">ELŐRENDELHETŐ</span><h3>Torták</h3><p>Egy fontos napra, előre egyeztetve és boltban átvéve.</p><a href="#elorendeles">Tortáról érdeklődöm <span aria-hidden="true">↗</span></a></div></article></div></section>
    <section class="section order-section" id="elorendeles"><div class="order-ornament" aria-hidden="true">✳</div><div class="order-copy"><span class="eyebrow">02 / ELŐRENDELÉS</span><h2>Válassz, írd meg, mit és mikorra szeretnél. Mi visszajelzünk.</h2><p>Egész kenyeret és tortát legalább egy nappal korábban kérhetsz. Az átvétel és a fizetés a boltban történik. A rendelést a visszaigazolásunk után tekintsd elfogadottnak.</p><div class="steps"><span><b>01</b> Válassz</span><span><b>02</b> Írd meg a részleteket</span><span><b>03</b> Várd a visszajelzésünket</span></div><a class="button button-light" href="#kapcsolat">Nézd meg, hol veheted át <span aria-hidden="true">↗</span></a><p class="prototype-note">Az előrendelő űrlap a választott terv alapján készül el.</p></div></section>
    <section class="section about-section" id="rolunk"><div class="about-photo"><img src="../assets/hands.webp" alt="Lisztes kézzel formált tészta" loading="lazy"><span class="photo-note">KÉT TESTVÉR · EGY KEMENCE</span></div><div class="about-copy"><span class="eyebrow">03 / RÓLUNK</span><h2>Marci a kemencénél. Lili a pultnál. Jó reggelt, Pécs!</h2><p>A Hajnalban a nap nem a nyitással kezdődik. Marci már előbb megérkezik, hogy friss kenyér kerüljön a pultra. Lili a betérőket fogadja, és közben készül a kávé. Két testvér, egy kis belvárosi pékség, tizenkét hely egy nyugodt reggelihez.</p><a class="text-link" href="#workshop">Ismerd meg a kovász világát <span aria-hidden="true">↗</span></a></div></section>
    <section class="section workshop-section" id="workshop"><div><span class="eyebrow">04 / HAVONTA EGY SZOMBATON</span><h2>Liszt a kézen. Kovász az asztalon.</h2><p>Havonta egyszer kovászkészítő workshopot tartunk. Ha szívesen belekóstolnál a folyamatba, figyeld a következő alkalmat.</p><a class="text-link" href="#kapcsolat">Érdeklődöm a workshopról <span aria-hidden="true">↗</span></a></div><div class="workshop-photo"><img src="../assets/hands.webp" alt="Tészta készítése lisztes felületen" loading="lazy"></div></section>
    <section class="section visit-section" id="kapcsolat"><div><span class="eyebrow">05 / TALÁLKOZUNK REGGEL</span><h2>Egy hely, ahová jó reggel érkezni.</h2><p>Pécs belvárosában, egy csendes utcasarkon várunk. Ugorj be egy kenyérért, vagy ülj le egy kávé mellé.</p><p class="address">Hajnalzug utca 2.<br><span>A Kovász köz sarkán, Pécs</span></p><small>A cím a fiktív vizsgaprojekt része.</small></div><div class="hours"><span class="stamp">NYITVATARTÁS</span><div><span>Kedd–péntek</span><strong>7:00–14:00</strong></div><div><span>Szombat</span><strong>7:00–14:00</strong></div><div><span>Vasárnap–hétfő</span><strong>Zárva</strong></div></div></section>
    <section class="final-cta"><span class="eyebrow">HOLNAP REGGEL?</span><h2>Tedd félre a következő kenyered.</h2><a class="button" href="#elorendeles">Előrendelést indítok <span aria-hidden="true">↗</span></a></section>'''

heroes = {
    "01-szerkesztosegi": '''<section class="hero hero-editorial"><div class="hero-copy"><span class="eyebrow">PÉCS · KOVÁSZOS PÉKSÉG ÉS REGGELIZŐ</span><h1>Legyen jó reggeled <em>mindig!</em><br><span>A jó reggel, a jó kenyérnél kezdődik.</span></h1><p>Friss kovászos kenyér, péksütemény és ráérős reggeli vár Pécs belvárosában. Nézz be hozzánk, vagy rendeld elő, amit biztosan haza szeretnél vinni.</p><div class="hero-actions"><a class="button" href="#elorendeles">Előrendelek <span aria-hidden="true">↗</span></a><a class="text-link" href="#kinalat">Megnézem a kínálatot <span aria-hidden="true">↘</span></a></div><div class="hero-smallprint">FRISSEN SÜTVE · K–SZO 7–14</div></div><div class="hero-media"><img src="../assets/bread.webp" alt="Frissen sült kovászos kenyér" fetchpriority="high"><div class="hero-ticket"><b>HAJNAL</b><span>EGY JÓ REGGELHEZ</span></div></div></section>''',
    "02-plakat": '''<section class="hero hero-poster"><div class="poster-heading"><span class="eyebrow">A KIS PÉKSÉG A SARKON · PÉCS</span><h1>Legyen jó reggeled <em>mindig!</em></h1><p class="poster-lead">A jó reggel, a jó kenyérnél kezdődik.</p><div class="hero-actions"><a class="button" href="#elorendeles">Előrendelek <span aria-hidden="true">↗</span></a><a class="text-link" href="#kinalat">Mi sül ma? <span aria-hidden="true">↘</span></a></div></div><div class="poster-collage"><div class="poster-image poster-main"><img src="../assets/bread.webp" alt="Kovászos kenyér közelről" fetchpriority="high"></div><div class="poster-image poster-side"><img src="../assets/coffee.webp" alt="Kávé és péksütemény" loading="lazy"></div><div class="round-seal" aria-hidden="true">KOVÁSZOS<br>REGGELEK<br>✳ PÉCS ✳</div></div><div class="poster-bottom"><span>MARCI SÜT · LILI KÍNÁL</span><p>Friss kovászos kenyér, péksütemény és ráérős reggeli vár Pécs belvárosában. Nézz be hozzánk, vagy rendeld elő, amit biztosan haza szeretnél vinni.</p><span>NYITVA K–SZO 7–14</span></div></section>''',
    "03-mozaik": '''<section class="hero hero-mosaic"><div class="mosaic-intro"><span class="eyebrow">JÓ REGGELT, PÉCS!</span><h1>Legyen jó reggeled <em>mindig!</em></h1><p class="mosaic-quote">A jó reggel, a jó kenyérnél kezdődik.</p><p>Friss kovászos kenyér, péksütemény és ráérős reggeli vár Pécs belvárosában. Nézz be hozzánk, vagy rendeld elő, amit biztosan haza szeretnél vinni.</p><a class="button" href="#elorendeles">Előrendelek <span aria-hidden="true">↗</span></a></div><div class="mosaic-photos"><div class="mosaic-large"><img src="../assets/bread.webp" alt="Frissen sült kovászos kenyér" fetchpriority="high"></div><div class="mosaic-tile"><img src="../assets/breakfast.webp" alt="Friss reggeli tányéron" loading="lazy"></div><div class="mosaic-tile mosaic-type"><span>REGGEL<br>7:00-TÓL</span><small>KEDD–SZOMBAT</small></div><div class="mosaic-tile"><img src="../assets/cake.webp" alt="Málnás csokoládétorta" loading="lazy"></div></div></section>''',
}

labels = {"01-szerkesztosegi": "1. Szerkesztőségi", "02-plakat": "2. Retró plakát", "03-mozaik": "3. Reggeli mozaik"}
for slug, hero in heroes.items():
    target = ROOT / "tervek" / slug
    target.mkdir(parents=True, exist_ok=True)
    page = f'''<!doctype html><html lang="hu"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Hajnal Kovászos Pékség · {labels[slug]}</title><meta name="description" content="Hajnal Kovászos Pékség és reggeliző Pécsen. Három főoldali látványterv a fiktív vizsgaprojekthez."><link rel="stylesheet" href="../../style.css"></head><body class="variant-{slug}" id="top">{header()}<main id="tartalom">{hero}{common_sections()}</main>{footer()}<script src="../../site.js" defer></script></body></html>'''.replace('../assets/', '../../assets/')
    (target / "index.html").write_text(page, encoding="utf-8")

index = '''<!doctype html><html lang="hu"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Hajnal · Három főoldali terv</title><link rel="stylesheet" href="style.css"></head><body class="index-page"><main class="variant-index"><span class="eyebrow">HAJNAL KOVÁSZOS PÉKSÉG · TERVEZÉSI KÖR</span><h1>Három hangulat.<br>Egy jó reggel.</h1><p>A jóváhagyott szövegre és a Hajnali retró arculatra épülő három főoldali terv. Válassz egy irányt, és abból készül el a teljes, hatoldalas weboldal.</p><div class="variant-grid"><a href="tervek/01-szerkesztosegi/"><span>01</span><img src="assets/bread.webp" alt="Kenyérfotó az első tervből"><h2>Szerkesztőségi</h2><p>Nyugodt, nagy tipográfia és oldalra rendezett kenyérfotó.</p><b>Megnézem ↗</b></a><a href="tervek/02-plakat/"><span>02</span><img src="assets/coffee.webp" alt="Kávéfotó a második tervből"><h2>Retró plakát</h2><p>Karakteres címek, pecsét és kétképes nyitórész.</p><b>Megnézem ↗</b></a><a href="tervek/03-mozaik/"><span>03</span><img src="assets/breakfast.webp" alt="Reggelifotó a harmadik tervből"><h2>Reggeli mozaik</h2><p>Életteli képrács, hangsúlyos nyitvatartás és változatos ritmus.</p><b>Megnézem ↗</b></a></div><p class="index-note">Ezek főoldali látványtervek. Az előrendelő űrlap és a további oldalak a választott irány után készülnek.</p></main></body></html>'''
(ROOT / "index.html").write_text(index, encoding="utf-8")
print("Built three homepage design studies in", ROOT)
