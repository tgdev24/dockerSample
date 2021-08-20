1. go to terminal window and type
docker compose up

if you need to build image again, type:
docker-compose up -d --no-deps --build helloworld

2. while server is running, open another terminal window to run client script
docker exec -it dockersample_helloworld_1 /bin/bash

if that command doesn't work then we would have to get the name from the running container by
typing the following command and looking at the name column:
docker ps

3. run the client script in the container bash:
python client_script.py "how are you, little piggy?"
the part in the string for the above

then script will return a response like so:
{"translation":"owhay areay ouyay, ittlelay iggypay?"}

