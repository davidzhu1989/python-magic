# 0-100 找出所有的被5整除的数目

# 列表元素可以按照某周算法推算出来
# 不用创造完整的list, 从而节省 大量的空间
# python中一边循环一边计算的叫做 generator

g = (x for x in range(0,101) if x %10
     == 0)
for n in g:
    print(n)
# next(g)