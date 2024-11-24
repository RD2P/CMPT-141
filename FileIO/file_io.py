# 'r' is default
# file = open('listfile.txt', 'r')


# text = ''
# for i in file:
#   text+= i.strip()
# print(text)


# access file in diff directory
# f = open('./d/test.txt', 'r')
# for i in f:
#   print(i.strip())


# tabular text file - just split(',')
# tf = open('tab.txt', 'r')
# for l in tf:
#   l = l.strip().split(',,') # try out double commas
#   print(l)
# tf.close()


# using with
# grades = [
#   [1,2,3],
#   [4,5,6]
# ]
# data = ''
# for i in grades:
#   data += f"{i}\n"


# with open('newfile.txt', 'w') as f:
#   for g in grades:
#     # f.write(str(g))
#     # f.write('\n')
#     f.write(f"{g}\n")


# for g in grades:
#   print(','.join([str(x) for x in g]))


# f1 = open('f1.txt','w')
# f2 = open('f2.txt','w')
# f1.write('one\n')
# f2.write('two\n')
# f1.write('three\n')
# f2.write('four\n')
# f1.close()
# f2.close()


# f = open('data.txt')
# nums = []
# for i in f:
# 	nums.append(int(i))
# f.close()
# p = open('dataplus.txt','w')
# for i in nums:
# 	if i > 0:
# 		p.write(str(i))
# 		p.write('\n')
# p.close
# m = open('dataminus.txt','w')
# for i in nums:
# 	if i < 0:
# 		m.write(str(i))
# 		m.write('\n')
# m.close()


# len(f) is NOT ALLOWED
# f = open('data.txt')
# for i in range(len(f)):
#   print(f(i))