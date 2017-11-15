#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Documentation here.
"""
# Stdlib
from __future__ import print_function, division
import os
import tkFileDialog
from functools import partial
import chimera
from vina.ws import VinaDocking

class Controller(object):

    def __init__(self, gui):
        self.gui = gui
        self.set_mvc()
        self.data = {}

    def set_mvc(self):
        self.gui.ui_receptor_btn['command'] = partial(self.cmd_browse, var=self.gui.var_receptor)
        self.gui.ui_ligand_btn['command'] = partial(self.cmd_browse, var=self.gui.var_ligand)
        self.gui.ui_config_btn['command'] = partial(self.cmd_browse2, var=self.gui.var_config,
                                                    filetypes=[('Conf', '*.conf')])
        self.gui.ui_output_btn['command'] = partial(self.cmd_browse, var=self.gui.var_output,
                                                    kind='saveas')
        self.gui.buttonWidgets['OK']['command'] = self.cmd_OK

    def cmd_browse(self, kind='open', var=None, filetypes=[('PDBQT', '*.pdbqt' )], **kwargs):
        ask = getattr(tkFileDialog, 'ask{}filename'.format(kind))
        path = ask(parent=self.gui.canvas,
                   filetypes=filetypes + [('All files', '*.*' )], **kwargs)
        if not path:
            return
        if var:
            var.set(path)
        return path

    def cmd_browse2(self, *args, **kwargs):
        path = self.cmd_browse(*args, **kwargs)
        if not path:
            return
        basename, ext = os.path.splitext(path)
        self.gui.var_output.set(basename + '.results.pdbqt')

    def cmd_OK(self):
        self.data['receptor'] = receptor = self.gui.ui_receptor_mol.getvalue()
        self.data['receptor_file'] = receptor_file = self.gui.ui_receptor_fld.get()
        self.data['ligand'] = ligand = self.gui.ui_ligand_mol.getvalue()
        self.data['ligand_file'] = ligand_file = self.gui.ui_ligand_fld.get()
        self.data['conf_file'] = conf_file = self.gui.ui_config_fld.get()
        self.data['output_file'] = output_file = self.gui.ui_output_fld.get()

        self.gui.buttonWidgets['OK']['text'] = 'Launching...'
        self.gui.buttonWidgets['OK']['state'] = 'disabled'
        vina = VinaDocking(receptorFile=receptor_file, receptor=receptor,
                           ligandFile=ligand_file, ligand=ligand,
                           confFile=conf_file, output=output_file)
        self.gui.Close()
        chimera.dialogs.display('task panel')