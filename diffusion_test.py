def calculate_time_step(grid_spacing,diffusivity):
    return 0.5 * grid_spacing**2 / diffusivity
import math
from diffusion import calculate_time_step

GRID_SPACING = 1.0
DIFFUSIVITY = 1.0
TIME_STEP = 0.5
TOLERANCE = 0.01

from diffusion import calculate_time_step
def test_time_step():
    time_step=calculate_time_step(GRID_SPACING, DIFFUSIVITY)
    assert type(time_step) is float
    assert math.isclose(time_step, TIME_STEP, rel_tol=TOLERANCE) 
