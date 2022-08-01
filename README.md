# Debug code for function app eventhub trigger.

## Deploy to Function App
I write hard code in this repo for eventhub connection string and eventhub name, please change the `<eventhub-connection-string>`, `<eventhub-name-1>` and `<eventhub-name-2>` to your own setting.

# Calling routine

the trigger listen event from `<eventhub-name-1>` and send it to `<eventhub-name-2>`

use 
```bash
python3 sender.py
```

to send `small.json` as event data to `<eventhub-name-1>`

use https://github.com/ZejiaJiang/Eventhub-Processor-Sample to start a processor to receive event from `<eventhub-name-2>`