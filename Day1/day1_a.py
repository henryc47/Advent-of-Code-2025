import sys

def day_1_a(filename):
    first_list,second_list = extract_lists(filename)
    first_list.sort()
    second_list.sort()
    num_pairs = len(first_list)
    total_distance = 0
    for pair_num in range(num_pairs):
        distance = abs(first_list[pair_num]-second_list[pair_num])
        total_distance += distance
    return total_distance



def extract_lists(filename):
    file = open(filename,"r")
    first_list = []
    second_list = []
    for line in file:
        line_elements = line.split()
        first_element = int(line_elements[0])
        second_element = int(line_elements[1])
        first_list.append(first_element)
        second_list.append(second_element)
    return first_list,second_list



if __name__ == "__main__":
    num_args = len(sys.argv)-1
    if num_args<1:
        print("ERROR : Please provide filename",file=sys.stderr)
        sys.exit(1)
    else:
        filename = sys.argv[1]
        result = day_1_a(filename)
        print(result)
        