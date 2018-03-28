# Import function for opening XLS files
import xlrd 

# Open relevant files
wb = xlrd.open_workbook("Domain Boundaries.xls")
sheet = wb.sheet_by_name("hESC Combined") # Change sheet name for different tissue type
chromosomeLengthsFile = open('chromosomeLengths.txt', 'r')


# Request user inputs for chromosome and length of CNV
chromosomeNumber = raw_input('Enter chromosome number or X or Y: ')
CNV_length = int(raw_input('Enter CNV length in base pairs: '))


# Extract chromosome size
chromosomeLength = chromosomeLengthsFile.read()
chromosomeLength = chromosomeLength.split("\n")
for row in chromosomeLength:
    length_data = row.split("\t")
    if length_data[0] == chromosomeNumber:
        chromosomeSize = int(length_data[1])


# Extract boundaries
number_of_rows = sheet.nrows
chromosomeID = "chr" + chromosomeNumber
boundaries = [1]
TAD_count = 0
for row in range(number_of_rows):
    if sheet.cell(row, 0).value == chromosomeID:
        TAD_count += 1
        boundaries.append(int(sheet.cell(row,1).value))
        boundaries.append(int(sheet.cell(row,2).value))
boundaries = list(set(boundaries))
boundaries.sort()


# Calculate number of non-overlap
nonOverlapCount = 0
boundaries.append(chromosomeSize)
for index in range(1, len(boundaries)):
    count = boundaries[index] - boundaries[index-1] - CNV_length
    if count > 0:
        nonOverlapCount += count


# Print results
totalPositions = chromosomeSize - CNV_length + 1
print "Number of TAD: " + str(TAD_count)
print "Number of possible positions: " + str(totalPositions)
print"Number of TAD boundary overlaps: " + str(totalPositions - nonOverlapCount)
print "Percentage of overlaps/possible: " + str(round((1 - float(nonOverlapCount) / totalPositions), 3) * 100)



