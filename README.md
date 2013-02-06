Lojban-Translator
=================

A lojban to english translator written in python.

Required Software
=================

* python 2.7
* easy_install (python package manager)
* camxes (python package)


Installation and Usage
======================

Getting this project working can be a bit daunting, especially when using a non-unix based system.


1. Install easy_install: on ubuntu/debian
    sudo apt-get install easy_install
or install easy_install for windows
2. Install camxes
   easy_install camxes

3. Run main.py
    python main.py

You can run with any number with the following flags
-tree prints out the entire parse tree for the sentence
-c prints out the dictionary of cmavos
-g prints out the entire dictionary of gismu

OR

-w will enter word mode and will print out the dictionary entry for an entered word

4. After running enter "exit" to quit

Examples To Try
===============

do patfu mi / do mi patfu
you are the father of me

mi vecnu ti do
i sell this to you

do blari'o
you are blue/green

ta bloti
that is a boat

tu plise tricu
that yonder is an apple tree

xunre barda gerku
that is a big and red dog

many other basic examples can be found here:
http://www.lojban.org/tiki/tiki-index.php?page=Simple+phrases
