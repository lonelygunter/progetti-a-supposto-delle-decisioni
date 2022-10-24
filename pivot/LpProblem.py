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

        # turn contraints into standard: <=, >= -> var, = 
        for i in range(0, len(self.constraints)):
            # set <= -> = + +var
            if self.constraints[i].type == 'L':
                self.constraints[i].type = 'E'
                self.constraints[i].a["x"] = 1
            # set >= -> = + -var
            if self.constraints[i].type == 'G':
                self.constraints[i].type = 'E'
                self.constraints[i].a["x"] = -1
        
        # check if f.o. have negative values:
        index = 0
        tmp = ({})
        for var in self.objective.c.items():
            if var[1] < 0:
                tmp[str(index)] = var[1] 
                index = index + 1

        # sort negative values:
        if len(tmp) != 0:
            tmp = sorted(tmp.items(), key = lambda item: item[1])

            i = 0
            x = ({})
            try :
                while tmp[i][1] == tmp[i+1][1]:
                    if tmp[i][0] < tmp[i+1][0]:
                        x[tmp[i][0]] = tmp[i][1]
                    else:
                        x[tmp[i+1][0]] = tmp[i+1][1]
                    i = i + 1
            except:
                print()
            
            if tmp[0][1] < tmp[1][1]:
                tmp = ({tmp[0][0]: tmp[0][1]})
            


        # return tableau
        matrix = np.array[[]]
        matrix.append(1)


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