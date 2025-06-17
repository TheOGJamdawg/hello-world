originating_file = input("Please input the name of the file you want to copy: ")
destination_file = input("Please input the name of the file you want the contents copied to: ")

source = open(originating_file, 'r')
contents = source.read()

destination = open(destination_file, 'w')
destination.write(contents)

source.close()
destination.close()

print("If you see this text, the file copy was completed.")
