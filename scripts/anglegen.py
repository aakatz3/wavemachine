#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Andrew A. Katz
#
# Created:     18/11/2024
# Copyright:   (c) Andrew A. Katz 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import csv

def main():
    with open('table.csv','w') as file:
        tablewriter = csv.writer(file)
        for x in range(0, 365, 5):
            tablewriter.writerow([str(x)+'Deg', x])

if __name__ == '__main__':
    main()
