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

* Make ellipses in `Button.svelte` when text is too long not overflow to the right
* Add cool banner backgroud to H1 heading (similar to how the button works)
* Add tab indeces to checkboxes and all other input elements
* Add select all for checkbox lists
* Add locked state for buttons and checkboxes (make them gray using filter: saturation(0%) and unclickable)
* Add custom scrollbar in EU4 style? <https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_custom_scrollbar>
* Add credits file which says where everything comes from (textures, sounds, idea etc.) and add it as a link to the footer
* Button text is not centered when button is shorter than one `button_middle.png`
