import random as r
import copy as c
import matplotlib.pyplot as plt

GENOM_LENGTH = 100
POPULATION_LENGTH = 50
CROSSING_CHANCE = 0.9
MUTATION_CHANCE = 0.1
GENERATIONS_NEEDED = 500

r.seed()

class Individual:
    """pass"""
    def __init__(self):
        self.genom = [r.randint(0, 1) for i in range(GENOM_LENGTH)]
        self.fitness = sum(self.genom)

    def calc_fitness(self):
        """pass"""
        self.fitness = sum(self.genom)

    def get_info(self):
        """pass"""
        return self.fitness, self.genom


class Population:
    """pass"""
    def __init__(self):
        self.individuals = [Individual() for i in range(POPULATION_LENGTH)]
        # self.individuals[0].genom = [1 for i in range(GENOM_LENGTH)]
        # self.individuals[0].fitness = 100

    def show_info(self):
        """pass"""
        for i in self.individuals:
            print(i.get_info(), sep='\n')

    def get_sum(self):
        """pass"""
        summa = 0
        for i in self.individuals:
            summa += i.fitness
        return summa

    def get_best(self):
        """pass"""
        return max(self.individuals, key=lambda ind: ind.fitness).fitness

    def get_worse(self):
        """pass"""
        return min(self.individuals, key=lambda ind: ind.fitness).fitness

    # def get_chances(self):
    #     """pass"""
    #     summa = 0
    #     chance = [0]
    #     for i in self.individuals:
    #         summa += i.fitness
    #     for i in range(len(self.individuals)):
    #         print(self.individuals[i].fitness * 100/summa)
    #     return chance

    def tournament(self):
        """pass"""
        best_individuals = []
        for i in range(POPULATION_LENGTH):
            a1 = a2 = a3 = 0
            while a1 == a2 or a1 == a3 or a2 == a3:
                a1, a2, a3 = r.randint(0, POPULATION_LENGTH-1), r.randint(0, POPULATION_LENGTH-1), r.randint(0, POPULATION_LENGTH-1)
            best = max(self.individuals[a1], self.individuals[a2], self.individuals[a3], key=lambda individ: individ.fitness)
            best_individuals.append(c.deepcopy(best))
        self.individuals = best_individuals

        # print(self.get_sum(), 'b')

        for i in self.individuals:
            i.calc_fitness()
        # map(Individual.calc_fitness, self.individuals)

        # print(self.get_sum(), 'a')

    def cross_two_inds(self, list, ind1, ind2):
        point = r.randint(1, GENOM_LENGTH-1)
        ind1.genom[:point], ind2.genom[:point] = ind2.genom[:point], ind1.genom[:point]
        # ind1.calc_fitness()
        # ind2.calc_fitness()
        list.append(ind1)
        list.append(ind2)
        return list

    def crossing(self):
        """pass"""
        new_individuals = []
        for i in range(0, POPULATION_LENGTH, 2):
            if r.random() <= CROSSING_CHANCE:
                self.cross_two_inds(new_individuals, self.individuals[i], self.individuals[i+1])
            else:
                new_individuals.append(self.individuals[i])
                new_individuals.append(self.individuals[i+1])
        self.individuals = new_individuals
        for i in self.individuals:
            i.calc_fitness()


    def mutate(self):
        """pass"""
        for ind in self.individuals:
            if r.random() <= MUTATION_CHANCE:
                gen = r.randint(0, GENOM_LENGTH-1)
                ind.genom[gen] = 1 if ind.genom[gen] == 0 else 0

    def run_simulation(self):
        """pass"""
        generation_number = 0
        best_list = [self.get_best()]
        mean_list = [self.get_sum() / POPULATION_LENGTH]
        print(f"Generation: {generation_number}")
        print(f"Best fitness: {self.get_best()}")
        print(f"Mean fitness: {self.get_sum() / POPULATION_LENGTH}\n")
        generation_number += 1
        while generation_number <= GENERATIONS_NEEDED and self.get_best() != 100:
            self.tournament()
            self.crossing()
            self.mutate()

            #Статистика
            best = self.get_best()
            mean = self.get_sum() / POPULATION_LENGTH
            best_list.append(best)
            mean_list.append(mean)
            print(f"Generation: {generation_number}")
            print(f"Best fitness: {best}")
            print(f"Worst fitness: {self.get_worse()}")
            print(f"Mean fitness: {mean}\n")
            generation_number += 1

        #Графік
        fig, ax = plt.subplots()
        plt.plot(best_list, color="red")
        plt.plot(mean_list, color="green")
        plt.show()












pop = Population()
pop.run_simulation()







