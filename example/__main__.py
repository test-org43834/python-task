import argparse

import example.commands.version

def _parse_arguments() -> argparse.Namespace:
	argument_parser = argparse.ArgumentParser(description="This is an example project that does some things.")
	subparsers = argument_parser.add_subparsers(help="The command to run.", dest="command")
	subparsers.required = True
	subparsers.add_parser("version", help="Show the version of the application.")
	return argument_parser.parse_args()

def main() -> None:
	arguments = _parse_arguments()
	if arguments.command == "version":
		example.commands.version.command(arguments)

if __name__ == "__main__":
	main()
