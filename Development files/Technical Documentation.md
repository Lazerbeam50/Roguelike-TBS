Part I: Wargaming
=

1. AI
2. Attacking
3. Battle setup
4. Mission data
5. Movement
6. Phases
7. Terrain
8. UI
9. Units
10. Unit generation
11. Weapons and spells


Part IX: General and misc
=

1. Game data structure
2. General flow and setup
3. Main menu
4. Sprite scaling
5. Surfaces

---

Part I: Wargaming
=

AI
-

At stage one, the enemy AI should be very simple. Each enemy unit should generate it's attack range, and see if there are any ally units in it. If not, the enemy should wait. If so, the enemy should select the ally in its 
attack range with the lowest current HP, move towards it, and attack it.

Attacking
-

When selecting to attack a target, the following derived attributes are calculated:

- Attack power
- Attack speed
- Avoid
- Critical rate
- Defence power
- Hit rate

The following are then calculated and shown to the player, while asking them if they want to proceed with the attack:

- Accuracy
- Critical chance
- Damage (including if the unit can attack twice)

In addition the game should show both combatants current HP and equipped weapon.

Once the player confirms the attack, its result is calculated as follows:

- Roll to see if the attacker hit. If so, roll for the chance to crit.
  - If the attack was a successful hit or crit, deduct damage from the defender's current HP.
- If the defender is still alive and can counterattack, roll for the chance to hit, and then to crit if the hit was successful. Deduct the appropriate damage from the attacker's current HP.
- Finally, if both units are still alive and one of them has an attack speed of 4 points higher than the other, then they can make a second attack.

Once the outcome has been calculated, the game can show this visually. The attacking unit's turn is then over. 

Battle setup
-

For stage one, generate the player's units and some enemy units using the same method. 

Set up the map by loading the only map from the Maps table. Pull all tiles for this map from the MapTiles table and create the background sprites using this information.

Create both the player and enemy units.

Randomly place units in their appropriate deployment tiles.

Begin player phase.

Mission data
-

For stage one, the game simply checks to see if all enemies are dead, and if so, the mission is considered complete. This check is done after every player action, and the start of the player phase. 

Additionally, the game should also check if the player's units are all still alive, and give a game over if they're not.

Movement
-

Selecting a unit that hasn't acted will generate its movement range and attack range using Cython scripts. A unit's attack range is calculated as its movement range plus its maximum attack range of the equipped weapon. 
Additionally, any nodes taken by an enemy will be considered part of the unit's attack range but not its movement range. Finally, any nodes in both the movement and attack range are removed form the attack range.

Movement range tiles and attack range tiles are coloured blue and red respectively.

Moving the mouse into a node within the current movement range will create a path to it using the A* Cython script. This path will change the tiles in it green. Clicking on a tile within the movement range saves the path to 
that tile and bring up the “move” option. From there, the player can opt to move their unit to that tile through the highlighted path, or click on more tiles, which will then be added to the existing path.

Phases
-

Battle alternates between the player phase and the enemy phase. The player can hit a button to end their phase prematurely, or the game will automatically end the player phase one all player units have acted.

At the start of a phase (either player or enemy), the game should loop through the player or enemy units (as appropriate) and mark them as not having acted yet.

Once a unit has acted, replace its standard sprite with a greyscale one.

Enemy turns are run automatically without player input. Will need to spread them out across frames.

Terrain
-

At stage one, only walkable and unwalkable terrain is available. No bonuses to defence, avoidance, healing or height.

UI
-

UI, as well as any other text elements, need to be a bespoke size as appropriate for the current resolution. UI elements are rendered as sprites and drawn on the finalSurface, and so are unaffected by scrolling.

Units
-

The unit class should be structured with the following attributes:

- id (int)
- gender (int)
- firstName (string)
- lastName (string)
- unitClass (int)
- level (int)
- currentHP (int)
- maxHP (int)
- currentStrength (int)
- maxStrength (int)
- currentMagic (int)
- maxMagic (int)
- currentDexterity (int)
- maxDexterity (int)
- currentSpeed (int)
- maxSpeed (int)
- currentLuck (int)
- maxLuck (int)
- currentDefence (int)
- maxDefence (int)
- currentResistance (int)
- maxResistance (int)
- currentMovement (int)
- maxMovement (int)
- ability (int)
- WeaponsSpells (list of Weapon objects)
- sprite (GameSprite object)
- isDead (bool)
- hasActed (bool)

Unit generation
-

**Stage 1** – Create a unit by randomly selecting a gender, and then a first name, last name and sprite accordingly. Their class will be selected randomly from the stage 1 classes. Their weapon will be a random weapon from 
the classes proficiencies. 

All units will start at level 1, with their attributes equal to the their classes' base stats.

Enemy units are all named “Enemy Soldier”.

Part IX: General and misc
=

Game data structure
-

Will need to set up a relational schema with the following tables and attributes:

- AmbiguousNames
  - id (int)
  - name (text)
- Classes
  - id (int)
  - name (string)
  - usesSwords (int)
  - usesAxes (int)
  - usesLances (int)
  - usesBows (int)
  - usesDaggers (int)
  - usesDestruction (int)
  - usesRestoration (int)
  - catForm (int)
  - bearForm (int)
  - breathWeapon (int – Randomly decide on an element if this is true)
  - usesTime (int)
  - usesEnchanting (int)
  - usesWitchcraft (int)
  - hpBase (int)
  - strengthBase (int)
  - magicBase (int)
  - dexterityBase (int)
  - speedBase (int)
  - defenceBase (int)
  - resistanceBase (int)
  - luckBase (int)
  - hpBaseSD (int)
  - strengthBaseSD (int)
  - magicBaseSD (int)
  - dexterityBaseSD (int)
  - speedBaseSD (int)
  - defenceBaseSD (int)
  - resistanceBaseSD (int)
  - luckBaseSD (int)
  - hpGrowth (int)
  - strengthGrowth (int)
  - magicGrowth (int)
  - dexterityGrowth (int)
  - speedGrowth (int)
  - defenceGrowth (int)
  - resistanceGrowth (int)
  - luckGrowth (int)
  - hpGrowthSD (int)
  - strengthGrowthSD (int)
  - magicGrowthSD (int)
  - dexterityGrowthSD (int)
  - speedGrowthSD (int)
  - defenceGrowthSD (int)
  - resistanceGrowthSD (int)
  - luckGrowthSD (int)
  - movement (int)
  - flying (int)
  - mounted (int)
  - critBonus (int)
  - sprite (text)
- WeaponsSpells
  - id (int)
  - name (text)
  - magic (int)
  - itemType (int – Sword, Axe, Lance, Dagger, Destruction, Holy, Restoration)
  - rank (int)
  - uses (int)
  - power (int)
  - hit (int)
  - crit (int)
  - scalesWith (int – Strength, Dexterity, Magic or None)
  - minRange (int)
  - maxRange (int)
  - weight (int)
  - exp (int)
  - value (int)
  - effect (int)
  - bonus_vs1 (int – Mounted, Flying)
  - bonus_vs2 (int)
- FemaleNames
  - id (int)
  - name (text)
- LastNames
  - id (int)
  - name (text)
- MaleNames
  - id (int)
  - name (text)
- Maps
  - id (int)
  - name (text)
  - tileSet (int)
- MapTiles
  - id (int)
  - x (text – Represents the tiles in the row)
  - y (int – Represents the height of the row)
- MapDeployment
  - id (int – FK for the Maps table)
  - force (int – Player, enemy, ally or other)
  - boss (int – Flags if a boss can spawn in this tile)
  - x (int)
  - y (int)
- Tiles
  - id (int)
  - name (text)
  - def (int)
  - avoid (int)
  - heal (int)
  - moveCost (int)
  - sprite (text)

General flow and setup
-

**main.py** – This module does nothing more than import game.py, run the init, and run the game loop method.

**game.py** – Creates the game class with the following methods:
- **init** – Initiates pygame, sets up the valueholder and its attributes, sets up the screen and fonts, and sets up the first flow manager.
- **main_loop** – Set up a try-except block. Within this block, get pygame events and pass these to the appropriate flow manager. Outside of the event loop, run the appropriate flow manager's update method, refresh the 
background, draw sprites, blit surfaces to the screen. Finally, update the display. The except section should catch all exceptions and display error messaging.
- **quit_game** – simply run pygame.quit() and sys.exit()

**misc.py** – Holds the ValueHolder class, the GameSettings class, and any other classes or functions which do not fit elsewhere.

**sprites.py** – Holds the GameSprite class, as well as classes for buttons and text boxes.

**resources.py** – Loads sprites, sounds, music and backgrounds.

**loaddata.py** – Holds all functions for loading data from SQLite.

**savedata.py** – Holds all functions for saving data to SQLite.

The ValueHolder uses a state integer to determine which of the current managers is in control.

Main menu
-

Handled by a **main_menu.py** MainMenuManager. Just needs to display a title and a “Start Game” button.

Surfaces
-

**screen** – This is the actual window surface (pygame.display.set_mode). Its dimensions are set by the current resolution, which by default are 1280 x 720.

**nativeWorld** – World surface that sprites are originally blitted onto.

**scaledWorld** – Scaled version of the world.

**finalSurface** – A camera cut of the scaledWorld is blitted here, along with any text and UI elements (which are not scaled). This surface is blitted directly onto the screen.

Sprite scaling
-

The nativeWorld is scaled by 2x or 3x to produce the scaledWorld, for resolutions 720p and 1080p respectively.

