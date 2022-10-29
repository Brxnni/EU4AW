# EU4AW

## How to use

You can build it like this:

```cmd
# git clone the repo into "EU4AW"
cd EU4AW
cd src
# build svelte to ./dist
npm run build
# start preview server for static files
npm run preview
```

## Dirs

### ./src

Source files for the Website (Made in Svelte. God I love Svelte so much)

### ./etc

Tools I used to make the website.

Includes <a href="https://gitmoji.dev">
  <img src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg?style=flat-square" alt="Gitmoji">
</a>.

### ./extracted

Files grabbed from the EU4 source that may be used for the Website, but are still unorganized.

## TODO

* Make border of `BoardContainer.svelte` look nicer by adding some semi-transparent pixels to `./assets/gold_border.png`
* Make ellipses in `Button.svelte` when text is too long not overflow to the right
* Make good favicon
* Replace `button_hover_*.png` with CSS filters, just like with checkboxes (perhaps `brightness(110%)` could work?)
* Add site metadata
* Make font size smaller on mobile devices
* Mirrored end for buttons doesn't look quite right, fix that
* Fix .wav files not being served on build or dev
* Add cool banner backgroud to H1 heading (similar to how the button works)
