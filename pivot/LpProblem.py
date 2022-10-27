from ast import arg
from re import L
from uuid import NAMESPACE_X500
import numpy as np

nMinVar = 0
nMaxCons = 0
nMaxVar = 0

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
        global nMaxCons
        global nMinVar
        global nMaxVar

        # turn objective into standard: max z -> min -z
        # set max -> min
        if self.objective.max == True:
            self.objective.max = False
            # set z -> -z
            for item in self.objective.c.items():
                self.objective.c.update({item[0]: (item[1] * -1)})

        # check max number of variable
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
                self.constraints[i].a[str(nMaxVar)] = 1
            # set >= -> = + -var
            elif self.constraints[i].type == 'G':
                nMaxVar += 1
                self.constraints[i].type = 'E'
                self.constraints[i].a[str(nMaxVar)] = -1
            
            # enter constraint row a
            j = 0
            for valA in self.constraints[i].a.values():
                # create a 0s gap is necessary
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

        # return tableau
        print("Tableau:\n", tableau)
        return tableau


    def argmin(self, n):
        '''
        This method find the min between numbers
        :param n: a dictionary with
        - key = tableau column
        - value = number to compare
        :return res: dictionary with
        - key = tableau row
        - value = number
        '''

        # in case of equal values
        i = 0
        res = ({})
        try :
            while n[i][1] == n[i+1][1]:
                # take minus index
                if n[i][0] < n[i+1][0]:
                    res[n[i][0]] = n[i][1]
                else:
                    res.update({n[i+1][0]: n[i+1][1]})
                i += 1
        except:
            print()
        
        # in case of only one max negative value
        try:
            if n[0][1] < n[1][1]:
                res[n[0][0]] = n[0][1]
            elif n[0][1] > n[1][1]:
                res[n[1][0]] = n[1][1]
        except:
            return dict(n)

        
        # return the result
        return res


    def checkNegFo(self):
        '''
        This method find negative value in f.o.
        :return: dictionary of values with:
        - key: variable number (1 = x1, ...)
        - value: negative number
        '''
        global nMaxCons
        global nMaxVar

        neg = {}
        for i in range(0, nMaxVar):
            if self.tableau[nMaxCons, i] < 0:
                neg.update({i: self.tableau[nMaxCons, i]})

        return neg


    def findPivot(self):
        '''
        This method find Pivot numerbers
        :return: coordinate where make Pivot
        '''
        global nMaxCons

        # check if f.o. have negative values:
        neg = self.checkNegFo()

        # sort negative values:
        if len(neg) != 0:
            neg = sorted(neg.items(), key = lambda item: item[1])
        else:
            return None

        # take min value from dictionary 'neg'
        neg = self.argmin(neg)

        # take arguments for argmin
        argminNum = {}
        sPiv = 0
        for i in range(0, nMaxCons):
            for negVar in neg.keys():
                argminNum[i] = (self.tableau[i, nMaxVar]/self.tableau[i, negVar])
                sPiv = negVar

        # call argmin function to determin min value
        rPiv = list(self.argmin(list(argminNum.items())))

        coord = (rPiv[0], sPiv)
        print("Pivot in (", coord[0], ", ", coord[1], "):")

        return coord


    def bfs(self):
        '''
        This method find the basic feasible solution
        :return: 
        '''
        global nMaxVar
        
        # loop while not have BFS
        while bool(self.checkNegFo()):
            # find coordinate where make Pivot function
            rsPiv = self.findPivot()

            # check if we are in BFS
            if rsPiv is None:
                print("BFS !!!!!")
                return 0

            # take number of coordinate
            nPiv = self.tableau.item(rsPiv[0], rsPiv[1])
            
            # first operation to tranform Pivot coordinate in "1"
            for i in range(0, nMaxVar+1):
                self.tableau[rsPiv[0], i] /= nPiv
            
            # swap Pivot row with first row
            self.tableau[[rsPiv[0], 0]] = self.tableau[[0, rsPiv[0]]]

            # operation to tranform other row of tableau
            for i in range(1, nMaxCons+1):
                stat = self.tableau[i, rsPiv[1]]
                for j in range(0, nMaxVar+1):
                    self.tableau[i, j] += (self.tableau[0, j] * (stat * -1.0))
                
            print(self.tableau, "\n")




constraint_1 = LinearConstraint({1: 2, 2: 1}, 'L', 10)  # x1 + 2 x2 <= 10
constraint_2 = LinearConstraint({1: 1, 2: 2}, 'L', 10)  # 2 x1 + x2 <= 10
objective = LinearObjective({1: 10, 2: 10}, True)  # Max z = x1 + x2
problem_1 = LpProblem([constraint_1, constraint_2], objective)
problem_1.tableau = problem_1.buildTableau()
problem_1.bfs()