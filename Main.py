import copy
def order_values(max_value, number_of_elements):
    working_list = [0] * number_of_elements
    working_value_matrix = []

    done_flag = False

    while not done_flag:
        working_value_matrix.append(working_list[:])
        print(working_list) 

        index = number_of_elements - 1
        while index >= 0:
            if working_list[index] < max_value:
                working_list[index] += 1
                break
            else:
                working_list[index] = 0
                index -= 1
        else:
            done_flag = True
    return working_value_matrix

def remove_duplicates(matrix):
    seen = set()
    unique = []

    for lst in matrix:
        t = tuple(lst)
        t_rev = tuple(reversed(lst))
        if t not in seen and t_rev not in seen:
            unique.append(lst)
            seen.add(t)
            seen.add(t_rev)
    return unique



def generate_codes_within_family(matrix, template):
    ribbon_codes = []
    for i in matrix:
        temp_code = copy.deepcopy(template)
        temp_code[0][0] = i[:]
        ribbon_codes.append(temp_code[:])
    print(len(ribbon_codes))
    return ribbon_codes



    
four_vertex_template = [[[],0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

x = order_values(3, 4)
x = remove_duplicates(x)

print(generate_codes_within_family(x,four_vertex_template))

