import os, shutil, glob, math

print(os.getcwd())
os.chdir("./image")

train_percentage = 70
val_ratio = 20

def move(file, dir):
    for f in glob.glob(f"./{file}*"):
        print(f)
        shutil.move(f"{f}", f"./{dir}/{f}")

def moveExt(ext, dir):
    try:
        os.mkdir(dir)
    except:
        pass
    for f in glob.glob(f"./*.{ext}"):
        print(f)
        shutil.move(f"{f}", f"./{dir}/{f}")

files = os.listdir()
dataset = 0

# count total dataset that will be used
for f in files:
    if os.path.isfile(f) and "classes" not in f:
        dataset += 1


print(files)
# for handle no duplicate
before=""
exist = 0

# change datasets to test, train, val directory
for f in files:
    try:
        i=int(f[:-4])
        if os.path.isfile(f) and exist <2:
            if before == str(i):
                before = str(i)
                exist+=1
            else: exist = 0
            if i < math.floor((train_percentage/100)*dataset): 
                dir = "train"
            elif math.ceil((train_percentage/100)*dataset) <= i < math.floor((train_percentage+val_ratio)/100 * dataset):
                dir = "val"
            else: 
                dir = "test"
            try:
                os.mkdir(dir)
            except:
                pass
            move(str(i), dir)
            print(f"moved dataset {f} to {dir}")
        else:
            print(f"gaada {f}")
            continue
    except Exception as e:
        print(e)
        continue

# change directory hirearchy for YOLOv5 training
files = os.listdir()
for f in files:
    if os.path.isdir(f):
        os.chdir(f)
        moveExt("txt", "labels")
        moveExt("jpg", "images")
        os.chdir("..")
