from textteaser import TextTeaser
import sys
reload(sys)
sys.setdefaultencoding('utf8')

tt = TextTeaser()

with open("page18499Leftwingpolitics.txt","r") as fl:
    data = fl.read()
    fl.close()
sentences = tt.summarize("Politics",data)
for sen in sentences:
    print sen

print("end")