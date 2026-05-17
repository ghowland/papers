#!/bin/bash
pandoc README.md -o index.html -s --css=style.css --metadata title=" "
sed -i 's|href="@HOWL-VDR-\([^"]*\)/manuscript.md"|href="https://github.com/ghowland/papers/tree/main/papers/papers/VDR/HOWL-VDR-\1/manuscript.md"|g' index.html
sed -i 's|<title> </title>|'"$(cat social_meta.html | tr '\n' '~')"'|' index.html
sed -i 's|~|\n|g' index.html
