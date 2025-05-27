# ShareTarget - WebApp

This repo contains a minimal example for a webapp that is capable of receiving shared data from other apps (eg. text, urls, files).

**Important Code**: (`./www` directory)
- The `manifest.json` file contains a `share_target` section
- The `index.html` file contains a `<script>` section, which parses the **shared data** (via GET Query-Parameters)
- All other files in this repo are related to the Demo App (hosted on Vercel)

**HINT:**
The code has been tested on ...

- User Device: Android-Version 14
- Browser Versions:
    - Mobile Chrome (136.0.7103.125)
    - Mobile Samsung Internet (28.0.0.59)
- Cloud Provider: [Vercel Demo App](https://share-target-webapp.vercel.app/)

The application needs to be installed as a WebApp (or WebAPK), not just as a shortcut! Otherwise, the Android-Device doesn't register the application for receiving shared data (from other applications).

## Demo: How to use?
Please visit the following [demo website](https://share-target-webapp.vercel.app/) to test the `share_target` functionality on your own mobile device.
Follow instructions accordingly:
1. You need to install the WebApp / PWA / WebAPK (whatever you want to call it)
    - Visit the [demo website](https://share-target-webapp.vercel.app/) via **Mobile Chrome Browser** on your **Android Device**.
    - Install the website as a WebApp
2. Then you can open youtube app (as an example) and click on "share video" button.
    - any other app can be also used (which allows sharing data)
3. Here you need to choose "ShareTarget" WebApp from the list of available target apps.
    - **WARNING**: If you don't find "ShareTarget" WebApp in the available list, your setup (android device or chrome version) doesn't support `share_target` functionality
4. All shared information (`title`, `text` and `url`) will be displayed in the WebApp.
    - For `file-sharing` support please refer to following [documentation](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/share_target#receiving_shared_files)

## Usefull Links
Here are some usefull links for further details:
- [Chrome: web share target](https://developer.chrome.com/docs/capabilities/web-apis/web-share-targe)
- [Mozilla: share_target](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/share_target)
- [W3C: Web Share Target](https://w3c.github.io/web-share-target/)
- [FileSharing via WebApp](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/share_target#receiving_shared_files)

## License

This project is licensed under the [MIT License](LICENSE).