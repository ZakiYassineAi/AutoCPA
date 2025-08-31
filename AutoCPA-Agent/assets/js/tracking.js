// Simple tracking script to monitor affiliate link clicks.
// This script sends data to a Google Apps Script endpoint, which then logs it in a Google Sheet.

(function() {
    // IMPORTANT: Replace this placeholder URL with your actual Google Apps Script Web App URL.
    const GOOGLE_APPS_SCRIPT_URL = 'YOUR_GOOGLE_APPS_SCRIPT_URL_HERE';

    const trackClick = (source, offer) => {
        // If the placeholder URL hasn't been replaced, do not proceed.
        if (GOOGLE_APPS_SCRIPT_URL.includes('YOUR_GOOGLE_APPS_SCRIPT_URL_HERE')) {
            console.log('Tracking script not configured. Please set the GOOGLE_APPS_SCRIPT_URL.');
            return;
        }

        const data = {
            timestamp: new Date().toISOString(),
            source: source,
            offer: offer,
            userAgent: navigator.userAgent,
            referrer: document.referrer,
            url: window.location.href
        };

        // Use navigator.sendBeacon if available for more reliable background sending.
        // Fallback to fetch for older browsers.
        if (navigator.sendBeacon) {
            navigator.sendBeacon(GOOGLE_APPS_SCRIPT_URL, JSON.stringify(data));
        } else {
            fetch(GOOGLE_APPS_SCRIPT_URL, {
                method: 'POST',
                body: JSON.stringify(data),
                keepalive: true
            });
        }
    };

    // Find all links with the 'data-affiliate' attribute and attach a click listener.
    document.querySelectorAll('a[data-affiliate="true"]').forEach(link => {
        link.addEventListener('click', (event) => {
            // Get the source from a data attribute on the link or default to 'main_page'.
            const source = link.dataset.source || 'main_page';
            const offer = link.dataset.offer || 'unknown';
            trackClick(source, offer);
        });
    });
})();
