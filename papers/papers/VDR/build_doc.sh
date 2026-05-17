#!/bin/bash
pandoc README.md -o index.html -s --css=style.css --metadata title=" "
sed -i 's|<span class="citation" data-cites="[^"]*">@\([^<]*\)</span>|\1|g' index.html

