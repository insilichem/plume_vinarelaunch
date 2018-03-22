#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Documentation here.
"""

from __future__ import print_function, division
import Tkinter as tk
import Pmw
import chimera
from chimera.widgets import MoleculeOptionMenu
from libtangram.ui import TangramBaseDialog
from core import Controller

def showUI(*args, **kwargs):
    if chimera.nogui:
        tk.Tk().withdraw()
    ui = VinaRelaunchDialog(*args, **kwargs)
    controller = Controller(gui=ui)
    ui.enter()


class VinaRelaunchDialog(TangramBaseDialog):

    buttons = ('OK', 'Close')
    statusResizing = False
    default = 'Preview'
    help = "https://github.com/insilichem/vinarelaunch"
    # VERSION = '0.0.1'
    # VERSION_URL = "https://api.github.com/repos/insilichem/vinarelaunch/releases/latest"

    def __init__(self, *args, **kwargs):
        # GUI init
        self.title = 'AutoDock Vina Relaunch'

        # Vars
        self.var_receptor = tk.StringVar()
        self.var_ligand = tk.StringVar()
        self.var_config = tk.StringVar()
        self.var_output = tk.StringVar()

        # Fire up
        super(VinaRelaunchDialog, self).__init__(*args, **kwargs)

    def fill_in_ui(self, parent):
        self.canvas.columnconfigure(0, weight=1)
        # Select molecules
        self.ui_labelframe = tk.LabelFrame(self.canvas, text='Select molecules & files')
        self.ui_receptor_mol = MoleculeOptionMenu(self.canvas)
        self.ui_receptor_fld = tk.Entry(self.canvas, textvariable=self.var_receptor)
        self.ui_receptor_btn = tk.Button(self.canvas, text='...')
        self.ui_ligand_mol = MoleculeOptionMenu(self.canvas)
        self.ui_ligand_fld = tk.Entry(self.canvas, textvariable=self.var_ligand)
        self.ui_ligand_btn = tk.Button(self.canvas, text='...')
        self.ui_config_fld = tk.Entry(self.canvas, textvariable=self.var_config)
        self.ui_config_btn = tk.Button(self.canvas, text='...')
        self.ui_output_fld = tk.Entry(self.canvas, textvariable=self.var_output)
        self.ui_output_btn = tk.Button(self.canvas, text='...')

        grid = [
            ['Receptor', self.ui_receptor_mol],
            ['', self.ui_receptor_fld, self.ui_receptor_btn],
            ['Ligand', self.ui_ligand_mol],
            ['', self.ui_ligand_fld, self.ui_ligand_btn],
            ['Config', self.ui_config_fld, self.ui_config_btn],
            ['Output', self.ui_output_fld, self.ui_output_btn]
        ]

        self.auto_grid(self.ui_labelframe, grid)
        self.ui_labelframe.grid(row=0, column=0, sticky='news', padx=5, pady=5)
        self.ui_labelframe.columnconfigure(1, weight=1)

    def OK(self, *args):
        pass
