# load-screen
Wanna create a loading screen ideal for your Python console project? You came to the right place.
- Use "pip install loadgui" to install library
- (Package published in PyPI as "loadgui 1.0.0")

## Docs
First of all, to test if the library is working, run the __main__.py inside loadgui-master\loadgui
- If nothing outputs/Outputs "OS compatible with library", you are good to go!

### Start the loading screen
To start loading: 
- Import the library. Import loadgui.
- Prefixes for next step: D = delay, a = all, t = text, r = right, d = down, l = left, u = up
- Call load_screen(rD, dD, lD, uD, aD, t)

OPTIONAL STEPS [
- For 1 second delay for each: load_screen(0, 0, 0, 0, 1, "TEXT")
- For 1 second delay added for each: load_screen(0, 1, 2, 3, 1, "TEXT")

]

No need to download any additional libraries