from numpy import amax
import beer_demand

# default var
d_o_cost = 100
d_oos_cost = 1
d_i_cost = 1
d_inventory_initial = 540
lead_time = 2

# var
amount_supp = 0
backlog = 0
inv_level = d_inventory_initial
order = 0
i_cost = 0
oos_cost = 0
o_cost = 0
arr_1 = 0
arr_2 = 0
bool_2_week = False
tot_cost = 0
curr_cost = 0

for i in range(0, 20):
    print("-------------------------\n" + "| WEEK " + str(i+1) + "\n-------------------------")
    amount_supp = beer_demand.get_demand(i)
    o_cost = 0
    inv_level = inv_level - amount_supp + arr_1

    if amount_supp < inv_level:
        print("| Amount supplied..| " + str(amount_supp))
    else:
        backlog = amount_supp - inv_level
        print("| Amount supplied..| " + str(amount_supp - inv_level))
    
    print("| backlog..........| " + str(backlog))
    print("| inv level........| " + str(inv_level))
    


    order = int(input("| ?................| "))

    i_cost = inv_level * d_i_cost
    oos_cost = backlog * d_oos_cost

    if bool_2_week == True:
        arr_1 = arr_2
        arr_2 = 0

    if order != 0:
        o_cost = 100
        arr_2 = order
        bool_2_week = True

    tot_cost = i_cost + oos_cost + o_cost
    curr_cost = curr_cost + tot_cost
    
    
    print("| inv cost.........| " + str(i_cost))
    print("| oos cost.........| " + str(oos_cost))
    print("| order cost.......| " + str(o_cost))
    print("| arr 1 week.......| " + str(arr_1))
    print("| arr 2 week.......| " + str(arr_2))
    print("| tot cost.........| " + str(tot_cost))
    print("| curr cost........| " + str(curr_cost))
    print("-------------------------\n")
