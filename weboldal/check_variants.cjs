const { chromium } = require('C:/Users/Timi/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch({ headless: true, executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
  const out = path.join(__dirname, 'ellenorzes');
  fs.mkdirSync(out, { recursive: true });
  const variants = ['01-szerkesztosegi', '02-plakat', '03-mozaik'];
  const results = [];
  for (const variant of variants) {
    for (const [label, width, height] of [['desktop', 1440, 900], ['mobil', 390, 844]]) {
      const page = await browser.newPage({ viewport: { width, height }, deviceScaleFactor: 1 });
      const url = 'file:///' + path.join(__dirname, 'tervek', variant, 'index.html').replace(/\\/g, '/');
      await page.goto(url, { waitUntil: 'domcontentloaded' });
      await page.evaluate(async () => {
        await Promise.all([...document.images].map(async img => {
          img.loading = 'eager';
          if (img.complete) return;
          await new Promise(resolve => { img.addEventListener('load', resolve, { once: true }); img.addEventListener('error', resolve, { once: true }); });
        }));
      });
      await page.screenshot({ path: path.join(out, `${variant}-${label}.png`), fullPage: true });
      const result = await page.evaluate(() => ({
        h1: document.querySelectorAll('h1').length,
        brokenImages: [...document.images].filter(img => !img.complete || img.naturalWidth === 0).map(img => img.src),
        horizontalOverflow: document.documentElement.scrollWidth > innerWidth + 2,
        topCtaVisible: !!document.querySelector('.hero .button'),
      }));
      results.push({ variant, viewport: label, ...result });
      await page.close();
    }
  }
  console.log(JSON.stringify(results, null, 2));
  await browser.close();
})().catch(error => { console.error(error); process.exit(1); });
