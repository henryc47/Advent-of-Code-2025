import sys

def calculation(filename):
    reports = extract_reports(filename)
    print(reports)


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