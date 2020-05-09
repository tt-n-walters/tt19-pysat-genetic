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


from random import choice


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


def simulate(population):
    next_gen = []

    for chromosome in population:
        # Do nothing

        next_gen.append(chromosome)
    
    return next_gen


if __name__ == "__main__":
    population = random_population()
    print("Starting simulation.")

    generations = []
    for i in range(100):
        population = generations[-1]
        next_gen = simulate(population)
        generations.append(next_gen)

    totals = []
    for gen in generations:
        total = sum(gen)
    
    print("Finished simulation.")
