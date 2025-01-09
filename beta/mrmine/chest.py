import random
def generate_chest(max):
    roll_basic=random.randint(1, 73)==1
    roll_gold=random.randint(1, 158)==1
    roll_ethereal=random.randint(1, 790)==1
    #prioritize highest rarity chest spawn
    if roll_ethereal:
        return ['ethereal', random.randint(1, max)]
    elif roll_gold:
        return ['gold', random.randint(1, max)]
    elif roll_basic:
        return ['basic', random.randint(1, max)]
    else:
        return ['none', 0]