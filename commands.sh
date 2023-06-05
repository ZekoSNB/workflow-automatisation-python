#!/bin/bash

function create() {
	mkdir /home/$USER/Documents/$1
	cd /home/$USER/Documents/$1
	touch README.md
	code .
}

function creategit() {
	mkdir /home/$USER/Documents/$1
	python source/git_repository.py $1
	echo "Done $1 folder in /home/$USER/Documents/$1"
	cd /home/$USER/Documents/$1
	git init
	touch README.md
	git add README.md
	git commit -a -m "initial commit"
	echo "initial commit"
	git branch -M main
	git remote add origin git@github.com:ZekoSNB/$1.git
	git push -u origin main
	echo "your repository is done"
	code .	
}