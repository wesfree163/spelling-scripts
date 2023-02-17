def hanoi(n, s, e, t):
	if n == 0:
		return
	if n == 1:
		print(f"moving 1 from {s} to {e}")
		return
	if n == 2:
		print(f"moving 1 from {s} to {t}")
		print(f"moving 2 from {s} to {e}")
		print(f"moving 1 from {t} to {e}")
		return

	hanoi(n-1, s, t, e)	
	print(f"moving {n} from {s} to {e}")
	hanoi(n-1, t, e, s)

def main():
	hanoi(5, 'A', 'B', 'C')

if __name__ == "__main__":
	main()
 
