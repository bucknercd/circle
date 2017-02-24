
* Note:  in.txt and in2.txt are input files. *


Linux build instructions:

1. Python 2.7 should already be installed as it is used by the OS.
2. pip may or may not already be installed.
    a. if not, use the package manger to install it.

    $ sudo apt-get install pip

3. Next you will need to install pygame for the gui.

    $ sudo pip install pygame

4. you can now run the program.
    make sure you direct any input (that is in the correct format)
    to standard in using redirection.

    $ python circle.py < in.txt

5. optional:  If you want to invoke the interpreter directly,
                make circle.py executable if its not already.

                $ sudo chmod 755 circle.py

                I have the path to the interpreter at the top of the file after
                the shebang as #!/usr/bin/python. You may have to change this if
                it does not match your system.

                Now you can invoke like:

                $ ./circle < in.txt



Windows build instructions:

1. You may need to install python 2.7 on your machine.
    go to the internet and download python 2.7 (make a mental note of where its installed) i.e. C:\Python27

2. Python will only run in the directory that its installed in so we need to add it to the path.

2a.  To change the path in windows:

    From the desktop, right-click My Computer and click Properties.
    In the System Properties window, click on the Advanced tab
    In the Advanced section, click the Environment Variables button.
    Finally, in the Environment Variables window (as shown below), highlight the
    Path variable in the Systems Variable section and click the Edit button.
    Add the python path to the existing path. i.e.  C:\Python27
    Each different directory is separated with a semicolon as shown below.

    C:\Program Files; C:\Winnt; C:\Winnt\System32; C:\Python27

3. Install pip:  I included a get-pip.py file in my circle folder.
    Now that python is added to your path: got cmd

    $ python get-pip.py

4. From cmd (command prompt) use pip to install pygame.

    $ python -m pip install pygame

5. Now you can run program.

    $ python circle.py < in.txt

    Note: you must redirect the input file to stdin.
