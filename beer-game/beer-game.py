import beer_demand as bd

# default var
d_o_cost = 100 # default variable of order cost
d_oos_cost = 1 # default variable of out of stock cost
d_i_cost = 1 # default variable of inventory cost
d_initial_inventory = 540 # default variable of initial inventory pallets
lead_time = 2 # default variable of lead time

# var
demand = 0 # variable of demand
amount_supp = 0 # variable of amount supplied to customers this week
backlog = 0 # variable of backlog
inv_level = d_initial_inventory # variable of inventory level
order = 0 # variable of order
i_cost = 0 # variable of inventory cost
oos_cost = 0 # variable of out of stock cost
o_cost = 0 # variable of order cost
arr_1 = 0 # variable of goods arriving in 1 week
arr_2 = 0 # variable of goods arriving in 2 week
tot_cost = 0 # variable of total cost this week
curr_cost = 0 # variable of cumulative total cost

# function to print all data usefull befor take the order
def preorder(i, demand, amount_supp, backlog, inv_level):
    print("-------------------------\n" + "| WEEK " + str(i + 1) + "\n-------------------------")
    print("| Demand...........| " + str(demand))
    print("| Amount supplied..| " + str(amount_supp))
    print("| backlog..........| " + str(backlog))
    print("| inv level........| " + str(inv_level))

# function to take the order and make a little check
def takeorder():
    while True:
        try:
            order = int(input("| ?................| "))
            break
        except KeyboardInterrupt:
            exit(1)
        except:
            print("| Only Integers....|")

    return order

# function to print all data usefull after taked the order
def postorder(i_cost, oos_cost, o_cost, arr_1, arr_2, tot_cost, curr_cost):
    print("| inv cost.........| " + str(i_cost))
    print("| oos cost.........| " + str(oos_cost))
    print("| order cost.......| " + str(o_cost))
    print("| arr 1 week.......| " + str(arr_1))
    print("| arr 2 week.......| " + str(arr_2))
    print("| tot cost.........| " + str(tot_cost))
    print("| curr cost........| " + str(curr_cost))
    print("-------------------------\n")


# for cycle to iterate weekly demand
for i in range(0, 20):
    # set initial variable of amount_supp, demand and inv_level
    demand = bd.get_demand(i)
    inv_level = inv_level + arr_1

    if demand < inv_level:
        amount_supp = demand
    else:
        backlog = demand - inv_level
        amount_supp = inv_level

    inv_level = inv_level - amount_supp

    # print and take order
    preorder(i, demand, amount_supp, backlog, inv_level)
    order = takeorder()

    # set cost variable and lead time
    i_cost = inv_level * d_i_cost
    oos_cost = backlog * d_oos_cost

    # track lead time
    arr_1 = arr_2
    arr_2 = order

    if order != 0:
        o_cost = 100
    else:
        o_cost = 0

    tot_cost = i_cost + oos_cost + o_cost
    curr_cost = curr_cost + tot_cost

    # print all weekly data
    postorder(i_cost, oos_cost, o_cost, arr_1, arr_2, tot_cost, curr_cost)