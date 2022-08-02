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
To run the program, follow the installation steps above, then run
```bash
python3 main.py
```
while in the directory you cloned earlier. 

## Materials:
If you would like to learn more about the phenomena shown in this simulation, you can take a look at the [chapter I wrote in Mark Galassi's Serious Programming Courses book](https://markgalassi.codeberg.page/small-courses-html/). There is also a slideshow in the materials directory, however it is much less pedagogically effective without a presenter.

## Contributing:
If there is a bug or inaccuracy you would like to fix, feel free to send a pull request. For larger contributions, it is a good idea to create a new issue to discuss the changes you would like to make before you spend a lot of time implementing them.