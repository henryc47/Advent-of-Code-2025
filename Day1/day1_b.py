import sys

def day_1_a(filename):
    first_list,second_list = extract_lists(filename)
    first_list.sort()
    second_list.sort()
    total_similarity = 0
    second_frequency_dict = {}
    for item in second_list:
        if item in second_frequency_dict:
            second_frequency_dict[item] += 1
        else:
            second_frequency_dict[item] = 1
    for item in first_list:
        if item in second_frequency_dict:
            frequency = second_frequency_dict[item]
            similarity = item*frequency
            total_similarity += similarity
    
    return total_similarity

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