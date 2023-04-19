# DiffractionSimulation
DiffractionSimulation is a simulation of X-Ray diffraction from a crystal lattice. 

This program acts as a pedagogical tool to visualize this diffraction and it's components.

## Installation:
------------
First, clone this git repository.
```bash 
git clone https://github.com/hentisch/ProgramName.git
```

As DiffractionSimulation does have a fairly heavy list of dependencies, it is recommended to create a [virtual environment](https://docs.python.org/3/tutorial/venv.html) for the program to run in. This can be done with the following commands. 

```bash
cd ProgramName
python3 -m venv env
source env/bin/activate
```
Note that the final line, "source env/bin/activate", will allow you to work within the virtual enviornment. You will want to run this command whenever you run this program.

Now that you have created your virtual envionrment, you will want to install the programs dependencies. These are all listed in requirments.txt, and as such can be installed with the following  command: 
```bash
pip install -r requirements.txt
```

## Usage:
---------
In the code directory, you will find a variety of scripts to run. For whichever script you are interested in running, use the command,
```bash
python3 script.py
```
, though replace script.py with the name of the script you would like to run. Make sure to run this command while in the code directory.

## Materials:

To build this slideshow from it's LaTeX source, first run generate_plots_new.py to generate the plots and download the images which will be used.
## Contributing:
If there is a bug or inaccuracy you would like to fix, feel free to send a pull request. For larger contributions, it is a good idea to create a new issue to discuss the changes you would like to make before you spend a lot of time implementing them.
