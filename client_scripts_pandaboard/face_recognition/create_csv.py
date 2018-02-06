import sys
import os.path


if __name__ == "__main__":


# Base path is the path to the directory just before going into the sample images
    if len(sys.argv) != 2:
        print "usage: create_csv.py <base_path>"
        sys.exit(1)

    BASE_PATH=sys.argv[1]
    print(BASE_PATH)
    SEPARATOR=";"
    
    label = 0
    for dirname, dirnames, filenames in os.walk(BASE_PATH):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                abs_path = "%s/%s" % (subject_path, filename)
                print "%s%s%d" % (abs_path, SEPARATOR, label)
            label = label + 1
