# region
# Hand-written Genetic Algorithm
# Implement a binary genetic algorithm with:

#     fitness proportional selection
#     1-point crossover
#     bit-flip mutation

# Fitness is the number of 1s in the chromosome.
# The optimal solution is the chromosome where all the genes are set to 1.
# Simulate for various populations and chromosome lengths.
# endregion


from random import choice, randrange, random
from pprint import pprint
from copy import copy


def random_chromosome():
    chromosome = []
    for i in range(10):
        chromosome.append(choice([0, 1]))
    return chromosome


def random_population():
    population = []
    for i in range(50):
        population.append(random_chromosome())
    return population


def simulate(population):
    next_gen = []

    for chromosome in population:
        if random() < 0.01:
            chromosome = mutute(chromosome)

        next_gen.append(chromosome)
    
    return next_gen


def mutute(chromosome):
    pos = randrange(0, len(chromosome))
    mutated = copy(chromosome)
    mutated[pos] = int(not chromosome[pos])
    return mutated


if __name__ == "__main__":
    print("Starting simulation.")

    generations = []
    generations.append(random_population())
    for i in range(1000):
        population = generations[-1]
        next_gen = simulate(population)
        generations.append(next_gen)

    totals = []
    for gen in generations:
        totals.append(sum(sum(chromosome) for chromosome in gen))
    
    from matplotlib import pyplot
    pyplot.plot(range(0, len(generations)), totals)
    pyplot.show()

    print("Finished simulation.")
