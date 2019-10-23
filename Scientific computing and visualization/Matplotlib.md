## Matplotlib案例

### 绘图参数

​	分享一个Matplotlib画图查询表，转自[rougier/matplot-cheatsheet]( https://github.com/rougier/matplotlib-cheatsheet/blob/master/matplotlib-cheatsheet.png )

![matplotlib](/pictures/matplotlib-cheatsheet.png)

​	plot函数的一般调用格式：

```python
#单线条
plot([x],y,[fmt],data = None,**kwargs)
#多条线
plot([x],y,[fmt],[x2],y2,[fmt],...,**kwargs)

'''
fmt = '[color][marker],[line]'
缩写  plot(x,y,'bo-')  蓝色圆点实线
全名  plot(x,y,color = 'green',marker = 'o',linestyle = 'dashed',linewidth = 1,\
markersize = 6)
'''
```



### 案例精选

1.绘制带有中文标签和图例的正弦余弦曲线

```python
import numpy as np
import pylab as pl
from matplotlib import font_manager as fm

myfont = fm.FontProperties(fname = r'C:\Windows\Fonts\STKAITI.ttf') #设置字体
t = np.arange(0.0,2.0*np.pi,0.01)  #自变量取值范围
s = np.sin(t)
z = np.cos(t)
pl.plot(t,s,label = '正弦')
pl.plot(t,z,label = '余弦')
pl.xlabel('x-变量',fontproperties = 'STKAITI',fontsize = 24)  #设置x标签
pl.ylabel('y-正余弦函数值',fontproperties = 'STKAITI',fontsize = 24)  #设置y标签
pl.title('sin-cos函数图像',fontproperties = 'STKAITI',fontsize = 32)  #图形标题
pl.legend(prop = myfont)
pl.savefig("Figure_1.png",dpi=500)  #储存图片
pl.show()
```

<img src="/pictures/Figure_1.png" alt="Figure_1" style="zoom: 67%;" />

2.绘制饼状图

```python
import numpy as np
import matplotlib.pyplot as plt

labels = 'Frogs','Hogs','Dogs','Logs'  #定义标签
sizes = [15,30,45,10]     #每块值
colors = ['yellowgreen','gold','#FF0000','lightcoral']  #每块颜色定义
explode = (0,0.1,0,0.1)   #将某一块分割出来

fig = plt.figure()
ax = fig.gca()

#随机生成每块值
ax.pie(np.random.random(4),explode=explode,labels=labels,colors=colors
       autopct='% 1.1f% %',shadow=True,startangle=90,
       radius=0.25,center=(0,0),frame=True)
ax.pie(np.random.random(4),explode=explode,labels=labels,colors=colors
       autopct='% 1.1f% %',shadow=True,startangle=90,
       radius=0.25,center=(1,1),frame=True)
ax.pie(np.random.random(4),explode=explode,labels=labels,colors=colors
       autopct='% 1.1f% %',shadow=True,startangle=90,
       radius=0.25,center=(0,1),frame=True)
ax.pie(np.random.random(4),explode=explode,labels=labels,colors=colors
       autopct='% 1.1f% %',shadow=True,startangle=90,
       radius=0.25,center=(1,0),frame=True)

ax.set_xticks([0,1])
ax.set_yticks([0,1])
ax.set_xticklabels(["Sunny","Cloudy"])
ax.set_xticklabels(["Dry","Rainy"])
ax.set_xlim((-0.5,1.5))
ax.set_ylim((-0.5,1.5))
ax.set_aspect('equal')

plt.show()
```

<img src="/pictures/Figure_2.png" alt="Figure_2" style="zoom: 100%;" />

3.pyplot绘制多个图形

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,500)
y = np.sin(x)
z = np.cos(x*x)
plt.figure()  
#标签前后加$ 使用内嵌LaTex将其显示为公式
plt.plot(x,y,label = '$sin(x)$',color='red',linewidth = 2)
plt.plot(x,z,'b--',label = '$cos(x^2)$')
plt.xlabel('Time(s)')
plt.ylabel('Volt')
plt.title('Sin and Cos figure using pyplot')
plt.ylim(-1.2,1.2)
plt.legend()
plt.show()
```

<img src="/pictures/Figure_3.png" alt="Figure_3" style="zoom: 67%;" />

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,500)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.cos(x*x)

plt.figure()  
#创建三个坐标
ax1 = plt.subplot(2,2,1)
ax2 = plt.subplot(2,2,2)
ax3 = plt.subplot(2,1,2)

plt.sca(ax1)
plt.plot(x,y1,color='red')
plt.ylim(-1.2,1.2)

plt.sca(ax2)
plt.plot(x,y2,'b--')
plt.ylim(-1.2,1.2)

plt.sca(ax1)
plt.plot(x,y3,'g--')
plt.ylim(-1.2,1.2)

plt.legend()
plt.show()
```

<img src="/pictures/Figure_3(2).png" alt="Figure_3(2)" style="zoom: 67%;" />



