# DiffractionSimulation
DiffractionSimulation is a simulation of X-Ray diffraction from a crystal lattice. 


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

## High Level Overview
-------------------
X-ray crystallography is an extraordinarily important set of techniques for understanding the atomic properties of matter. A lot of this relies on Bragg's law. This is shown in more detail in the next section, but you can think of it as saying that given a crystal lattice with a certain distance between atoms, you can predict the angle at which a beam of light will need to shine onto your crystals for the light diffracted by different atoms to constructively interfere. 

This program acts as a pedagogical tool to visualize this diffraction.

## Description of Science
-------------------------
### Thomson Scattering
Thomson scattering is the form of light scattering from an electron most relevant to this kind of diffraction.

$$ E_{rad}(R, t) = -E_{x0} {r_0} \frac{e^{i(kR-\omega t)}}{R} cos \psi$$

$R$ represents the distance between the point of scattering and the point of observation.

$t$ represents the time of observation.

$e_{x0}$ represents the amplitude of the incident electric field.

$r_0$ represents the classical electron radius, which is about 2.82x10-15 m.

$e$ is Euler's number, and $i$ is the copmlex number.

$k$ is the wavenumber of the incident electric field.

$\omega$ is the angular frequency of the incident electric field.

$\psi$ is the angle at which the scattering is observed, relitive to the plane of polarization for the incident electric field.


From an atom, the equation is 
$$ E_{rad} = 2 \pi  \int_{R=0}^{R=\infin} \int_{\psi = 0}^{\psi = \pi} \frac{e^{ikR}}{R} (R^2 sin \psi) drd\psi$$

With the same variale definitions as before .
## Pheonomena Demonstrated:


## Contributing:
If there is a bug or inaccuracy you would like to fix, feel free to send a pull request. For larger contributions, it is a good idea to create a new issue to discuss the changes you would like to make before you spend a lot of time implementing them.