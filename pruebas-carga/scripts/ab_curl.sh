#!/usr/bin/env bash
# Alternativa con ApacheBench (ab) o curl en paralelo. Uso: ./ab_curl.sh http://localhost:3000/health 200 100
URL=${1:?url}; TOTAL=${2:-200}; CONC=${3:-100}
if command -v ab >/dev/null; then ab -n "$TOTAL" -c "$CONC" "$URL"
else seq "$TOTAL" | xargs -P "$CONC" -I{} curl -s -o /dev/null -w "%{http_code} %{time_total}\n" "$URL" | sort | uniq -c | sort -rn | head; fi
