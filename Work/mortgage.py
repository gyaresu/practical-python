"""mortgage calculation module"""
# mortgage.py
#
# Exercise 1.7


def main():
    """main function to calculate mortgage payments"""
    principal = 500000.0
    rate = 0.05
    payment = 2684.11
    expay = 1000  # extra payment
    expay_start_month = 5
    expay_end_month = 9
    total_paid = 0.0
    months = 1

    while principal > 0:
        if expay_start_month <= months <= expay_end_month:
            pay = payment + expay
        else:
            pay = payment
        if pay >= principal:
            total_paid = total_paid + principal
            principal = 0
        else:
            principal = principal * (1+rate/12) - pay
            total_paid = total_paid + pay
        print('%s %s %s' % (months, total_paid, principal))
        months += 1

    print(f'Months: {months-1} Total paid: ${total_paid:0.2f}')


if __name__ == "__main__":
    main()
