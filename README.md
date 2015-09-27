# Annotation Counter version 4.0

The annotation counter is a python script for dedicated for the counting of descriptions in biographies. This version is built for the annotation tast "SystematicDescriptions". This annotation task is defined in the Celc Annotation Tool web application. This last is only accesible with admin rights. 

- Author: M. Yassine Karimi
- Date: September the 27th,2015
- Project BiographyNet: "Time Will Tell A Different Story"
- @VU University Amsterdam:

Requirements:
- OS X or Linux OS (UbuntuGNOME v14.02 for example) installed
- Installed version of Python 2.7 or higher (script was built on v2.7)
- KafNafParser for Python (https://github.com/cltl/KafNafParserPy)
- Terminal (comes with Linux OS)
- XML v1.0 or higher
- Text editor (Sublime Text 2, gedit)


Commands;

Open the terminal

Download the complete github repository with the follwing command to location of your choise (this location will be called "my_location" in the folloeing steps:

    - git clone https://github.com/mykarimi/annotation_counter

Go to the folder 

    - my_location/annotation_counter/

Place the file(s) that you want to proces in the folder

    - my_location/annotation_counter/annotated/

go by using the terminal, go to the folder 

    - my_location/annotation_counter/
    
...with the following command (in the terminal): 

    - cd my_location/annotation_counter/

Run the script tle_v2.py via the terminal with the next command

    - python annotation_counter_v4.py
