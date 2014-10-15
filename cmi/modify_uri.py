#! /usr/bin/env python
#
# Replaces the extension ".la" with ".so" in the library URI in all 
# ".cca" files in %{buildroot}%{_datadir}/cca.
#
# Mark Piper (mark.piper@colorado.edu)

import os
import sys
import glob
from subprocess import check_call

try:
    install_share_dir = sys.argv[1]
    cca_dir = os.path.join(install_share_dir, "cca")
    print("Modifying *.cca files in " + cca_dir)
    for f in glob.glob(os.path.join(cca_dir, "*.cca")):
        check_call(["sed", "--in-place", "s/\.la/.so/", f])
except:
    print("Error in post-install modification of *.cca files.")
    sys.exit(1)
