rbs = 'AACAGAGGAGA'
start_codon = 'ATG'

def make_rev_complement(string):
    new_str = ''
    for s in string:
        char = ''
        if s == 'A':
            char = 'T'
        elif s == 'T':
            char = 'A'
        elif s == 'C':
            char = 'G'
        elif s == 'G':
            char = 'C'
        else:
            print('UH OH! Character not A, T, C, or G')
        new_str += char
    new_str = new_str[::-1]
    return new_str

# Make function to check for stop codons
def check_for_stop(toehold):
    stop_codons = ['TAG', 'TAA', 'TGA']
    location_of_start = 47
    search1 = toehold.find(stop_codons[0]) == location_of_start
    search2 = toehold.find(stop_codons[1]) == location_of_start
    search3 = toehold.find(stop_codons[2]) == location_of_start
    return (search1 | search2  | search3)

# Make function to actually turn trigger into toehold
def turn_switch_to_toehold(switch):
    stem1 = make_rev_complement(switch[24:30])
    stem2 = make_rev_complement(switch[12:21])
    toehold = switch + rbs + stem1 + start_codon + stem2
    return toehold


# check rev comp
def check_rev_comp(full_59nt):
    stem1 = make_rev_complement(full_59nt[24:30])
    stem2 = make_rev_complement(full_59nt[12:21])
    stem1_comp = full_59nt[41:47]
    stem2_comp = full_59nt[50:59]

    return ((stem1 == stem1_comp) and (stem2 == stem2_comp))
# check rbs and start codon are unchanged
def check_rbs_and_start(full_59nt):
    rbs_exists = (full_59nt[30:41] == rbs)
    start_exists = (full_59nt[47:50] == start_codon)
    return(rbs_exists and start_exists)