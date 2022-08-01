#1
def sum_to(n):
  sum = 0
  for num in range (1, n + 1):
    sum += num
  return sum
print(sum_to(6))

#2
def largest(nums):
  largest = 0
  for n in nums:
    if n > largest:
      largest = n
  return largest
print(largest([11, 11111, 11111111, 1, 1111]))

#3
def occurrences(str1, str2):
  return str1.count(str2)
print(occurrences('fleep flotp', 'e'))


#4 
def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product
print(product(4, 5, 7, 2, 5))
print(product(4, 5))