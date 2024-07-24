grades_st = [[5, 3, 3, 5,4], [2,2,2,3], [4,5,5,2],[4,4,3], [5,5,5,4,5]]
print(type(grades_st))
print(grades_st)

name_st = {'Johnny', 'Bilbo', 'Steva', 'Khendrik', 'Aaron'}
print(type(name_st))
print(name_st)


name_st_sort = sorted(name_st)
print(type(name_st_sort))
print(name_st_sort)

zipped_name_gr = zip(name_st_sort, grades_st)
print(zipped_name_gr)
print(type(zipped_name_gr))
name_gr_list = list(zipped_name_gr)
print(type(name_gr_list))
print(name_gr_list)

grades_aver = [[sum(grades_st[0])/len(grades_st[0])],[sum(grades_st[1])/len(grades_st[1])],
               [sum(grades_st[2])/len(grades_st[2])],[sum(grades_st[3])/len(grades_st[3])],
               [sum(grades_st[4])/len(grades_st[4])]]
print(name_st_sort[0],':',grades_aver[0],';',
      name_st_sort[1],':',grades_aver[1],';',
      name_st_sort[2],':',grades_aver[2],';',
      name_st_sort[3],':',grades_aver[3],';',
      name_st_sort[4],':', grades_aver[4])





