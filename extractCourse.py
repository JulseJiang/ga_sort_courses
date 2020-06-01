# encoding: utf-8
"""
@author: julse@qq.com
@time: 2020/5/31 21:28
@desc:
"""
def exgroup1():
    fin = r'file\course_structure.txt'
    mydict = ''
    stage = ''
    step = ''
    course = []
    with open(fin, 'r', encoding="utf-8") as fo:
        line = fo.readline()
        while (line):
            print(line)
            if '阶段' == line[0:2]:
                stage = line.split('.')[-1][:-1]
                course.append()
                print('success')
            break
            line = fo.readline()
def extractgroup2():
    fin = r'file/course_group2.txt'
    fout = r'file/course_group2_1.txt'
    courselist = []
    with open(fin,'r',encoding="utf-8") as fi,open(fout,'w') as fo:
        line = fi.readline()
        while(line):
            line = line[4:].strip(' ')
            line.replace('：', '')
            fo.write(line)
            courselist.append(line[:-1])
            fo.flush()
            line = fi.readline()
    return courselist
def init_consine_similarity():
    fout = r'file/course_group2_2.txt'
    courselist = extractgroup2()
    coursetext = str(courselist).replace("\'",'')[1:-1]
    coursetext = coursetext.replace(', ','')
    dictlist = list(set(list(coursetext)))
    with open(fout,'w') as fo:
        for course in courselist:
            coursevector = [0]*len(dictlist)
            for word in list(course):
                i = dictlist.index(word)
                coursevector[i] = 1
            line = str(coursevector)
            fo.write(line[1:-1]+'\n')
            fo.flush()
        print(courselist)
if __name__ == '__main__':
    print()

