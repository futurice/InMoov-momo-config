# Momo configuration for InMoov

This repository contains the [MyRobotLab](http://myrobotlab.org/) [InMoov](http://inmoov.fr/) service configuration used by [Futurice](https://futurice.com) to study robot assisted speech therapy for children with autism. The particular physical robot is called Momo.

InMoov is an open sourced robot design by Gael Langevin. MyRobotLab is an Open Source Java Framework for Robotics and Creative Machine Control.

## Considerations

This repository...

... assumes MyRobotLab [Manticore release](https://github.com/MyRobotLab/myrobotlab/releases/tag/1.0.2693).

... assumes OSX or Linux operating system. MyRobotLab is usually run on Windows. 

... contains, among other things, servo motor configuration that is applicable only for the particular physical instance of the InMoob robot, Futurice's Momo. Taking this configuration in use with another physical robot requires going through the skeleton configuration carefully, **else you risk damaging your hardware**. 

## Installation and setup

Install MyRobotLab as per instructions found in [here](https://github.com/MyRobotLab/inmoov/wiki/HOWTO---SETUP-&-PREREQUISITES) (you need to adjust for your OS of choice). 

Replace the myrobotlab/InMoov directory with the one you find in this repository, after reading *considerations* above. 

## Behaviour

With this configuration, your robot will:

* Try to talk with a Finnish accent, and some automatic messages will be in Finnish
* Not do stuff unless prompted (live config is false)
* Attach all limbs except torso
* Attach OpenCV for the eye cam
* Be able to do a bunch of *gestures* that are actually simplified sign language

## Gestures

TBD, implementation ongoing
