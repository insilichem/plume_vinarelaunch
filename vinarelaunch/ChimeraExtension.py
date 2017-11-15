# --- UCSF Chimera Copyright ---
# Copyright (c) 2000 Regents of the University of California.
# All rights reserved.  This software provided pursuant to a
# license agreement containing restrictions on its disclosure,
# duplication and use.  This notice must be embedded in or
# attached to all copies, including partial copies, of the
# software or any revisions or derivations thereof.
# --- UCSF Chimera Copyright ---

import chimera.extension

class VinaRelaunchEMO(chimera.extension.EMO):

    def name(self):
        return 'AutoDock Vina (Relaunch)'

    def description(self):
        return 'Relaunch a failed AutoDock Vina calculation'

    def categories(self):
        return ['InsiliChem', 'Surface/Binding Analysis']

    def icon(self):
        return

    def activate(self):
        self.module('gui').showUI()


chimera.extension.manager.registerExtension(VinaRelaunchEMO(__file__))
