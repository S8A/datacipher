#!/usr/bin/env python3
# coding=utf-8
"""Graphical version of the DataCipher text ciphering tool."""

from PyQt4 import QtGui, QtCore
import ascii_conversion as asciic
import atbash_cipher as atbsh
import caesar_cipher as caesr
import col_transposition as coltr
import os
import sys
import vigenere_cipher as vignr

this_path = os.path.dirname(os.path.realpath(__file__))

class datacipher_window(QtGui.QMainWindow):

    def __init__(self):

        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle('DataCipher')

        main_box = QtGui.QWidget()
        main_layout = QtGui.QHBoxLayout(main_box)
        outp_box = QtGui.QWidget()
        tab_box = QtGui.QTabWidget()
        ascii_tab = QtGui.QWidget()
        atbsh_tab = QtGui.QWidget()
        caesr_tab = QtGui.QWidget()
        coltr_tab = QtGui.QWidget()
        vignr_tab = QtGui.QWidget()

        ascii_box = QtGui.QVBoxLayout(ascii_tab)

        self.ascii_mod_lbl = QtGui.QLabel('Modo:')
        self.ascii_mod_cmb = QtGui.QComboBox()
        self.ascii_mod_cmb.addItem('Binario')
        self.ascii_mod_cmb.addItem('Decimal')
        self.ascii_mod_cmb.addItem('Hexadecimal')
        self.ascii_mod_cmb.addItem('Octal')

        self.ascii_txt_lbl = QtGui.QLabel('Texto:')
        self.ascii_txt_inp = QtGui.QTextEdit()

        self.ascii_exe_btn = QtGui.QPushButton('Ejecutar')
        self.ascii_exe_btn.clicked.connect(self.ascii_txt)

        ascii_box.addWidget(self.ascii_mod_lbl)
        ascii_box.addWidget(self.ascii_mod_cmb)
        ascii_box.addWidget(self.ascii_txt_lbl)
        ascii_box.addWidget(self.ascii_txt_inp)
        ascii_box.addWidget(self.ascii_exe_btn)

        atbsh_box = QtGui.QVBoxLayout(atbsh_tab)

        self.atbsh_txt_lbl = QtGui.QLabel('Texto:')
        self.atbsh_txt_inp = QtGui.QTextEdit()

        self.atbsh_exe_btn = QtGui.QPushButton('Ejecutar')
        self.atbsh_exe_btn.clicked.connect(self.atbsh_txt)

        atbsh_box.addWidget(self.atbsh_txt_lbl)
        atbsh_box.addWidget(self.atbsh_txt_inp)
        atbsh_box.addWidget(self.atbsh_exe_btn)

        caesr_box = QtGui.QVBoxLayout(caesr_tab)

        self.caesr_mod_lbl = QtGui.QLabel('Modo:')
        self.caesr_mod_cmb = QtGui.QComboBox()
        self.caesr_mod_cmb.addItem('Encriptar')
        self.caesr_mod_cmb.addItem('Decriptar')
        self.caesr_mod_cmb.addItem('Fuerza bruta')

        self.caesr_key_lbl = QtGui.QLabel('Clave:')
        self.caesr_key_inp = QtGui.QSpinBox()
        self.caesr_key_inp.setMaximum(26)
        self.caesr_key_inp.setMinimum(1)

        self.caesr_txt_lbl = QtGui.QLabel('Mensaje:')
        self.caesr_txt_inp = QtGui.QTextEdit()

        self.caesr_exe_btn = QtGui.QPushButton('Ejecutar')
        self.caesr_exe_btn.clicked.connect(self.caesr_txt)

        caesr_box.addWidget(self.caesr_mod_lbl)
        caesr_box.addWidget(self.caesr_mod_cmb)
        caesr_box.addWidget(self.caesr_key_lbl)
        caesr_box.addWidget(self.caesr_key_inp)
        caesr_box.addWidget(self.caesr_txt_lbl)
        caesr_box.addWidget(self.caesr_txt_inp)
        caesr_box.addWidget(self.caesr_exe_btn)

        coltr_box = QtGui.QVBoxLayout(coltr_tab)

        self.coltr_mod_lbl = QtGui.QLabel('Modo:')
        self.coltr_mod_cmb = QtGui.QComboBox()
        self.coltr_mod_cmb.addItem('Encriptar')
        self.coltr_mod_cmb.addItem('Decriptar')

        self.coltr_key_lbl = QtGui.QLabel('Columnas:')
        self.coltr_key_inp = QtGui.QSpinBox()
        self.coltr_key_inp.setMinimum(1)

        self.coltr_txt_lbl = QtGui.QLabel('Mensaje:')
        self.coltr_txt_inp = QtGui.QTextEdit()

        self.coltr_exe_btn = QtGui.QPushButton('Ejecutar')
        self.coltr_exe_btn.clicked.connect(self.coltr_txt)

        coltr_box.addWidget(self.coltr_mod_lbl)
        coltr_box.addWidget(self.coltr_mod_cmb)
        coltr_box.addWidget(self.coltr_key_lbl)
        coltr_box.addWidget(self.coltr_key_inp)
        coltr_box.addWidget(self.coltr_txt_lbl)
        coltr_box.addWidget(self.coltr_txt_inp)
        coltr_box.addWidget(self.coltr_exe_btn)

        vignr_box = QtGui.QVBoxLayout(vignr_tab)

        self.vignr_mod_lbl = QtGui.QLabel('Modo:')
        self.vignr_mod_cmb = QtGui.QComboBox()
        self.vignr_mod_cmb.addItem('Encriptar')
        self.vignr_mod_cmb.addItem('Decriptar')

        self.vignr_key_lbl = QtGui.QLabel('Clave (letras):')
        self.vignr_key_inp = QtGui.QLineEdit()

        self.vignr_txt_lbl = QtGui.QLabel('Mensaje:')
        self.vignr_txt_inp = QtGui.QTextEdit()

        self.vignr_exe_btn = QtGui.QPushButton('Ejecutar')
        self.vignr_exe_btn.clicked.connect(self.vignr_txt)

        vignr_box.addWidget(self.vignr_mod_lbl)
        vignr_box.addWidget(self.vignr_mod_cmb)
        vignr_box.addWidget(self.vignr_key_lbl)
        vignr_box.addWidget(self.vignr_key_inp)
        vignr_box.addWidget(self.vignr_txt_lbl)
        vignr_box.addWidget(self.vignr_txt_inp)
        vignr_box.addWidget(self.vignr_exe_btn)

        tab_box.addTab(ascii_tab, 'Conversión ASCII')
        tab_box.addTab(atbsh_tab, 'Cifrado Atbash')
        tab_box.addTab(caesr_tab, 'Cifrado Caesar')
        tab_box.addTab(vignr_tab, 'Cifrado Vigenère')
        tab_box.addTab(coltr_tab, 'Transposición columnar')

        outp_layout = QtGui.QVBoxLayout(outp_box)

        self.outp_lbl = QtGui.QLabel('Salida de datos:')
        self.outp_txt = QtGui.QTextEdit()
        self.outp_txt.setReadOnly(True)

        self.clean_outp_btn = QtGui.QPushButton('Limpiar')
        self.clean_outp_btn.clicked.connect(self.clean_output)

        outp_layout.addWidget(self.outp_lbl)
        outp_layout.addWidget(self.outp_txt)
        outp_layout.addWidget(self.clean_outp_btn)

        main_layout.addWidget(tab_box)
        main_layout.addWidget(outp_box)

        self.setCentralWidget(main_box)
        self.resize(856, 512)
        self.center_in_desktop()
        self.show()

    def ascii_txt(self):
        sel_mod = self.ascii_mod_cmb.currentIndex()
        r = asciic.convert(sel_mod, self.ascii_txt_inp.toPlainText())
        self.outp_txt.append(r)

    def atbsh_txt(self):
        self.outp_txt.append(atbsh.cipher(self.atbsh_txt_inp.toPlainText()))

    def caesr_txt(self):
        sel_mod = self.caesr_mod_cmb.currentIndex()
        sel_key = 0
        if self.caesr_key_inp.text().isdigit():
            sel_key += int(self.caesr_key_inp.text())
        txt = self.caesr_txt_inp.toPlainText()
        r = ''
        if sel_mod != 2:
            r += caesr.shift(sel_key, txt, sel_mod)
        else:
            for k in range(1, 27):
                r += str(k) + ': ' + caesr.shift(k, txt, 1) + '.\n'
        self.outp_txt.append(r)

    def coltr_txt(self):
        d = self.coltr_mod_cmb.currentIndex()
        key = 0
        if self.coltr_key_inp.text().isdigit():
            key += int(self.coltr_key_inp.text())
        txt = self.coltr_txt_inp.toPlainText()
        r = ''
        if d:
            r += coltr.reverse(key, txt)
        else:
            r += coltr.cipher(key, txt)
        self.outp_txt.append(r)

    def vignr_txt(self):
        sel_mod = self.vignr_mod_cmb.currentIndex()
        key = ''
        if self.vignr_key_inp.text().isalpha():
            key += self.vignr_key_inp.text()
        txt = self.vignr_txt_inp.toPlainText()
        self.outp_txt.append(vignr.cipher(key, txt, sel_mod))

    def clean_output(self):
        self.outp_txt.clear()

    def center_in_desktop(self):
        window_geometry = self.frameGeometry()
        center_of_screen = QtGui.QDesktopWidget().availableGeometry().center()
        window_geometry.moveCenter(center_of_screen)
        self.move(window_geometry.topLeft())

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(this_path + os.sep + 'datacipher.png'))
    dcw = datacipher_window()
    sys.exit(app.exec_())
