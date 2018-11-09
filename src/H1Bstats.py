'''
Name : Shruti Nair
Insight Data Engineering Program Code Challenge
'''
import sys


# Read csv and store the data in a dictionary with key as case id and the remaining fields as values. Repeat with header.
def read_csv(data_file):
    data = {}
    header = {}

    with open(data_file, 'r') as f:
        for line in f:
            colnames = line.strip().split(';')
            header[colnames[1]] = colnames[2:]
            break

        for line in f:
            words = line.strip().split(';')
            data[words[1]] = words[2:]

    return data, header


# Standardize column names for input files
def change_col_names(header):
    for k,v in header.iteritems():
        if("STATUS" in v):
        	v[v.index("STATUS")] = "CASE_STATUS"
        if("LCA_CASE_SOC_NAME" in v):
            v[v.index("LCA_CASE_SOC_NAME")]  = "SOC_NAME"
        if("LCA_CASE_WORKLOC1_STATE" in v):
            v[v.index("LCA_CASE_WORKLOC1_STATE")] = "WORKSITE_STATE"


# Retrieve column number for the required columns from the header dictionary
def get_colnum(header):
    for key, value in header.iteritems():
        casestatus_colnum = value.index("CASE_STATUS")
        casesoc_colnum = value.index("SOC_NAME")
        casestate_colnum = value.index("WORKSITE_STATE")
        return casestatus_colnum, casesoc_colnum, casestate_colnum


# Retrieve occupations for certified cases
def get_certified_soc(data, col_status, col_soc):
    col_values = []
    for key, value in data.iteritems():
        if value[col_status] == 'CERTIFIED':
            col_values.append(value[col_soc].replace('"', ''))
    return col_values


# Retrieve states for certified cases
def get_certified_state(data, col_status, col_state):
    col_values = []
    for key, value in data.iteritems():
        if value[col_status] == 'CERTIFIED':
            col_values.append(value[col_state].replace('"', ''))
    return col_values


# Calculate frequency grouped by occupation
def get_freq_soc(data):
    frequency_occupation = {}
    for val in data:
        if len(val) != 0:
            if val not in frequency_occupation.keys():
                frequency_occupation[val] = 1
            else :
                frequency_occupation[val] += 1
    return frequency_occupation


# Calculate frequency grouped by state
def get_freq_states(data):
    frequency_states = {}
    for val in data:
        if len(val) != 0:
            if val not in frequency_states.keys():
                frequency_states[val] = 1
            else :
                frequency_states[val] += 1
    return frequency_states


# Write final output to csv
def write_to_csv(data, output_file, option):
    with open(output_file, 'w') as f:
        if option == 1 :
            f.write("TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE" + "\n")
        if option == 2 :
            f.write("TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE" + "\n")
        for row in range(len(data)):
            for val in range(len(data[row])):
                if val != len(data[row]) - 1:
                	f.write(str(data[row][val]) + ";")
                else :
                    f.write(str(data[row][val]))
            f.write("\n")


# Read file names from command line
input_file, output_file1, output_file2 = sys.argv[1], sys.argv[2], sys.argv[3]

data, header = read_csv(input_file)
change_col_names(header)
col_status, col_soc, col_state = get_colnum(header)
certified_soc = get_certified_soc(data, col_status, col_soc)
certified_state = get_certified_state(data, col_status, col_state)

# Occupation wise count
count1 = get_freq_soc(certified_soc)
occupation, count = (list(count1.keys()), list(count1.values()))
# Sort by count and incase of tie alphabetically by occupation name
sorted_occupation = sorted(zip(occupation, count), key=lambda val:(-val[1], val[0]))
occupation, count = zip(*sorted_occupation)
total = sum(count)
# calculate percentage for each occupation
percents = [str(round(a*b, 1)) +'%' for a,b in zip(count, [100.0 / total] * 10)]
# Retrieve top 10 from list
occupation_stats = [[occupation[i],count[i],percents[i]] for i in range(0, min(10, len(count)))]

# State wise count
count2 = get_freq_soc(certified_state)
state, count = (list(count2.keys()), list(count2.values()))
# Sort by count and incase of tie alphabetically by state name
sorted_state = sorted(zip(state, count), key=lambda val:(-val[1], val[0]))
unzipped_ = list(zip(*sorted_state))
state, count = list(unzipped_[0]), list(unzipped_[1])
total = sum(count)
# calculate percentage for each state
percents = [str(round(a*b, 1)) +'%' for a,b in zip(count, [100.0 / total] * 10)]
# Retrieve top 10 from list
state_stats = [[state[i],count[i],percents[i]] for i in range(0, min(10, len(count)))]

write_to_csv(occupation_stats, output_file1, 1)
write_to_csv(state_stats, output_file2, 2)

