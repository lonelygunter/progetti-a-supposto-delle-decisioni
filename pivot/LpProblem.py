import numpy as np

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

        # It's your turn !
        var = []

        # check all variable
        for key in self.constraints.a.keys():
            var.append(key)
        
        var = list(set(var))
        
        # if not == add +-variable
        for max in self.constraints:
            if max.type == 'L':
                max.a['X'] = 1
            elif max.type == 'G':
                max.a['X'] = -1
            
            # change max to min and z to -z
            elif self.objective.max == True:
                self.objective.max == False
                for obj in self.objective.c:
                    boo[obj.key]

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
objective = LinearObjective({'x1': 1, 'x2': 1}, True)  # Max z = x1 + x2
problem_1 = LpProblem([constraint_1, constraint_2], objective)
