# flask-workouts-sqlalchemy-menu-tree
flask-workouts is a collection of my scratch pads.  I use them to work out new concepts in flask.  

This one is an attempt to work out the model for a tree (for a menu):
- items need to be linked to the one before and the one after.  
- if there is no parent, it is the start of a menu
- nodes can also have child nodes and parent nodes representing submenu's


## Usage
```
clone the repo
virtualenv env
env/bin/pip install -r requirements.txt
```
Checkout a new branch and start experimenting.

Or try this (from this [Stackoverflow question](http://stackoverflow.com/questions/2227062/how-do-i-move-a-git-branch-out-into-its-own-repository)):
```
git push url://to/new/repository.git branch-to-move:new-branch-name
```

Look for several repos `flask-workouts-xxxxx` as I explore various aspects of flask.
