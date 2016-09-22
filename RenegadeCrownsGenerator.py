import random

def mapTable(d100):
    if d100 == 1 or d100 == 11 or d100 == 21 or d100 == 31 or d100 == 41 or d100 == 51 or d100 == 61 or d100 == 71 or d100 == 83 or d100 == 93:
        if d100 == 83:
            size = random.randint(1,10) * 20
        elif d100 == 92:
            size = random.randint(1,10) * 50  #Fixed math here <<21Sep2016
        else:
            size = random.randint(1,100)
        mapGen = ['Barren Plains', size]
        return mapGen
    elif d100 == 2 or d100 == 12 or d100 == 22 or d100 == 32 or d100 == 42 or d100 == 52 or d100 == 62 or d100 == 72 or d100 == 82 or d100 == 92:
        if d100 == 82:
            size = random.randint(1,10) * 20
        elif d100 == 92:
            size = random.randint(1,10) * 50
        else:
            size = random.randint(1,100)
        mapGen = ['Scrubland Plains', size]
        return mapGen
    elif d100 == 3 or d100 == 23 or d100 == 43 or d100 == 63 or d100 == 81:
        if d100 == 81:
            size = random.randint(1,10) * 20
        else: 
            size = random.randint(1,100)
        mapGen = ['Forested Plains', size]
        return mapGen
    elif d100 == 4 or d100 == 14 or d100 == 24 or d100 == 34 or d100 == 44 or d100 == 54 or d100 == 64 or d100 == 74 or d100 == 86 or d100 == 96:
        if d100 == 86:
            size = random.randint(1,10) * 20
        elif d100 == 96:
            size = random.randint(1,10) * 20
        else:
            size = random.randint(1,100)
        mapGen = ['Barren Hills', size]
        return mapGen
    elif d100 == 5 or d100 == 15 or d100 == 25 or d100 == 35 or d100 == 45 or d100 == 55 or d100 == 65 or d100 == 75 or d100 == 85 or d100 == 95:
        if d100 == 85:
            size = random.randint(1,10) * 20
        elif d100 == 95:
            size = random.randint(1,10) * 50
        else:
            size = random.randint(1,100)
        mapGen = ['Scrubland Hills', size]
        return mapGen
    elif d100 == 6 or d100 == 26 or d100 == 46 or d100 == 66 or d100 == 84:
        if d100 == 84:
            size = random.randint(1,10) * 20
        else:
            size = random.randint(1,100)
        mapGen = ['Grassy Hills', size]
        return mapGen
    elif d100 == 7 or d100 == 37 or d100 == 67 or d100 == 97:
        if d100 == 97:
            size = random.randint(1,10) * 50
        else:
            size = random.randint(1,100)
        mapGen = ['Barren Mountains', size]
        return mapGen
    elif d100 == 8 or d100 == 38 or d100 == 68:
        size = random.randint(1,100)
        mapGen = ['Barren Swamps', size]
        return mapGen
    elif d100 == 9 or d100 == 39 or d100 == 69 or d100 == 99:
        if d100 == 99:
            size = random.randint(1,10) * 50
        else:
            size = random.randint(1,100)
        mapGen = ['Barren Badlands', size]
        return mapGen
    elif d100 == 13 or d100 == 33 or d100 == 53 or d100 == 73 or d100 == 91:
        if d100 == 91:
            size = random.randint(1,10) * 50
        else:
            size = random.randint(1,100)
        mapGen = ['Grassy Plains', size]
        return mapGen
    elif d100 == 16 or d100 == 36 or d100 == 56 or d100 == 76 or d100 == 94:
        if d100 == 94:
            size = random.randint(1,10) * 50
        else:
            size = random.randint(1,100)
        mapGen = ['Forested Hills', size]
        return mapGen
    elif d100 == 17 or d100 == 47 or d100 == 87:
        if d100 == 87:
            size = random.randint(1,10) * 20
        else:
            size = random.randint(1,100)
        mapGen = ['Scrubland Mountains', size]
        return mapGen
    elif d100 == 18 or d100 == 48 or d100 == 88 or d100 == 98:
        if d100 == 88:
            size = random.randint(1,10) * 20
        elif d100 == 98:
            size = random.randint(1,10) * 50
        else:
            size = random.randint(1,100)
        mapGen = ['Scrubland Swamps', size]
        return mapGen
    elif d100 == 19 or d100 == 49 or d100 == 89:
        if d100 == 89:
            size = random.randint(1,10) * 20
        else:
            size = random.randint(1,100)
        mapGen = ['Scrubland Badlands', size]
        return mapGen
    elif d100 == 27 or d100 == 57:
        size = random.randint(1,100)
        mapGen = ['Forested Mountains', size]
        return mapGen
    elif d100 == 28 or d100 == 58:
        size = random.randint(1,100)
        mapGen = ['Grassy Swamps', size]
        return mapGen
    elif d100 == 29 or d100 == 59:
        size = random.randint(1,100)
        mapGen = ['Grassy Badlands', size]
        return mapGen
    elif d100 == 77:
        size = random.randint(1,100)
        mapGen = ['Grassy Mountains', size]
        return mapGen
    elif d100 == 78:
        size = random.randint(1,100)
        mapGen = ['Forested Swamps', size]
        return mapGen
    elif d100 == 79:
        size = random.randint(1,100)
        mapGen = ['Forested Badlands', size]
        return mapGen
    elif d100 % 10 == 0:
        mapGen = ['River', 0] #/!\Second value is 0 to preserve math (unless you want rivers to be 5mi wide)/!\
        return mapGen
    else:
        return 'Error or Undefined value: ' + str(d100)
    
def specialTable(d10):
    if d10 == 1:
        size = random.randint(1,100)
        caveGen = ['\tCaves', 0, size] #/!\Second Value MUST be zero or the math will be incorrect/!\
        return caveGen
    elif d10 == 2:
        return '\tCliffs'
    elif d10 == 3:
        return '\tFertile Valley'
    elif d10 == 4:
        return '\tGeyser'
    elif d10 == 5:
        return '\tIsolated Mountain'
    elif d10 == 6:
        return '\tPool'
    elif d10 == 7:
        return '\tTor'
    elif d10 == 8:
        return '\tVolcano'
    elif d10 == 9:
        return '\tWaterfall'
    elif d10 == 10:
        return '\tWhirlpool'

def ruinCountGen(ruinGenNum):
    if ruinGenNum >= 1 and ruinGenNum <= 10:
        ruinCount = 1
        return ruinCount
    elif ruinGenNum >= 11 and ruinGenNum <= 22:
        ruinCount = 2
        return ruinCount
    elif ruinGenNum >= 23 and ruinGenNum <= 34:
        ruinCount = 3
        return ruinCount
    elif ruinGenNum >= 35 and ruinGenNum <= 47:
        ruinCount = 4
        return ruinCount
    elif ruinGenNum >= 48 and ruinGenNum <= 60:
        ruinCount = 5
        return ruinCount
    elif ruinGenNum >= 61 and ruinGenNum <= 72:
        ruinCount = 6
        return ruinCount
    elif ruinGenNum >= 73 and ruinGenNum <= 83:
        ruinCount = 7
        return ruinCount
    elif ruinGenNum >= 84 and ruinGenNum <= 92:
        ruinCount = 8
        return ruinCount
    elif ruinGenNum >= 93 and ruinGenNum <= 98:
        ruinCount = 9
        return ruinCount
    elif ruinGenNum >= 99 and ruinGenNum <= 100:
        ruinCount = 10
        return ruinCount

def ruinTypeGen(ruinCount):
    typeGen = random.randint(1,101)
    if typeGen >= 1 and typeGen <= 20:
        print('\tType: Unknown Civilization')
        menaceGen = random.randint(1,101)
        if menaceGen >= 1 and menaceGen <= 25:
            print('\tMenace: Summoned Monster')
        elif menaceGen >= 26 and menaceGen <= 55:
            print('\tMenace: Degenerate Tribe')
        elif menaceGen >= 56  and menaceGen <= 75:
            print('\tMenace: Plague')
        elif menaceGen >= 76 and menaceGen <= 85:
            print('\tMenace: Swarms')
        elif menaceGen >= 86 and menaceGen <= 95:
            print('\tMenace: Undead')
        elif menaceGen >= 96 and menaceGen <= 100:
            print('\tNo Menace')
        purposeGen = random.randint(1,101)
        if purposeGen >= 1 and purposeGen <= 30:
            print('\tOriginal Purpose: Fortress')
        elif purposeGen >= 31 and purposeGen <= 60:
            print('\tOriginal Purpose: Outpost')
        elif purposeGen >= 61 and purposeGen <= 70:
            print('\tOriginal Purpose: Settlement')
        elif purposeGen >= 71 and purposeGen <= 90:
            print('\tOriginal Purpose: Temple Complex')
        elif purposeGen >= 91 and purposeGen <= 100:
            print('\tOriginal Purpose: Catacombs')
    elif typeGen >= 21 and typeGen <= 30:
        print('\tType: Cultist')
        menaceGen = random.randint(1,101)
        if menaceGen >= 1 and menaceGen <= 20:
            print('\tMenace: Summoned Monster')
        elif menaceGen >= 21 and menaceGen <= 25:
            print('\tMenace: Degenerate Tribe')
        elif menaceGen >= 26 and menaceGen <= 35:
            print('\tMenace: Golem or Construct')
        elif menaceGen >= 36 and menaceGen <= 50:
            print('\tMenace: Plague')
        elif menaceGen >= 51 and menaceGen <= 65:
            print('\tMenace: Swarm')
        elif menaceGen >= 66 and menaceGen <= 85:
            print('\tMenace: Undead')
        elif menaceGen >= 86 and menaceGen <= 95:
            print('\tMenace: Weapon')
        elif menaceGen >= 96 and menaceGen <= 100:
            print('\tNo Menace')
        purposeGen = random.randint(1,101)
        if purposeGen >= 1 and purposeGen <= 20:
            print('\tOriginal Purpose: Fortress')
        elif purposeGen >= 21 and purposeGen <= 25:
            print('\tOriginal Purpose: Outpost')
        elif purposeGen >= 26 and purposeGen <= 30:
            print('\tOriginal Purpose: Settlement')
        elif purposeGen >= 31 and purposeGen <= 80:
            print('\tOriginal Purpose: Temple Complex')
        elif purposeGen >= 81 and purposeGen <= 100:
            print('\tOriginal Purpose: Catacombs')
    elif typeGen >= 31 and typeGen <= 45:
        print('\tType: Dwarven or Underdark')
        menaceGen = random.randint(1,101)
        if menaceGen >= 1 and menaceGen <= 5:
            print('\tMenace: Summoned Monster')
        elif menaceGen >= 6 and menaceGen <= 30:
            print('\tMenace: Golem or Construct')
        elif menaceGen >= 31 and menaceGen <= 55:
            print('\tMenace: Plauge')
        elif menaceGen >= 56 and menaceGen <= 75:
            print('\tMenace: Swarm')
        elif menaceGen >= 76 and menaceGen <= 95:
            print('\tMenace: Weapon')
        elif menaceGen >= 96 and menaceGen <= 100:
            print('\tNo Menace')
        purposeGen = random.randint(1,101)
        if purposeGen >= 1 and purposeGen <= 25:
            print('\tOriginal Purpose: Fortress')
        elif purposeGen >= 26 and purposeGen <= 60:
            print('\tOriginal Purpose: Outpost')
        elif purposeGen >= 61 and purposeGen <= 80:
            print('\tOriginal Purpose: Settlement')
        elif purposeGen >= 81 and purposeGen <= 90:
            print('\tOriginal Purpose: Temple Complex')
        elif purposeGen >= 91 and purposeGen <= 100:
            print('\tOriginal Purpose: Catacombs')
    elif typeGen >= 46 and typeGen <= 65:
        print('\tType: Ancient Human or Elven')
        menaceGen = random.randint(1,101)
        if menaceGen >= 1 and menaceGen <= 15:
            print('\tMenace: Summoned Monster')
        elif menaceGen >= 16 and menaceGen <= 40:
            print('\tMenace: Degnerate Tribe')
        elif menaceGen >= 41 and menaceGen <= 50:
            print('\tMenace: Plague')
        elif menaceGen >= 51 and menaceGen <= 60:
            print('\tMenace: Swarm')
        elif menaceGen >= 61 and menaceGen <= 85:
            print('\tMenace: Undead')
        elif menaceGen >= 86 and menaceGen <= 95:
            print('\tMenace: Weapon')
        elif menaceGen >= 96 and menaceGen <= 100:
            print('\tNo Menace')
        purposeGen = random.randint(1,101)
        if purposeGen >= 1 and purposeGen <= 20:
            print('\tOriginal Purpose: Fortress')
        elif purposeGen >= 21 and purposeGen <= 50:
            print('\tOriginal Purpose: Outpost')
        elif purposeGen >= 51 and purposeGen <= 60:
            print('\tOriginal Purpose: Settlement')
        elif purposeGen >= 61 and purposeGen <= 70:
            print('\tOriginal Purpose: Temple Complex')
        elif purposeGen >= 71 and purposeGen <= 100:
            print('\tOriginal Purpose: Catacombs')
    elif typeGen >= 66 and typeGen <= 90:
        print('\tType: Recent Civilized')
        menaceGen = random.randint(1,101)
        if menaceGen >= 1 and menaceGen <= 15:
            print('\tMenace: Summoned Monster')
        elif menaceGen >= 16 and menaceGen <= 40:
            print('\tMenace: Degenerate Tribe')
        elif menaceGen >= 41 and menaceGen <= 60:
            print('\tMenace: Plague')
        elif menaceGen >= 61 and menaceGen <= 70:
            print('\tMenace: Swarm')
        elif menaceGen >= 71 and menaceGen <= 85:
            print('\tMenace: Undead')
        elif menaceGen >= 86 and menaceGen <= 95:
            print('\tMenace: Weapon')
        elif menaceGen >= 96 and menaceGen <= 100:
            print('\tNo Menace')
        purposeGen = random.randint(1,101)
        if purposeGen >= 1 and purposeGen <= 20:
            print('\tOriginal Purpose: Fortress')
        elif purposeGen >= 21 and purposeGen <= 50:
            print('\tOriginal Purpose: Outpost')
        elif purposeGen >= 51 and purposeGen <= 75:
            print('\tOriginal Purpose: Settlement')
        elif purposeGen >= 76 and purposeGen <= 90:
            print('\tOriginal Purpose: Temple Complex')
        elif purposeGen >= 91 and purposeGen <= 100:
            print('\tOriginal Purpose: Catacombs')
    elif typeGen >= 91 and typeGen <= 100:
        print('\tType: Oddity')
        menaceGen = random.randint(1,101)
        if menaceGen >= 1 and menaceGen <= 15:
            print('\tMenace: Summoned Monster')
        elif menaceGen >= 16 and menaceGen <= 30:
            print('\tMenace: Degenerate Tribe')
        elif menaceGen >= 31 and menaceGen <= 45:
            print('\tMenace: Golem')
        elif menaceGen >= 46 and menaceGen <= 60:
            print('\tMenace: Plague')
        elif menaceGen >= 61 and menaceGen <= 75:
            print('\tMenace: Swarm')
        elif menaceGen >= 76 and menaceGen <= 80:
            print('\tMenace: Undead')
        elif menaceGen >= 81 and menaceGen <= 95:
            print('\tMenace: Weapon')
        elif menaceGen >= 96 and menaceGen <= 100:
            print('\tNo Menace')

def ruinationReason(d10):
    if d10 == 1:
        return 'Civil War'
    elif d10 == 2:
        return 'Enigma'
    elif d10 == 3:
        return 'Famine'
    elif d10 == 4:
        return 'Magic'
    elif d10 == 5:
        return 'Military Attack'
    elif d10 == 6:
        return 'Natural Decay'
    elif d10 == 7:
        return 'Natural Disaster'
    elif d10 == 8:
        return 'Plague'
    elif d10 == 9:
        return 'Abandonned'
    elif d10 == 10:
        return 'Resource Loss'
				
def princeTypeGen(princeGen):
    if princeGen >= 1 and princeGen <= 30:
        return 'Bandit'
    elif princeGen >= 31 and princeGen <= 50:
        return 'Knight'
    elif princeGen >= 51 and princeGen <= 85:
        return 'Mercenary'
    elif princeGen >= 86 and princeGen <= 90:
        return 'Merchant'
    elif princeGen >= 91 and princeGen <= 94:
        return 'Politician'
    elif princeGen >= 95 and princeGen <= 98:
        return 'Priest'
    elif princeGen >= 99 and princeGen <= 100:
        return 'Wizard'
				
def princeRaceGen(princeGen):
    if princeGen >= 1 and princeGen <= 50:
        return 'Common Race'
    elif princeGen >= 51 and princeGen <= 83:
        return 'Featured Race'
    elif princeGen >= 84 and princeGen <= 100:
        return 'Uncommon/Monstrous Race'
				
def princeGoalGen(princeGen):
    if princeGen == 1:
        return 'Wants to simply control their subjects'
    elif princeGen ==2:
        return 'Wants to be praised and glorified'
    elif princeGen == 3 or princeGen == 4:
        return 'Wants to control a large territory'
    elif princeGen == 5:
        return 'Wants to pass their rule to their children'
    elif princeGen == 6:
        return 'Wants to do as they please, without ramnifications'
    elif princeGen == 7:
        return 'Wants to simply survive'
    elif princeGen == 8 or princeGen == 9:
        return 'Wants to remain in control of his principality'
    elif princeGen == 10:
        return 'Wants to hoard money'
				
def princelyPrinciples(princeGen):
    if princeGen == 1 or princeGen == 2:
        return 'Will not abide "monsters" on their territory'
    elif princeGen == 3:
        return 'Abides by the code of chivalry'
    elif princeGen == 4 or princeGen == 5:
        return 'Is xenophobic in general'
    elif princeGen == 6:
        return 'Will keep to agreements made'
    elif princeGen == 7:
        return 'Will go out of their way to protect innocents'
    elif princeGen >= 8 and princeGen <= 10:
        return 'Is an amoral monster'
				
def princeStyle(princeGen):
    if princeGen == 1 or princeGen == 2:
        return 'Generally speaks in terms of orders and commands'
    elif princeGen == 3:
        return 'Speaks to others as if they were friends'
    elif princeGen == 4 or princeGen == 5:
        return 'Tends to be condescending'
    elif princeGen == 6 or princeGen == 7:
        return 'Speaks very businesslike'
    elif princeGen == 8:
        return 'Is rude to everyone'
    elif princeGen == 9 or princeGen == 10:
        return 'Acts like a pretentious nobleman'
				
def courtSize (princeGen):
    if princeGen == 1 or princeGen == 2:
        return 0
    elif princeGen == 3:
        return 1
    elif princeGen == 4:
        return 3
    elif princeGen == 5:
        return 4
    elif princeGen == 6:
        return 6
    elif princeGen == 7:
        return 8
    elif princeGen == 8:
        return 10
    elif princeGen == 9:
        return 12
    elif princeGen == 10:
        return 15

def territorySize (territoryGen):
    if territoryGen <= 50:
        territory = 'Small'
        return territory
    elif territoryGen >= 51 and territoryGen <= 80:
        territory = 'Medium'
        return territory
    elif territoryGen > 80:
        territory = 'Large'
        return territory

def townGen (territory):
    if territory == 'Small':
        townGenNum = (random.randint(1,100) + random.randint(1,80))
        if townGenNum > 99:
            towns = 1
        else:
            towns = 0
        return towns
    elif territory == 'Medium':
        townGenNum = (random.randint(1,100) + random.randint(80,150))
        if townGenNum > 99:
            towns = 1
        else:
            towns = 0
        return towns
    elif territory == 'Large':
        townGenNum = (random.randint(1,100) + 150)
        if townGenNum > 99:
            towns = 1
        else:
            towns = 0
        return towns
def villageGen (territory):
    villageGenNum = random.randint(1,10)
    if territory == 'Small':
        if villageGenNum >= 1 and villageGenNum <= 3:
            villages = 1
        elif villageGenNum >= 4 and villageGenNum <= 6:
            villages = 2
        elif villageGenNum >= 7 and villageGenNum <= 8:
            villages = 3            
        elif villageGenNum >= 9 and villageGenNum <= 10:
            villages = 4
        else:
            print('Error: VillageGenNum = ' + str(villageGenNum))
    elif territory == 'Medium':
        if villageGenNum == 1 or villageGenNum == 2:
            villages = 1
        elif villageGenNum == 3 or villageGenNum == 4:
            villages = 2
        elif villageGenNum == 5 or villageGenNum == 6:
            villages = 3
        elif villageGenNum == 7 or villageGenNum == 8:
            villages = 4
        elif villageGenNum == 9:
            villages = 5
        elif villageGenNum == 10:
            villages = 6
        else:
            print('Error: VillageGenNum = ' + str(villageGenNum))
    elif territory == 'Large':
        if villageGenNum == 1:
            villages = 1
        elif villageGenNum == 2:
            villages = 2
        elif villageGenNum == 3:
            villages = 3
        elif villageGenNum == 4 or villageGenNum == 5:
            villages = 4
        elif villageGenNum == 6 or villageGenNum == 7:
            villages = 5
        elif villageGenNum == 8:
            villages = 6
        elif villageGenNum == 9:
            villages = 7
        elif villageGenNum == 10:
            villages = 8
        else:
            print('Error: VillageGenNum = ' + str(villageGenNum))
    return villages

def townFeatureGen(d10):
    if d10 >= 1 and d10 <= 6:
        feature = 'Economic Resource'
        d10 = random.randint(1,10)
        if d10 >= 1 and d10 <= 4:
            ecoGen = 'Resource'
        elif d10 >= 5 and d10 <= 7:
            ecoGen = 'Craft'
        elif d10 == 8:
            return 'Oddity'
        elif d10 >= 9:
            return 'Market'
        if ecoGen == 'Resource':
            resourceGen = random.randint(1,100)
            if resourceGen >= 1 and resourceGen <= 10:
                return 'Furs'
            elif resourceGen >= 11 and resourceGen <= 20:
                return 'Medicinal Plants'
            elif resourceGen >= 21 and resourceGen <= 30:
                return 'Coal Mines'
            elif resourceGen >= 31 and resourceGen <= 36:
                return 'Copper Mines'
            elif resourceGen >= 37 and resourceGen <= 46:
                return 'Iron Mines'
            elif resourceGen >= 47 and resourceGen <= 53:
                return 'Lead Mines'
            elif resourceGen >= 54 and resourceGen <= 55:
                return 'Gemstone Mines'
            elif resourceGen >= 56 and resourceGen <= 57:
                return 'Gold Mines'
            elif resourceGen >= 58 and resourceGen <= 61:
                return 'Silver Mines'
            elif resourceGen >= 62 and resourceGen <= 72:
                return 'Tin Mines'
            elif resourceGen >= 73 and resourceGen <= 84:
                return 'Stone Quarries'
            elif resourceGen >= 85 and resourceGen <= 95:
                return 'Clay Quarries'
            elif resourceGen >= 96 and resourceGen <= 100:
                return 'Marble Quarries'
        elif ecoGen == 'Craft':
            craftGen = random.randint(1,100)
            if craftGen >= 1 and craftGen <= 5:
                return 'Armorer'
            elif craftGen >= 6 and craftGen <= 10:
                return 'Bowyer'
            elif craftGen >= 11 and craftGen <= 18:
                return 'Brewery'
            elif craftGen >= 19 and craftGen <= 22:
                return 'Chandler'
            elif craftGen >= 23 and craftGen <= 30:
                return 'Carpenter'
            elif craftGen >= 31 and craftGen <= 36:
                return 'Cooper'
            elif craftGen == 37:
                return 'Gem Cutter'
            elif craftGen >= 38 and craftGen <= 39:
                return 'Goldsmith'
            elif craftGen == 40:
                return 'Gunsmith'
            elif craftGen >= 41 and craftGen <= 48:
                return 'Potter'
            elif craftGen >= 49 and craftGen <= 55:
                return 'Cobbler'
            elif craftGen >= 56 and craftGen <= 64:
                return 'Smith'
            elif craftGen >= 65 and craftGen <= 74:
                return 'Tailor'
            elif craftGen >= 75 and craftGen <= 84:
                return 'Tanner'
            elif craftGen >= 85 and craftGen <= 95:
                return 'Vintner'
            elif craftGen >= 96 and craftGen <= 100:
                return 'Weaponsmith'
    elif d10 == 7:
        return 'Stronghold'
    elif d10 == 8:
        return 'Chokepoint'
    elif d10 == 9:
        return  'Cultist Haven'
    elif d10 == 10:
        feature = 'Special'
        specialGen = random.randint(1,8)
        if specialGen == 1:
            return 'Cultist Haven'
        elif specialGen == 2:
            return 'Hospital'
        elif specialGen == 3:
            return 'Magical Effect'
        elif specialGen == 4:
            return 'Monastery'
        elif specialGen == 5:
            return 'Monster'
        elif specialGen == 6:
            return 'Templar Order'
        elif specialGen == 7:
            return 'Witch'
        elif specialGen == 8:
            return 'Wizard'

########################
###PRIMARY CODE BLOCK###
########################
        
print('How many squares wide is the map?')
mapWidth = int(input())
print('How many squares long is the map?')
mapLength = int(input())
print('') #LineBreak
#Start Global Variables for Generation Here:
mapArea = mapWidth * mapLength
runningMod = 0
townList = []
villageList= []

###MapGeneration
print('~*~{GEOGRAPHY}~*~')
while mapArea > 0:
    geoNumber = (random.randint(1,101) + runningMod)
    if geoNumber <= 100:
        currentMap = mapTable(geoNumber)
        #print('Debug Info (G,M) : ' + str(geoNumber) + ', ' + str(runningMod))
        runningMod = runningMod + 10
        if currentMap[1] < mapArea:
            mapArea = mapArea - currentMap[1]
            print(currentMap)
        else:
            currentMap[1] = mapArea
            mapArea = 0
            print(currentMap)
    elif geoNumber >= 101:
        print(specialTable(random.randint(1,10)))
        #print('Debug Info (G,M) : ' + str(geoNumber) + ', ' + str(runningMod))
        runningMod = 0
    else:
        print('Error Value: ' + str(geoNumber))
print('') #LineBreak

###RuinGeneration
ruinGen = random.randint(1,101)
ruinCount = ruinCountGen(ruinGen)
print('~*~{RUINS}~*~')
for i in range (ruinCount):
    print('Ruin ' + str(i + 1))
    ruinTypeGen(i)
    print('\tReason for Fall: ' + str(ruinationReason(random.randint(1,11))))
print('')#LineBreak

###PrinceGeneration
print('~*~{PRINCES}~*~')
princeCount = ruinCountGen(random.randint(1,101))
#print('Debug Prince Count :' + str(princeCount))
for i in range (princeCount):
    princeGoal = random.randint(1,10)
    print('Prince ' + str(i + 1) + ': ' + str(princeTypeGen(random.randint(1,101))))
    print('\tRace: ' + str(princeRaceGen(random.randint(1,101))))
    print('\t' + str(princeGoalGen(random.randint(1,10))))
    print('\t' + str(princelyPrinciples(random.randint(1,10))))
    print('\t' + str(princeStyle(random.randint(1,10))))
    print('\tCourt Size: ' + str(courtSize(random.randint(1,10))))
    territory = territorySize(random.randint(1,100))
    print('\t' + str(territory) + ' Territory')
    towns = townGen(territory)
    townList.append(towns)
    
    villages = villageGen(territory)
    villageList.append(villages)
    print('\t' + str(towns) + ' town(s)')
    print('\t' + str(villages) + ' village(s)')
unclaimedVillages = villageGen('Medium')
villageList.append(unclaimedVillages)
print('Unclaimed Villages: ' + str(unclaimedVillages))
print('')

##Village Generation
print('~*~{TOWNS AND VILLAGES)~*~')
for index in range(len(villageList)):
    if (index + 1) == len(villageList):
        print('Unclaimed Villages')
    else:
        print('Principality ' + str(index + 1))
        if towns > 0:
            for value in range(townList[index]):
                diceroll = random.randint(1,10)
                townFeature = townFeatureGen(diceroll) 
                print('\tTown ' + str(value + 1) + ': ' + str(townFeature))
    for value in range(villageList[index]):
        diceroll = (random.randint(1,10))
        townFeature = townFeatureGen(diceroll) 
        print('\tVillage ' + str(value + 1) + ': ' + str(townFeature))
