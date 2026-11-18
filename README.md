# Hajnal Kovászos Pékség — vizsgaprojekt

- **`public/`**: a Netlifyra közzétehető, kész weboldal. Helyi belépő: `public/index.html`.
- **`projektanyagok/`**: brief, vizsgafeltételek, UX és arculati tervek, eredeti fotók, receptek, forráskód és ellenőrzési képek. Ezt a mappát a Netlify nem teszi közzé.
- **`netlify.toml`**: a Netlify publikálási beállítása; a közzétételi mappa `public`.

A weboldal újraépítése a projekt gyökeréből:

```powershell
python projektanyagok/weboldal/build_site.py
python projektanyagok/weboldal/check_links.py
```

A weboldal szerkesztési alapjai a `projektanyagok/weboldal/` mappában vannak. A kész oldalt a `public/` mappában érdemes átnézni; a generált fájlokat az építő script szükség esetén újraírja.
