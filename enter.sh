#!/usr/bin/env bash

# Run the container.
run() {
  if [ -z "$(docker ps -f "name=day1" -f "status=running" -q)" ]; then
    docker run \
      -d \
      -it \
      --rm \
      --name day1 \
      --hostname day1 \
      -e DISPLAY=$DISPLAY \
      -v /tmp/.X11-unix:/tmp/.X11-unix \
      astrogewgaw/ftsky:day1 \
      /bin/bash
  fi
}

# Enter the container.
enter() { docker exec -it day1 bash -i; }

run && enter
