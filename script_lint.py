import sys
import os.path
from xml.etree import ElementTree

first = None
file_list = [
    "/Users/tedomanvelidze/StudioProjects/Dangerplayground/app/build/reports/lint-results-debug.xml",
    "/Users/tedomanvelidze/StudioProjects/Dangerplayground/testmodule/build/reports/lint-results-debug.xml"]

lintFile = 'lint-report-orig.xml'
editedlintFile = 'lint-report.xml'

for filename in file_list:
    if os.path.isfile(filename):
        data = ElementTree.parse(filename).getroot()
        if first is None:
            first = data
        else:
            first.extend(data)
if first is not None:
    f = open(lintFile, 'wb')
    f.write('\n'.encode())
    f.write(ElementTree.tostring(first))
    f.close()

delete_list = ["/Users/tedomanvelidze/StudioProjects/Dangerplayground/"]
fin = open(lintFile)
fout = open(editedlintFile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()
