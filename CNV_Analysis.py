lineCount = 0
chromosome = list()
beginBound = list()
endBound = list()
totalPositions = 1 #The total number of possible positions for a CNV

chromosomeNumber = raw_input('Enter chromosome number or X or Y: ')
CNV_length = int(raw_input('Enter CNV length in base pairs: '))

try:
    TAD_boundaries = open('TAD_boundaries.txt', 'r')
except:
    print 'The TAD boundary file (TAD_boundaries.txt) is missing'
    exit()
        
try:
    chromosomeLengthsFile = open('chromosomeLengths.txt', 'r')
except:
    print 'The chromosome length file (chromosomeLengths.txt) is missing'
    exit()

#The coordinates of theoretical CNV that will move along the chromosome
coordOne = 1
coordTwo = CNV_length

for line in chromosomeLengthsFile:
    data = line.split('\t')
    if data[0] == chromosomeNumber:
        chromosomeLength=(data[1].strip())
        chromosomeLength = int(chromosomeLength)

for line in TAD_boundaries:
    data = line.split('\t')
    if data[0] == chromosomeNumber:
        chromosome.append(data[0].strip())
        beginBound.append(data[1].strip())
        endBound.append(data[2].strip())
        lineCount+=1
    else:
        continue

#Total number of positions for the CNV
totalPositions = chromosomeLength - CNV_length

#Total number of positions that overlap at least 1 TAD boundary
overlapCount = 0
while coordTwo <= chromosomeLength:
    for i in range(lineCount):
        if coordOne == beginBound[i] or coordOne == endBound[i] or coordTwo == beginBound[i] or coordTwo == endBound[i]:
            overlapCount+=1
            print 'overlap count = ', overlapCount
            break
        elif coordOne < beginBound[i] and coordTwo > beginBound[i]:
            overlapCount+=1
            print 'overlap count = ', overlapCount
            break
        elif coordOne <endBound[i] and coordTwo > endBound[i]:
            overlapCount+=1
            print 'overlap count = ', overlapCount
            break
        else:
            i+=1
    coordOne+=1
    coordTwo+=1
    
print 'There number of boundaries is', lineCount
print 'There are %d possible positions.' %(totalPositions)
print 'The number of TAD boundary overlaps is %d.' %(overlapCount)
