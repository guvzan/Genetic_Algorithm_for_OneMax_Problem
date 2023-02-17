import random as r

GENOM_LENGTH = 100
POPULATION_LENGTH = 50
CROSSING_CHANCE = 0.9
MUTATION_CHANCE = 0
GENERATIONS_NEEDED = 50

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
            best_individuals.append(max(self.individuals[a1], self.individuals[a2], self.individuals[a3], key=lambda individ: individ.fitness))
        self.individuals = best_individuals

        print(self.get_sum(), 'b')

        for i in self.individuals:
            i.calc_fitness()
        # map(Individual.calc_fitness, self.individuals)

        print(self.get_sum(), 'a')

    def cross_two_inds(self, list, ind1, ind2):
        point = r.randint(1, GENOM_LENGTH-1)
        ind1.genom[:point], ind2.genom[:point] = ind2.genom[:point], ind1.genom[:point]
        ind1.calc_fitness()
        ind2.calc_fitness()
        list.append(ind1)
        list.append(ind2)
        return list

    def crossing(self):
        """pass"""
        new_individuals = []
        for ind1, ind2 in zip(self.individuals[::2], self.individuals[1::2]):
            print(self.individuals.index(ind1), self.individuals.index(ind2))
            if r.random() <= CROSSING_CHANCE:
                new_individuals = self.cross_two_inds(new_individuals, ind1, ind2)
            else:
                new_individuals.append(ind1)
                new_individuals.append(ind2)
        self.individuals = new_individuals


    def mutate(self):
        """pass"""
        for ind in self.individuals:
            if r.random() <= MUTATION_CHANCE:
                gen = r.randint(0, GENOM_LENGTH-1)
                ind.genom[gen] = 1 if ind.genom[gen] == 0 else 0

    def run_simulation(self):
        """pass"""
        generation_number = 0
        print(f"Generation: {generation_number}")
        print(f"Best fitness: {self.get_best()}")
        print(f"Mean fitness: {self.get_sum() / self.get_best()}\n")
        generation_number += 1
        while generation_number <= GENERATIONS_NEEDED:
            self.tournament()
            self.crossing()
            self.mutate()
            print(f"Generation: {generation_number}")
            print(f"Best fitness: {self.get_best()}")
            print(f"Mean fitness: {self.get_sum() / POPULATION_LENGTH}\n")
            generation_number += 1












pop = Population()
pop.run_simulation()







