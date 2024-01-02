f = open("routes_paris.csv", 'r')
next(f)

for line in f:
    items = line.rstrip("\n").split(";")
    
    num_attributes = len(items)

    i = 0
    insert_line = "INSERT INTO routes_paris VALUES ( "
    while i < num_attributes:
        item = items[i].replace("'", "''")
        insert_line = insert_line + "'" + item + "'"
        if i != num_attributes - 1:
            insert_line = insert_line + ", "
        i = i + 1

    insert_line = insert_line + ");"
    print(insert_line)
