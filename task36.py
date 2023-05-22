def print_operation_table(operation, num_rows=6, num_columns=6):
    el_lst1 = list()
    for i in range(1, num_rows + 1):
        el_lst = list()
        for j in range(1, num_columns + 1):
            el_lst.append(operation(i, j))
        el_lst1.append(el_lst)
    # print(el_lst1)
    
    for num in el_lst1:
        print(*[f"{el}" for el in num])

print_operation_table(lambda x, y: x * y)
