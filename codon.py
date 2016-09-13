# codon = input('Input your codon please: ')
# codon_list = ['UAA','UAG','UGA']
# if codon == 'AUG':
#     print('Start codon.')
# elif codon in codon_list:
#     print('This codon is a stop codon.')
# else:
#     print('Not.')

seq = 'GACAGACUCCAUGCACGUGGGUAUCUGUC'
start_codon = 'AUG'
i           = 0

while seq[i:i+3] != start_codon and i < len(seq):
    i += 1

# Show the result
print('The start codon starts at index', i)
