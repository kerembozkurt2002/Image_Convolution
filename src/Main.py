
# On PPM and PGM formats see http://paulbourke.net/dataformats/ppm/
# On convolution operation see https://youtu.be/KiftWz544_8
# To view .pgm and .ppm files, you can use IrfanView, see https://www.irfanview.com/
# To check whether your outputs are the same as ours, you can use the same techniques as in Homework 2, or you can write your own code.

filename = input()
operation = int(input())


def img_printer(img):
    row = len(img)
    col = len(img[0])
    cha = len(img[0][0])
    for i in range(row):
        for j in range(col):
            for k in range(cha):
                print(img[i][j][k], end=" ")
            print("\t|", end=" ")
        print()


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

def read(fil):
    img=[]
    fp=open(fil)
    modp=fp.readline().strip()
    if str(modp)=="P2":
        rc=fp.readline().strip().split()
        row,col=int(rc[1]),int(rc[0])
        img=[[[0] for i in range(col)] for r in range(row)]
        fp.readline()
        res_info=fp.read()
        res_info_split=res_info.split()
        i=0
        fp.close()
        for r in range(row):
            for c in range(col):
                img[r][c]=int(res_info_split[i])
                i+=1
        return img
    elif str(modp)=="P3":
        rc=fp.readline().strip().split()
        row,col= int(rc[1]),int(rc[0])
        img = [[["","",""] for i in range(col)] for r in range(row)]
        fp.readline()
        res_info=fp.read().split()
        i=0
        fp.close()
        for i1 in range(len(img)):
            for i2 in range(len(img[0])):
                for i3 in range(len(img[0][0])):
                    img[i1][i2][i3]=int(res_info[i])
                    i+=1
        return img


def tf_table(lst):
    l = [[False for i in range(len(lst[0]))] for i2 in range(len(lst))]
    return l


finl=[]
def controller(lst,sat,sut):
    global tft
    global finl
    try:
        if tft[sat][sut]==True or lst[sat][sut]==0:
            return 0

        elif tft[sat][sut]==False:
            tft[sat][sut]=True
            finl.append(lst[sat][sut])
            if sat==0 and sut==0:
                return controller(lst,sat+1,sut),controller(lst,sat,sut+1)

            elif sat==0 and len(lst[0])-1>sut>0:
                return controller(lst,sat+1,sut),controller(lst,sat,sut+1),controller(lst, sat + 1, sut)

            elif sat==0 and sut==len(lst[0])-1:
                return controller(lst, sat + 1, sut),controller(lst, sat, sut - 1)

            elif sut==len(lst[0])-1 and len(lst)>sat>0:
                return controller(lst, sat + 1, sut),  controller(lst, sat - 1, sut) ,controller(lst, sat, sut - 1)

            elif sat==len(lst) and sut==len(lst[0])-1:
                return controller(lst, sat - 1, sut),controller(lst, sat, sut - 1)

            elif sat==len(lst)-1 and len(lst[0])-1>sut>0:
                return controller(lst, sat, sut + 1),controller(lst, sat, sut - 1),controller(lst, sat - 1, sut)

            elif sat==len(lst)-1 and sut==0:
                return controller(lst, sat - 1, sut),controller(lst, sat, sut + 1)

            elif len(lst)-1>sat>0 and sut==0:
                return controller(lst, sat + 1, sut), controller(lst, sat - 1, sut),controller(lst, sat, sut + 1)

            else:
                return controller(lst, sat, sut + 1),controller(lst, sat, sut - 1),  controller(lst, sat + 1, sut),controller(lst, sat - 1,sut)
    except:
        return

def empty_final_table(lst):
    l = [["" for i in range(len(lst[0]))] for i2 in range(len(lst))]
    return l
def zero_adder(table,empty):
    for i in range(len(table)):
        for i2 in range(len(table[0])):
            if table[i][i2]==0: empty[i][i2]=0
    return empty

def average(lst):
    sum=0
    for i in lst:
        sum+=int(i)
    return int(sum/len(lst))


def formating(empty,table):
    global tft
    global finl
    for i in range(len(table)):
        for i2 in range(len(table[0])):
            if empty[i][i2]=="" and tft[i][i2]==False:
                controller(table,i,i2)
                average_value=average(finl)
                for sat in range(len(tft)):
                    for sut in range(len(tft[0])):
                        if tft[sat][sut]==True and empty[sat][sut]=="":
                            empty[sat][sut]=average_value
                        else:
                            continue
                finl=[]
            elif empty[i][i2]==0:
                continue
            elif tft[i][i2]==True:
                continue
    return empty

def converterfinal(lst):
    l = [[[] for i in range(len(lst[0]))] for i2 in range(len(lst))]
    for i in range(len(lst)):
        for i2 in range(len(lst[0])):
            l[i][i2]=[lst[i][i2]]
    return l











def filter_maker(fil):
    fp=open(fil)
    first=fp.readline().strip().split()
    fin=[]
    fin.append(first)
    for i in range(len(first)-1):
        tmpt=fp.readline().strip().split()
        fin.append(tmpt)
    fp.close()
    return fin

def copy_table(lst):
    l = [[[] for i in range(len(lst[0]))] for i2 in range(len(lst))]
    for i in range(len(lst)):
        for i2 in range(len(lst[0])):
            l[i][i2] = lst[i][i2]
    return l

def tableslicer(table2,stride,a):
    table2 = table2[a:-a]
    lfin = []
    for i2 in table2:
        element = i2[a:-a]
        lfin.append(element)
    return lfin

def deepcopy(lst):
    l = [[[] for i in range(len(lst[0]))] for i2 in range(len(lst))]
    return l

def value_find(table1,filter,i,j,c,a):
    i=i
    j=j
    sum=0
    for sat in range(len(filter)):
        for sut in range(len(filter)):
            value=float(filter[sat][sut])*int(table1[i+sat][j+sut][c])
            sum+=value
    if sum>255: return 255
    elif sum<0: return 0
    else:
        return int(sum)

def maker(real_table,sliced_table,final_table,stride,a,i,j,c):
    limsat=len(sliced_table)-1
    limsut=len(sliced_table[0])-1

    if i>limsat:
        return final_table
    if j>limsut:
        j=0
        return maker(real_table,sliced_table,final_table,stride,a,i+stride,j,c)
    else:
        value1=value_find(real_table,filter_l,i,j,0,a)
        value2=value_find(real_table,filter_l,i,j,1,a)
        value3=value_find(real_table,filter_l,i,j,2,a)
        final_table[i][j]=[value1,value2,value3]
        return maker(real_table,sliced_table,final_table,stride,a,i,j+stride,c)

def slicing(lst):
    finall=[]
    for i in range(len(lst)):
        finall.append([])
        for i2 in range(len(lst[0])):
            if len(lst[i][i2])>0:
                finall[-1].append(lst[i][i2])
        if len(finall[-1])==0:
            finall.pop(-1)
    return finall


if operation==1:
    our_lst = read(filename)
    tft = tf_table(our_lst)
    empty_table=empty_final_table(our_lst)
    empty = zero_adder(our_lst, empty_table)
    final_form = formating(empty, our_lst)
    img_printer(converterfinal(final_form))
if operation==2:
    filtre = str(input())
    stride = int(input())
    table = read(filename)
    filter_l = filter_maker(filtre)
    table2 = copy_table(table)
    a = int(len(filter_l) / 2)
    table2 = tableslicer(table2, stride, a)
    empty_table = deepcopy(table)
    mk = maker(table, table2, empty_table, stride, a, 0, 0, 0)
    img_printer(slicing(mk))


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

