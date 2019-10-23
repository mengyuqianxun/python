## Numpy简单应用



导入NumPy模块：

```python
>>>import numpy as np
```



1. 生成数组

```python
a = np.array((1,2,3,4,5))                  #一维数组
b = np.array(([1,2,3],[4,5,6],[7,8,9]))    #三维数组
x = np.linspace(0,5,10)		               #起点，终点，取点数  均匀取点
y = np.logspace(0,9,10,base=10)            #以10为底的指数 1 10 100 ... 1e9
```



2.  数组与数值的算术运算

```python
a = np.array([1,2,3,4,5])
>>>a*2
array([2,4,6,8,10])
>>>a/2
array([0,1,1,2,2])
>>>a/2.0
array([0.5,1.,1.5,2.,2.5])
>>>a**2
array([1,4,9,16,25])
```



3. 数组与数组的算术运算

```python
>>>a = np.array([1,2,3])
>>>b = np.array([[1,2,3],[4,5,6],[7,8,9]])
>>>c=a*b        #对应位置相乘
[[1,4,9]
 [4,10,18]
 [7,16,27]]
>>>print(c/b)   #对应位置相除
[[1. 2. 3.]
 [1. 2. 3.]
 [1. 2. 3.]]

```



4. 二维数组转置

```python
>>>a = np.array(([1,2,3],[4,5,6],[7,8,9]))
>>>a.T
[[1 4 7
 [2 5 8]
 [3 6 9]]
```



5. 向量点积

```python
>>>a = np.array((5,6,7))
>>>b = np.array((6,6,6))
>>>print(np.dot(a,b))
108
```



6. 数组元素访问

```python
>>>a = np.array(([1,2,3],[4,5,6],[7,8,9]))
>>>b[0,0]
1
>>>b[0][2]
3
```



7. 矩阵不同维度上元素的求和

```python
>>>x = np.arange(0,10).reshape(2,5)  #(start,end,step)不包含end   reshape 改变数组形状
>>>x
array(([0,1,2,3,4],
     [5,6,7,8,9]))
>>>np.sum(x)
45
>>>np.sum(x,axis = 0)  #列相加    均返回一列向量
array([5,7,9,11,13])
>>>np.sum(x,axis = 1)  #行相加
array([10,35])
```



8. 生成特殊数组

```python
>>>print(np.zeros((3,3)))
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
>>>print(np.ones((3,3)))
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]
>>>print(np.identity(3))  #生成方阵
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```



9. 切片操作

```python
>>>a = np.arrange(10)
>>>a
array([0,1,2,3,4,5,6,7,8,9])
>>>a[::-1]
array([9,8,7,6,5,4,3,2,1,0])
>>>a[::2]
array([0,2,4,6,8])
>>>c = np.array([[j*10 + i for i in range(6)] for j in range(6)])
>>>c[0,3:5]
array([3,4])
>>>c[2:5,2:5]
array([[22,23,24],
      [32,33,34],
      [42,43,44]])


```



10. 矩阵运算

```python
>>>a_list = [3,5,7]
>>>a_mat = np.matrix(a_l)
>>>a_mat
matrix([[3,5,7]])
>>>np.shape(a_mat)
(1,3)
>>>b_mat = np.matrix((1,2,3))

>>>a_mat * b_mat.T
matrix([[34]])
```

