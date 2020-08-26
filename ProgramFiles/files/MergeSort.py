import datetime

class MergeSort:
	
	def merge_sort(self, l1, l2):
		# initiator
		i = 0
		j = 0
		# sorted_array
		sorted_array = []

		while i < len(l1) and j < len(l2):
			if l1[i] < l2[j]:
				sorted_array.append(l1[i])
				i += 1
			else:
				sorted_array.append(l2[j])
				j += 1
		while i < len(l1):
			sorted_array.append(l1[i])
			i += 1
		while j < len(l2):
			sorted_array.append(l2[j])
			j += 1
		return sorted_array

	def divide_array(self,l):
		if len(l) < 2:
			return l[:]
		else:
			mid_value = len(l) // 2
			left_list = l[:mid_value]
			right_list = l[mid_value:]
			l1 = self.divide_array(left_list)
			l2 = self.divide_array(right_list)
			return self.merge_sort(l1, l2)
