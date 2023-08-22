# Memory Consumption Calculator
Author : Runping Lai <rlai@juniper.net>\
SRX Platform Team

## Objective:
The primary purpose of the PFE-Memory-Calculator is to assist in determining whether the total memory size is adequate to support the required scale number during the early design stages of PFE memory allocation. Therefore, developed an app using **Qt**.

## Background:
In our SRXTVP platforms, memory allocation is done via a config file. Ensuring the correct memory allocation is crucial. It requires calculations in advance to guarantee that the numbers specified in this config file do not exceed the overall available memory. Notably, if the utilized memory exceeds the total memory capacity, the device fails to boot up. This not only wastes valuable development time but also fails to provide effective feedback to the developers.


## Features:

**Config File Analysis:**\
•	The app can parse configurations from the 'dst_pfe_capacity.conf' file.
**Embedded Formula Calculation:**\
•	It calculates the total memory usage based on the parsed configurations using embedded formulas.
```
usedMem = kernelHeap + \
        DPQMemory + \
        IDPMemory + \
        services + \
        PacketMBuf + \
        HostMBuf + \
        UserHeap
(More details on formula can be found at app.py line35 update_result() )
```
**Visual Memory Analysis:**\
•	Provides users with a visual representation of memory usage, making it easier to understand the distribution.\
**Real-time Configuration Adjustments:**\
•	Allows users to make real-time changes to configurations and simulate memory usage scenarios.\
**Memory Overuse Prevention:**\
•	Helps to avoid situations where excessive memory usage might prevent the system from booting up, ensuring the efficiency of user workflow.

## Highlights:

**Hexadecimal Input Support:**\
•	Users can input values in hexadecimal format (e.g., 0x02000000).\
**Kilobyte Notation Support:**\
•	Allows for input in 'k' notation, where, for instance, 5k would translate to 5*1024.\
**Config File Viewer:**\
•	Features a read-only viewer for the 'dst_pfe_capacity.conf' file on the user interface's right side, empowering users with search and check functionalities post-parsing.



## Installation

#### *Prerequisites:*
1. Make sure to have *Python* as executable in system

*WINDOWS:*
```
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
pip install pyinstaller qdarkstyle
pyinstaller --onefile --name mem_calculator src/app.py
.\dist\mem_calculator
```

*macOS:*
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install pyinstaller qdarkstyle
pyinstaller --onefile --name mem_calculator src/app.py
./dist/mem_calculator
```

## TODO
1. Adding a setting page that supports user change calculate formula.

# Qt-Memory-Calculator
