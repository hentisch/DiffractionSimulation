# DiffractionSimulation
DiffractionSimulation is a simulation of X-Ray diffraction from a crystal lattice. 


Installation:
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


Usage:
------
To run the program, follow the installation steps above, then run
```bash
python3 main.py
```
while in the directory you cloned earlier. 

High Level Overview
-------------------
X-ray crystallography is an extraordinarily important set of techniques for understanding the atomic properties of matter. A lot of this relies on Bragg's law. This is shown in more detail in the next section, but you can think of it as saying that given a crystal lattice with a certain distance between atoms, you can predict the angle at which a beam of light will need to shine onto your crystals for the light diffracted by different atoms to constructively interfere. 

This program acts as a pedagogical tool to visualize this diffraction.

Description of Science
----------------------

    Thomson Scattering
    ------------------
    


Pheonomena Demonstrated:
------------------------


Contributing:
--------------
If there is a bug or inaccuracy you would like to fix, feel free to send a pull request. For larger contributions, it is a good idea to create a new issue to discuss the changes you would like to make before you spend a lot of time implementing them.