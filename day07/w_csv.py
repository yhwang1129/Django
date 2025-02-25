
import csv

with open('test_csv.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)
    writer.writerow(['a', 'b', 'c'])
    writer.writerow(['d', 'e'])