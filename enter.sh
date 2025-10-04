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
      --user 1000:1000 \
      -e DISPLAY="$DISPLAY" \
      --platform linux/amd64 \
      --mount type=bind,src="$PWD/data",dst=/data \
      --mount type=bind,src=/tmp/.X11-unix,dst=/tmp/.X11-unix \
      astrogewgaw/ftsky:day1 \
      /bin/bash
  fi
}

# Enter the container.
enter() { docker exec -it day1 /bin/bash -i; }

run && enter
