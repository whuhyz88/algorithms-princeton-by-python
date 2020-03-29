#准备函数
#创造格子类，定义属性
import random
import copy
class grid():
    def __init__(self,idx,blocked=True,parent=None,tree_size=1):
        self.idx = idx
        self.blocked = blocked
        if parent is None:
            self.parent = idx
        else:
            self.parent = parent       
        self.tree_size = tree_size 
        
        
#生成格子方阵
def generate_grid_array(size):
    n = size**2
    grid_list = [grid(i) for i in range(n)]
    return grid_list
    

#找到根
def find_root(grid_list,id_1):
    #print(id1)
    p = grid_list[id_1].parent
    #print(p)
    while p != grid_list[p].parent:
        p = grid_list[p].parent
    #print(p)
    return p
#合并两个元素所在树
def union(grid_list,id_1,id_2):   
    m = find_root(grid_list,id_1)
    n = find_root(grid_list,id_2)
    if m == n:
        return
    if grid_list[m].tree_size >= grid_list[n].tree_size:
        grid_list[n].parent = m
        grid_list[m].tree_size = grid_list[m].tree_size + grid_list[n].tree_size
    if grid_list[m].tree_size < grid_list[n].tree_size:
        grid_list[m].parent = n
        grid_list[n].tree_size = grid_list[m].tree_size + grid_list[n].tree_size
#判断两个格子是否相连
def connected(grid_list,id_1,id_2):
    return find_root(grid_list,id_1) == find_root(grid_list,id_2)

#percolation问题
def percolate(grid_list,size):
    flag = False
    n = size**2
    for i in range(0,size):
        if grid_list[i].blocked is False:
            for j in range(n-size,n):
                if grid_list[j].blocked is False:
                    if connected(grid_list,i,j):
                        flag = True
                        break
    return flag
#初始状态所有格子都是闭合blocked,随机打开一个格子，检查跟之前打开的格子是否相连
def percolation(size):
    grid_list = generate_grid_array(size)
    n = size**2
    blocked_list = copy.deepcopy(grid_list)#深copy，否则会改变grid_list
    opened_list = []
    #开始循环随机打开格子和检查是否渗透
    flag = False
    x = 1
    y = 0
    while flag is not True:
        #print("round:",x)
        random_num = random.randint(0,n-1)
        #print("random_num:",random_num)
        id_o = blocked_list[random_num].idx
        #print("id_o:",id_o)
        grid_list[id_o].blocked = False
        opened_list.append(grid_list[id_o])
        y = y + 1
        
        del blocked_list[random_num]
        #print("实方块数量：",len(blocked_list))
        n = n-1
        x = x+1
        
        if y > 1:
            for i in range(y-1):
                id_1 = opened_list[i].idx
                #print("id_1:",id_1)
                #print("id1.parent:",grid_list[id_1].parent)
                if (id_1 == id_o + 1) or (id_1 == id_o - 1) or (id_1 == id_o + size) or (id_1 == id_o - size):
                    #print('exacute unio')
                    union(grid_list,id_1,id_o)
        flag = percolate(grid_list,size)
        #print("flag:",flag)
    return y/len(grid_list)
#测试
percolation(10)
