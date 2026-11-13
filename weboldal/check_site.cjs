const { chromium } = require('C:/Users/Timi/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch({ headless: true, executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
  const root = path.join(__dirname, 'hajnal-site');
  const out = path.join(__dirname, 'ellenorzes', 'teljes-oldal');
  fs.mkdirSync(out, { recursive: true });
  const pages = ['index', 'kinalat', 'elorendeles', 'rolunk', 'workshop', 'kapcsolat', 'adatkezeles'];
  const results = [];
  for (const slug of pages) {
    for (const [label, width, height] of [['desktop', 1440, 900], ['mobil', 390, 844]]) {
      const page = await browser.newPage({ viewport: { width, height } });
      const file = path.join(root, `${slug}.html`);
      await page.goto('file:///' + file.replace(/\\/g, '/'), { waitUntil: 'domcontentloaded' });
      await page.evaluate(async () => {
        await Promise.all([...document.images].map(img => new Promise(resolve => {
          img.loading = 'eager';
          if (img.complete) return resolve();
          img.addEventListener('load', resolve, { once: true });
          img.addEventListener('error', resolve, { once: true });
        })));
      });
      if (['index', 'elorendeles', 'rolunk', 'adatkezeles'].includes(slug)) {
        await page.screenshot({ path: path.join(out, `${slug}-${label}.png`), fullPage: true });
      }
      const result = await page.evaluate(() => ({
        h1: document.querySelectorAll('h1').length,
        brokenImages: [...document.images].filter(img => !img.complete || img.naturalWidth === 0).map(img => img.getAttribute('src')),
        horizontalOverflow: document.documentElement.scrollWidth > innerWidth + 2,
        brokenLocalLinks: [...document.querySelectorAll('a[href]')].filter(a => a.protocol === 'file:' && !a.href.includes('#') && !a.href.startsWith('file:///')).map(a => a.href),
      }));
      results.push({ slug, viewport: label, ...result });
      await page.close();
    }
  }
  console.log(JSON.stringify(results, null, 2));
  await browser.close();
})().catch(error => { console.error(error); process.exit(1); });
