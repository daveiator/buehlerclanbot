import csv

def getAttribute(attr):
    filepath = "config.txt"
    output = 404
    try:
        f = open(filepath)
    except IOError:
        print(filepath+" not found! Creating new file")
        f = open(filepath, "w")
    finally:
        f.close()
    csv_file = open(filepath, "r")
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        try:
            if(row[0] == attr):
                print(attr+" found!")
                output = row[1]
                csv_file.close()
                return output
        except IndexError:
            pass
    print("No "+attr+" found!\nPlease set new "+attr+": ")
    output = input()
    csv_file.close()
    csv_file = open(filepath, "a")
    csv_writer = csv.writer(csv_file, delimiter='\t')
    csv_writer.writerow([attr,output])
    csv_file.close()
    return output
