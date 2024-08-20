## Setup de l'environnement

### VM Linux

#### Installer une VM Linux avec WSL

Si les droits nécessaires sont disponibles le mieux est de passer par une installation via WSL.

- Ouvrez PowerShell en tant qu'administrateur et exécutez la commande suivante pour activer WSL :

   ```bash
   wsl --install
   ```

- Redémarrez votre ordinateur
- Ouvrez le Microsoft Store et installer Ubuntu par exemple
- Lancez la distribution depuis le menu démarrer et suivre les instructions (ne pas oublier le mdp!)
- C'est bon ! Vous pouvez ouvrir un terminal powershell et faire ``wsl`` ou directement ouvrir un terminal ``wsl``.

Si possible utilisez le ``Windows Terminal`` qui est installé par défaut sur Windows 11 ou disponible sur Github ou le Microsoft Store sur Windows 10.

#### Installer une VM Linux avec VirtualBox

[Guide Ubuntu](https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox#1-overview)


- Téléchargez et installez VirtualBox depuis le site officiel.
- Téléchargez un ISO Linux, typiquement Ubuntu sur le site officiel.
- Ouvrez VirtualBox et cliquez sur "New"
- Donnez un nom et sélectionner le type "Linux" avec la bonne version
- Attribuez de la mémoire RAM et un disque dur virtuel (dépend de votre PC)
- Démarrez la machine virtuelle et sélectionnez l'ISO télécharger puis suivre les instructions d'installation.

### Vim et Visual Studio Code (VSC)

Pour faire du scripting il faut un éditeur de texte, et plus celui-ci est puissant, plus il sera agréable de manipuler des fichiers textes et scripts divers et variés.

#### Vim

``vim`` est un éditeur de texte très ancien, entièrement en TUI (Terminal User Interface) soit disponible seulement dans un terminal. Il est en général installé sur la plupart des serveurs Linux et lors d'actions sur ces serveurs il peut être nécessaire de savoir l'utiliser ne serait-ce qu'un minimum.

En effet ``vim`` est un éditeur de texte modale, c'est à dire que par défaut appuyer sur des lettres n'écrit pas du texte mais fait toute une série d'actions diverses et variés qui peuvent se combiner entre elles (ex: ``dap`` = Delete All Paragrah). Ce principe rend l'outil strictement inutilisable si on ne connait pas.

Utilisation très simpliste de ``vim`` : 

- Ouvrir ``vim`` (``vim fichier.txt``)
- Appuyer sur ``i`` pour rentrer en mode insertion, puis se déplacer avec les flèches et faire les modifications voulues.
- Appuyer sur ``esc`` pour repasser en mode "normal" une fois les actions faites.
- Appyuer exactement sur ``:wq`` pour Write (enregistrer) et Quit.
- Si on veut quitter sans sauvegarder il faut passer en mode normal (``esc``) et ``:q!``.


Vim est cependant bien plus puissant que cela, il dispose de mouvements et actions trés poussés ainsi que d'une énorme quantité de plugins à sa disposition (en ``vimscript``). 
Son successeur ``neovim`` est encore plus populaire grâce à ses plugins écrits en ``lua``, un langage plus pratique et universel que le ``vimscript``.

Vim/neovim sont tellement populaires que chaque année il est élu éditeur le plus apprécié et envié au monde. Cependant il reste bien moins utilisé que Visual Studio Code à cause de sa forte courbe d'apprentissage.


#### Visual Studio Code

Visual Studio Code est donc l'éditeur de texte le plus populaire chez les développeurs. Il ne faut pas le confondre avec Visual Studio qui lui est un IDE à part entière. VSC est open source et disponible sur Linux, MacOS et Windows. Il a une interface utilisateur user friendly et de fortes possibilités de customisation via de nombreux plugins.

VSC n'étant pas un logicel "free" au sens de sa licence il n'est pas dispo dans les paquets par défaut, il faut donc l'installer comme suit : 

Si ``snap`` est disponible :

```bash
sudo snap install code --classic
```

Sinon sur Debian/Ubuntu : 
```bash
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/keyrings/microsoft-archive-keyring.gpg
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/microsoft-archive-keyring.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
```
Puis :
```bash
sudo apt install apt-transport-https
sudo apt-get update
sudo apt-get install code
```

On peut lancer normalement VSC, mais on peut aussi ouvrir un projet depuis un terminal (que ce soit sur Linux ou Windows) en faisant simplement ``code .`` dans le répertoire du projet.

VSC propose une intégration très pratique avec WSL si la VM installée utilise WSL.

### git

Git est un système de contrôle de version distribué utilisé pour suivre les modifications du code source tout au long du développement logiciel. Il permet aux développeurs de collaborer efficacement, de gérer différentes versions d'un projet, et de conserver un historique complet des modifications.

Git n'est initialement qu'un logiciel et est à ne pas confondre avec Github qui est une plateforme permettant de fournir un serveur distant git et un GUI tout en rajoutant d'autres fonctionnalités (issues, github actions etc...). Il y a d'autres solutions similaires à Github tel que Gitlab, Gitea, sourcehut etc...

#### Installation de git sur Ubuntu/Debian
Dans un terminal faire : 
```bash
sudo apt-get update
sudo apt-get install git
```

Git permet de faire beaucoup d'actions sur le code source mais pour ce cours il sera simplement nécessaire de cloner le repo du cours :
```bash
git clone https://github.com/BouleJaune/scripting-unix.git
```
