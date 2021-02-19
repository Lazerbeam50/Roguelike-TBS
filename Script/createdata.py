"""
Used to set up the empty database and tables.
"""
import sqlite3

def set_up_empty_database():
    db = sqlite3.connect('Game data/game_data')
    cursor = db.cursor()

    #Ambiguous names

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS AmbiguousNames
    (
    id INTEGER PRIMARY KEY,
    name TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Classes
    (
    id INTEGER PRIMARY KEY,
    name TEXT,
    usesSwords INTEGER,
    usesAxes INTEGER,
    usesLances INTEGER,
    usesBows INTEGER,
    usesDaggers INTEGER,
    usesDestruction INTEGER,
    usesRestoration INTEGER,
    catForm INTEGER,
    bearForm INTEGER,
    breathWeapon INTEGER,
    usesTime INTEGER,
    usesEnchanting INTEGER,
    usesWitchcraft INTEGER,
    hpBase INTEGER,
    strengthBase INTEGER,
    magicBase INTEGER,
    dexterityBase INTEGER,
    speedBase INTEGER,
    defenceBase INTEGER,
    resistanceBase INTEGER,
    luckBase INTEGER,
    hpBaseSD INTEGER,
    strengthBaseSD INTEGER,
    magicBaseSD INTEGER,
    dexterityBaseSD INTEGER,
    speedBaseSD INTEGER,
    defenceBaseSD INTEGER,
    resistanceBaseSD INTEGER,
    luckBaseSD INTEGER,
    hpGrowth INTEGER,
    strengthGrowth INTEGER,
    magicGrowth INTEGER,
    dexterityGrowth INTEGER,
    speedGrowth INTEGER,
    defenceGrowth INTEGER,
    resistanceGrowth INTEGER,
    luckGrowth INTEGER,
    hpGrowthSD INTEGER,
    strengthGrowthSD INTEGER,
    magicGrowthSD INTEGER,
    dexterityGrowthSD INTEGER,
    speedGrowthSD INTEGER,
    defenceGrowthSD INTEGER,
    resistanceGrowthSD INTEGER,
    luckGrowthSD INTEGER,
    movement INTEGER,
    flying INTEGER,
    mounted INTEGER,
    critBonus INTEGER,
    sprite TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS WeaponsSpells
    (
    id INTEGER PRIMARY KEY,
    name TEXT,
    magic INTEGER,
    itemType INTEGER,
    rank INTEGER,
    uses INTEGER,
    power INTEGER,
    hit INTEGER,
    crit INTEGER,
    scalesWith INTEGER,
    minRange INTEGER,
    maxRange INTEGER,
    weight INTEGER,
    exp INTEGER,
    value INTEGER,
    effect INTEGER,
    bonus_vs1 INTEGER,
    bonus_vs2 INTEGER
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS FemaleNames
    (
    id INTEGER PRIMARY KEY,
    name TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS LastNames
    (
    id INTEGER PRIMARY KEY,
    name TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS MaleNames
    (
    id INTEGER PRIMARY KEY,
    name TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS AmbiguousNames
    (
    id INTEGER PRIMARY KEY,
    name TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Maps
    (
    id INTEGER PRIMARY KEY,
    name TEXT,
    tileset INTEGER
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS MapTiles
    (
    id INTEGER,
    x TEXT,
    y INTEGER
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS MapDeployment
    (
    id INTEGER,
    force INTEGER,
    boss INTEGER,
    x INTEGER,
    y INTEGER
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Tiles
    (
    id INTEGER PRIMARY KEY,
    name TEXT,
    def INTEGER,
    avoid INTEGER,
    heal INTEGER,
    moveCost INTEGER,
    sprite INTEGER
    )
    ''')

    db.commit()
    cursor.close()
    db.close()

set_up_empty_database()