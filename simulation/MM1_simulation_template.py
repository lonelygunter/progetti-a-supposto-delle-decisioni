import random
import csv
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

# Class 'Request' models a customer request
class Request:
    def __init__(self, arrival_time, service_time, service_start_time):
        '''
        :param arrival_time:
        :param service_time:
        :param service_start_time:
        '''
        self.arrival_time = arrival_time    # the arrival time
        self.service_time = service_time    # the duration of service
        self.service_start_time = service_start_time    # the time at which service starts n(dato che potrebbe esserci una coda e dev aspettare)
        self.service_end_time = self.service_start_time + self.service_time # the time at which service ends
        self.waiting_time = self.service_start_time - self.arrival_time # request waiting time

# A function sampling a negative exponential distribution with parameter par
def neg_exp(par):
    return random.expovariate(par)

def MM1_sim(lbd=None, mu=None, simulation_time=None, R=None):
    '''
    a function simulating a M/M/1 queue
    :param lbd: customer arrival rate
    :param mu: service rate (=1/expected service time)
    :param simulation_time: duration of a simulation run
    :param R: number od simulation runs
    :return: None
    '''

    # make the simulation reproducible
    random.seed(1234567)

    # if the parameters of the simulation experiment are not provided as input, ask them
    if not lbd:
        lbd = input('Request interarrival rate: ')
    if not mu:
        mu = input('Server service rate: ')
    if not simulation_time:
        simulation_time = input('Simulation time (for each run): ')
    if not R:
        R = input("Number of simulation runs to be executed: ")

    # here initialize statistics over R runs

    # executing R simulation runs
    for i in range(R):
        print("a")
        # initialise statistics for i-th simulation run

        # initialize list of requests
        requests = []

        # initialise clock
        t = 0

        # main loop
        while t < simulation_time:
            print(t)
            # generate request
            arrival_time = t + neg_exp(lbd)
            service_time = neg_exp(mu)
            if len(requests) == 0:
                service_start_time = arrival_time
            else:
                service_start_time = max(arrival_time, requests[-1].service_end_time)
            requests.append(Request(arrival_time, service_time, service_start_time))
            t = arrival_time

        # collect statistics on i-th simulation run
        waiting_times = []
        for request in requests:
            waiting_times.append(request.waiting_time)
        arrival_times = []
        for request in requests:
            arrival_times.append(request.arrival_time)

        num_time = []
        num_tail = []
        for i in range(0, len(requests)):
            if i == 0:
                num_tail.append(0);
            elif (requests[i-1].service_end_time > requests[i].arrival_time):
                num_tail.append(requests[i].arrival_time)
                num_tail.append(requests[i].service_end_time)


        plt.plot(num_tail, num_tail)
        plt.show()


    # show results on the whole simulation experiment


# Test
# MM1_sim(lbd=1, mu=10, simulation_time=300, R=1)
# MM1_sim(lbd=8, mu=10, simulation_time=300, R=1)
MM1_sim(lbd=9.9, mu=10, simulation_time=300, R=1)
# MM1_sim(lbd=11, mu=10, simulation_time=300, R=1)
