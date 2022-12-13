import random
import csv
import math
import statistics
from scipy.stats import t
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
        self.service_start_time = service_start_time    # the time at which service starts
        self.service_end_time = self.service_start_time + self.service_time # the time at which service ends
        self.waiting_time = self.service_start_time - self.arrival_time # request waiting time

# A function sampling a negative exponential distribution with parameter par
def neg_exp(par):
    return random.expovariate(par)

def MM1_sim(lbd=None, mu=None, simulation_time=None, Delta_t=None, R=None):
    '''
    a function simulating a M/M/1 queue
    :param lbd: customer arrival rate (10 requests/minute)
    :param mu: service rate (14 requests/minute=1/expected service time)
    :param simulation_time: duration of a simulation run
    :param Delta_t: width of subintervals in which interval [0, simulation_time] is divided
    :param R: number od simulation runs
    :return: None
    '''

    # make the simulation reproducible


    # number of subintervals in which interval [0, simulation_time] is divided
    m = math.ceil(simulation_time / Delta_t)

    # if the parameters of the simulation experiment are not provided as input, ask them
    if not lbd:
        lbd = input('Request interarrival rate: ')
    if not mu:
        mu = input('Server service rate: ')
    if not simulation_time:
        simulation_time = input('Simulation time (for each run): ')
    if not Delta_t:
        Delta_t = input("Width of subintervals in which interval [0, simulation_time] is divided: ")
    if not R:
        R = input("Number of simulation runs to be executed: ")

    # here initialize statistics over R runs
    mean_waiting_times = [[] for i in range(m)]

    # executing R simulation runs
    for i in range(R):
        # initialise statistics for i-th simulation run

        # initialize list of requests
        requests = []

        # initialise clock
        t = 0

        # main loop
        while t < simulation_time:
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
        waiting_times = [[] for i in range(m)]
        for request in requests:
            for i in range(m):
                if request.arrival_time >= i * Delta_t and request.arrival_time < (i+1) * Delta_t:
                    waiting_times[i].append(request.waiting_time)
        for i in range(m):
            mean_waiting_times[i].append(statistics.mean(waiting_times[i]))

    # show results on the whole simulation experiment
    y_max = 0
    for i in range(m):
        if max(mean_waiting_times[i]) > y_max:
            y_max = max(mean_waiting_times[i])

    # 1. draw boxplots on L_1, ..., L_R over time
    # plt.boxplot(mean_waiting_times, showmeans=True)
    # plt.xticks([i+1 for i in range(m)], [Delta_t*(i+1) for i in range(m)], rotation='vertical')
    # plt.show()

    # 2. plot theta_R and S_R over time
    means = []
    std_devs = []
    for sample in mean_waiting_times:
        means.append(np.mean(sample))
        std_devs.append(np.std(sample))

    alpha = 0.05  # confidence level = 1 - alpha = 0.95
    from scipy.stats import t
    qt = t.ppf(1 - alpha / 2, R-1)
    totti = std_devs * np.array(qt) / np.sqrt(R)

    return mean_waiting_times, m, y_max, means, std_devs, totti

    # plt.plot(means, color='b')
    # plt.ylim(0, y_max)
    # plt.xticks([i+1 for i in range(m)], [Delta_t*(i+1) for i in range(m)], rotation='vertical')
    # plt.errorbar([i for i in range(m)],means, std_devs, fmt='.k')
    # plt.show()
    #
    # plt.plot([i for i in range(m)], means, 'ok')
    # plt.plot([i for i in range(m)], means, color='black')
    # plt.plot([i for i in range(m)], np.array(means) - np.array(std_devs), color='grey')
    # plt.plot([i for i in range(m)], np.array(means) + np.array(std_devs), color='grey')
    # plt.ylim(0, y_max)
    # plt.xticks([i+1 for i in range(m)], [Delta_t*(i+1) for i in range(m)], rotation='vertical')
    # plt.fill_between([i for i in range(m)], np.array(means) - np.array(std_devs), np.array(means) + np.array(std_devs),
    #                  color='gray', alpha=0.2)
    # plt.show()

    # 3. plot the confidence interval on theta = expected waiting time
    # alpha = 0.05  # confidence level = 1 - alpha = 0.95

    # from scipy.stats import t
    # qt = t.ppf(1 - alpha / 2, R-1)
    #
    # plt.plot(means, color='b')
    # plt.ylim(0, y_max)
    # plt.xticks([i+1 for i in range(m)], [Delta_t*(i+1) for i in range(m)], rotation='vertical')
    # plt.errorbar([i for i in range(m)], means, std_devs*np.array(qt)/np.sqrt(R), fmt='.k')
    # plt.show()
    #
    # plt.plot([i for i in range(m)], means, 'ok')
    # plt.plot([i for i in range(m)], means, color='black')
    # plt.plot([i for i in range(m)], np.array(means) - np.array(std_devs)*np.array(qt)/np.sqrt(R), color='grey')
    # plt.plot([i for i in range(m)], np.array(means) + np.array(std_devs)*np.array(qt)/np.sqrt(R), color='grey')
    # plt.ylim(0, y_max)
    # plt.xticks([i+1 for i in range(m)], [Delta_t*(i+1) for i in range(m)], rotation='vertical')
    # plt.fill_between([i for i in range(m)], np.array(means) - np.array(std_devs)*np.array(qt)/np.sqrt(R), np.array(means) + np.array(std_devs)*np.array(qt)/np.sqrt(R),
    #                  color='gray', alpha=0.2)
    # plt.show()


def plot(mean_waiting_times, m, y_max, means, devs, totti, Delta_t):
    # 1. draw boxplots on L_1, ..., L_R over time
    plt.boxplot(mean_waiting_times, showmeans=True)
    plt.xticks([i+1 for i in range(m)], [Delta_t*(i+1) for i in range(m)], rotation='vertical')
    plt.show()

    plt.plot(means, color='b')
    plt.ylim(0, y_max)
    plt.xticks([i+1 for i in range(m)], [Delta_t*(i+1) for i in range(m)], rotation='vertical')
    plt.errorbar([i for i in range(m)],means, devs, fmt='.k')
    plt.show()

    plt.plot([i for i in range(m)], means, 'ok')
    plt.plot([i for i in range(m)], means, color='black')
    plt.plot([i for i in range(m)], np.array(means) - np.array(devs), color='grey')
    plt.plot([i for i in range(m)], np.array(means) + np.array(devs), color='grey')
    plt.ylim(0, y_max)
    plt.xticks([i+1 for i in range(m)], [Delta_t*(i+1) for i in range(m)], rotation='vertical')
    plt.fill_between([i for i in range(m)], np.array(means) - np.array(devs), np.array(means) + np.array(devs),
                     color='gray', alpha=0.2)
    plt.show()

    plt.plot(means, color='b')
    plt.ylim(0, y_max)
    plt.xticks([i+1 for i in range(m)], [Delta_t*(i+1) for i in range(m)], rotation='vertical')
    plt.errorbar([i for i in range(m)], means, totti, fmt='.k')
    plt.show()

    plt.plot([i for i in range(m)], means, 'ok')
    plt.plot([i for i in range(m)], means, color='black')
    plt.plot([i for i in range(m)], np.array(means) - totti, color='grey')
    plt.plot([i for i in range(m)], np.array(means) + totti, color='grey')
    plt.ylim(0, y_max)
    plt.xticks([i+1 for i in range(m)], [Delta_t*(i+1) for i in range(m)], rotation='vertical')
    plt.fill_between([i for i in range(m)], np.array(means) - totti, np.array(means) + totti,
                     color='gray', alpha=0.2)
    plt.show()


def MM1_sim2(lbd, mu, simulation_time, Delta_t, interval_nr=10, accurarcy=0.05):
    R = 50  # try this R value

    mean_waiting_times, m, y_max, means, devs, totti = MM1_sim(lbd, mu, simulation_time, Delta_t, R)
    # in base a theta_R e np.array(std_devs)*np.array(qt)/np.sqrt(R), devo decidere se STOP o aumentare R
    accurarcy_iniziale = totti[interval_nr]/means[interval_nr]
    print("Accuracy iniziale: {}".format(accurarcy_iniziale))
    if accurarcy_iniziale > accurarcy:
        n = int(accurarcy_iniziale/accurarcy)
        print("Numero di R adeguato: {}".format(n*n*R))
        mean_waiting_times, m, y_max, means, devs, totti = MM1_sim(lbd, mu, simulation_time, Delta_t, n*n*R)
        print("Accuracy finale: {}".format(totti[interval_nr] / means[interval_nr]))

    plot(mean_waiting_times, m, y_max, means, devs, totti, Delta_t)


random.seed(1234567)
MM1_sim2(lbd=9.9, mu=10, simulation_time=1200, Delta_t=50, interval_nr=10, accurarcy=0.05)
