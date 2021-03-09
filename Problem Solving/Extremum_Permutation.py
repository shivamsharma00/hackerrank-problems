# from sets import Set

def main():
	N, K, L = map(int, input().split())
	K_indices = set(map(int, input().split()))
	L_indices = set(map(int, input().split()))
	done = False
	if len(K_indices & L_indices) > 0:
		done = True
	M = 10**9 + 7

	Q_12, Q_22 = 0, 0
	if 2 in K_indices:
		Q_12 = 1
		Q_22 = 0
	elif 2 in L_indices:
		Q_12 = 0
		Q_22 = 1
	else:
		Q_12 = 1
		Q_22 = 1
	prev_Q_partials = {}

	prev_Q_partials[0] = 0
	prev_Q_partials[1] = Q_12
	prev_Q_partials[2] = Q_12 + Q_22
	
	for j in range(3, N + 1):
		current_Q_partials = {}
		current_Q_partials[0] = 0
		for i in range(1, j + 1):
			if j in K_indices:
				Q_ij = 0
				if j - 1 in K_indices:
					done = True
					break
				else:
					Q_ij = (prev_Q_partials[j - 1] - prev_Q_partials[i - 1]) % M
			elif j in L_indices:
				if j - 1 in L_indices:
					done = True
					break
				Q_ij = prev_Q_partials[i - 1] % M
			else:
				if j - 1 in K_indices:
					Q_ij = prev_Q_partials[i - 1] % M
				elif j - 1 in L_indices:
					Q_ij = (prev_Q_partials[j - 1] - prev_Q_partials[i - 1]) % M
				else:
					Q_ij = prev_Q_partials[j - 1] % M
					
			current_Q_partials[i] = (current_Q_partials[i - 1] + Q_ij) % M
		prev_Q_partials = current_Q_partials
		if done:
			break
	if done:
		print(0)
	else:
		print(current_Q_partials[N] % M)



if __name__ == "__main__":
	main()