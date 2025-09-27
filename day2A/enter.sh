#!/usr/bin/env bash

# Run the container.
run() {
  if [ -z "$(docker ps -f "name=day2A" -f "status=running" -q)" ]; then
    docker run \
      -d \
      -it \
      --rm \
      --name day2A \
      --hostname day2A \
      -e DISPLAY=$DISPLAY \
      -v /tmp/.X11-unix:/tmp/.X11-unix \
      astrogewgaw/ftsky:day2A \
      /bin/bash
  fi
}

# Enter the container.
enter() { docker exec -it day2A bash -i; }

run && enter
