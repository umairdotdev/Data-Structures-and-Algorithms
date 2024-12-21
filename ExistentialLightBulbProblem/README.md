# Existential LightBulb Problem

This project solves the "Existential LightBulb Problem," which involves determining if a set of switches can be configured so that all connected lightbulbs remain on. It uses graph traversal and SAT solving techniques.

## Problem Description

Given:
- **N switches**: Represented as integers `1` to `N`.
- **M lightbulbs**: Each connected to two switches with specific on/off configurations.

Goal:
- Determine if there exists a configuration of the switches (on/off) such that all the lightbulbs remain ON.
- If no solution exists, identify the conflict-causing variable.

## Files in the Repository

- **`instance*.txt`**: Input files containing switch and lightbulb configurations.
- **`ExistentialLightBulbProblem.PY`**: Python implementation of the solver.
- **`README.md`**: This documentation file.

## How to Use

### Prerequisites
- Python 3.x installed

### Running the Program
1. Place the input files (`instance*.txt`) in the same directory as `REEIMP1.PY`.
2. Run the script:
   ```bash
   python REEIMP1.PY
   ```
3. Follow the on-screen prompts to analyze predefined instances or load a custom instance file.

### Outputs
- If a solution exists, the script outputs the configuration of switches (e.g., `1 -2 3`).
- If no solution exists, the script identifies the conflicting variable.

## Example
For `instance1.txt`:
- Input:
  ```
  3
  2
  1 2
  -1 3
  ```
- Output:
  ```
  The solution for instance 1 is:
  1 -2 3
  ```

For `instance4.txt`:
- Output:
  ```
  There is no solution for instance 4
  The switch that caused the problem is: X
  ```

## Extensions
- Add additional instance files to test other scenarios.
- Improve the solver for scalability with larger datasets.

## References
This project demonstrates applications of graph theory and SAT solvers for computational problem-solving.
