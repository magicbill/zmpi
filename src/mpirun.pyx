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

DEBUG=True

import argparse
import os
import subprocess
import sys

parser = argparse.ArgumentParser(description='Start MPI jobs.')
parser.add_argument("-np", dest="np", type=int)
args, pos_args = parser.parse_known_args()
pos_args = " ".join(pos_args)

if DEBUG:
    print "Starting %d processes."%args.np
    print "Executable:", pos_args

#TODO parse hostfile
#TODO how many processes on this host?

# setup environments
envs = []
for i in range(args.np):
    envs.append(os.environ.copy())
    envs[i]["ZMPI_RANK"] = str(i)
    envs[i]["ZMPI_SIZE"] = str(args.np)

pool = []
for i in range(args.np):
    pool.append(subprocess.Popen(pos_args, shell=True, env=envs[i]))

ret = []
for item in pool:
    ret.append(item.wait())

sys.exit(-min(ret))