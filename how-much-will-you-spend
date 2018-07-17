#https://www.codewars.com/kata/how-much-will-you-spend
def getTotal(costs, items, tax):
    for key in items:
        if key not in costs:
            costs[key] = 0
    return round(sum(costs[i] for i in items)*(1+tax),2)
