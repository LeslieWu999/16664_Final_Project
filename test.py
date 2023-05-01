import numpy as np
from glob import glob
import csv

classes = np.loadtxt('classes.csv', skiprows=1, dtype=str, delimiter=',')
labels = classes[:, 2].astype(np.uint8)


def write_labels(path):
    files = glob('{}/*/*_image.jpg'.format(path))
    files.sort()
    name = '{}/test_labels.csv'.format(path)
    with open(name, 'w') as f:
        writer = csv.writer(f, delimiter=',', lineterminator='\n')
        writer.writerow(['guid/image'])

        for file in files:
            guid = file.split('/')[-2]
            guid = 'D:/learning/Gradute Study/Trustworthy AI/' + guid
            idx = file.split('/')[-1]

            writer.writerow(['{}/{}'.format(guid, idx)])

    print('Wrote report file `{}`'.format(name))


if __name__ == '__main__':
    np.random.seed(0)
    for path in ['D:/learning/Gradute Study/Trustworthy AI/Project/test']:
        print(path)
        write_labels(path)