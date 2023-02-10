
ben = [-100, 250, 320, 480, 520, 520, 410, 120]
stages = int(input('Enter Number of Stages : '))
storage = int(input('Enter Storage : '))
inflow = int(input('Enter inflow : '))

maxben=[]
def maximum(s):
    st= (s+inflow)%storage
    return max(ben[st:(s+inflow+1)])

print("Stage %d :"%stages)
print("S4\tR4\tBenifit\t MAX\tR4")
print("---------------------------------------")
for i in range(storage+1):
    for j in range(i+inflow+1):
        if i+inflow-j <= 4:
            print(i,'\t',j,'\t',ben[j],'\t')
    m =  maximum(i)
    maxben.append(m)
    print('\t\t\t',m,'\t',[index for index, value in enumerate(ben) if value == m and index <=j])

stages-=1
while stages>0:
    temp2=[]
    print("\n--------------------------------------------------------------")
    print("Stage %d:"%stages)
    inflow = int(input('Enter inflow : '))
    print("S%d\tR%d\tBenifit\tS+Q-R\t B[R%d]\t F%d\t MAX \t R%d"%(stages,stages,stages,stages,stages))
    print("--------------------------------------------------------------")
    for i in range(storage+1):
        tmp=[]
        tmp3=[]
        for j in range(i+inflow+1):
            if i+inflow-j <= 4:
                print(i,'\t',j,'\t',ben[j],'\t',(i+inflow-j),'\t',maxben[i+inflow-j],'\t',maxben[i+inflow-j]+ben[j])
                tmp.append(maxben[i+inflow-j]+ben[j])
                tmp3.append(j)
        m =  max(tmp)
        temp2.append(m)
        print('\t\t\t\t\t\t',m,'\t',[tmp3[k] for k in [index for index, value in enumerate(tmp) if value == m and index <=j]])
    stages-=1
    maxben=temp2





maxben

