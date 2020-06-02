# ga_sort_courses
sort courses with ga algorithm


## 本项目主要复现论文[《基于知识图谱的学习路径图生成技术研究_胡文韬.caj》](https://github.com/JulseJiang/ga_sort_courses/blob/master/file/%E5%9F%BA%E4%BA%8E%E7%9F%A5%E8%AF%86%E5%9B%BE%E8%B0%B1%E7%9A%84%E5%AD%A6%E4%B9%A0%E8%B7%AF%E5%BE%84%E5%9B%BE%E7%94%9F%E6%88%90%E6%8A%80%E6%9C%AF%E7%A0%94%E7%A9%B6_%E8%83%A1%E6%96%87%E9%9F%AC.caj) 第四章遗传算法
遗传算法主要参考https://blog.csdn.net/czrzchao/article/details/52314455

入口：ga.py 二进制表示的遗传算法，与原博客有关，本项目无关
入口：ga_my.py 自然数表示课程的遗传算法，最后得出最优课程序列
### 主要工作如下：

1. 从慕课网爬取一系列课程数据 [file/course_group2.txt](http://https://github.com/JulseJiang/ga_sort_courses/blob/master/file/course_group2.txt)
1. 数据预处理：删除第x课以及空格，分号等其他字符 [file/course_group2_1.txt](https://github.com/JulseJiang/ga_sort_courses/blob/master/file/course_group2_1.txt),[extractCourse.py](http://https://github.com/JulseJiang/ga_sort_courses/blob/master/extractCourse.py)
1. 将课程分别编码成向量，数字。相关文件：[file/course_group2_2.txt](https://github.com/JulseJiang/ga_sort_courses/blob/master/file/course_group2_2.txt) 
1. 随机初始化课程的相对重要程度，基础程度，初始化数据见文件 [file/course_group2_3_important_list.npy,file/course_group2_4_elementary_list.npy]
代码：[file/extractCourse.py](http//:)
1. 计算课程向量间的余弦相似度
1. 列出适应度函数
1. 修改原遗传算法（二进制编码）的部分内容，使之可用于课程序列排序
修改：geneEncoding.py,calobjValue.py,selection.py,crossover.py,mutation.py
分别为 问题描述，适应度函数表示，选择，交叉，变异（也是遗传算法的主要流程）
- 问题描述：生成初始种群序列，将原二进制表示改为自然数表述
- 适应度函数表示：论文中的适应度公式
- 选择：该算法中的轮盘选择和论文一致，不用做修改
- 交叉：交叉后的序列，重复课程位置与被交换父序列一致，解决交叉后出现重复课程的问题
- 变异：随机生成变异对，如该条序列中， 编号 25 的课程变异为56，编号为56的课程变异为25


参数设置参考论文：
初始种群100，交叉概率0.4，变异概率0.1，
适应度函数的基础性，重要性，关联性特征权值为 1：85.6：1
![输入图片说明](https://images.gitee.com/uploads/images/2020/0602/110007_4d3a7ee0_1869546.png "屏幕截图.png")

迭代300次的结果
![输入图片说明](https://images.gitee.com/uploads/images/2020/0602/113643_f048d025_1869546.png "屏幕截图.png")
```
适应度，课程序列
[51.53, [[55, 30, 21, 11, 34, 74, 66, 59, 31, 76, 42, 40, 49, 23, 79, 47, 25, 64, 27, 52, 72, 65, 18, 7, 48, 77, 20, 69, 75, 67, 51, 13, 81, 26, 56, 63, 16, 53, 10, 36, 37, 24, 9, 35, 12, 70, 73, 2, 32, 78, 62, 41, 38, 43, 3, 1, 8, 44, 58, 68, 22, 28, 57, 19, 17, 45, 4, 54, 15, 39, 0, 46, 6, 5, 29, 50, 71, 33, 80, 14, 61, 60]]]

```
序列再映射到课程
