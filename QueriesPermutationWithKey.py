import argparse, sys

def options():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m','--max', type=int, help='Enter integer number')
    parser.add_argument('-l','--list', type=str, help='Enter queries list')
    args = parser.parse_args()
    if args.max is None and args.list is None:
        print('Please insert integer number and queries list ')
        sys.exit(1)
    return args.max, args.list

if __name__ == '__main__':
    output = []
    queries = []
    m, list_data = options()
    # Check condition for parameter
    if m < 1 or m > 10**3:
        print('Need to provide max integer number from: 1<= m <= 10^3')
        sys.exit(1)
    for x in list_data:
        if x != ',':
            queries.append(int(x))
    
    # Compare data and return output
    P = [i for i in range(m +1)][1:]
    for index in queries:
        for i in P:
            if  index == i:
                output.append(P.index(index))
                P.remove(i)
                P.insert(0,i)

    print('Output: ', output)
    

    