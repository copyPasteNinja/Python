def test():
    from csv import reader
    # open file in read mode
    with open('Trips.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            for item in row:
                if 'John Doe' in item:
                    one_row = row
                
    return one_row
