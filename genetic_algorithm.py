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


from random import choice, randint, random
import matplotlib.pyplot as plt
import copy


def random_chromosome():
    chromosome = []
    for i in range(10):
        chromosome.append(choice([0, 1]))
    return chromosome


def random_population():
    population = []
    for i in range(5):
        population.append(random_chromosome())
    return population


def fitness(chromosome):
    return sum(chromosome) / len(chromosome)


def mutate(chromosome):
    print("Mutating chromosome")
    mutated = copy.copy(chromosome)
    pos = randint(0, len(chromosome) - 1)
    if chromosome[pos] == 1:
        mutated[pos] = 0
    else:
        mutated[pos] = 1
    return mutated


def simulate(population):
    next_gen = []
    
    for chromosome in population:
        if random() < 0.01:
            chromosome = mutate(chromosome)

        next_gen.append(chromosome)
    
    return next_gen



if __name__ == "__main__":
    population = random_population()
    print("Starting simulation.")

    generations = []
    generations.append(population)
    for i in range(100):
        population = generations[-1]
        next_gen = simulate(population)
        generations.append(next_gen)
    
    print("Finished simulation.")
    
    gen_fitnesses = []
    for population in generations:
        pop_fitness = []
        for chromosome in population:
            pop_fitness.append(fitness(chromosome))
        gen_fitnesses.append(sum(pop_fitness))
    
    plt.plot(range(101), gen_fitnesses)
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.show()
