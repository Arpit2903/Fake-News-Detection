import pickle


def pickle_data(data, output_binary_file):
    # Pickling the data
    outfile = open(output_binary_file, 'wb')  # w = writing to the file, b=binary mode
    pickle.dump(data, outfile)
    outfile.close()


def unpickle_data(output_binary_file):
    # Unpickling the data
    infile = open(output_binary_file, 'rb')
    new_data = pickle.load(infile)
    infile.close()
    return new_data
