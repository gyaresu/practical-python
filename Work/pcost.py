"""pcost module"""
# pcost.py
#
# Exercise 1.27


def portfolio_cost(filename):
    """main function"""
    total = 0
    with open(filename, 'rt') as f:
        next(f)
        for line in f:
            row = line.split(',')
            try:
                temp = int(row[1]) * float(row[2])
                total = total + temp
            except ValueError:
                print("Couldn't parse", line)
    return total


if __name__ == "__main__":
    cost = portfolio_cost('./Data/portfolio.csv')
    print('Total cost:', cost)
