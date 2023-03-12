import sys
import os.path
from xml.etree import ElementTree

first = None
file_list = [
    "/Users/tedomanvelidze/StudioProjects/Dangerplayground/app/build/reports/ktlint/ktlintAndroidTestSourceSetCheck/ktlintAndroidTestSourceSetCheck.xml",
    "/Users/tedomanvelidze/StudioProjects/Dangerplayground/app/build/reports/ktlint/ktlintMainSourceSetCheck/ktlintMainSourceSetCheck.xml",
    "/Users/tedomanvelidze/StudioProjects/Dangerplayground/app/build/reports/ktlint/ktlintTestSourceSetCheck/ktlintTestSourceSetCheck.xml"
]

ktlintFile = 'ktlint-report-orig.xml'
editedKtlintFile = 'ktlint-report.xml'

for filename in file_list:
    if os.path.isfile(filename):
        data = ElementTree.parse(filename).getroot()
        if first is None:
            first = data
        else:
            first.extend(data)
if first is not None:
    f = open(ktlintFile, 'wb')
    f.write("<?xml version='1.0' encoding='utf-8'?>".encode())
    f.write(bytes('\n', encoding='utf8'))
    f.write(ElementTree.tostring(first))
    f.close()

delete_list = ["/Users/tedomanvelidze/StudioProjects/Dangerplayground/"]
fin = open(ktlintFile)
fout = open(editedKtlintFile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()
