import numpy as np

def simulate_probs(N=1_000_000):
    rolls = np.random.randint(1, 7, size=(N, 2))
    sums = rolls.sum(axis=1)
    # індекси 2–12
    counts = np.bincount(sums, minlength=13)[2:]
    return counts / N

def compare_with_analytic(sim_probs):
    # Аналітичні ймовірності (1/36, 2/36, …, 6/36, …, 1/36)
    analytic_probs = np.array([1,2,3,4,5,6,5,4,3,2,1]) / 36
    
    for s, (p_sim, p_ana) in enumerate(zip(sim_probs, analytic_probs), start=2):
        diff = p_sim - p_ana
        print(f"|  {s:2d}  |  {p_sim*100:6.3f}%  |  {p_ana*100:6.3f}%  | Δ={diff*100:6.3f}%  |\n")


if __name__ == "__main__":
    sim = simulate_probs(N=1_000_000)
    print("Порівняння емпіричних і аналітичних ймовірностей:")
    compare_with_analytic(sim)
