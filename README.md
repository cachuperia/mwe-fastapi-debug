# mwe-fastapi-debug

IDE configuration for debugging an application running inside a remote Docker Compose stack. 

In this example, we will be working with an Ubuntu 20.04 virtual machine, but any instance with SSH access can be used.


# Bootstrap

This step can be skipped for VS Code [Remote - SSH](https://code.visualstudio.com/docs/remote/ssh) sessions.

```shell
# Local shell
git clone https://github.com/cachuperia/mwe-fastapi-debug.git
cd mwe-fastapi-debug
```

SSH credentials and debugger port for forwarding. 

Please change these values to your own if you need to connect to a different instance.

```shell
# Local shell
DEBUGGER_PORT=5678
USER=vagrant
HOST=192.168.56.5
KEY_PATH=.vagrant/machines/focal64/virtualbox/private_key
SSH_OPTIONS="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -S /tmp/%r@%h-%p"
```

# Start VM 

```shell
# Local shell
vagrant up
```

# Configure Debugger

## Configure VS Code

You can connect to the instance with debugger server port forwarded

```shell
# Local shell
ssh -L ${DEBUGGER_PORT}:localhost:${DEBUGGER_PORT} ${USER}@${HOST} -i ${KEY_PATH} ${SSH_OPTIONS}
```

or [Remote SSH](https://code.visualstudio.com/docs/remote/ssh) session.

Start debugging compose stack:

```shell
# Remote shell
cd mwe-fastapi-debug
docker compose -f docker-compose.debug-vscode.yml up
```

Start `VS Code: Attach to Debugger` [debug](https://code.visualstudio.com/docs/python/debugging) [configuration](.vscode/launch.json), set breakpoint and send API request.

### Local shell(debugger port should be forwarded from remote)

![VSCode debugger](docs/vscode_breakpoint.png)

```shell
# Local shell
curl 192.168.56.5:8000
```

### Remote SSH

![VSCode debugger](docs/vscode_breakpoint_remote.png)

```shell
# Remote shell
curl localhost:8000
```

## Configure PyCharm

Create configuration for `Python Debug Server`,  host - `0.0.0.0`, port - `5678`, mapping - `/path/to/project:/app`

![PyCharm Debug Server](docs/pycharm_debug_server.png)

Start `Python Debug Server`.


Connect to the instance with debugger server port forwarded to remote:

```shell
# Local shell
ssh -R 0.0.0.0:${DEBUGGER_PORT}:localhost:${DEBUGGER_PORT} ${USER}@${HOST} -i ${KEY_PATH} ${SSH_OPTIONS}
```

Copy `pydevd-pycharm.egg` to the remote:

```shell
# Local shell
# Change path to debugger egg to yours
PYCHARM_DEBUGGER=/path/to/PyCharm/debug-eggs/pydevd-pycharm.egg 
scp ${PYCHARM_DEBUGGER} ${USER}@${HOST}:/home/${USER}/mwe-fastapi-debug/
```

Start debugging compose stack:

```shell
# Remote shell
cd mwe-fastapi-debug
docker compose -f docker-compose.debug-pycharm.yml up
```

Set Breakpoint and send API request:

![PyCharm Debug Server](docs/pycharm_breakpoint.png)

```shell
# Local shell
curl 192.168.56.5:8000
```

## Code modification with "hot (no build) reload"

Modify the service code locally or remotely.

**Make sure that your local code is synchronized with the remote folder [mounted](./docker-compose.debug.yml#L7) as the `/app` folder if you are working locally.**

Next, restart the `docker-compose.debug-<IDE name>.yml` stack.

**If you are working in a Remote SSH VS Code session, ensure that your remote changes are pushed to `origin`.**

# Cleanup

## Close SSH connection

```shell
# Local shell
ssh -S /tmp/%r@%h-%p -O exit ${USER}@${HOST}
```

## Stop VM 

```shell
# Local shell
vagrant halt
```

## Destroy VM 

```shell
# Local shell
vagrant destroy -f
```
