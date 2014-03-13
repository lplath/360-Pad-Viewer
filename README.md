360-Pad-Viewer
==============

A tool that allows you to visualize your gamepad for livestreaming.
It works with the XBox 360 Pad for PC and Logitech Gamepads but
it can also be tweaked to work with other devices.

Download
========

The download link can be found <a href="bin/xbox_viewer.zip">here</a>.<br>
For installation simply extract the zip file to your hardrive and then run the programm.
Make sure you dont change the folder structure, otherwise the programm might not run properly.

Setting up
==========
Although the viewer should run with any gamepad, you might want to configure the key bindings to
fit your gamepad. To do so you need to modify the 'config.txt' file which is located next to the executable.

The following problems could occur:
----------------------------------

**The program crashes immediately**
Your gamepad only has a limited number of analog axes. Therefore make sure that 'LX', 'RX', etc. are set to an          appropriate number. You could even set them all to '0' and see, if the error still occurs.

The viewer doesn't respond to your gamepad
------------------------------------------
If you have multiple input devices plugged into your PC, the program does not know which device it should respond to. Therefore you can change the 'ID' to the number of your device.

The button mappings are wrong
-----------------------------
You can change all the button- and axis mappings to fit your gamepad. It is also possible to use the same physical      button for multiple buttons on the viewer.

Development
===========

If you want to develop your own version you will need
* pygame
* py2exe

Then you just need to run the build script or run the command manually.

The programm is build for windows but should also run on linux and mac.
