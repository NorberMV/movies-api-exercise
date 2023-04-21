#!/usr/bin/env bash

init_server() {
  echo "Launch the server ;) ..."
  uvicorn app.main:app --reload --host 0.0.0.0 --port 80
}

if [[ "$1" == 'fast-up' ]]; then
  init_server
fi