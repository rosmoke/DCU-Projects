from weight_111 import Weight

def main():

    # Create some weights
    d1 = Weight()
    d2 = Weight(3, 12)
    d3 = Weight(8, 6)

    # Display ounces per pound
    print('Ounces in a pound: {}'.format(Weight.OUNCES_PER_POUND))

    # Display weights
    print('Weights...')
    print('d1 : {}'.format(d1))
    print('d2 : {}'.format(d2))
    print('d3 : {}'.format(d3))

    # Equality
    print('Equality...')
    print(Weight(4, 4) == Weight(4, 4))
    print(d2 == d3)
    print(d2 != d3)

    # Greater than, greater than or equal to
    print('Greater than, greater than or equal to...')
    print(d2 > d1)
    print(d1 >= d2)

    # Less than, less than or equal to
    print('Less than, less than or equal to...')
    print(d1 < d2)
    print(d1 <= d1)

    # Addition
    print('Addition...')
    d4 = d2 + d3
    print('d4 : {}'.format(d4))
    print(d4 > d2)

    # In-place addition
    print('In-place addition...')
    d2_alias = d2
    d2 += d3
    print('d2 : {}'.format(d2))
    print(d2 > d3)
    print(d2_alias == d2)
    # Multiplication
    print('Multiplication...')
    d5 = d3 * 2
    print('d5 : {}'.format(d5))

    # In-place multiplication
    print('In-place multiplication...')
    d6 = Weight(1, 1)
    d6_alias = d6
    d6 *= 2
    print('d6 : {}'.format(d6))
    print(d6_alias == d6)
    print(d6 > d1)

    # Right multiplication
    print('Right multiplication...')
    d7 = 3 * d6
    print('d7 : {}'.format(d7))
    print(d6 < d7)

    # Subtraction
    print('Subtraction...')    
    d8 = d7 - d6
    print('d8 : {}'.format(d8))
    print(d8 < d7)

    # In-place subtraction
    print('In-place subtraction...')
    d7_alias = d7
    d7 -= d6
    print('d7 : {}'.format(d7))
    print(d7_alias == d7)

    # From ounces
    print('From ounces...')
    d9 = Weight.from_ounces(100)
    print('d9 : {}'.format(d9))
    print(d9 > d7)

if __name__ == '__main__':
    main()