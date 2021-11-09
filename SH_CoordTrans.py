import csv
import gaode_geocode
import coordTransform_utils
with open('Shanghai New House CoordTrans full.csv', mode='r', encoding='utf-8', newline='') as csvFile:  # encoding可用utf-8
    rows = csv.reader(csvFile)
    with open('Shanghai New House CoordTrans full2.csv', mode='a', encoding='utf-8', newline='') as f:
        for row in rows:
            if row[17] and row[18]:
                gcj_coord_lng = float(row[17])
                gcj_coord_lat = float(row[18])
                print(gcj_coord_lng, gcj_coord_lat, '火星坐标')
                wgs_84_coord = coordTransform_utils.gcj02_to_wgs84(gcj_coord_lng, gcj_coord_lat)
                row.append(wgs_84_coord[0])
                row.append(wgs_84_coord[1])
                csv_write = csv.writer(f)
                csv_write.writerow(row)
            else:
                row.append('')
                row.append('')
                csv_write = csv.writer(f)
                csv_write.writerow(row)