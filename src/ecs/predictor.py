# coding=utf-8

import bpnn
#整数矩阵
def make_int_matrix(n, fill=0):
    mat = []
    for i in range(n):
        mat.append(0)
    return mat
def predict_vm(ecs_lines, input_lines):
    # Do your work from here#
    result = []
    if ecs_lines is None:
        print 'ecs information is none'
        return result
    if input_lines is None:
        print 'input file information is none'
        return result

    #物理服务器基本信息
    physicalServer = []
    physicalServerNum = []
    line = ecs_lines[0]
    physicalServer=line.split(' ')
    physicalServerNum.append(int(physicalServer[0]))
    physicalServerNum.append(int(physicalServer[1]))
    physicalServerNum.append(int(physicalServer[2]))

    virNum = int(ecs_lines[2])
    virDev = ecs_lines[3:virNum+3]
    opPara = ecs_lines[virNum+4]
    timePreone = int(ecs_lines[virNum+6][8:10])
    timePretwo = int(ecs_lines[virNum+7][8:10])
    testTime = []
    for itime in range(timePreone,timePretwo+1):
        testTime.append(itime)
    # print virNum
    # print virDev
    # print opPara
    #print timePreone
    #print timePretwo

    res = make_int_matrix(25)
    #print res

    dfs = []
    cases = []
    labels = []
    dt = input_lines[0].split('\t')[2][:10]
    dfs.append(int(dt[8:10]))
    cases.append(int(dt[8:10]))
    #print input_lines[0].split('\t')[1][6:]
    for ip_line in input_lines:
        dts =ip_line.split('\t')
        if (cmp(dts[2][:10],dt)==0):
            #print int(ip_line.split('\t')[1][6:])
            res[int(ip_line.split('\t')[1][6:])] = res[int(ip_line.split('\t')[1][6:])]+1
        else:
            labels.append(res)
            res = make_int_matrix(25)
            dt = ip_line.split('\t')[2][:10]
            #dfs.append(int(dt[8:10]))
            cases.append(int(dt[8:10]))
            res[int(ip_line.split('\t')[1][6:])] = res[int(ip_line.split('\t')[1][6:])] + 1
    labels.append(res)
    caseList = []
    for ki in cases:
        caseList.append([ki])
    print caseList
    print labels
    nn = bpnn.BPNeuralNetwork()
    nn.test(cases,labels,testTime)
    return result
