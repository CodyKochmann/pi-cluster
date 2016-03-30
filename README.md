# pi-cluster

To celebrate pi day and to get a little more public in the clustering community when it comes to raspberry pi, I am putting together a raspberry pi cluster which will be live come pi day! If you have any suggestions, let hear em. If you wanna copy this and be on your way, so be it! Just know my stuff evolves fast so keep an eye on the repo after you do. :)

### Layout of this repo

This repo is split into two sections to make it so those who just want the deatils on one side of the build can have what they need and leave but also to make a clean seperation of the two pieces of nature that is this computer science project.

### The hardware side

This is the section where the schematics will be going for how things are being powered, how things are wired, reasoning behind it and how I built some of the pieces. It will also have the details on what I bought and where I bought it in order to give you a better idea on exactly how you can do this too.

### The software side 

The design of this cluster is a headless one. I've seen a lot of schematics of "clusters" where there was one load balancer and a ton of servers behind it, this is not one of those. I wanted to create an architecture that offered just as many access points as it added points where things could be processed. I'll include illustrations in how I did that as this project goes on.

---

### Current Overview

##### Software 

| role     | name     |
|----------|----------|
| server   | cherrypy |
| database | couchdb  |

##### Hardware 
![](https://github.com/CodyKochmann/pi-cluster/raw/master/hardware/pictures/version_0.1.jpg)


