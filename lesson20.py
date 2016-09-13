import numpy as np

# Test Data
xa_high = np.loadtxt('data/xa_high_food.csv')
xa_low  = np.loadtxt('data/xa_low_food.csv')

# Array Generation
A = np.array([[6.7, 1.3, 0.6, 0.7],
              [0.1, 5.5, 0.4, 2.4],
              [1.1, 0.8, 4.5, 1.7],
              [0.0, 1.5, 3.4, 7.5]])

b = np.array([1.1, 2.3, 3.3, 3.9])

# Functions
def xa_to_diameter(xa):
    """
    Convert an array of cross-sectional areas
    to diameters with commensurate units.
    """

    # Compute diameter from area
    diameter = 2*np.sqrt(xa/np.pi)

    return diameter
