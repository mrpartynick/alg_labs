def merge_sort_and_count(arr):
		count = 0
		left_count = 0
		right_count = 0

		cur = []

		if len(arr) > 1:
			mid = len(arr) // 2

			left, left_count = merge_sort_and_count(arr[:mid])
			right, right_count = merge_sort_and_count(arr[mid:])

			i, j = 0, 0

			while i < len(left) and j < len(right):
				if left[i] <= right[j]:
					cur.append(left[i])
					i += 1
				else:
					cur.append(right[j])
					j += 1

					count += len(left[i:])

			while i < len(left):
				cur.append(left[i])
				i += 1

			while j < len(right):
				cur.append(right[j])
				j += 1
		else:
			cur = arr[:]

		return cur, count + left_count + right_count

l = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]

result_arr, result_inversions = merge_sort_and_count(l)

print(result_inversions)