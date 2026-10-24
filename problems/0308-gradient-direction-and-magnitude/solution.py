import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	#  We have numpy !!!
	my_dict = {}
	array_gradient = np.array(gradient)

	# Calculating the norm L2 of the gradient vector. Storing the magnitude (L2 norm) in the dictionary. 
	magnitude = np.sqrt(sum(array_gradient ** 2))
	my_dict["magnitude"] = magnitude

	# Calculating the unit vector pointing in the direction of steepest ascent, and the descent gradient, which represents the negation of the direction of steepest ascent. 
	if magnitude == 0:
		magnitude = 1

	direction = array_gradient / magnitude
	my_dict["direction"] = direction
	my_dict["descent_direction"] = direction * (-1)

	return my_dict
	