# Copyright (c) 2013 Thomas Spura
#
# This file is part of ZMPI.
#
# ZMPI is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# ZMPI is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
cwd = os.sep.join(__file__.split(os.sep)[:-1])
env = os.environ.copy()
env["LD_LIBRARY_PATH"] = cwd + "/../src:" + env.get("LD_LIBRARY_PATH", "")
env["PYTHONPATH"] = cwd + "/../src:"
env["PATH"] = cwd + "/../bin:" + env.get("PATH", "")

def run_cmd(cmd):
    import subprocess
    subprocess.check_call(cmd,
                          shell=True,
                          stderr=subprocess.PIPE,
                          stdout=subprocess.PIPE,
                          env=env
                         )

def test_generate():
    import glob
    files = glob.glob("%s/*.c.out"%cwd)
    for f in files:
        yield run_cmd, "%s"%f
        yield run_cmd, "mpirun -np 2 %s"%f
        yield run_cmd, "mpirun -np 3 %s"%f
        yield run_cmd, "mpirun -np 5 %s"%f
