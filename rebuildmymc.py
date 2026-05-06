import os
import platform

# OS Detection
osname = platform.system()
if osname == "Windows":
    print("Windows detected.")
elif osname == "Linux":
    print("Linux detected.")
elif osname == "Darwin":
    print("macOS detected.")
else:
    print("Your OS is currently unsupported!")
    print("This script currently only supports Windows, Linux and macOS.")
    print("Press Ctrl+C to exit...")
    while True:
        print("", end="")

def clear():
    if osname == "Windows":
        os.system("cls")
    else:
        os.system("clear")

print("================================================================================")
print("                              SCRIPT PREREQUISITES                              ")
print("--------------------------------------------------------------------------------")
print("JDK and JRE must be fully installed.")
print("The following files must be present in the same folder as this script:")
print("1. The Minecraft .jar")
print("2. The 'jar' and 'native' folders from the LWJGL .zip")
print("Other than these files, it is recommended to run this script in an empty folder!")
print("================================================================================")
print("To cancel the script, press Ctrl+C.")
print("Once these requirements are met, enter 'ready' to continue: ")
conf = ""
while conf != "ready":
    conf = input()

def exists(fname):
    try:
        tmp = open(fname)
    except FileNotFoundError:
        return False
    else:
        tmp.close()
        return True

valid = False
clear()
while not valid:
    mcjar = input("Enter the name of the Minecraft .jar file (excluding '.jar'): ")
    mcjar += ".jar"
    if exists(mcjar):
        if mcjar in ["lwjgl.jar", "lwjgl_util.jar", "jinput.jar"]:
            print("")
            print("That is the wrong file!")
        else:
            valid = True
    else:
        print("")
        print("File not found!")

# Check that LWJGL files exist
clear()
if osname == "Windows":
    os.system("copy jar\\* .")
else:
    os.system("cp jar/* .")
prereqs = True
for x in ["lwjgl.jar", "lwjgl_util.jar", "jinput.jar"]:
    if not exists(x):
        prereqs = False
if not prereqs:
    print("One or more LWJGL files not found!")
    print("The required files are: lwjgl.jar, lwjgl_util.jar, jinput.jar")
    print("Please ensure that the 'jar' folder contains the correct files!")
    print("Press Ctrl+C to exit...")
    while True:
        print("", end="")
else:
    print("LWJGL files found.")

# Extract .jar files
for x in [mcjar, "lwjgl.jar", "lwjgl_util.jar", "jinput.jar"]:
    print("Extracting " + x + "...")
    command = "jar xf \"" + x + "\""
    os.system(command)

# Delete META-INF folder
if osname == "Windows":
    os.system("rmdir /s /q META-INF")
else:
    os.system("rm -rf META-INF")

# Write project info to manifest
manifest = open("MANIFEST.MF", "w")
manifest.write("Manifest-Version: 1.0\n")
manifest.write("Main-Class: net.minecraft.client.Minecraft\n")
manifest.close()

# Build .jar
print("Building minecraft.jar...")
os.system("jar cfm minecraft.jar MANIFEST.MF .")

# Add natives
os.system("mkdir natives")
for x in ["windows", "linux", "macosx"]:
    if osname == "Windows":
        command = "copy native\\" + x + "\\* natives"
    else:
        command = "cp native/" + x + "/* natives"
    os.system(command)

# Add run scripts
run = open("run.cmd", "w")
run.write("java -Djava.library.path=..\\natives -jar ..\\minecraft.jar")
run.close()

run = open("run-nogpu.cmd", "w")
run.write("java -Dorg.lwjgl.opengl.Display.allowSoftwareOpenGL=true -Djava.library.path=..\\natives -jar ..\\minecraft.jar")
run.close()

run = open("run.sh", "w")
run.write("#!/bin/bash\n")
run.write("java -Djava.library.path=../natives -jar ../minecraft.jar\n")
run.close()

run = open("run-nogpu.sh", "w")
run.write("#!/bin/bash\n")
run.write("java -Dorg.lwjgl.opengl.Display.allowSoftwareOpenGL=true -Djava.library.path=../natives -jar ../minecraft.jar\n")
run.close()

os.system("mkdir run")
if osname == "Windows":
    os.system("move *.cmd run")
    os.system("move *.sh run")
else:
    os.system("chmod +x run.sh")
    os.system("chmod +x run-nogpu.sh")
    os.system("mv *.cmd run")
    os.system("mv *.sh run")

print("\n\n\n")
print("Done! Scripts to run the game can be found in the run folder.")
if osname == "Windows":
    os.system("pause")
else:
    print("Press any key to continue...")
    os.system("read -n 1")
