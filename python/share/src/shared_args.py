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