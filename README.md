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

[![Sponsored](https://img.shields.io/badge/chilicorn-sponsored-brightgreen.svg?logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAAA4AAAAPCAMAAADjyg5GAAABqlBMVEUAAAAzmTM3pEn%2FSTGhVSY4ZD43STdOXk5lSGAyhz41iz8xkz2HUCWFFhTFFRUzZDvbIB00Zzoyfj9zlHY0ZzmMfY0ydT0zjj92l3qjeR3dNSkoZp4ykEAzjT8ylUBlgj0yiT0ymECkwKjWqAyjuqcghpUykD%2BUQCKoQyAHb%2BgylkAyl0EynkEzmkA0mUA3mj86oUg7oUo8n0k%2FS%2Bw%2Fo0xBnE5BpU9Br0ZKo1ZLmFZOjEhesGljuzllqW50tH14aS14qm17mX9%2Bx4GAgUCEx02JySqOvpSXvI%2BYvp2orqmpzeGrQh%2Bsr6yssa2ttK6v0bKxMBy01bm4zLu5yry7yb29x77BzMPCxsLEzMXFxsXGx8fI3PLJ08vKysrKy8rL2s3MzczOH8LR0dHW19bX19fZ2dna2trc3Nzd3d3d3t3f39%2FgtZTg4ODi4uLj4%2BPlGxLl5eXm5ubnRzPn5%2Bfo6Ojp6enqfmzq6urr6%2Bvt7e3t7u3uDwvugwbu7u7v6Obv8fDz8%2FP09PT2igP29vb4%2BPj6y376%2Bu%2F7%2Bfv9%2Ff39%2Fv3%2BkAH%2FAwf%2FtwD%2F9wCyh1KfAAAAKXRSTlMABQ4VGykqLjVCTVNgdXuHj5Kaq62vt77ExNPX2%2Bju8vX6%2Bvr7%2FP7%2B%2FiiUMfUAAADTSURBVAjXBcFRTsIwHAfgX%2FtvOyjdYDUsRkFjTIwkPvjiOTyX9%2FAIJt7BF570BopEdHOOstHS%2BX0s439RGwnfuB5gSFOZAgDqjQOBivtGkCc7j%2B2e8XNzefWSu%2BsZUD1QfoTq0y6mZsUSvIkRoGYnHu6Yc63pDCjiSNE2kYLdCUAWVmK4zsxzO%2BQQFxNs5b479NHXopkbWX9U3PAwWAVSY%2FpZf1udQ7rfUpQ1CzurDPpwo16Ff2cMWjuFHX9qCV0Y0Ok4Jvh63IABUNnktl%2B6sgP%2BARIxSrT%2FMhLlAAAAAElFTkSuQmCC)](http://spiceprogram.org/oss-sponsorship)
