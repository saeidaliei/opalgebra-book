#!/usr/bin/env bash
# Quality gate for the LaTeX build log.
#   usage: scripts/check_log.sh <logfile> [pdf]
# Fails (exit 1) on unresolved references/citations or multiply defined labels.
# Overfull boxes are reported as warnings so that they are visible but do not block a build.
set -u
LOG="${1:?usage: check_log.sh <logfile> [pdf]}"
PDF="${2:-}"

undefined=$(grep -cE "LaTeX Warning: (Reference|Citation) .* undefined|There were undefined references|multiply defined" "$LOG")
overfull=$(grep -c "^Overfull" "$LOG")
pages="?"
if [ -n "$PDF" ] && command -v pdfinfo >/dev/null 2>&1; then
  pages=$(pdfinfo "$PDF" | awk '/^Pages:/ {print $2}')
fi

echo "pages=$pages  undefined=$undefined  overfull=$overfull"
if [ -n "${GITHUB_STEP_SUMMARY:-}" ]; then
  {
    echo "### LaTeX build report"
    echo ""
    echo "| Pages | Undefined refs / cites | Overfull boxes |"
    echo "|---|---|---|"
    echo "| $pages | $undefined | $overfull |"
  } >> "$GITHUB_STEP_SUMMARY"
fi

if [ "$overfull" -gt 0 ]; then
  echo "::warning::$overfull overfull box(es) in the log"
  grep -n "^Overfull" "$LOG" | head -20
fi
if [ "$undefined" -gt 0 ]; then
  echo "::error::$undefined unresolved reference/citation warning(s)"
  grep -nE "LaTeX Warning: (Reference|Citation) .* undefined|multiply defined" "$LOG" | head -20
  exit 1
fi
