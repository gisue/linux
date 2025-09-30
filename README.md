# linux

Comandi utili:
	tldr "nome di un comando" -> elenca e spiega i vari comandi
	rm -rf(remove forced) when a dir isn't empty

Programmi:
	-cava(https://github.com/karlstav/cava?tab=readme-ov-file#installing)
	-Oh my bash(https://github.com/ohmybash/oh-my-bash)
	-Rust:
		curl https://sh.rustup.rs -sSf | sh
	-Catppuccin folder(https://github.com/catppuccin/papirus-folders?tab=readme-ov-file)

#!/bin/bash

# Update package lists
sudo pacman -Syu

# Install desired packages
sudo pacman -S git btop neovim ranger neofetch cowsay cmatrix sl lolcat

# Create programs folder if it doesn't exist
mkdir -p Programs

# Install Pokemon Colorscripts
git clone https://gitlab.com/phoneybadger/pokemon-colorscripts.git Programs/pokemon-colorscripts
cd Programs/pokemon-colorscripts
sudo ./install.sh
cd ../..  # Navigate back to original directory

# Install Shell Color Scripts
git clone https://gitlab.com/dwt1/shell-color-scripts.git Programs/shell-color-scripts
cd Programs/shell-color-scripts
sudo make install
cd ../..

# Install Cbonsai (commented out, uncomment if desired)
git clone https://gitlab.com/jallbrit/cbonsai Programs/cbonsai
cd Programs/cbonsai
sudo make install
cd ../..

# Install Pipe.sh (commented out, follow project instructions)
git clone https://github.com/pipeseroni/pipes.sh.git Programs/pipe.sh

echo "Installation complete!"
