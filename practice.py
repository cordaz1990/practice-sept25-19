def sum_number_pairs(input_file: TextI0, out_file: TextIO) -> None:
    """ Read the data from input_file, which contains two floats per line 
        seperated by a space. output_file for writing and, for each line in 
        input_file, write a line to output_file that contains the two floats from the 
        corresponding line of input_file plus a space and the sum of the two floats."""
    
    for number_pair in input_file:
        number_pair = number_pair. strip()
        operands = number_pair.split()
        total = float(operands[0]) + float(operands[1])
        new_line = '{0} {1}\n'.format(number_pair, total)
        output_file.write(new_line)
        
    if __name__ == '__main__':
       with open('numbers_pairs.txt', 'r') as input_file,\
        open('number_pair_sums.txt','w')as output_file:
       sum_nmber_pairs(input_file, output_file)
