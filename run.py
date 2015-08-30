#!/usr/bin/python
import argparse

def run_cli():
    from src.CommandLineInterface import CommandLineInterface
    
    cli = CommandLineInterface()
    cli.start()

def run_ui():
    from PyQt4.QtGui import QApplication
    import sys
    from src.MainWidget import mainWindow

    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--cli', '-c', help='Command-line interface', action="store_true")
    args = parser.parse_args()
    if args.cli:
        run_cli()
    else:
        run_ui()
