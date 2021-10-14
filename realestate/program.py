import os
import csv
try:
    import statistics
except:
    # error code instead
    import statistics_standin_for_py2 as statistics
from data_types import Purchase


def main():
    show_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def show_header():
    print('-----------------------------')
    print(' REAL ESTATE DATA MINING APP')
    print('-----------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, "data", "SacramentoRealEstateTransactions2008.csv")


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:

        reader = csv.DictReader(fin)
        purchases = []

        for row in reader:
            # print(type(row), row)
            # print(f"Bed count: {row['beds']}")
            p = Purchase.create_from_dict(row)
            purchases.append(p)
        return purchases

        # header = fin.readline().strip()
        # reader = csv.reader(fin, delimiter=",", )
        # for row in reader:
        #     print(type(row), row)

# basic load file
# def load_file(filename):
#     with open(filename, 'r', encoding='utf-8') as fin:
#         header = fin.readline().strip()
#         print("Found header: " + header)

#         lines = []
#         for line in fin:
#             line_data = line.strip().split(",")
#             bed_count = line_data[4]
#             lines.append(line_data)

#         print(lines[:5])


# def get_price(p):
#     return p.price

def query_data(data):  # : list[Purchase]):

    # if data was sorted by price
    # data.sort(key=get_price)
    data.sort(key=lambda p: p.price)

    # most ex house
    high_price = data[-1]
    print(
        f"The most expensive house was sold for ${high_price.price:,}, located at {high_price.street.title()} with {high_price.beds} beds and {high_price.baths} baths.")

    # least ex house
    low_price = data[0]
    print(
        f"The cheapest house was sold for ${low_price.price:,}, located at {low_price.street.title()} with {low_price.beds} beds and {low_price.baths} baths.")

    # average price

    """procedural method commented out"""
    # prices = []
    # for pur in data:
    #     prices.append(pur.price)

    """list comprehension method"""
    prices = [
        p.price # projection or items to create
        for p in data # source / set to process 
    ]

    avg_price = statistics.mean(prices)
    print(f"The average home price is ${int(avg_price):,}.")


    # average price of 2 bedroom houses
    """procedural method commented out"""
    # prices = []
    # baths = []
    # for pur in data:
    #     if pur.beds == 2:
    #         prices.append(pur.price)
    #         baths.append(pur.baths)

    """list comprehension to make it more declarative"""
    # two_bed_homes = [
    #     p # projection or items to create
    #     for p in data # source / set to process 
    #     if p.beds == 2 # test / condition / filter
    # ]
    # avg_price = statistics.mean([p.price for p in two_bed_homes])
    # avg_baths = statistics.mean([p.baths for p in two_bed_homes])
    # avg_sqft = statistics.mean([p.sq__ft for p in two_bed_homes])

    # print(f"The average 2-bedroom home is ${int(avg_price):,} at {int(avg_sqft):,} sqft with {int(avg_baths)} baths.")

    """list comprehension + generator. to convert to generator change the list [] to () and add a homes list instead""" 
    two_bed_homes = (
        p  # projection or items
        for p in data  # the set to process
        if announce(p, '2-bedrooms, found {}'.format(p.beds)) and p.beds == 2  # test / condition
    )

    homes = []
    for h in two_bed_homes:
        if len(homes) > 5:
            break
        homes.append(h)

    avg_price = statistics.mean((announce(p.price, 'price') for p in homes))
    avg_baths = statistics.mean((p.baths for p in homes))
    avg_sqft = statistics.mean((p.sq__ft for p in homes))
    print(f"The average 2-bedroom home is ${int(avg_price):,} at {int(avg_sqft):,} sqft with {int(avg_baths)} baths.")


def announce(item, msg):
    print(f"Pulling {item} for {msg}")
    return item

if __name__ == "__main__":
    main()
