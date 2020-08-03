#text = g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
#Rules:
#K->M
#O->Q
#E->G


import string

coded_string = "map"

alphabet_string = string.ascii_lowercase


alphabet_list = list(alphabet_string)

decoded_string = ""
for i in coded_string:
    if i in alphabet_list:
        coded_index = alphabet_list.index(i)
        decoded_index = coded_index+2
        if decoded_index>25:
            decoded_index-=26
        decoded_letter = alphabet_list[decoded_index]
    else:
        decoded_letter = i
    
    decoded_string= decoded_string+decoded_letter


print(decoded_string)
    
    



