import csv
import gaode_geocode
with open('Shanghai New House Geocode.csv', mode='r', encoding='utf-8', newline='') as csvFile:  # encoding可用utf-8
    rows = csv.reader(csvFile)
    with open('Shanghai New House Geocode2.csv', mode='a', encoding='utf-8', newline='') as f:
        for row in rows:
            if row[17] == '有':
                pass
            else:
                location = row[1] + ' ' + row[4]
                print(location)
                content = gaode_geocode.geocode(location, '上海')
                print(content)
                row.append(content[0])
                row.append(content[1])
            csv_write = csv.writer(f)
            csv_write.writerow(row)