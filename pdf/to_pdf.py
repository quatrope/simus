import os
import glob

PATH = os.path.abspath(os.path.dirname(__file__))

GLOB = os.path.join(PATH, "..", "*.ipynb")

CMD = "jupyter-nbconvert --to pdf {}"

for fn in glob.glob(GLOB):
    print(fn)
    cmd = CMD.format(fn)
    os.system(cmd)

os.system("rm notebook.tex")
