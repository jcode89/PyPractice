from sys import argv

script, filename = argv

print "Opening %r" % filename
target = open(filename)

print "If you want to read the file hit ENTER."
raw_input("?")

print target.read()

target.close()