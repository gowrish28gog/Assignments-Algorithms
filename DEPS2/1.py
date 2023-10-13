def critical_events(l, t):
    count = 0
    length=len(l)

    for i in range(length):
        for j in range(i + 1, length):
            if l[i] > t * l[j]:
                count = count+1
    return count


def main():
    # Read test cases from file
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    # Process each test case
    cases = len(lines)
    for i in range(0,cases,4):

        # Read array from test case
        array = eval(lines[i].strip())

        # Read threshold from test case
        threshold = float(lines[i+ 1].replace(" ",""))

        # Read threshold from test case
        c = int(lines[i + 2].strip())
      
       # Count critical events
        critical = critical_events(array, threshold)

        # Output the result
        print(f'Array: {array}')
        print(f'Threshold: {threshold}')
        print(f'Number of critical events: {critical}')
        print(f'expected events: {c}')


if __name__ == '__main__':
    main()
