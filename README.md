# share-target-webapp

This repo contains a minimal example for a webapp that is capable of receiving shared data from other apps (eg. text, urls, files).

**Important Code**:
- The `manifest.json` file contains a `share_target` section
- The `index.html` file contains a `<script>` section, which parses the **shared data** (from Query-Parameters)

**HINT:**
The code has been tested on ...
- Cloud Provider: [Vercel Platform](https://share-target-webapp.vercel.app/)
- User Device: Android-Version 14
- Browser Versions:
    - Mobile Chrome (136.0.7103.125)
    - Mobile Samsung Internet (28.0.0.59)

The application needs to be installed as a WebApp (or WebAPK), not just as a shortcut! Otherwise, the Android-Device didn't register the application for receiving shared data (from other applications).

### Usefull Links
- [Chrome: web share target](https://developer.chrome.com/docs/capabilities/web-apis/web-share-targe)
- [Mozilla: share_target](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/share_target)
- [W3C: Web Share Target](https://w3c.github.io/web-share-target/)