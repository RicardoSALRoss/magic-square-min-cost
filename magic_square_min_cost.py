def formingMagicSquare(s):
    import numpy as np
    from itertools import permutations
    matrix=[]
    count=0
    numeros=[]
    while (count<len(s)**2):
        numeros.append(count+1)
        count=count+1

    def obter_arranjos(elementos, tamanho_arranjo):
        return list(permutations(elementos, tamanho_arranjo))

    def possui_duplicatas(lista):
        conjunto = set()
        for elemento in lista:
            if elemento in conjunto:
                return True
            conjunto.add(elemento)
        return False

    rows_control=obter_arranjos(numeros,len(s)) 
    rows=[]
    for row in rows_control:
        rows.append(list(row))
    i_rows_control=obter_arranjos(list(range(1,len(rows)+1)),len(s))
    i_rows=[]
    for i_row in i_rows_control:
        double=False
        n=[]
        for indice in i_row:
            for number in rows[indice-1]:
                n.append(number) 
        double=possui_duplicatas(n)
        if (double!=True):
            i_rows.append(list(i_row))
    j=[]
    for conjunto in i_rows:
        list_control=[]
        for i in conjunto:
            k=i-1
            list_control.append(k)
        j.append(list_control)
    row_sum=0
    column_sum=0
    all_costs=[]
    min_cost=0
    for lines in j:
        matrix_control=[]
        is_magic=True
        for i in lines:
            matrix_control.append(list(rows[i]))
        row_sum=sum(matrix_control[0])
        for row in matrix_control:
            if (sum(row)!=row_sum):
                is_magic=False
        matrix_transpost=np.transpose(matrix_control)
        control=[]
        for line in matrix_transpost:
            line_control=list(line)
            control.append(line_control)
        column_sum=sum(control[0])
        for column in control:
            if (sum(column)!=column_sum or (is_magic==True and column_sum!=row_sum)):
                is_magic=False
        diagonal_principal=[matrix_control[i][i] for i in range(min(len(matrix_control), len(matrix_control[0])))]
        diagonal_secundaria=[matrix_control[i][len(matrix_control)-1-i] for i in range(min(len(matrix_control), len(matrix_control[0])))]
        if (is_magic==True and sum(diagonal_principal)==sum(diagonal_secundaria) and sum(diagonal_principal)==column_sum and sum(diagonal_principal)==row_sum):
            costs=[]
            for line in matrix_control:
                for element in line:
                    cost=abs(element-(s[matrix_control.index(line)][line.index(element)]))
                    costs.append(cost)
            all_costs.append(sum(costs))
            if (sum(costs)<min(all_costs)):
                matrix=matrix_control
            print("Magic Square: ",matrix_control, "COST: ", sum(costs))
        else:
            is_magic=False
    if (all_costs!=[]):
        return min(all_costs)
