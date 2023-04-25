# lott
The official AxOS's Assistant. 

# Note

Check if all the requirements are installed on your pc. The required package are in ```requirements.txt```.

To install a requirement, run ```pip install <pkgname>```.


WARNING: The original Lott uses special api keys that only the developper can access. To run this code, You will need: 
    - Openai api key
    - Spotipy secret id
    - Spotipy Client id
    - Openweather api key
   
  Note that Spotipy needs spotify pemium account id to works. The code still works without these keys, but they are necessary to listen music.
  
# Installation

* Clone this repository by using command line: ```$git clone https://github.com/LeVraiArdox/lott.git```.
* Add your API Keys in ```src/core/lott-core.py```.
* Run the PKGBUILD: ```makepkg -si``` in the root directory.

# Usage

Just run ```lott``` in your terminal.

___________________________________
*Still in developpement, functionnality are limited and may be improved in the future. bugs may be encountered, but cannot be dangerous.*
