
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	dot_v_L = 0
	dot_L_L = 0
	for i in range(len(L)):
		dot_v_L += (v[i] * L[i])
		dot_L_L += (L[i] ** 2)

	proj_v_L = [x * (dot_v_L / dot_L_L ) for x in L]
	return proj_v_L
