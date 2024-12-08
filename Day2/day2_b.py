import sys

def calculation(filename):
    reports = extract_reports(filename)
    num_safe = 0
    for report in reports:
        is_safe = is_report_safe(report)
        if is_safe:
            num_safe += 1
    
    return num_safe

def is_report_safe(report):
    is_safe = True
    removed_level = False
    num_removed = 0
    num_levels = len(report)
    if num_levels<=1: #only one report (or none!) always safe
        return is_safe
    last_level = report[0]
    direction = 0
    for i in range(1,num_levels):
        new_level = report[i]
        if new_level>last_level:
            if direction==-1:
                if removed_level==False:
                    num_removed += 1 #debug
                    removed_level = True
                    continue
                is_safe = False
                break
            direction = 1
            difference = new_level-last_level

        elif new_level<last_level:
            if direction==1:
                if removed_level==False:
                    num_removed += 1 #debug
                    removed_level = True
                    continue
                is_safe = False
                break
            direction = -1
            difference = last_level-new_level
        else: #new_level==old_level, is unsafe
            if removed_level==False:
                num_removed += 1 #debug
                removed_level = True
                continue
            is_safe = False
            break
        if difference<1 or difference>3:
            if removed_level==False:
                num_removed += 1 #debug
                removed_level = True
                continue
            is_safe = False
            break
        last_level = new_level
    print("report = ",report)
    print("levels removed = ",num_removed)
    print('safe = ',is_safe)
    print()
    return is_safe


def extract_reports(filename):
    reports = []
    file = open(filename,'r')
    for line in file:
        levels = line.split()
        report = [int(level) for level in levels]
        reports.append(report)
    return reports


if __name__ == "__main__":
    num_args = len(sys.argv)-1
    if num_args<1:
        print("ERROR : Please provide filename",file=sys.stderr)
        sys.exit(1)
    else:
        filename = sys.argv[1]
        result = calculation(filename)
        print(result)