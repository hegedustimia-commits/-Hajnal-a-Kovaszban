const { chromium } = require('C:/Users/Timi/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const path = require('path');
(async()=>{
  const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
  const page=await browser.newPage();
  await page.goto('file:///'+path.join(__dirname,'hajnal-site','elorendeles.html').replace(/\\/g,'/'),{waitUntil:'domcontentloaded'});
  await page.locator('#termek').selectOption('kenyer');
  await page.locator('#reszletek').fill('Klasszikus kovászos kenyér');
  await page.locator('#nev').fill('Teszt Elek');
  await page.locator('#telefon').fill('06000000000');
  await page.locator('#email').fill('teszt@example.com');
  const date=new Date();date.setDate(date.getDate()+2);while([0,1].includes(date.getDay()))date.setDate(date.getDate()+1);
  await page.locator('#atvetel').fill(`${date.getFullYear()}-${String(date.getMonth()+1).padStart(2,'0')}-${String(date.getDate()).padStart(2,'0')}`);
  await page.locator('button[type="submit"]').click();
  const message=await page.locator('.form-error').textContent();
  console.log({message,stayedOnForm:page.url().includes('elorendeles.html')});
  await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
