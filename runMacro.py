import csv
from subprocess import run
from pywinauto.application import Application
from threading import Thread
from time import sleep



def pressOkParallel():
    def clickit():
        sleep(5)
        sapExe = r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe"
        app = Application(backend="uia").connect(path=sapExe)
        # app.window(title_re="^SAP Easy Access")
        app["SAP LogonPane"]["OKButton"].click()
    
    t = Thread(target=clickit)
    t.start()


def run_sap_enter_part_v1(materialnumber, description, distributionchannel, salesorg):
    run(["cscript.exe", "./sap_enter_part_v1.vbs", materialnumber, description, distributionchannel, salesorg])


def pickATask(row):
    if 5 > 4:
        run_sap_enter_part_v1(**row)
    elif 4 < 2:
        print("Todo: add real conditions here")


def main():
    with open("data.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            pressOkParallel()       
            pickATask(row)


if __name__ == "__main__":    
    main()
    