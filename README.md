# matrix_transform

The code was designed to transform a complex matrix (comtaining variable number of rows and columns) into one-line observation

This folder contains 9 different scripts, 8 Python and 1 R that were used to process CRIC 12SL and INFO files. There is an additional csv file containing lead heading labels for the R script to use during data wrangling. 

Each of the Python scripts extracts data from a specific section of the CRIC output files. The basic logic behind each Python file is as follows:

1. Read in all the output files. These files are separated into lists based on the number of lines present in that file. 
2. Each list is then acted on independently. The section of the CRIC 12SL file is extracted based on line number. 
3. An output is created for each section containing information for each unique patient, based on EcgID, on each line of a CSV file.

The R script then:

1. Merges all the separate line number CSVs for a certain section into one singular CSV.
2. Perform any data wrangling steps still required for easier analysis.
3. Join all separate data sets into a final analytical day set using EcgID as the key. 
