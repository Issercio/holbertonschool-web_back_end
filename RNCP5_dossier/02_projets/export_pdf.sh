#!/bin/bash
# Export du dossier RNCP 5 en PDF avec mise en forme professionnelle
# Usage: bash export_pdf.sh

set -e

DOSSIER_DIR="/root/holbertonschool-web_back_end/RNCP5_dossier/02_projets"
INPUT="$DOSSIER_DIR/dossier_projet_rncp5.md"
OUTPUT="$DOSSIER_DIR/Dossier_Projet_RNCP5_Jaille_Dimitri.pdf"

echo "=== Export PDF du Dossier Projet RNCP 5 ==="
echo "Input:  $INPUT"
echo "Output: $OUTPUT"

cd "$DOSSIER_DIR"

pandoc "$INPUT" \
  -o "$OUTPUT" \
  --pdf-engine=xelatex \
  -V documentclass=report \
  -V geometry:top=2cm \
  -V geometry:bottom=2cm \
  -V geometry:left=2cm \
  -V geometry:right=2cm \
  -V fontsize=11pt \
  -V linestretch=1.1 \
  -V mainfont="DejaVu Sans" \
  -V monofont="DejaVu Sans Mono" \
  -V colorlinks=true \
  -V linkcolor=blue \
  -V urlcolor=blue \
  -V header-includes='\usepackage{fancyhdr}\pagestyle{fancy}\fancyhead[L]{\small Dossier Projet RNCP 5}\fancyhead[R]{\small Jaille Dimitri}\fancyfoot[C]{\thepage}\fancyfoot[R]{\includegraphics[height=0.8cm]{screenshots/holberton_logo.png}}\usepackage{float}\floatplacement{figure}{H}\usepackage{fvextra}\DefineVerbatimEnvironment{Highlighting}{Verbatim}{fontsize=\footnotesize,breaklines,commandchars=\\\{\}}' \
  -V lang=fr \
  --highlight-style=tango \
  --columns=80 \
  2>&1

if [ -f "$OUTPUT" ]; then
  PAGES=$(pdfinfo "$OUTPUT" 2>/dev/null | grep "Pages:" | awk '{print $2}' || echo "?")
  SIZE=$(ls -lh "$OUTPUT" | awk '{print $5}')
  echo ""
  echo "=== Export reussi ==="
  echo "Fichier: $OUTPUT"
  echo "Taille:  $SIZE"
  echo "Pages:   $PAGES"
else
  echo "ERREUR: le fichier PDF n'a pas ete genere."
  exit 1
fi
