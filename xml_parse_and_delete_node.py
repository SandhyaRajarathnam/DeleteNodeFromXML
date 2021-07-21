import xml.etree.ElementTree as ET
import time
import sys
import argparse
import getopt
import os

def showhelp(msg):
    print("""
usage: To delete the employee data of a specific employee id given as user input [--help] [--eid=EMPLOYEEID]
    
    Arguments:
    --help - Show help message and exit
    --eid - Input employee id
    
Script usage : python xml_parse_and _delete.py --eid <employee id>
    """)
    if msg: print("Error: %s"%msg)
    sys.exit()
#To read input.xml and remove the employee id provided as input and write it to output-timestsamp file
def removeEmployeeData(EMPLOYEEID):
    workingDir=os.path.dirname(os.path.realpath(__file__))
    xmlPath=workingDir + "/input.xml"
    tree=ET.parse(xmlPath)
    root=tree.getroot()
    employees = root.findall('employee')
    for employee in employees:
        employeeID=int(employee.find('id').text)
        eid=int (EMPLOYEEID)
        if employeeID == eid :
            root.remove(employee)
    timestamp=time.strftime("%Y-%m-%d-%H-%M-%s")
    fileToWrite=workingDir + "/" + timestamp + ".xml"
    tree.write(fileToWrite)
    print(fileToWrite)

if __name__ == '__main__':
    try:
        opts,xargs = getopt.getopt(sys.argv[1:],"", ["help","eid="])
    except getopt.GetoptError as err:
        showhelp()

    EMPLOYEEID=""
    for k,v in opts:
        if k=="--eid":
            EMPLOYEEID=v.strip()
    if not (EMPLOYEEID):
        showhelp("")

    if EMPLOYEEID:
        removeEmployeeData(EMPLOYEEID)

