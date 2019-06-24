



def peak_element_position(means, demands, supplies):
    min_cnt = 0
    min_mean = means[0][0]

    for i in range(1, len(means)):
        if means[i][0] == min_mean:
            min_cnt += 1

    # print('min_cnt', min_cnt)

    position_li = []
    min_cost = 1e9
    for i in range(min_cnt + 1):
        x = min(means[i][3])
        if x < min_cost:
            min_cost = x

    for i in range(min_cnt + 1):
        li = means[i][3]
        for j in range(len(li)):
            # print('li', li)
            # print('min cost', min_cost)
            if li[j] == min_cost:
                if means[i][2] == 'col':
                    col = means[i][1]
                    row = j
                else:
                    row = means[i][1]
                    col = j
                # print('row, col', row, col)

                supply = supplies[row]
                demand = demands[col]
                if demand <= supply:
                    a = demand
                    b = supply
                else:
                    a = supply
                    b = demand

                position = [row, col]
                position_li.append([a, b, position])

    position_li = sorted(position_li)
    # print(position_li)
    position = position_li[-1]
    return position


def brain(costs, demands, supplies):
    f = len(costs)
    s = len(costs[0])

    tr_costs = [[costs[j][i] for j in range(f)] for i in range(s)]

    means = []

    # print(costs)
    # print(tr_costs)

    for i in range(f):
        x = sorted(costs[i])
        if s >= 2:
            m = (x[0] + x[1])/2
        else:
            m = x[0]

        means.append([m, i, 'row', costs[i]])

    for i in range(s):
        x = sorted(tr_costs[i])
        if f >= 2:
            m = (x[0] + x[1])/2
        else:
            m = x[0]

        means.append([m, i, 'col', tr_costs[i]])

    means = sorted(means)

    # print(sorted(means))

    position = peak_element_position(means, demands, supplies)
    # print(position)
    return position


def main():
    print("Enter Number of Factories and Stores: ")
    f, s = map(int, input().split())

    print("Enter the cost Matrix: ")
    costs = [[int(i) for i in input().split()] for j in range(f)]

    print("Enter supplies: ")
    supplies = [int(i) for i in input().split()]

    print("Enter Demands: ")
    demands = [int(i) for i in input().split()]

    total_supplies = sum(supplies)
    total_demands = sum(demands)
    d = 0
    total_min_cost = 0

    if total_demands != total_supplies:
        print("Here Demands and supplies are not balanced!")
        return

    while d != total_demands:
        position = brain(costs, demands, supplies)
        a = position[0]
        row = position[2][0]
        col = position[2][1]
        total_min_cost += a * costs[row][col]

        supply = supplies[row]
        demand = demands[col]
        if demand <= supply:
            demands[col] = 0
            supplies[row] = supply - a
        else:
            supplies[row] = 0
            demands[col] = demand - a

        if supplies[row] == 0:
            del costs[row]
            del supplies[row]
        else:
            # print(costs)
            f = len(costs)
            s = len(costs[0])
            for i in range(f):
                for j in range(s):
                    if j == col:
                        del costs[i][j]
            del demands[col]

        #print("The new cost matrix: ")
        #print(costs)
        #print(supplies)
        #print(demands)
        #print(total_min_cost)

        d += a

    print('Total minimum cost of the transportation problem: ', total_min_cost)

if __name__ == "__main__":
    main()

