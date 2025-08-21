import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument("--dist")
args, unknownArgs = argParser.parse_known_args()

argDist = args.dist