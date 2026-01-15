import pulp
import matplotlib.pyplot as plt
import numpy as np

# 1. Define the Optimization Problem
problem = pulp.LpProblem("Maximize_Factory_Profit", pulp.LpMaximize)

# Decision Variables
x = pulp.LpVariable('Chairs', lowBound=0, cat='Integer')
y = pulp.LpVariable('Tables', lowBound=0, cat='Integer')

# Objective Function (Profit)
problem += 20 * x + 50 * y, "Total_Profit"

# Constraints
problem += 2 * x + 5 * y <= 40, "Labor_Constraint"
problem += 1 * x + 3 * y <= 30, "Wood_Constraint"

# Solve
problem.solve()

# 2. Setup Visualization Data
# Labor: 2x + 5y = 40 => y = (40 - 2x)/5
# Wood: 1x + 3y = 30 => y = (30 - x)/3
x_vals = np.linspace(0, 20, 400)
y_labor = (40 - 2*x_vals) / 5
y_wood = (30 - x_vals) / 3

# 3. Create the Plot
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_labor, label='Labor Constraint (40 hrs)', color='blue', linestyle='--')
plt.plot(x_vals, y_wood, label='Wood Constraint (30 units)', color='green', linestyle='--')

# Fill the Feasible Region
y_feasible = np.minimum(np.maximum(0, y_labor), np.maximum(0, y_wood))
plt.fill_between(x_vals, 0, y_feasible, color='gray', alpha=0.3, label='Feasible Region')

# Mark the Optimal Point (0 Chairs, 8 Tables)
plt.scatter(int(x.varValue), int(y.varValue), color='red', s=100, zorder=5, label=f'Optimal: {int(y.varValue)} Tables')

# Formatting
plt.xlim(0, 15)
plt.ylim(0, 12)
plt.xlabel('Number of Chairs')
plt.ylabel('Number of Tables')
plt.title('Production Optimization: Maximizing Profit')
plt.legend()
plt.grid(True, alpha=0.3)

print(f"Optimal Solution: Build {int(y.varValue)} Tables and {int(x.varValue)} Chairs.")
plt.savefig('optimization_results.png', dpi=300, bbox_inches='tight')
plt.show()


def stress_test(labor_hours, wood_units):
    # Setup a temporary problem
    test_prob = pulp.LpProblem("Stress_Test", pulp.LpMaximize)
    x_test = pulp.LpVariable('Chairs', lowBound=0, cat='Integer')
    y_test = pulp.LpVariable('Tables', lowBound=0, cat='Integer')
    
    # Same Profit
    test_prob += 20 * x_test + 50 * y_test
    
    # New Constraints based on input
    test_prob += 2 * x_test + 5 * y_test <= labor_hours
    test_prob += 1 * x_test + 3 * y_test <= wood_units
    
    test_prob.solve(pulp.PULP_CBC_CMD(msg=0)) # Solve quietly
    return pulp.value(test_prob.objective)

# Scenario 1: Labor Shortage (Losing 10 hours)
profit_low_labor = stress_test(30, 30) 

# Scenario 2: Supply Chain Issue (Losing 10 units of wood)
profit_low_wood = stress_test(40, 20)

print("-" * 30)
print("SENSITIVITY ANALYSIS:-")
print(f"Original Max Profit: ${pulp.value(problem.objective)}")
print(f"Profit if Labor drops to 30hrs: ${profit_low_labor} (Loss of ${pulp.value(problem.objective) - profit_low_labor})")
print(f"Profit if Wood drops to 20 units: ${profit_low_wood} (Loss of ${pulp.value(problem.objective) - profit_low_wood})")
print("-" * 30)



# SENSITIVITY ANALYSIS:-
# Original Max Profit: $400.0
# Profit if Labor drops to 30hrs: $300.0 (Loss of $100.0)
# Profit if Wood drops to 20 units: $400.0 (Loss of $0.0)