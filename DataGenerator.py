import random

def DataGenerator(nb_node, nb_obs, min_val, max_val):

    # Filename to write
    filename = "newfile.txt"

    # Open the file with writing permission
    myfile = open(filename, 'a')

    # Write a line to the file
    for i in range(0, nb_node):
        values = ""
        for obs in range(0, nb_obs):
            obs = random.randrange(min_val, max_val)
            values = values + str(obs) + ','
        values = values[:-1]
        if i == nb_node - 1:
            myfile.write(str(i) + ":" + values)
        else:
            myfile.write(str(i) + ":" + values + "\n")

    # Close the file
    myfile.close()

DataGenerator(10, 5, 0, 10)