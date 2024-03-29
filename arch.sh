#!/bin/bash

# Update package lists
sudo pacman -Syu

# Install desired packages
sudo pacman -S git btop htop vim neovim ranger neofetch cowsay cmatrix sl lolcat

# Create programs folder if it doesn't exist
mkdir -p programs

# Install Pokemon Colorscripts
git clone https://gitlab.com/phoneybadger/pokemon-colorscripts.git programs/pokemon-colorscripts
cd programs/pokemon-colorscripts
sudo ./install.sh
cd ../..  # Navigate back to original directory

# Install Shell Color Scripts
git clone https://gitlab.com/dwt1/shell-color-scripts.git programs/shell-color-scripts
cd programs/shell-color-scripts
sudo make install
cd ../..

# Install Cbonsai (commented out, uncomment if desired)
git clone https://gitlab.com/jallbrit/cbonsai programs/cbonsai
cd programs/cbonsai
sudo make install
cd ../..

# Install Pipe.sh (commented out, follow project instructions)
git clone https://github.com/pipeseroni/pipes.sh.git programs/pipe.sh

echo "Installation complete!"
