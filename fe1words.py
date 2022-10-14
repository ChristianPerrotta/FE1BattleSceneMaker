#Constants for coordinates
CO_ENEMY_HP_BAR = (17, 186); CO_ALLY_HP_BAR = (137, 186)
CO_ENEMY_LV = (104,152); CO_ALLY_LV = (224,152)

CO_TERRAIN = (40, 136)
CO_ENEMY_TERRAIN_ICON = (96, 153); CO_ALLY_TERRAIN_ICON = (136, 153)

CO_ATK_BOX = (16, 136)
CO_MSG_BOX = (56, 136)
CO_EXP_BOX = (104, 192)
CO_EXP_BARS = (144, 204)

CO_ENEMY_NAME = (16, 152); CO_ALLY_NAME = (136, 152)
CO_ENEMY_CLASS = (16,168); CO_ALLY_CLASS = (136,168)
CO_ENEMY_WEAPON = (64,168); CO_ALLY_WEAPON = (184,168)
CO_ENEMY_TERRAIN = (48,152); CO_ALLY_TERRAIN = (176,152)

CO_ATK_MSG = (24,160)
CO_FINAL_MSG_BLACK_SCREEN = (64,144)

CO_ALLY_SPRITE = (186,127); CO_ENEMY_SPRITE = (70,127)

PURE_WHITE = (255,255,255,255)
PINK_WHITE = (255,191,179,255)
LIGHT_BLUE = (63,191,255,255)
DARK_BLUE = (31,56,239,255)
LIGHT_PINK = (247,123,255,255)
PEGASUS_PINK = (255,88,159,255)
DARK_PINK = (171,0,19,255)

#Sprites
sprites = {'Cavalier':20, 'Knight':23, 'Pegasus Knight':22, 'Paladin':25, 'Wyvern Knight':21, 'Mercenary':9,
           'Fighter':10, 'Pirate': 10, 'Thief':5, 'Hero':15, 'Archer':14, 'Hunter':14, 'Ballistician':28,
           'Horseman':12, 'Sniper':10, 'Freelancer':7, 'Manakete':11, 'Mage':4, 'Curate':3, 'Bishop':4,
           'General':11, 'Lord':15, 'Medeus':6}

sprite_sizes = {'Cavalier':47, 'Knight':48, 'Pegasus Knight':57, 'Paladin':54, 'Wyvern Knight':96, 'Mercenary':39,
                'Fighter':53, 'Pirate': 47, 'Thief':30, 'Hero':45, 'Archer':32, 'Hunter':31, 'Ballistician':63,
                'Horseman':38, 'Sniper':42, 'Freelancer':31, 'Manakete':86, 'Mage':43, 'Curate':15, 'Bishop':35,
                'General':53, 'Lord':37, 'Medeus':96}

#Constants for Alphabet
aA = (0,0); aB = (8,0); aC = (16,0); aD = (24,0); aE = (32,0); aF = (40,0); aG = (48,0); aH = (56,0)
aI = (64,0); aJ = (72,0); aK = (80,0); aL = (88,0); aM = (96,0); aN = (104,0); aO = (112,0); aP = (120,0)
aQ = (128,0); aR = (136,0); aS = (144,0); aT = (152,16); aU = (160,16); aV = (168,16); aW = (176,16)
aX = (184,0); aY = (192,0); aZ = (200,0); SPACE = (208,0)

#Constants for Number
N0 = (0,8); N1 = (8,8); N2 = (16,8); N3 = (24,8); N4 = (32,8); N5 = (40,8)
N6 = (48,8); N7 = (56,8); N8 = (64,8); N9 = (72,8)

#Constants for punctuation etc.
EXCL = (80,8); PERC = (88,8); APOS = (96,8); OPEN_PAREN = (104,8); CLOSE_PAREN = (112,8); ASTER = (120,8)
"!               %              '                 (                     )                    *           "
#Constants for Hiragana
ha = (0,16); hA = (8,16); hi = (16,16); hI = (24,16); hu = (32,16)
hU = (40,16); he = (48,16); hE = (56,16); ho = (64,16); hO = (72,16)
hKA = (80,16); hKI = (88,16); hKU = (96,16); hKE = (104,16); hKO = (112,16)
hSA = (120,16); hSHI = (128,16); hSU = (136,16); hSE = (144,16); hSO = (152,16)
hTA = (160,16); hCHI = (168,16); htsu = (176,16); hTSU = (184,16); hTE = (192,16); hTO = (200,16)

hNA = (0,24); hNI = (8,24); hNU = (16,24); hNE = (24,24); hNO = (32,24)
hHA = (40,24); hHI = (48,24); hFU = (56,24); hHE = (64,24); hHO = (72,24)
hMA = (80,24); hMI = (88,24); hMU = (96,24); hME = (104,24); hMO = (112,24)
hya = (120,24); hYA = (128,24); hyu = (136,24); hYU = (144,24); hyo = (152,24); hYO = (160,24)
hRA = (168,24); hRI = (176,24); hRU = (184,24); hRE = (192,24); hRO = (200,24)

hWA = (0,32); hWO = (8,32); hNN = (16,32); TENTEN = (24,37); MARU = (32,36); MID_DOT = (40,32)
DASH = (48,32); TEN = (56,32); PERIOD = (64,32); OPEN_KAGI = (72,32); CLOSE_KAGI = (80,32)

#Constants for Katakana
ka = (0,40); kA = (8,40); ki = (16,40); kI = (24,40); ku = (32,40)
kU = (40,40); ke = (48,40); kE = (56,40); ko = (64,40); kO = (72,40)
kKA = (80,40); kKI = (88,40); kKU = (96,40); kKE = (104,40); kKO = (112,40)
kSA = (120,40); kSHI = (128,40); kSU = (136,40); kSE = (144,40); kSO = (152,40)
kTA = (160,40); kCHI = (168,40); ktsu = (176,40); kTSU = (184,40); kTE = (192,40); kTO = (200,40)

kNA = (0,48); kNI = (8,48); kNU = (16,48); kNE = (24,48); kNO = (32,48)
kHA = (40,48); kHI = (48,48); kFU = (56,48); kHE = (64,48); kHO = (72,48)
kMA = (80,48); kMI = (88,48); kMU = (96,48); kME = (104,48); kMO = (112,48)
kya = (120,48); kYA = (128,48); kyu = (136,48); kYU = (144,48); kyo = (152,48); kYO = (160,48)
kRA = (168,48); kRI = (176,48); kRU = (184,48); kRE = (192,48); kRO = (200,48)

kWA = (0,56); kWO = (8,56); kNN = (16,56)

#Units Per Class

ally_units = {'Lord':['Marth'],
              'Mercenary':['Ogma', 'Navarre', 'Caesar', 'Radd'],
              'Hero':['Ogma', 'Navarre', 'Caesar', 'Radd', 'Astram', 'Samson'],
              'Thief':['Julian', 'Rickard'],
              'Freelancer':['Xane'],
              'Fighter':['Bord', 'Cord', 'Barst'],
              'Pirate':['Darros'],
              'Archer':['Gordin', 'Tomas'],
              'Sniper':['Gordin', 'Tomas', 'Jeorge'],
              'Hunter':['Castor'],
              'Horseman':['Sedgar', 'Wolf'],
              'Cavalier':['Abel', 'Cain', 'Matthis', 'Roshea', 'Vyland', 'Hardin'],
              'Paladin':['Abel', 'Cain', 'Matthis', 'Roshea', 'Vyland', 'Hardin', 'Jagen', 'Midia', 'Arran'],
              'Knight':['Draug', 'Roger', 'Dolph', 'Macellan'],
              'General':['Lorenz'],
              'Pegasus Knight':['Caeda', 'Catria', 'Palla', 'Est'],
              'Wyvern Knight':['Caeda', 'Catria', 'Palla', 'Est', 'Minerva'],
              'Ballistician':['Jake', 'Beck'],
              'Mage':['Merric', 'Linde'],
              'Curate':['Wrys', 'Lena', 'Maria', 'Elice'],
              'Bishop':['Merric', 'Linde','Wrys', 'Lena', 'Maria', 'Elice','Wendell', 'Boah', 'Gotoh'],
              'Manakete':['Tiki', 'Bantu']}

enemy_units = {'Mercenary':['Navarre', 'Grust', 'Ruffian', 'Raman', 'Opponent'],
              'Hero':['Astram', 'Grust', 'Dolhr', 'Raman', 'Opponent'],
              'Thief':['Rickard', 'Galder', 'Soothsire', 'Macedon', 'Grust', 'Pyrathi', 'Gra', 'Khadein',
                       'Dolhr', 'Raman', 'Sable Knight', 'Dragoon', 'Opponent'],
              'Freelancer':['Xane', 'Opponent'],
              'Fighter':['Hyman', 'Soothsire', 'Macedon', 'Opponent'],
              'Pirate':['Darros','Gazzak', 'Gomer', 'Galder', 'Pyrathi', 'Opponent'],
              'Archer':['Galder', 'Macedon', 'Grust', 'Gra', 'Opponent'],
              'Sniper':['Grust', 'Gra', 'Dolhr', 'Raman', 'Dragoon', 'Opponent'],
              'Hunter':['Castor', 'Galder', 'Soothsire', 'Macedon', 'Pyrathi', 'Raman', 'Opponent'],
              'Horseman':['Macedon', 'Grust', 'Dolhr', 'Sable Knight', 'Dragoon', 'Opponent'],
              'Cavalier':['Matthis', 'Bentheon', 'Macedon', 'Grust', 'Dolhr', 'Sable Knight', 'Opponent'],
              'Paladin':['Heimler', 'Sternlin', 'Camus', 'Orridyon', 'Grust', 'Sable Knight', 'Dragoon', 'Opponent'],
              'Knight':['Roger', 'Merach', 'Kannival', 'Macedon', 'Grust', 'Gra', 'Dolhr', 'Opponent'],
              'General':['Emereus', 'Harmein', 'Zharov', 'Jiol', 'Hollstadt', 'Grust', 'Sable Knight',
                         'Dragoon', 'Dolhr', 'Opponent'],
              'Pegasus Knight':['Catria', 'Palla', 'Est', 'Macedon', 'Dragoon', 'Grust', 'Dolhr', 'Opponent'],
              'Wyvern Knight':['Minerva', 'Michalis', 'Dragoon', 'Grust', 'Dolhr', 'Reinforcements', 'Opponent'],
              'Ballistician':['Jake', 'Grigas', 'Grust', 'Gra', 'Sable Knight', 'Dragoon', 'Opponent'],
              'Mage':['Macedon', 'Pyrathi', 'Grust', 'Khadein', 'Dolhr', 'Raman', 'Dragoon', 'Opponent'],
              'Curate':['Maria', 'Macedon', 'Grust', 'Pyrathi', 'Grust', 'Gra', 'Khadein', 'Dolhr', 'Sable Knight', 'Raman', 'Dragoon'],
              'Bishop':['Wendell', 'Volzhin', 'Gharnef', 'Khadein', 'Dolhr', 'Dragoon', 'Opponent'],
              'Manakete':['Tiki', 'Mannu', 'Khozen', 'Morzas', 'Xemcel', 'Medeus', 'Grust', 'Dolhr']}

#Unit Names in Japanese

namesJP = {'Marth':[kMA, kRU, kSU],'Ogma':[kO, kKU, TENTEN, kMA], 'Navarre':[kNA, kHA, TENTEN, DASH, kRU],
           'Caesar':[kSHI, DASH, kSA, TENTEN, DASH], 'Radd':[kRA, kTE, TENTEN, ki],
           'Astram':[kA, kSU, kTO, kRI, kA], 'Samson':[kSA, kMU, kSO, kNN],
           'Julian':[kSHI, TENTEN, kyu, kRI, kA, kNN], 'Rickard':[kRI, kKA, DASH, kTO, TENTEN],
           'Xane':[kCHI, ke, kI, kNI, DASH],'Bord':[kSA, kSHI, TENTEN], 'Cord':[kMA, kSHI, TENTEN],
           'Barst':[kHA, TENTEN, DASH, kTSU], 'Darros':[kTA, TENTEN, kRO, kSU],
           'Gordin':[kKO, TENTEN, DASH, kTO, TENTEN, kNN], 'Tomas':[kTO, DASH, kMA, kSU],
           'Jeorge':[kSHI, TENTEN, kyo, kRU, kSHI, TENTEN, kyu],
           'Castor':[kKA, kSHI, kMU],'Sedgar':[kSA, TENTEN, kKA, TENTEN, kRO], 'Wolf':[kU, kRU, kFU],
           'Abel':[kA, kHE, TENTEN, kRU], 'Cain':[kKA, kI, kNN], 'Matthis':[kMA, kCHI, kSU],
           'Roshea':[kRO, kSHI, ke], 'Vyland':[kHI, TENTEN, kRA, kKU], 'Hardin':[kHA, DASH, kTE, TENTEN, ki, kNN],
           'Jagen':[kSHI, TENTEN, ke, kI, kKA, TENTEN, kNN], 'Midia':[kMI, kTE, TENTEN, ki, kA],
           'Arran':[kA, kRA, kNN], 'Draug':[kTO, TENTEN, DASH, kKA, TENTEN],
           'Roger':[kRO, kSHI, TENTEN, kya, DASH], 'Dolph':[kTO, kMU, kSU], 'Macellan':[kMI, kSHI, ke, kRA, kNN],
           'Lorenz':[kRO, kRE, kNN, kSU], 'Caeda':[kSHI, DASH, kTA, TENTEN], 'Catria':[kKA, kCHI, kyu, kA],
           'Palla':[kHA, MARU, kO, kRA], 'Est':[kE, kSU, kTO], 'Minerva':[kMI, kNE, kRU, kHA, TENTEN],
           'Jake':[kSHI, TENTEN, ke, kI, kKU], 'Beck':[kHE, TENTEN, ktsu, kKU],'Merric':[kMA, kRI, kKU],
           'Linde':[kRI, kNN, kTA, TENTEN], 'Wrys':[kRI, kFU], 'Lena':[kRE, kNA],
           'Maria':[kMA, kRI, kA], 'Elice':[kE, kRI, kSU],'Wendell':[kU, ke, kNN, kTE, TENTEN, kRU],
           'Boah':[kHO, TENTEN, kA], 'Gotoh':[kKA, TENTEN, kTO, DASH], 'Tiki':[kCHI, kKI],
           'Bantu':[kHA, TENTEN, kNU, kTO, ku],
           #Enemy Territories and Groups
           'Grust':[kKU, TENTEN, kRU, kNI, kA, hHE, hI], 'Ruffian':[hNA, hRA, hSU, TENTEN, hMO, hNO],
           'Raman':[kRA, DASH, kMA, kNN, hHE, hI], 'Dolhr':[kTO, TENTEN, kRU, DASH, kA, hHE, hI],
           'Galder':[kKA, TENTEN, kRU, kTA, TENTEN, hHE, hI],
           'Soothsire':[kSA, kMU, kSHI, kA, kNN], 'Macedon':[kMA, kKE, kTO, TENTEN, kNI, kA, hHE, hI],
           'Pyrathi':[kHE, MARU, kRA, kTE, ki, hHE, hI], 'Gra':[kKU, TENTEN, kRA, hHE, hI],
           'Khadein':[kKA, kTA, TENTEN, kI, kNN, kMA, DASH, kSHI, TENTEN],
           'Sable Knight':[hKU, hRO, hKI, hSHI, hTA, TENTEN, hNN],
           'Dragoon':[hRI, hyu, hU, hKI, hSHI, hTA, TENTEN, hNN],
           'Opponent':[hTE, hKI], 'Reinforcements':[hSO, TENTEN, hU, hE, hNN, hFU, TENTEN, hTA, hI],
           #Enemy Boss Names
           'Hyman':[kHA, kI, kMA, kNN], 'Gazzak':[kKA, TENTEN, kSA, TENTEN, ktsu, kKU],
           'Gomer':[kKO, TENTEN, kME, kSU], 'Emereus': [kMA, kRI, kO, kNE, kSU],
           'Bentheon':[kHE, TENTEN, kNN, kSO, kNN], 'Heimler':[kHI, kMU, kRA, DASH],
           'Sternlin':[kSU, kTA, DASH, kRO, kNN],
           'Camus':[kKA, kMI, kyu], 'Orridyon':[kO, DASH, kTA, TENTEN, kI, kNN], 'Merach':[kMU, kRA, kKU],
           'Kannival':[kKA, kNA, kRI, kSU], 'Michalis':[kMI, kSHI, ke, kI, kRU],
           'Volzhin':[kHO, TENTEN, DASH, kSE, TENTEN, kNN], 'Gharnef':[kKA, TENTEN, DASH, kNE, kFU],
           'Mannu':[kMA, kNU, DASH], 'Khozen':[kSHI, kyo, DASH, kSE, TENTEN, kNN],
           'Morzas':[kMO, DASH, kSE, TENTEN, kSU],
           'Xemcel':[kSE, TENTEN, kMU, kSE, kRU], 'Medeus':[kME, kTE, TENTEN, ki, kU, kSU]}

#Classes
classes = ['Lord', 'Mercenary', 'Hero', 'Thief', 'Freelancer', 'Fighter', 'Pirate', 'Archer', 'Sniper', 'Hunter',
           'Horseman', 'Cavalier', 'Paladin', 'Knight', 'General', 'Pegasus Knight', 'Wyvern Knight', 'Ballistician',
           'Mage', 'Curate', 'Bishop', 'Manakete']
en_classes = ['Mercenary', 'Hero', 'Thief', 'Freelancer', 'Fighter', 'Pirate', 'Archer', 'Sniper', 'Hunter',
           'Horseman', 'Cavalier', 'Paladin', 'Knight', 'General', 'Pegasus Knight', 'Wyvern Knight', 'Ballistician',
           'Mage', 'Curate', 'Bishop', 'Manakete']
sword_classes = ['Lord', 'Mercenary', 'Hero', 'Thief', 'Freelancer', 'General']
sword_and_lance_classes = ['Cavalier', 'Paladin', 'Knight', 'Pegasus Knight', 'Wyvern Knight']
axe_classes = ['Fighter', 'Pirate']
bow_classes = ['Archer', 'Sniper', 'Hunter', 'Horseman']
dragon_classes = ['Manakete']

#Class names in JP

classesJP = {'Lord':[kRO, DASH, kTO, TENTEN], 'Mercenary':[hYO, hU, hHE, hI], 'Hero':[hYU, hU, hSHI, hya],
             'Thief':[hTO, hU, hSO, TENTEN, hKU], 'Freelancer':[kKO, kMA, kNN, kTO, TENTEN],
             'Fighter':[hSE, hNN, hSHI], 'Pirate':[hKA, hI, hSO, TENTEN, hKU],
             'Archer':[kA, DASH, kCHI, kya, DASH], 'Sniper':[kSU, kNA, kI, kHA, MARU, DASH],
             'Hunter':[kHA, kNN, kTA, DASH], 'Horseman':[kHO, DASH, kSU, kME, kNN],
             'Cavalier':[aS, kNA, kI, kTO], 'Paladin':[kHA, MARU, kRA, kTE, TENTEN, ki, kNN],
             'Knight':[aA, kNA, kI, kTO], 'General':[hSHI, hyo, hU, hKU, TENTEN, hNN],
             'Pegasus Knight':[aP, kNA, kI, kTO], 'Wyvern Knight':[aD, kNA, kI, kTO],
             'Ballistician':[kSHI, kyu, DASH, kTA, DASH], 'Mage':[hMA, hTO, TENTEN, hU, hSHI],
             'Curate':[hSO, hU, hRI, hyo], 'Bishop':[hSHI, hSA, hI],
             'Manakete':[kMA, kMU, kKU, DASH, kTO]}

#Terrain
terrains = ['Floor', 'Grassland', 'Village', 'Mountain', 'Castle', 'Fortress', 'Forest', 'Sky',
            'Bridge', 'Sea', 'River', 'Desert', 'Stadium', 'Stairs', 'Pillar', 'Stone Wall']

terrainsJP = {'Floor':[hYU, SPACE, hKA], 'Grassland':[hSO, hU, hKE, TENTEN, hNN], 'Village':[hMU, SPACE, hRA],
              'Mountain':[hYA, SPACE, hMA], 'Castle':[hSHI, SPACE, hRO], 'Fortress':[hTO, hRI, hTE, TENTEN],
              'Forest':[hHA, hYA, hSHI], 'Sky':[hSO, SPACE, hRA], 'Bridge':[hHA, SPACE, hSHI],
              'Sea':[hU, SPACE, hMI], 'River':[hKA, SPACE, hWA], 'Desert':[hSA, hHA, TENTEN, hKU],
              'Stadium':[kSU, kTA, kSHI, TENTEN, kU, kMU], 'Stairs':[hKA, hI, hTA, TENTEN, hNN],
              'Pillar':[hHA, hSHI, hRA], 'Stone Wall':[hI, hSHI, hKA, TENTEN, hKI]}

terrains_avoid = {'Floor': 0, 'Grassland': 5, 'Village': 0, 'Mountain': 25, 'Castle': 30, 'Fortress': 20,
                  'Forest': 15, 'Sky': 0, 'Bridge': 0, 'Sea': 30, 'River': 0, 'Desert': 0, 'Stadium': 0,
                  'Stairs': 0, 'Pillar': 20, 'Stone Wall':0}

#Weapons
weapons = ['Iron Sword', 'Steel Sword', 'Silver Sword', 'Killing Edge', 'Levin Sword', 'Devil Sword',
           'Wyrmslayer', 'Armorslayer', 'Rapier', 'Mercurius', 'Falchion', 'Lance', 'Silver Lance',
           'Ridersbane', 'Javelin', 'Gradivus', 'Axe', 'Steel Axe', 'Hammer', 'Devil Axe', 'Hand Axe',
           'Bow', 'Steel Bow', 'Bowgun', 'Silver Bow', 'Parthia', 'Arrowspate', 'Stonehoist', 'Hoistflamme',
           'Thunderbolt', 'Pachyderm', 'Firestone', 'Divinestone', 'Magestone', 'Earthstone', 'Fire', 'Thunder',
           'Blizzard', 'Elfire', 'Bolganone', 'Thoron', 'Swarm', 'Aura', 'Excalibur', 'Imhullu', 'Starlight',
           'Heal', 'Mend', 'Recover', 'Physic', 'Fortify', 'Warp', 'Barrier', 'Hammerne', 'Aum']
swords = ['Iron Sword', 'Steel Sword', 'Silver Sword', 'Killing Edge', 'Levin Sword', 'Devil Sword',
           'Wyrmslayer', 'Armorslayer', 'Rapier', 'Mercurius', 'Falchion']
lances = ['Lance', 'Silver Lance','Ridersbane', 'Javelin', 'Gradivus', ]
axes = ['Axe', 'Steel Axe', 'Hammer', 'Devil Axe', 'Hand Axe']
bows = ['Bow', 'Steel Bow', 'Bowgun', 'Silver Bow', 'Parthia']
ballistae = ['Arrowspate', 'Stonehoist', 'Hoistflamme','Thunderbolt', 'Pachyderm']
dragonstones = ['Firestone', 'Divinestone', 'Magestone', 'Earthstone']
tomes = ['Fire', 'Thunder','Blizzard', 'Elfire', 'Bolganone', 'Thoron', 'Swarm', 'Aura', 'Excalibur',
         'Imhullu', 'Starlight']
staves = ['Heal', 'Mend', 'Recover', 'Physic', 'Fortify', 'Warp', 'Barrier', 'Hammerne', 'Aum']
items = ['Door Key', 'Bridge Key', 'Master Key', 'Vulnerary', 'Pure Water', 'Power Ring', 'Secret Book',
         'Secret Book', 'Speed Ring', 'Goddess Icon', 'Dracoshield', 'Talisman', 'Seraph Robe', 'Manual',
         'Boots', "Paladin's Honor", 'Hero Crest', "Bishop's Ring", "Orion's Bolt", "Skydrake Whip",
         'Silver Card', "VIP Card", 'Geosphere', 'Starsphere', 'Lightsphere']

#Weapon Names in Japanese
weaponsJP = {'Iron Sword':[hTE, hTSU, hNO, hTSU, hRU, hKI, TENTEN],
             'Steel Sword':[hHA, hKA, TENTEN, hNE, hNO, hTSU, hRU, hKI, TENTEN],
             'Silver Sword':[hKI, TENTEN, hNN, hNO, hTSU, hRU, hKI, TENTEN],
             'Killing Edge':[kKI, kRU, kSO, DASH, kTO, TENTEN],
             'Levin Sword':[kSA, kNN, kTA, TENTEN, DASH, kSO, DASH, kTO, TENTEN],
             'Devil Sword':[kTE, TENTEN, kHI, TENTEN, kRU, kSO, DASH, kTO, TENTEN],
             'Wyrmslayer':[kTO, TENTEN, kRA, kKO, TENTEN, kNN, kKI, kRA, DASH],
             'Armorslayer':[kA, DASH, kMA, DASH, kKI, kRA, DASH],
             'Rapier':[kRE, kI, kHI, MARU, kA],
             'Mercurius':[kME, kRI, kKU, kRU],
             'Falchion':[kFU, ka, kRU, kSHI, kO, kNN],
             'Lance':[hYA, hRI],
             'Silver Lance':[hKI, TENTEN, hNN, hNO, hYA, hRI],
             'Ridersbane':[kNA, kI, kTO, kKI, kRA, DASH],
             'Javelin':[hTE, hYA, hRI],
             'Gradivus':[kKU, TENTEN, kRA, kTE, TENTEN, ki, kU, kSU],
             'Axe':[hO, hNO],
             'Steel Axe':[hHA, hKA, TENTEN, hNE, hNO, hO, hNO],
             'Hammer':[kHA, kNN, kMA, DASH],
             'Devil Axe':[kTE, TENTEN, kHI, TENTEN, kRU, kA, kKU, kSU],
             'Hand Axe':[hTE, hO, hNO],
             'Bow':[hYU, SPACE, hMI],
             'Steel Bow':[hHA, hKA, TENTEN, hNE, hNO, hYU, hMI],
             'Bowgun':[kHO, TENTEN, kU, kKA, TENTEN, kNN],
             'Silver Bow':[hKI, TENTEN, hNN, hNO, hYU, hMI],
             'Parthia':[kHA, MARU, kRU, kTE, ki, kA],
             'Arrowspate':[kKU, kI, kNN, kKU, kRE, kI, kNN],
             'Stonehoist':[kSU, kTO, DASH, kNN, kHE, ktsu, kSHI, TENTEN],
             'Hoistflamme':[kFU, ka, kI, kYA, DASH, kKA, TENTEN, kNN],
             'Thunderbolt':[kSA, kNN, kTA, TENTEN, DASH, kHO, TENTEN, kRU, kTO],
             'Pachyderm':[kE, kRE, kFU, ka, kNN, kTO],
             'Firestone':[hKA, hRI, hyu, hU, hSE, hKI],
             'Divinestone':[hSHI, hNN, hRI, hyu, hU, hSE, hKI],
             'Magestone':[hMA, hRI, hyu, hU, hSE, hKI],
             'Earthstone':[hCHI, hRI, hyu, hU, hSE, hKI],
             'Fire':[kFU, ka, kI, kA, DASH],
             'Thunder':[kSA, kNN, kTA, TENTEN, DASH],
             'Blizzard':[kFU, TENTEN, kRI, kSA, TENTEN, DASH],
             'Elfire':[kE, kRU, kFU, ka, kI, kA, DASH],
             'Bolganone':[kHO, TENTEN, kRU, kKA, TENTEN, kNO, kNN],
             'Thoron':[kTO, kRO, kNN],
             'Swarm':[kU, ko, DASH, kMU],
             'Aura':[kO, DASH, kRA],
             'Excalibur':[kE, kKU, kSU, kKA, kRI, kHA, TENTEN, DASH],
             'Imhullu':[kMA, kFU, DASH],
             'Starlight':[kSU, kTA, DASH, kRA, kI, kTO],
             'Heal':[kRA, kI, kFU, TENTEN],
             'Mend':[kRI, kRA, kI, kFU, TENTEN],
             'Recover':[kRI, kKA, kHA, TENTEN, DASH],
             'Physic':[kRI, kFU, TENTEN, kRO, DASH],
             'Fortify':[kRI, kSA, TENTEN, kFU, TENTEN],
             'Warp':[kWA, DASH, kFU, MARU],
             'Barrier':[aM, MID_DOT, kSHI, kRU, kTO, TENTEN],
             'Hammerne':[kHA, kMA, DASH, kNN],
             'Aum':[kO, DASH, kMU],
             'None': [hSO, hU, hHI, TENTEN, hNA, hSHI]}

itemsJP = {'Door Key':[hTO, hHI, TENTEN, hRA, hNO, kKA, kKI, TENTEN],
           'Bridge Key':[hHA, hNE, hHA, TENTEN, hSHI, hNO, kKA, kKI, TENTEN],
           'Master Key':[hTO, hU, hSO, TENTEN, hKU, hNO, kKA, kKI, TENTEN],
           'Vulnerary':[hKI, hSU, TENTEN, hKU, TENTEN, hSU, hRI],
           'Pure Water':[hSE, hI, hSU, hI],
           'Power Ring':[kHA, MARU, kWA, DASH, kRI, kNN, kKU, TENTEN],
           'Secret Book':[hHI, hTE, TENTEN, hNN, hNO, hSHI, hyo],
           'Speed Ring':[kSU, kHI, MARU, DASH, kTO, TENTEN, kRI, kNN, kKO, TENTEN],
           'Goddess Icon':[hME, hKA, TENTEN, hMI, hSO, TENTEN, hU],
           'Dracoshield':[hRI, hyu, hU, hNO, hTA, hTE],
           'Talisman':[hMA, hYO, hKE],
           'Seraph Robe':[hTE, hNN, hSHI, hNO, hKO, hRO, hMO],
           'Manual':[kMA, kNI, kyu, kA, kRU],
           'Boots':[kFU, TENTEN, DASH, kTSU],
           "Paladin's Honor":[hKI, hSHI, hKU, hNN, hSHI, hyo, hU],
           'Hero Crest':[hYU, hU, hSHI, hya, hNO, hA, hKA, hSHI],
           "Bishop's Ring":[hSHI, hSA, hI, hNO, hYU, hHI, TENTEN],
           "Orion's Bolt":[kO, kRI, kO, kNN, hNO, hYA],
           "Skydrake Whip":[hHI, hRI, hyu, hU, hNO, hMU, hCHI],
           'Silver Card':[kSHI, kRU, kHA, TENTEN, DASH, kKA, DASH, kTO, TENTEN],
           "VIP Card":[kME, kNN, kHA, TENTEN, DASH, kKA, DASH, kTO, TENTEN],
           'Geosphere':[hTA, TENTEN, hI, hCHI, hNO, kO, DASH, kFU, TENTEN],
           'Starsphere':[hHO, hSHI, hNO, kO, DASH, kFU, TENTEN],
           'Lightsphere':[hHI, hKA, hRI, hNO, kO, DASH, kFU, TENTEN]}

# Attack Messages

atk_msg = ['[UNIT] attacks!',
           '[DMG] damage!',
           '[UNIT] counterattacks!',
           '[UNIT] follows up!',
           '[UNIT] dodges!',
           '[UNIT] uses [MAGIC]',
           "[UNIT]'s HP is restored by [HP]",
           '[UNIT] warped!',
           '[UNIT] is protected by a magic shield!',
           '[WPN] broke!',
           "[UNIT]'s attack was ineffective", #Imhullu
           'No damage!',
           'Critical hit! [DMG] damage!']

atk_msgJP = {'[UNIT] attacks!':[hNO, SPACE, hKO, hU, hKE, TENTEN, hKI],
             '[DMG] damage!':[hNO, kTA, TENTEN, kME, DASH, kSHI, TENTEN, hWO, hA, hTA, hE, hTA],
             '[UNIT] counterattacks!':[hNO, SPACE, hHA, hNN, hKE, TENTEN, hKI],
             '[UNIT] follows up!':[hNO, hSA, hI, hKO, hU, hKE, TENTEN, hKI],
             '[UNIT] dodges!':[hHA, SPACE, hSU, hHA, TENTEN, hYA, hKU, hMI, hWO, hKA, hWA, hSHI, hTA],
             '[UNIT] uses [MAGIC]':[hWO, hTO, hNA, hE, hTA],
             "[UNIT]'s HP is restored by [HP]":[hKA, hI, hFU, hKU, hSHI, hTA],
             '[UNIT] warped!':[hHA, SPACE, kWA, DASH, kFU, MARU, hSHI, hTA],
             '[UNIT] is protected by a magic shield!':[hHA, SPACE, kMA, kSHI, TENTEN, ktsu, kKU,
                                                       kHA, TENTEN, kRI, kA, hWO, hHA, htsu, hTA],
             '[WPN] broke!':[hHA, SPACE, hKO, hWA, hRE, hTE, hSHI, hMA, htsu, hTA, EXCL, EXCL],
             "[UNIT]'s attack was ineffective":[hHA, SPACE, hKO, hU, hKE, TENTEN, hKI, hWO,
                                                hFU, hU, hSHI, TENTEN, hRA, hRE, hTA],
             'No damage!':[kTA, TENTEN, kME, DASH, kSHI, TENTEN, hWO, hA, hTA, hE, hRA, hRE, hNA, hI],
             'Critical hit! [DMG] damage!':[hHI, htsu, hSA, hTSU, hNO, hI, hCHI, hKE, TENTEN, hKI],
             'wa ': [hHA, SPACE],
             'wa HP ga': [hHA, SPACE, aH, aP, hKA, TENTEN],
             'nodameejiwoataeta': [hNO, kTA, TENTEN, kME, DASH, kSHI, TENTEN, hWO, hA, hTA, hE, hTA]}

final_msg_options = ['Hits: 1!', 'Hits: 2!', '[ENEMY] was defeated!',
                     '[ALLY] collapsed!', "Withstood [ENEMY]'s attack!"]

finalmsg = ['Hits: 1!',
            'Hits: 2!',
            "Withstood [ENEMY]'s attack!",
            '[ALLY] earns [EXP] EXP!', #[UNIT]は　9のけいけんちをえた
            '[ALLY] fell in battle',
            '[ENEMY] was defeated!',
            '[ALLY] collapsed!', #[UNIT]は　たおれた！！
            '[ENEMY] was holding [ITEM]!', #[ENEMY]は　[ITEM]をもっていた！！
            '[ALLY] obtained [ITEM].', #[UNIT]は　[ITEM]をてにいれた！
            'Level up! LV. [LV] attained.',
            '[STAT] increased by 1!']

finalmsgJP = {'Hits: 1!': [N1, hKA, hI, kHI, ktsu, kTO, EXCL, EXCL],
              'Hits: 2!': [N2, hKA, hI, kHI, ktsu, kTO, EXCL, EXCL],
              "Withstood [ENEMY]'s attack!": [hNO, hKO, hU, hKE, TENTEN, hKI, hWO, hTA, hE, hKI, htsu, hTA, EXCL, EXCL],
              '[ENEMY] was defeated!': [hWO, SPACE, hTA, hO, hSHI, hTA, EXCL, EXCL],
              '[ENEMY] was holding [ITEM]!': [hWO, hMO, htsu, hTE, hI, hTA, EXCL, EXCL],
              '[ALLY] obtained [ITEM].': [hWO, hTE, hNI, hI, hRE, hTA, EXCL],
              '[ALLY] earns [EXP] EXP!': [hNO, hKE, hI, hKE, hNN, hCHI, hWO, hE, hTA],
              '[ALLY] collapsed!': [hHA, SPACE, hTA, hO, hRE, hTA, EXCL, EXCL],
              '!!': [EXCL, EXCL],
              'level': [kRE, kHE, TENTEN, kRU],
              'ninatta!': [hNI, hNA, htsu, hTA, EXCL],
              'strength': [hCHI, hKA, hRA], 'skill': [hWA, hSA, TENTEN],
              'speed': [hSU, hHA, TENTEN, hYA, hSA], 'weapon level': [hFU, TENTEN, kRE, kHE, TENTEN, kRU],
              'luck': [hU, hNN], 'max hp': [hSA, hI, hTA, TENTEN, hI, aH, aP],
              'ga 1agatta!': [hKA, TENTEN, SPACE, N1, hA, hKA, TENTEN, htsu, hTA, EXCL]}

#Ally Fell (with death quote) 「death quote」\n [UNIT]は　いきたえた！！
#Death Quotes

numbers = {'0': [N0], '1': [N1], '2':[N2], '3': [N3], '4': [N4], '5': [N5], '6': [N6], '7': [N7], '8': [N8], '9': [N9]}

allJP = namesJP | weaponsJP | atk_msgJP | classesJP | terrainsJP | numbers | finalmsgJP | itemsJP