from open_webcam import start_surv
import os,re

def purge(dir,pattern):
    for f in os.listdir(dir):
        if f.endswith(pattern):
            os.remove(os.path.join(dir,f))

if __name__ == "__main__":
    purge("images",".png")
    start_surv()
