import os
import sys
sys.path.insert(0, os.path.abspath("C:\\Users\\lucas\\Documents\\GitHub\\trabalho1-dso"))

from control.controlador_ong import ControladorOng


if __name__=="__main__":
    ControladorOng().inicia_sistema()