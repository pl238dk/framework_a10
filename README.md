# A10 AXAPI Framework

This is a framework that connects to the API of an A10 device.

## Authentication

Credentials are passed as arguments to the object's `authenticate()` function. If a password keyword-argument is not provided, `getpass` will prompt for a password.

## Getting Started

To instantiate a `A10` object, pass a string of the host/ip to connect.

Connection will be established to 'https://' + host/ip.

```
>>> host = '192.168.1.50'
>>> a = A10(host)
```

Then to authenticate :

```
>>> username = 'jack_sparrow'
>>> pw = 'yarrrr123'
>>> a.authenticate(username, password=pw)
```

If configured, the partition may need to be set in order to interact with the appliance :

```
>>> partition = 'INSIDE'
>>> a.set_active_partition(partition)
```

## AXAPI Features

As of the most current update, only features for pulling SLB Server stats have been explored.

At the time of writing, numerous Incident tickets came in that requested inbound/outbound statistics of an SLB Server. The file `get_slb_server.py` was written to one-shot this data retrieval.

To use the `get_slb_server.py` script in Linux, save the file and make it executable :

```
> chmod u+x get_slb_server.py`
```

Then call the script by using `./` notation, passing the A10 host as the first argument and SLB Server as the second argument :

```
> ./get_slb_server.py a10.domain.com Website_80
```

## Logoff

To limit the number of sessions, it is important to log off after interactions are complete.

```
>>> a.logoff()
```