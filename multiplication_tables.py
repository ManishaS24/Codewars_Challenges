def multiplication_table(row,col):
    # Good Luck!
    final_arr = []
    new_arr = []
    

    for i in range(col):
        new_arr.append(i+1)

    #final_arr.append(new_arr)
    for i in range(row):
        final_arr.append(list(map(lambda x: x*(i+1), new_arr)))

    print(final_arr)

multiplication_table(3,3)