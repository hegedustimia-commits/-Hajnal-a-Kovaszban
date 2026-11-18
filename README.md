# Hajnal Kovászos Pékség — vizsgaprojekt

- **`public/`**: a Netlifyra közzétehető, kész weboldal. Helyi belépő: `public/index.html`.
- **`projektanyagok/`**: brief, vizsgafeltételek, UX és arculati tervek, eredeti fotók, receptek, forráskód és ellenőrzési képek. Ezt a mappát a Netlify nem teszi közzé.
- **`netlify.toml`**: a Netlify publikálási beállítása; a közzétételi mappa `public`.

A weboldal újraépítése a projekt gyökeréből:

```powershell
python projektanyagok/weboldal/build_site.py
python projektanyagok/weboldal/check_links.py
python projektanyagok/weboldal/check_seo.py
```

A weboldal szerkesztési alapjai a `projektanyagok/weboldal/` mappában vannak. A kész oldalt a `public/` mappában érdemes átnézni; a generált fájlokat az építő script szükség esetén újraírja.

## SEO és webcím

Az oldal alapértelmezett webcíme `https://hajnal-a-kovaszban.netlify.app`. A `build_site.py` ebből készíti a canonical és Open Graph URL-eket, a strukturált adatokat, a `public/sitemap.xml` és `public/robots.txt` fájlt. Ha a webcím később változik, újraépítéskor a `SITE_URL` környezeti változóval írható felül:

```powershell
$env:SITE_URL = 'https://uj-cim.example'
python projektanyagok/weboldal/build_site.py
```

A Hajnal és a weboldalon szereplő cím fiktív vizsgademó. Az űrlap utáni köszönőoldalak `noindex` jelölést kapnak, és nem szerepelnek a sitemapben.

## Betöltési sebesség

A kész oldal egyetlen `public/site.css` stíluslapot használ. A DM Sans és Fraunces betűk a `public/fonts/` mappából töltődnek be, licenceikkel együtt. A főoldal nyitóképe és a termékkártyák képei a böngésző szélességéhez illő WebP-változatokból választhatók a `srcset` alapján. A forrásképek és a stíluslapok a `projektanyagok/weboldal/` mappában vannak.
