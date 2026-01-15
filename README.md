# OPTIMIZATION-MODEL

### PERSONAL INFORMATION
* **Company:** CODTECH IT SOLUTIONS
* **Name:** Vipin Nishad
* **Intern ID:** CTIS2391
* **Domain:** Data Science
* **Batch Duration:** 6 Weeks
* **Mentor:** Neela Santosh

---

### PROJECT DESCRIPTION
This project applies mathematical optimization techniques to solve a classic business problem: maximizing profit under strict resource constraints. Using Linear Programming (LP), I modeled a furniture production scenario where a business must decide the optimal number of chairs and tables to produce given limited labor hours and raw materials (wood).

The core of the task uses the Mixed-Integer Linear Programming (MILP) solver to find the "Feasible Region"—the area where all business constraints are met. While the solver successfully identified the optimal production mix, I expanded the project to include **Sensitivity and "What-If" Analysis**. 

In a real business environment, resources are volatile. I wrote a stress-test algorithm to determine:
1. **Binding Constraints:** Identifying which resource is actually limiting growth. My analysis proved that labor hours were a "Binding Constraint"—meaning every lost hour directly reduced profit—whereas wood had a surplus, making it a "Non-Binding Constraint."
2. **Risk Assessment:** The script calculates exactly how much profit is lost if labor drops by 25% or if supply chain issues reduce wood availability.

Finally, I developed a visualization script using Matplotlib to plot the Feasible Region and the "Optimal Point." This allows non-technical managers to see the trade-offs between different production strategies. This project moves beyond simple coding into the realm of Business Intelligence and Decision Science.

### TOOLS & TECHNOLOGIES
* **Optimization Library:** PuLP (COIN-OR CBC Solver)
* **Visualization:** Matplotlib, NumPy
* **Editor:** VS Code

---

### OUTPUT

<img width="1104" height="541" alt="Image" src="https://github.com/user-attachments/assets/7855c30b-2fed-4df2-bacf-9aad73573f7d" />

<img width="1251" height="836" alt="Image" src="https://github.com/user-attachments/assets/6128df35-184b-465f-98fe-5ec8c7409b41" />
