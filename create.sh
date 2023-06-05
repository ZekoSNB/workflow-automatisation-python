#!/bin/bash

function create() {
	mkdir /home/$USER/Documents/$1
	cd /home/$USER/Documents/$1
	touch README.md
	code .
}
