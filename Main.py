import copy

#generates a list of all ways to order numbers up to max_value with number_of_elements slots
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


#removes cofrd that are mirrored versions of another code (leaving one of the two mirrored versions ofc)
#WARNING!!!!! ONLY WORKS WITH CODES WITH ONE EDGE AS OF 7/7/25
#to do: generalize this to all ribbon codes
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


#generates all codes that fit a certain template
#WARNING!!!!!!! ONLY WORKS WITH CODES WITH ONE EDGE AS OF 7/7/25
#To do: generalize to other code types
def generate_codes_within_family(matrix, template):
    ribbon_codes = []
    for i in matrix:
        temp_code = copy.deepcopy(template)
        temp_code[0][0] = i[:]
        ribbon_codes.append(temp_code[:])
    print(len(ribbon_codes))
    return ribbon_codes

def get_valence():
    pass
    #to do

#applies rule 5( and also 6) from Bounds, Jones determinants, irreducible codes to a list of ribbon codes to remove reducible codes
def apply_rule_5(code_list):
    filtered_code_list = []

    for code in code_list:
        should_remove = False
        for column in code:
            for marking in column:
                if marking == 0:
                    continue
                if not isinstance(marking, list):
                    continue
                if len(marking) < 2:
                    continue

                last_val = marking[0]
                for val in marking[1:]:
                    if val == last_val:
                        should_remove = True
                        break
                    last_val = val

                if should_remove:
                    break
            if should_remove:
                break

        if not should_remove:
            filtered_code_list.append(code)

    return filtered_code_list

                        
#applies reduction rules to remove reducible codes
#Not finished as of 7/7/35
def remove_reducible_codes(code_list):
    working_list = apply_rule_5(code_list)
    
four_vertex_template = [[[],0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

x = order_values(3, 4)
x = remove_duplicates(x)

code_list = generate_codes_within_family(x,four_vertex_template)

print(code_list)
for i in range(10):
    print()

print(apply_rule_5(code_list))

