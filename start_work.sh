#!/bin/bash
 
function create () {
	echo $USER
	mkdir /home/$USER/Documents/$1
	echo "Created $1 directory in Documents"
	cd /home/$USER/Documents/$1
	touch README.md
	git add -A
	git init

}

create hello_world 
