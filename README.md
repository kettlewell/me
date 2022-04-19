# me
Me is a personal python playground to explore and capture snippets of code to learn and grow from

# TODO
Rename and restructure the files in this project
* remove the me_ names
* get the libs and modules better organized
* move boiler plate files elsewhere to make things cleaner to work with / look at.
* include some numpy, pandas, opencv, etc example code as well
* include some graphical / plotting examples


# command line args ( still a work in progress )

```shell
usage: main.py [-h] [--practice] [--verbose] [--log {debug,info,warning,error,critical}]
               {lists,dicts,decorators,re,scope,functions,truthy,iterators,lambdas,generators,tuples,strings,sets,exceptions,filedir,unix,networking,threading,multiprocessing,async,coroutine,numerics,comparisons,compression,internet,play,modules}
               ...

Demo program that highlights a lot of functionality of the python programming language.

options:                           
  -h, --help            show this help message and exit
  --practice, -p        practice runs
  --verbose, -v         verbose levels
  --log {debug,info,warning,error,critical}, -l {debug,info,warning,error,critical}
                        log level

subcommands:
  Sub commands for executing specific code blocks

  {lists,dicts,decorators,re,scope,functions,truthy,iterators,lambdas,generators,tuples,strings,sets,exceptions,filedir,unix,networking,threading,multiprocessing,async,coroutine,numerics,comparisons,compression,internet,play,modules}
                        Available Subcommands
    lists               lists commands
    dicts               dicts commands
    decorators          decorator commands
    re                  regex commands
    scope               Scope commands
    functions           Function (builtin) commands
    truthy              Truthy commands
    iterators           Iterators commands
    lambdas             Lambdas commands
    generators          generators commands
    tuples              tuples commands
    strings             Strings commands
    sets                sets commands
    exceptions          Exceptions commands
    filedir             File and Directory commands
    unix                Unix commands
    networking          Networking and IPC commands
    threading           Threading commands
    multiprocessing     Multiprocessing commands
    async               async commands
    coroutine           coroutine commands
    numerics            numerics commands
    comparisons         comparison commands
    compression         Compression commands
    internet            Internet commands
    play                Play sub-command help
    modules             Modules commands
```