#!/bin/bash

echo "Installing DesignExplorer with Custom Patches..."

#git clone https://github.com/tt-acm/DesignExplorer

cp DesignExplorer_patch/index.html DesignExplorer/
cp DesignExplorer_patch/logo.gif DesignExplorer/
cp DesignExplorer_patch/settings.json DesignExplorer/

sed -i 's|background-image: url(../img/thorntontomasetti.jpg);|background-image: url(../logo.gif);|g' DesignExplorer/css/style.css
sed -i 's|cleanHeight = windowHeight - 115, // 2|cleanHeight = windowHeight - 55,|g' DesignExplorer/js/designExplorer.js

echo "DesignExplorer Installed."
