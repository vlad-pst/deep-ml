import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	
	dot_product = sum(v1*v2)
	v1_l2_norm = np.sqrt(sum(v1**2))  
	v2_l2_norm = np.sqrt(sum(v2**2))  
	
	cos_similarity = dot_product / (v1_l2_norm * v2_l2_norm)
	return cos_similarity

def cosine_similarity(v1, v2):
	return sum(v1*v2) / (np.sqrt(sum(v1**2)) * np.sqrt(sum(v2**2)))
	