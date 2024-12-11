# Changelog.md

## 12/13/24 v1.0
- NO GLOBALS!!
  - removed all global varibles
- NO BREAKS!
  - heck yeah baby
- Made FFA gamemode work for arrows mode
- Added more comments
- Added lots of exception handling
- Version 1.0 Release!
- submitting this as my final project for Programming I
## 12/2/24 v0.8
*Yes I know I went from 2 to 8. This is a significant update*
- CRASH DETECTION!
  - now the game won't randomly die
  - debug.mike gets value "True" when game was closed wrongly
  - if True, sends player to crash screen and refreshes game so it doesn't crash
- Added some error detection and mitigation
- Changed some values from strings to ints
- optimized some code and smashed some bugs
- GOT RID OF STORAGE.PY FINALLY
  - but I still 1 global variable, the target image :/
- added some more stuff to futureplans.md
- added Free For All mode!
  - hit as many targets as you can in 30 seconds
## 11/18/24 v0.7
- Configured gamemode selection screen
- Moving more variables away from storage.py
- added arrow key movement but only for Target Practice gamemode
  - Will be adding to other modes soon
- configured more modes
## 11/17/24 v0.6
- Added new images
- Added the choice selection screen for gamemodes 
- Updated How-to-play screen
## 11/13/24 v0.5
- Merged settings.py and storage.py
  - Did this to make things simpler and because they were just storing variables and non-changing values
- Created settings.txt
  - Used for storing individual values for settings that do change. Ex: background color, target size, etc.
- Saving values in settings.txt now works
  - Need to make a "reset to defaults" button
## 11/11/24 v0.4
- Removed all instances of exception handling, except for GraphicsErorrs.
  - This is because I found it easier to be able to tell exactly what goes wrong when I get an error
- Added storage.py
  - This is for all variable/object storage. It is imported into archery.py
- Added changelog.md
  - A changelog!
- Added How-to-Play screen and fixed bugs with returning to main() after settingsScreen()
- Added some templates for settings that I can change
  - Background color and target size