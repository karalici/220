"""
Name: Iva Karalic
lab13.py
"""


def binary_search(value, lst):
	left = 0
	right = len(lst)-1
	while left <= right:
		middle = (right + left) // 2
		middle_value = lst[middle]
		if value == middle_value:
			return True
		if value < middle_value:
			right = middle - 1
		if value > middle_value:
			left = middle + 1
	return False


def selection_sort(values):
	for i in range(len(values)):
		lowest = values[i]
		pos = i
		for k in range(i+1, len(values)):
			if lowest > values[k]:
				lowest = values[k]
				pos = k
		values[i], values[pos] = values[pos], values[i]
	return values


def calc_area(rect):
	p1 = rect.getP1()
	p2 = rect.getP2()
	dx = abs(p1.getX()-p2.getX())
	dy = abs(p1.getY() - p2.getY())
	return dx * dy


def rect_sort(rects):
	dict = {}
	areas = []
	for rect in rects:
		dict[calc_area(rect)] = rect
		areas.append(calc_area(rect))
	selection_sort(areas)
	for i in range(len(areas)):
		rects[i] = dict[areas[i]]


def star_find(filename):
	file = open(filename, "r")
	signals = file.read().split()
	found = []
	count_found = 0
	count = 0
	for i in signals:
		count += 1
		if eval(i) >= 4000 and eval(i) <= 5000:
			found.append(i)
			count_found += 1
		if count_found == 5:
			break
	print(count)
	print(found)


def main():
	print(binary_search(4, [2, 4, 6, 8, 10, 12]))
	print(selection_sort([2, 4, 5, 1, 3]))
	star_find("signals.txt")
	pass


main()
