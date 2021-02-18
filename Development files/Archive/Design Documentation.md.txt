Part I: Wargaming
=================

1. Abilities
2. Accuracy
3. Attack power
4. Attack speed
5. Attributes
6. Avoid
7. Battle preparation
8. Bonus damage
9. Cavalier mechanics
10. Classes
11. Critical chance
12. Critical damage
13. Critical rate
14. Damage
15. Defence power
16. Destruction magic
17. Direct combat
18. Enemy item drops
19. Enemy reinforcements
20. Equipment
21. Escaping
22. Experience
23. Flying units
24. Fog of war
25. Friendly units
26. Growth rates and levelling up
27. Holy magic
28. Hit rate
29. Indirect combat
30. Items
31. Mission types
32. Mounted units
33. MVP
34. Other units
35. Pikeman mechanics
36. Rescue
37. Shifter mechanics
38. Terrain
39. Trading items
40. Treasure
41. UI
42. Weapon ranks
43. Weight

Part II: Financial management
=============================

1. Contracts
2. Expenses
3. Income
4. Negotiations
5. Treasury

Part III: Army management
=========================

1. Friendships and support groups
2. Personality traits
3. Shopping
4. Training

Part IV: World generation
=========================

1. Factions and NPCs
2. Faction goals
3. Faction relationships
4. World map

Part V: Jobs
============

1. Approaching the player with jobs
2. Finding jobs
3. Refusing a job

Part VI: Travelling
===================

1. Controlling multiple groups
2. Towns and cities
3. Travelling

Part VII: Roguelike mechanics
=============================

1. Attribute distributions
2. Autosaving
3. Game over
4. Permadeath
5. Unit generation

Part VIII: Events
=================

1. Background events
2. Faction and NPC events
3. Unit events

Part IX: General and misc
=========================

1. Gameplay options
2. Main menu
3. Sprite scaling

-----

Part I: Wargaming
=

Accuracy
-

**Stage 1** – Accuracy represents the percentage chance for an attacker to land a hit on a defender. It is calculated as follows:

*Accuracy = Min((Max((HitRate – Avoid), 0)), 100)*

Attack power
-

**Stage 1** – Attack power represents how much damage the attacker will deal under optimum conditions, excluding abilities and critical hits. It is calculated as follows:

*AttackPower = ScalingAttribute + (Weapon or Spell Power * Weapon Bonus)*

Here, “ScalingAttribute” refers to strength, dexterity or magic depending on weapon or spell equipped. “Weapon Bonus” refers to scalars such as the 2x bonus for using a lance against a cavalier.

Attack speed
-

**Stage 1** – Attack speed is used to calculate whether or not a unit will attack twice in a fight, and is used in calculating the “avoid” statistic. The formula is as follows:

*IF WeaponWeight <= Strength THEN AttackSpeed = Speed*

*ELSE Attack Speed = Speed – (WeaponWeight – Strength)*

If one unit's attack speed is at least 4 points greater than its opponent, then it will attack twice in a fight.

Attributes
-

**Stage 1** – A units 8 main attributes are as follows:

- HP – Hit points.
- Strength – Used to determine damage with strength weapons, attack speed, and which friendly units can be rescued by this unit based on the friendly unit's weight.
- Magic – Determines damage with spells and some magic weapons. Also improves healing and increases the success rate of debuffing spells.
- Dexterity – Determines a unit's chance to hit, make critical hits, and to deal damage with dexterity weapons.
- Speed – Determines attack speed and chance to dodge attacks.
- Defence – Reduces damage taken from non-magical attacks.
- Resistance – Reduces damage taken from magical attacks, and reduces the chance of suffering debuffs from enemy spells.
- Luck – Increases the unit's chance to hit, dodge and avoid critical hits. 

Avoid
-

**Stage 1** – Avoid is used to calculate accuracy, and represents a unit's ability to dodge. It is calculated as follows:

*Avoid = (AttackSpeed * 2) + Luck + Terrain Bonus*

Cavalier mechanics
-

**Stage 2+** Cavaliers receive a bonus or penalty to their strength and speed attributes for a round based on how they move on their turn, if at all. The idea is that Cavaliers should be strongest when charging the enemy, and more vulnerable when stationary.

First, a movement score is calculated as follows:

*movementScore = abs(startX – finishX) + abs(startY – finishY)*

Then, the modifier to strength and speed is pulled from the following table:

| Movement score | Strength and speed modifier |
|-|-|
|>= 8|+2|
|6 to 7|+1|
|4 to 5|0|
|1 to 3|-1|
|0|-2|

Classes
-

**Stage 1** – Every unit has a class assigned to it which determines which weapons it can use, its typical (but not its exact) base stats and growth rates, weight, movement allowance, and other features, such as whether or not it counts as flying or mounted, class abilities and crit bonuses.

Critical chance
-

**Stage 1** – Critical chance is the exact chance a unit has to land a critical hit. It is calculated as follows:

*CriticalChance = Max((Min((CriticalRate – Luck), 100)), 0)*

Critical damage
-

**Stage 1** – Once a critical hit is confirmed, the damage dealt is calculated as follows:

*CriticalDamage = (AttackPower – DefencePower) * 2*


Critical rate
-

**Stage 1** – Represents a units chance to cause a critical hit, and is used to calculate crit chance. It is calculated as follows:

*CriticalRate = WeaponCritical + (Dexterity/2) + ClassBonus*

Damage
-

**Stage 1** – This is how much health the target loses after an attack.

*Damage = AttackPower  – DefencePower*

Damage must be at least 0

Defence power
-

**Stage 1** – Used to reduce damage. Calculated as:

*DefencePower = TerrainBonus + DefendingStat**

“DefendingStat” is Defence if the attack is non-magic, and Resistance if it is magical.

Destruction magic
-

**Stage 1** – Destruction magic comes in three standard types: Fire, Wind and Ice. Fire, Wind and Ice attacks enjoy bonus damage against Trolls/Shifters, Flying units, and Mythical Beasts respectively.

Direct combat
-

**Stage 1** – To initiate a direct attack, the attacker be equipped with a melee weapon or a spell, and must end their movement in one of the targets adjacent squares (diagonal squares do not count). This also works if the attacker starts its turn adjacent to its target.

The target will always counter-attack providing that it is also equipped with a melee weapon or spell, as is still alive after the aggressor's attack. After this, either the attacker or target will make a third attack according to the attack speed rules.

Experience
-

**Stage 2+** Experience should be gained after a battle, rather than during one. Additionally, experience earned should be based on factors such as:

- Damage dealt as a percentage of enemy health (scaled by level difference)
- Damage healed
- Number of refreshes
- Number of successful friendly buffs
- Number of successful enemy debuffs (scaled by level difference)
- Completed mission (Scaled by whether or not the unit actually *participated, and the difficulty of the mission)

*Participated means that the unit either dealt damage, healed allies, refreshed allies or buffed/debuffed units. A threshold should be applied to each of these (e.g. need to deal at least 50% damage).

Growth rates and levelling up
-

**Stage 2+** For each attribute, a unit has a percentage called a growth rate assigned to it, which represents its chance to improve upon level up. For example, a 50% growth rate in strength would mean a unit would have a 50% chance to enjoy a +1 to strength at level up, and would typically earn +1 strength every two levels.

Growth rates are typically between 0% and 100%, but can be higher or lower depending on the distribution they are pulled from. Growth rates below 0% are no different from 0%, as they still mean that the assigned attribute will never increase at level up. Growth rates above 100% give a chance for +2 or even +3 increases in the assigned attribute. 

The increase an attribute receives at level up is calculated as follows:

*increase = 0*

*If randint(1, 100) <= GrowthRate: increase += 1*

*If randint(1, 100) <= (GrowthRate – 100): increase += 1*

*If randint(1, 100) <= (GrowthRate – 200): increase += 1*

With the above method and a Growth Rate above 200, it is possible for a unit's attribute to increase by 3 at level up, but this is expected to be extremely rare, if at all possible.

Hit rate
-

**Stage 1** – Represents chance to hit and is a computational stepping stone to accuracy:

*HitRate = WeaponAccuracy + (Dexterity * 2) + Luck*

Indirect combat
-

**Stage 1** – To initiate an indirect attack, the attacker be equipped with a ranged weapon or a spell, and must end their movement on square away from their target (diagonal squares also count). This also works if the attacker starts its turn one square away from its target.

The target will always counter-attack providing that it is also equipped with a ranged weapon or spell, as is still alive after the aggressor's attack. After this, either the attacker or target will make a third attack according to the attack speed rules.

Mission types
-

**Stage 1** – Initially, only rout will be available as a mission type.

**Stage 2+** Add the additional objectives:
- Defeat the boss
- Defend for X turns
- Escape
- Arrive
- Protect for X turns
- Seize
- Survive for X turns
- Conquest (Hold more points than the opponent by the end of the turn count)
- Capture the flag

Terrain
-

**Stage 1** – Initially, only field tiles are available. 

**Stage 2+** Include woods, hills, mountains, sea, swamp and their equivalents for other tilesets.

UI
-

**Stage 1** – Only a simple UI is needed which shows terrain information in a corner box, and reports in another corner box. When a unit is selected the following information should also be shown:

- Name
- Level and Class
- HP bar
- XP bar 

It could also show:

- Core attributes


Part VII: Roguelike mechanics
=

Attribute distributions
-

**Stage 2+** When generating playable and recruitable units, the game will need to generate the unit's base stats and growth rates randomly, while aiming to typically keep them close to the typical values set out by that unit's class. For example, Barbarians should normally have high strength growth, but can, on occasion have low strength growth closer to that of a typical Swordsman or abnormally high strength growth (e.g. above 100%).

To generate base stats and growth rates for a unit, the game generates a normal distribution per attribute, per class, which uses the classes' pre-determined mean value and standard deviation. Such a distribution is determined at the start of the game (one for growth rates and one for base stats) and the recruitable characters are created then and saved. Should more characters need to be created later, a new distributions will need to be set up. Alternatively, the game could save the distribution seeds and replicate distributions exactly.


Unit generation
-

**Stage 1** – For now, give the player four units of random classes, with the classes' average base stats as the unit's stats.

Part IX: General and misc
=

Main menu
-

**Stage 1** – Just a “start game” option for now.

Sprite scaling
-

**Stage 1** –  The standard tileset size is 24x24.

The native world resolution will be 480 x 360, which is 20 tiles by 15 tiles – a ratio of 4:3. When scaling this to larger, 16:9 resolutions, more of the world will be visible on screen, with some tiles being cut-off.

The game's default resolution will be 1280 x 720.

**Stage 2+** Allow adjustment to 1080p.