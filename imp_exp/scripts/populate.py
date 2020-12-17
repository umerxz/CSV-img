from imp_exp import settings
import csv
from upload.models import Product

def run():
    # print("INNNNNNNNNNNNNNNNN")
    with open('data.csv',newline='') as csvfile:
        file=csv.reader(csvfile)
        # print(file)
        # print("_______________________________")

        next(file)

        for row in file:

            prod=Product(name=row[0],price=row[1],description=row[2],img=row[3])
            # print(prod)
            prod.save()
