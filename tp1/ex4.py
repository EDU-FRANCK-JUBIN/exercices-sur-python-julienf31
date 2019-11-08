import re
import random

def checkDNA(chaine):
    adn_pattern = '[^actg]'
    return not bool(re.compile(adn_pattern).search(chaine))

def generateValidDNA(length):
    return ''.join(random.choice('actg') for i in range(length))

def sequenceProportion(chaine, sequence):
    regex = sequence

    test_str = chaine

    matches = re.findall(regex, test_str)

    print(sequence,'apparrait',len(matches),'fois',sep=' ')


dna = input('Saisissez la chaîne ADN : ')

print(checkDNA(dna))
new_dna = generateValidDNA(25)
print(new_dna)
print(sequenceProportion(new_dna,'ca'))
