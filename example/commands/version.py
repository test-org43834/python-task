import argparse

import example.version

def command(arguments:argparse.Namespace) -> None:
	print(example.version.version())
