import os
import json
import argparse
import numpy as np

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='csv2json: A python tool to convert csv particle position data into json format compatible with tredify for animations.')
    parser.add_argument('-i', '--input', type=str, help='Input directory where the csv files are. Files are sorted numerically to create the sequence. Expected filename format #.csv, i.e: 1.csv, 2.csv ... 10.csv ... etc. Files are assumed to have x, y, z coordinates on columns 0, 1 and 2 respectively. One row per particle. One file per sequence step.',
                        required=True)
    parser.add_argument('-o', '--output', type=str, help='Output json file. Must be a full path', required=True)
    parser.add_argument('-s', '--skip', type=int, help='Number of lines to skip from the begining of the file (i.e column names, etc)', required=False, default=0)

    args = parser.parse_args()

    try:
        file_list = os.listdir(args.input)
    except OSError:
        print 'Invalid input directory'
        exit(1)

    indexes = []
    positions = []

    for file_name in file_list:
        try:
            index = int(file_name.split('.')[0])
        except (ValueError, IndexError):
            print 'Incorrect filename. Expected numeric, i.e: 1.csv, 2.csv, etc. Found: {filename}'.format(file_name=file_name)
            exit(1)
        else:
            indexes.append(index)
            file_data = np.loadtxt('{dir}/{filename}'.format(dir=args.input,
                                                             filename=file_name),
                                   skiprows=args.skip, delimiter=',')
            # Slice to get first 3 columns, assumed to contain x, y, z positions
            x = file_data[:, 0]
            y = file_data[:, 1]
            z = file_data[:, 2]

            positions.append({'x': x.tolist(),
                              'y': y.tolist(),
                              'z': z.tolist()})

    # Get the sorted indexes for the file names (contained in the indexes)
    # because listdir return them in random order.
    sorted_indexes = np.array(indexes).argsort()
    # Use the sorted indexes to sort the positions data in a valid sequence for animation
    positions = np.array(positions)[sorted_indexes]

    f = open(args.output, 'w')

    json.dump(positions.tolist(), f)

    f.close()
