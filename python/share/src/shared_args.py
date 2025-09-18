#* Market Engine Share
#* Copyright (C) 2025 OneFil (1FIL0) https://github.com/1FIL0
#*
#* This program is free software: you can redistribute it and/or modify
#* it under the terms of the GNU General Public License as published by
#* the Free Software Foundation, either version 3 of the License, or
#* (at your option) any later version.
#*
#* This program is distributed in the hope that it will be useful,
#* but WITHOUT ANY WARRANTY; without even the implied warranty of
#* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#* GNU General Public License for more details.
#*
#* You should have received a copy of the GNU General Public License
#* along with this program.  If not, see <http://www.gnu.org/licenses/>.
#* See LICENCE file.

import argparse
import logger

argParser = argparse.ArgumentParser()
argParser.add_argument("--dist")
args, unknownArgs = argParser.parse_known_args()

argDist = args.dist

if not argDist:
    logger.warnMessage("Dist argument not set, defaulting to [release]")
    argDist = "release"

if argDist != "release" and argDist != "dev":
    logger.errorMessage(f"Dist argument invalid: {argDist}, exiting")
    exit(-1)