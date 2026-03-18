#!/bin/bash
# Export du dossier professionnel DP en PDF avec structure RNCP
# Usage: bash export_dp_pdf.sh

set -e

DOSSIER_DIR="/root/holbertonschool-web_back_end/RNCP5_dossier/01_profil"
INPUT="$DOSSIER_DIR/dossier_professionnel_DP.md"
OUTPUT="$DOSSIER_DIR/Dossier_Professionnel_DP_Jaille_Dimitri.pdf"

echo "=== Export PDF du Dossier Professionnel DP ==="
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
  -V lang=fr \
  --highlight-style=tango \
  --columns=80 \
  2>&1

if [ -f "$OUTPUT" ]; then
  PAGES=$(pdfinfo "$OUTPUT" 2>/dev/null | grep "Pages:" | awk '{print $2}' || echo "?")
  SIZE=$(ls -lh "$OUTPUT" | awk '{print $5}')
  echo "=== Export reussi ==="
  echo "Fichier: $OUTPUT"
  echo "Taille:  $SIZE"
  echo "Pages:   $PAGES"
else
  echo "Erreur lors de la génération du PDF."
  exit 1
fi
