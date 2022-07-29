# Picobrick

## Running

```shell
# replace PI_PORT with the actual value where the Raspberry Pi Pico is connected
PI_PORT=/dev/tty.usbmodemXXX poe version
```

## Memo

### Regarding the Python Version

I chose to use python 3.10 because micropython versions don't work well with
Apple Silicon. Since I will be using it mainly for the code completion for the
LSP, it wouldn't matter too much (as of now)
