from time import perf_counter
import math
t1_start = perf_counter()

with open("input/day24.txt") as f:
    input = [l.strip('\n') for l in f.readlines()]

    def parsemonad (monad):
        inputs = list(str(monad))
        monad = []
        for i in inputs:
            monad += [int(i)]
        return monad

    def alurun (input, alu):
        wxyz = [0,0,0,0]
        posdict = {'w':0, 'x':1, 'y':2, 'z':3}
        for i in alu:
            i = i.split()
            if i[0] == 'inp':
                wxyz[posdict[i[1]]] = input.pop(0)

            elif i[2] in ['w','x','y','z']:
                b = wxyz[posdict[i[2]]]
            else:
                b = int(i[2])
            
            if i[0] == 'add':
                wxyz[posdict[i[1]]] += b
            elif i[0] == 'mul':
                wxyz[posdict[i[1]]] = wxyz[posdict[i[1]]] * b
            elif i[0] == 'div':
                if b == '0':
                    return False
                else:
                    wxyz[posdict[i[1]]] = math.floor(wxyz[posdict[i[1]]] / b)
            elif i[0] == 'mod':
                if b == '0':
                    return False
                else:
                    wxyz[posdict[i[1]]] = wxyz[posdict[i[1]]] % b
            elif i[0] == 'eql':
                if wxyz[posdict[i[1]]] == b:
                    wxyz[posdict[i[1]]] = 1
                else:
                    wxyz[posdict[i[1]]] = 0
        return wxyz

    alphabet =     'abcdefghijklmn'
    testingnumber = 91297395919993
    testingnumber = 71131151917891
    
    



    def psuedocode (input):
        mod26list = [0]
        divz = [1,  1,  1,  1,  26, 1, 1, 26, 1, 26, 26, 26, 26, 26]
        alu1 = [14, 13, 15, 13, -2, 10,13,-15,11,-9, -9, -7, -4, -6]
        alu2 = [0,  12, 14, 0,  3,  15,11,12, 1, 12, 3,  10, 14, 12]
        for n, w in enumerate(parsemonad(input)):
            x = mod26list[-1] + alu1[n]
            if divz[n] == 26:
                mod26list.pop()
            if x != w:
                mod26list += [w + alu2[n]]
        zheight = 0
        z = 0
        while len(mod26list) != 0:
            z += (26**zheight)*mod26list[-1]
            zheight += 1
            mod26list.pop()
        return z

    # print(f"psuedocode answer: {z}")
    # print(f"answer using alu:  {alurun(parsemonad(testingnumber), input)[3]}")
    
    task_1 = 91297395919993
    task_2 = 71131151917891

    print(f"Part 1: 91297395919993. z = {psuedocode(task_1)}, {alurun(parsemonad(task_1), input)[3]}")
    print(f"Part 2: 71131151917891. z = {psuedocode(task_2)}, {alurun(parsemonad(task_2), input)[3]}")

    # see spreadsheet for workings


    t1_stop = perf_counter()
    print("\nElapsed time:", t1_stop - t1_start