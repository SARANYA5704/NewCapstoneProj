import csv

# Read CSV and print details
def read_customers(file_path):
    customers_list = []
    customers_tuple = ()
    customers_set = set()
    customers_dict = {}

    with open(file_path, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Store in list
            customers_list.append(row)

            # Store in tuple (convert dict to tuple of items)
            customers_tuple += (tuple(row.items()),)

            # Store in set (store as tuple of items because dict is unhashable)
            customers_set.add(tuple(row.items()))

            # Store in dictionary with 'id' as key
            customers_dict[row['id']] = row

    # Print details
    print("=== Customers List ===")
    for c in customers_list:
        print(c)

    print("\n=== Customers Tuple ===")
    for c in customers_tuple:
        print(tuple(c))

    print("\n=== Customers Set ===")
    for c in customers_set:
        print(set(c))

    print("\n=== Customers Dictionary ===")
    for key, value in customers_dict.items():
        print(f"ID {key}: {value}")

    return customers_list, customers_tuple, customers_set, customers_dict
