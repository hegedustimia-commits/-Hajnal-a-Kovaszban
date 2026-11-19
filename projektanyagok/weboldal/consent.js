/* A GA4-azonosítót az éles bekötéskor itt kell megadni. Üresen nem töltődik mérőkód. */
const GA4_MEASUREMENT_ID = '';

(() => {
  if (!/^G-[A-Z0-9]+$/.test(GA4_MEASUREMENT_ID)) {
    document.querySelectorAll('[data-cookie-settings]').forEach(button => { button.hidden = true; });
    return;
  }

  const key = 'hajnal-analytics-consent';
  const stored = localStorage.getItem(key);
  let loaded = false;

  function loadAnalytics() {
    if (loaded) return;
    loaded = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', GA4_MEASUREMENT_ID);
    const script = document.createElement('script');
    script.async = true;
    script.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(GA4_MEASUREMENT_ID);
    document.head.appendChild(script);
  }

  function setConsent(value) {
    localStorage.setItem(key, value);
    banner.hidden = true;
    if (value === 'accepted') loadAnalytics();
    else if (loaded) location.reload();
  }

  const banner = document.createElement('section');
  banner.className = 'cookie-banner';
  banner.setAttribute('aria-label', 'Sütibeállítások');
  banner.hidden = true;
  banner.innerHTML = '<div><strong>Sütibeállítások</strong><p>Az oldal működéséhez szükséges tárolás mellett csak a hozzájárulásoddal használunk Google Analytics mérést. <a href="adatkezeles.html#sutik">Részletek az adatkezelési tájékoztatóban</a>.</p></div><div class="cookie-actions"><button type="button" class="button button-secondary" data-consent="rejected">Elutasítom</button><button type="button" class="button" data-consent="accepted">Elfogadom</button></div>';
  document.body.appendChild(banner);
  banner.addEventListener('click', event => {
    const choice = event.target.closest('[data-consent]');
    if (choice) setConsent(choice.dataset.consent);
  });
  document.querySelectorAll('[data-cookie-settings]').forEach(button => {
    button.addEventListener('click', () => { banner.hidden = false; banner.querySelector('button').focus(); });
  });
  if (stored === 'accepted') loadAnalytics();
  else if (stored !== 'rejected') banner.hidden = false;
})();
