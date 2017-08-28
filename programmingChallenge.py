import json
import pandas as pd
try:
    with open("./jsonDump.txt","r") as f:
        jsonDump = f.read()
except Exception as ex:
    print "Error: Make sure jsonDump.txt exists in current directory before running"
    exit()

page_json = json.loads(jsonDump)
# coords = [(106, 711, 131, 728), (335, 637, 433, 649), (254, 637, 334, 649), (104, 637, 253, 649), (335, 623, 433, 635), (254, 623, 334, 635), (104, 623, 253, 635), (335, 594, 433, 621), (254, 594, 334, 621), (104, 594, 253, 621), (434, 569, 532, 649), (335, 569, 433, 593), (254, 569, 334, 593), (104, 569, 253, 593), (434, 540, 532, 566), (335, 540, 433, 566), (254, 540, 334, 566), (104, 540, 253, 566), (362, 190, 543, 218), (291, 190, 361, 218), (170, 190, 289, 218), (121, 190, 169, 218), (362, 160, 543, 188), (291, 160, 361, 188), (170, 160, 289, 188), (121, 160, 169, 188), (362, 131, 543, 159), (291, 131, 361, 159), (170, 131, 289, 159), (121, 131, 169, 159), (101, 71, 144, 110), (104, 67, 146, 106)]
# coords = [(106, 711, 131, 728), (335, 637, 433, 649), (254, 637, 334, 649), (104, 637, 253, 649), (335, 623, 433, 635), (254, 623, 334, 635), (104, 623, 253, 635), (335, 594, 433, 621), (254, 594, 334, 621), (104, 594, 253, 621), (434, 569, 532, 649), (335, 569, 433, 593), (254, 569, 334, 593), (104, 569, 253, 593), (434, 540, 532, 566), (335, 540, 433, 566), (254, 540, 334, 566), (104, 540, 253, 566), (362, 190, 543, 218), (291, 190, 361, 218), (170, 190, 289, 218), (121, 190, 169, 218), (362, 160, 543, 188), (291, 160, 361, 188), (170, 160, 289, 188), (121, 160, 169, 188), (362, 131, 543, 159), (291, 131, 361, 159), (170, 131, 289, 159), (121, 131, 169, 159)]
coords = [(78, 710, 133, 729), (106, 711, 131, 728), (103, 539, 533, 652), (335, 637, 433, 649), (254, 637, 334, 649), (104, 637, 253, 649), (335, 623, 433, 635), (254, 623, 334, 635), (104, 623, 253, 635), (335, 594, 433, 621), (254, 594, 334, 621), (104, 594, 253, 621), (434, 569, 532, 649), (335, 569, 433, 593), (254, 569, 334, 593), (104, 569, 253, 593), (434, 540, 532, 566), (335, 540, 433, 566), (254, 540, 334, 566), (104, 540, 253, 566), (120, 130, 544, 219), (362, 190, 543, 218), (291, 190, 361, 218), (170, 190, 289, 218), (121, 190, 169, 218), (362, 160, 543, 188), (291, 160, 361, 188), (170, 160, 289, 188), (121, 160, 169, 188), (362, 131, 543, 159), (291, 131, 361, 159), (170, 131, 289, 159), (121, 131, 169, 159), (101, 71, 144, 110), (104, 67, 146, 106)]

# table_cord_dict = {(103, 539, 533, 652): {'cell': [(335, 637, 433, 649), (254, 637, 334, 649), (104, 637, 253, 649), (335, 623, 433, 635), (254, 623, 334, 635), (104, 623, 253, 635), (335, 594, 433, 621), (254, 594, 334, 621), (104, 594, 253, 621), (434, 569, 532, 649), (335, 569, 433, 593), (254, 569, 334, 593), (104, 569, 253, 593), (434, 540, 532, 566), (335, 540, 433, 566), (254, 540, 334, 566), (104, 540, 253, 566)], 'header_cells': [(434, 540, 532, 566), (335, 540, 433, 566), (254, 540, 334, 566), (104, 540, 253, 566)], 'left_cells': [(104, 637, 253, 649), (104, 623, 253, 635), (104, 594, 253, 621), (104, 569, 253, 593), (104, 540, 253, 566)], 'table_type': 2}, (120, 130, 544, 219): {'cell': [(362, 190, 543, 218), (369, 199, 533, 210), (291, 190, 361, 218), (170, 190, 289, 218), (121, 190, 169, 218), (362, 160, 543, 188), (291, 160, 361, 188), (170, 160, 289, 188), (121, 160, 169, 188), (362, 131, 543, 159), (291, 131, 361, 159), (170, 131, 289, 159), (121, 131, 169, 159)], 'header_cells': [(362, 131, 543, 159), (291, 131, 361, 159), (170, 131, 289, 159), (121, 131, 169, 159)], 'left_cells': [(121, 190, 169, 218), (121, 160, 169, 188), (121, 131, 169, 159)], 'table_type': 2}}

# table_cord_dict = {(103, 539, 533, 652): {'cell': [(335, 637, 433, 649), (254, 637, 334, 649), (104, 637, 253, 649), (335, 623, 433, 635), (254, 623, 334, 635), (104, 623, 253, 635), (335, 594, 433, 621), (254, 594, 334, 621), (104, 594, 253, 621), (434, 569, 532, 649), (335, 569, 433, 593), (254, 569, 334, 593), (104, 569, 253, 593), (434, 540, 532, 566), (335, 540, 433, 566), (254, 540, 334, 566), (104, 540, 253, 566)], 'header_cells': [(434, 540, 532, 566), (335, 540, 433, 566), (254, 540, 334, 566), (104, 540, 253, 566)], 'left_cells': [(104, 637, 253, 649), (104, 623, 253, 635), (104, 594, 253, 621), (104, 569, 253, 593), (104, 540, 253, 566)], 'columns': {104: [(104, 540, 253, 566), (104, 569, 253, 593), (104, 594, 253, 621), (104, 623, 253, 635), (104, 637, 253, 649)], 434: [(434, 540, 532, 566), (434, 569, 532, 649)], 254: [(254, 540, 334, 566), (254, 569, 334, 593), (254, 594, 334, 621), (254, 623, 334, 635), (254, 637, 334, 649)], 335: [(335, 540, 433, 566), (335, 569, 433, 593), (335, 594, 433, 621), (335, 623, 433, 635), (335, 637, 433, 649)]}, 'table_type': 2}, (120, 130, 544, 219): {'cell': [(362, 190, 543, 218), (369, 199, 533, 210), (291, 190, 361, 218), (170, 190, 289, 218), (121, 190, 169, 218), (362, 160, 543, 188), (291, 160, 361, 188), (170, 160, 289, 188), (121, 160, 169, 188), (362, 131, 543, 159), (291, 131, 361, 159), (170, 131, 289, 159), (121, 131, 169, 159)], 'header_cells': [(362, 131, 543, 159), (291, 131, 361, 159), (170, 131, 289, 159), (121, 131, 169, 159)], 'left_cells': [(121, 190, 169, 218), (121, 160, 169, 188), (121, 131, 169, 159)], 'columns': {121: [(121, 131, 169, 159), (121, 160, 169, 188), (121, 190, 169, 218)], 170: [(170, 131, 289, 159), (170, 160, 289, 188), (170, 190, 289, 218)], 291: [(291, 131, 361, 159), (291, 160, 361, 188), (291, 190, 361, 218)], 362: [(362, 131, 543, 159), (362, 160, 543, 188), (362, 190, 543, 218)], 369: [(369, 199, 533, 210)]}, 'table_type': 2}}

# table_cord_dict = {(103, 539, 533, 652): {'cell': [(335, 637, 433, 649), (254, 637, 334, 649), (104, 637, 253, 649), (335, 623, 433, 635), (254, 623, 334, 635), (104, 623, 253, 635), (335, 594, 433, 621), (254, 594, 334, 621), (104, 594, 253, 621), (434, 569, 532, 649), (335, 569, 433, 593), (254, 569, 334, 593), (104, 569, 253, 593), (434, 540, 532, 566), (335, 540, 433, 566), (254, 540, 334, 566), (104, 540, 253, 566)], 'header_cells': [(434, 540, 532, 566), (335, 540, 433, 566), (254, 540, 334, 566), (104, 540, 253, 566)], 'left_cells': [(104, 637, 253, 649), (104, 623, 253, 635), (104, 594, 253, 621), (104, 569, 253, 593), (104, 540, 253, 566)], 'columns': {434: [(434, 540, 532, 566), (434, 569, 532, 649)], 254: [(254, 540, 334, 566), (254, 569, 334, 593), (254, 594, 334, 621), (254, 623, 334, 635), (254, 637, 334, 649)], 335: [(335, 540, 433, 566), (335, 569, 433, 593), (335, 594, 433, 621), (335, 623, 433, 635), (335, 637, 433, 649)]}, 'table_type': 2}, (120, 130, 544, 219): {'cell': [(362, 190, 543, 218), (369, 199, 533, 210), (291, 190, 361, 218), (170, 190, 289, 218), (121, 190, 169, 218), (362, 160, 543, 188), (291, 160, 361, 188), (170, 160, 289, 188), (121, 160, 169, 188), (362, 131, 543, 159), (291, 131, 361, 159), (170, 131, 289, 159), (121, 131, 169, 159)], 'header_cells': [(362, 131, 543, 159), (291, 131, 361, 159), (170, 131, 289, 159), (121, 131, 169, 159)], 'left_cells': [(121, 190, 169, 218), (121, 160, 169, 188), (121, 131, 169, 159)], 'columns': {369: [(369, 199, 533, 210)], 170: [(170, 131, 289, 159), (170, 160, 289, 188), (170, 190, 289, 218)], 291: [(291, 131, 361, 159), (291, 160, 361, 188), (291, 190, 361, 218)], 362: [(362, 131, 543, 159), (362, 160, 543, 188), (362, 190, 543, 218)]}, 'table_type': 2}}
table_cord_dict = {(103, 539, 533, 652): {'cell': [(335, 637, 433, 649), (254, 637, 334, 649), (104, 637, 253, 649), (335, 623, 433, 635), (254, 623, 334, 635), (104, 623, 253, 635), (335, 594, 433, 621), (254, 594, 334, 621), (104, 594, 253, 621), (434, 569, 532, 649), (335, 569, 433, 593), (254, 569, 334, 593), (104, 569, 253, 593), (434, 540, 532, 566), (335, 540, 433, 566), (254, 540, 334, 566), (104, 540, 253, 566)]}, (120, 130, 544, 219): {'cell': [(362, 190, 543, 218), (369, 199, 533, 210), (291, 190, 361, 218), (170, 190, 289, 218), (121, 190, 169, 218), (362, 160, 543, 188), (291, 160, 361, 188), (170, 160, 289, 188), (121, 160, 169, 188), (362, 131, 543, 159), (291, 131, 361, 159), (170, 131, 289, 159), (121, 131, 169, 159)]}}
left = [104, 254, 335, 434]
top = [540, 569, 594, 623, 637]

final_dict = {}
matrix = {}
for page in page_json:
    #import pdb;pdb.set_trace()
    for child in page['blocks']:
        for line in child['lines']:
            for span in line['spans']:
                #we encode to ascii to ignore strange unicode characters.
                #if you need them for some purpose, you can remove the
                #'.encode()' call and replace it.
                current_text = span['text'].encode('ascii',errors='ignore')
                current_bbox = span['bbox']
                round_off = 5
                for table_values in table_cord_dict.values():
                    table = table_values['cell']

                    for coord in table:
                        # for coord in col_coord:
                        if current_bbox[0] > (coord[0] - round_off) and current_bbox[1] > (coord[1] - round_off) and current_bbox[2] < (coord[2] + round_off) and current_bbox[3] < (coord[3] + round_off):
                            # print str(current_bbox).ljust(34), ": ",
                            # print current_text, coord

                            x, y = 0, 0
                            for l in left:
                                if l == coord[0]: y = left.index(l)
                            for t in top:
                                if t == coord[1]: x = top.index(t)

                            # print ' Cords', x, y
                            t = x, y
                            #print t
                            #matrix[t] = current_text
                            #print t, matrix[t], current_text
                            if t in matrix:
                                matrix[t] += current_text
                                #matrix[t] = matrix[t] + 'X' + current_text
                            else:
                                matrix[t] = current_text

                            #final_dict =

                            #if coord in final_dict:
                            #    final_dict[coord].append(current_text)
                            #else:
                            #    final_dict.update({coord:[current_text]})
                    break

                    #             pair_value = (coord[1] - round_off,coord[3] + round_off)
                    #             if pair_value in final_dict:
                    #                 final_dict[(pair_value,coord[0])].append(current_text)
                    #             else:
                    #                 final_dict.update({(pair_value,coord[0]):[current_text]})

                    # table = table_values['left_cells']
                    # for coord in table:
                    #     for value_range in final_dict:
                    #         # if coord[0] == value_range[1]:
                    #         #     print coord

                    #         if coord[1] >= value_range[0][0]-1 and coord[3]<= value_range[0][1]+1:
                    #             print "coord",coord
                    #             print "final_dict[value_range]",final_dict[value_range]

                        # if current_bbox[0] > (coord[0] - round_off) and current_bbox[1] > (coord[1] - round_off) and current_bbox[2] < (coord[2] + round_off) and current_bbox[3] < (coord[3] + round_off):
                        #     print str(current_bbox).ljust(34), ": ",
                        #     print current_text, coord
                        #     if coord in final_dict:
                        #         final_dict[coord].append(current_text)
                        #     else:
                        #         final_dict.update({coord:[current_text]})

# print matrix
final_dict={}
for elem in matrix:
    if elem[0] > 0:
        if matrix[(elem[0],0)] not in final_dict:
            final_dict[matrix[(elem[0],0)]] = {}
    print final_dict
    for elem2 in matrix:
        if elem[0] > 0 and elem[1] == 0 and elem2[0] == 0 and elem2[1] > 0:
            try:
                final_dict[matrix[(elem[0],0)]][matrix[(0,elem2[1])]] = matrix[(elem[0], elem2[1])]
            except Exception as exc:
                print exc

df = pd.DataFrame.from_dict(final_dict, orient='index').fillna(method='ffill')

            # if elem[0] == elem2[1]:
            #     print matrix[elem[0],elem[0]]


# sorted_list = sorted(matrix)
# for elem in sorted_list:

#     if elem[0] == 3:
#         print matrix[elem]

# for i in range(1, len(top)):
#     for j in range(1, len(left)-1):
#         #final_dict[matrix[i, 0]] = {matrix[0,j]:matrix[i,j]}

#         if matrix[i, 0] in final_dict:
#             final_dict[matrix[i, 0]].append({matrix[0,j]:matrix[i,j]})
#         else:
#             final_dict.update({matrix[i, 0]:[{matrix[0,j]:matrix[i,j]}]})
# print final_dict