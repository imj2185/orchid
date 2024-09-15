import re

# Function to convert TXT to TSV
def txt_to_tsv(input_txt_file, output_tsv_file):
    with open(input_txt_file, 'r') as txt_file:
        lines = txt_file.readlines()

    # Assuming the input file is space-separated, you can modify this depending on the delimiter in your TXT file
    with open(output_tsv_file, 'w') as tsv_file:
        for line in lines:
            # Replace spaces with tabs
            line = line.strip().replace(' ', '\t')
            
            # Find all numbers in the line and add 1 to each
            modified_line = re.sub(r'\d+', lambda x: str(int(x.group()) + 1), line)
            
            tsv_file.write(modified_line + '\n')

# Example usage
input_txt = '/home/hbp5148/Desktop/orchid/data/edges.txt'
output_tsv = '/home/hbp5148/Desktop/orchid/data/edges.tsv'

txt_to_tsv(input_txt, output_tsv)
