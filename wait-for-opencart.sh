#!/bin/bash
set -e

OPENCART_URL=${OPENCART_URL:-http://opencart:8080}
RETRIES=30
SLEEP_TIME=5

echo "Ожидаем готовности OpenCart по адресу: $OPENCART_URL"

for i in $(seq 1 $RETRIES); do
  if curl -s -f "$OPENCART_URL" >/dev/null; then
    echo "OpenCart готов! Запускаем тесты..."
    break
  fi
  echo "Попытка $i/$RETRIES: OpenCart ещё не доступен. Ждём $SLEEP_TIME секунд..."
  sleep $SLEEP_TIME
done

if ! curl -s -f "$OPENCART_URL" >/dev/null; then
  echo "OpenCart не стал доступен после $((RETRIES*SLEEP_TIME)) секунд"
  exit 1
fi


pytest -v ./tests \
    --browser="$BROWSER" \
    --base_url="$OPENCART_URL"
