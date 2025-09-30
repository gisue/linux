#!/bin/sh

# Nome dello script Python
SCRIPT_NAME="gg.py"
COMMAND_NAME="gg"

# Controlla se il file Python esiste
if [ ! -f "$SCRIPT_NAME" ]; then
    echo "Errore: Il file '$SCRIPT_NAME' non esiste nella directory corrente."
    exit 1
fi

# Rende eseguibile lo script Python
chmod +x "$SCRIPT_NAME"

# Sposta il file in /usr/local/bin con il nome desiderato
sudo cp "$SCRIPT_NAME" "/usr/local/bin/$COMMAND_NAME"

# Conferma l'installazione
if [ $? -eq 0 ]; then
    echo "Il comando '$COMMAND_NAME' è stato installato con successo!"
    echo "Ora puoi usarlo digitando '$COMMAND_NAME' da qualsiasi posizione."
else
    echo "Errore durante l'installazione del comando."
fi
