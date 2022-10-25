from nis import cat
from warnings import catch_warnings
import numpy as np
from zmq import PROBE_ROUTER

class LinearConstraint ():
    '''
    Class LinearConstraint models a linear constraint
    '''
    def __init__(self, a, type, b):
        '''
        Constructor of an object of class LinearConstraint
        :param a: a dictionary with
        - key = variable name (a string)
        - value = the coefficient of the variable in the constraint
        :param type: a character
                    - 'L': <=
                    - 'E': =
                    - 'G': >=
        :param b: the rhs of the constraint
        '''
        self.a = a
        self.type = type
        self. b = b

class LinearObjective ():
    '''
    Class LinearObjective models a linear constraint
    '''
    def __init__(self, c, max):
        '''
        Constructor of an object of class LinearObjective
        :param c: a dictionary with
        - key = variable name (a string)
        - value = the coefficient of the variable in the constraint
        :param max: a Boolean = Treu iff the objective is to be maximized
        '''
        self.c = c
        self.max = max

class LpProblem():
    '''
    This class models a Linear Programming problem
    '''
    def __init__(self, constraints, objective):
        '''
        Constructor of an object of class Truck
        :param constraints: list of constraints (class LinearConstraint)
        :param objective: objective (class LinearObjective)
        :param tableau: problem in tableau format (standard form);
                        tableau is a Numpy bidimensioanl array;
                        tableau.shape=(m+1,n+1);
                        constraints are rows 0, ..., m-1;
                        variables are columns 0, ..., n-1;
                        the objective function is row m;
                        the rhs is column n.
        '''
        self.constraints = constraints
        self.objective = objective
        self.tableau = None

    def buildTableau(self):
        '''
        This method puts the problem in tableau (standard) form
        :return:
        '''

        # turn objective into standard: max z -> min -z
        # set max -> min
        if self.objective.max == True:
            self.objective.max = False
            # set z -> -z
            for item in self.objective.c.items():
                self.objective.c.update({item[0]: (item[1] * -1)})

        # check max number of variable
        nMinVar = 0
        nMaxCons = 0
        for cons in self.constraints:
            if len(cons.a) > nMinVar:
                nMinVar = len(cons.a)
            nMaxCons += 1
        
        # initialize tebleau
        tableau = np.zeros(((nMaxCons+1), (nMinVar+nMaxCons+1)))

        # turn contraints into standard: <=, >= -> var, =
        nMaxVar = nMinVar
        gap = 0
        for i in range(0, len(self.constraints)):
            # set <= -> = + +var
            if self.constraints[i].type == 'L':
                nMaxVar += 1
                self.constraints[i].type = 'E'
                self.constraints[i].a["x" + str(nMaxVar)] = 1
            # set >= -> = + -var
            elif self.constraints[i].type == 'G':
                nMaxVar += 1
                self.constraints[i].type = 'E'
                self.constraints[i].a["x" + str(nMaxVar)] = -1
            
            # insert constraint row a
            j = 0
            for valA in self.constraints[i].a.values():
                if j < nMinVar:
                    tableau[i, j] = valA
                else:
                    tableau[i, j+gap] = valA
                    gap += 1
                
                j+=1
        
            # insert constrint row b
            tableau[i, (nMinVar+nMaxCons)] = self.constraints[i].b
        

        # insert objective row
        i =0
        for val in self.objective.c.values():
            tableau[nMaxCons, i] = val
            i += 1




        
        # check if f.o. have negative values:
        index = 0
        neg = ({})
        for var in self.objective.c.items():
            if var[1] < 0:
                neg[str(index)] = var[1] 
                index += 1

        # sort negative values:
        if len(neg) != 0:
            neg = sorted(neg.items(), key = lambda item: item[1])

            i = 0
            res = ({})
            try :
                while neg[i][1] == neg[i+1][1]:
                    if neg[i][0] < neg[i+1][0]:
                        res[neg[i][0]] = neg[i][1]
                    else:
                        res[neg[i+1][0]] = neg[i+1][1]
                    i += 1
            except:
                print("range out, but no problem mate")
            
            if neg[0][1] < neg[1][1]:
                res = ({neg[0][0]: neg[0][1]})

    def argmin(self, n):
        '''
        This method find the min between numbers
        :param n: a dictionary with
        - key = tableau column
        - value = numer to compare
        '''

        # 


    def makePivot(self, r, s):
        '''
        This method performs a pivot operation on the tableau
        :param r: pivot row
        :param s: pivot columns
        :return:
        '''

        # It's your turn !




constraint_1 = LinearConstraint({'x1': 1, 'x2': 2}, 'L', 10)  # x1 + 2 x2 <= 10
constraint_2 = LinearConstraint({'x1': 2, 'x2': 1}, 'L', 10)  # 2 x1 + x2 <= 10
objective = LinearObjective({'x1': 10, 'x2': 10}, True)  # Max z = x1 + x2
problem_1 = LpProblem([constraint_1, constraint_2], objective)
problem_1.buildTableau()