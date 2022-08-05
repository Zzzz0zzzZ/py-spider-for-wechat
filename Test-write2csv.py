# -*- coding: utf-8 -*-

import csv

datas = ["1234", "5678", "9101112"]
file_name = input("please name the file")


with open('./' + file_name + '.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in datas:
        writer.writerow([row])