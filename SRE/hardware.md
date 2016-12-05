## Hardware

##### ECC memory

[WiKi](https://en.wikipedia.org/wiki/ECC_memory)

`Error-correcting code memory` (ECC memory) is a type of computer data storage that can detect and correct the most common kinds of internal data corruption. ECC memory is used in most computers where data corruption cannot be tolerated under any circumstances, such as for scientific or financial computing.

##### How to Check ECC RAM Functionality

**dmidecode**

```
$ sudo dmidecode --type memory
# dmidecode 3.0
Getting SMBIOS data from sysfs.
SMBIOS 2.8 present.

Handle 0x0042, DMI type 16, 23 bytes
Physical Memory Array
    Location: System Board Or Motherboard
    Use: System Memory
    Error Correction Type: Single-bit ECC
    Maximum Capacity: 64 GB
    Error Information Handle: Not Provided
    Number Of Devices: 4

...

Handle 0x0046, DMI type 17, 40 bytes
Memory Device
    Array Handle: 0x0042
    Error Information Handle: Not Provided
    Total Width: 128 bits
    Data Width: 64 bits
    Size: 16384 MB
    Form Factor: DIMM
    Set: None
    Locator: ChannelB-DIMM1
    Bank Locator: BANK 3
    Type: DDR4
    Type Detail: Synchronous
    Speed: 2133 MHz
    Manufacturer: Samsung
    Serial Number: 02231910
    Asset Tag: 9876543210
    Part Number: M391A2K43BB1-CRC    
    Rank: 2
    Configured Clock Speed: 2133 MHz
    Minimum Voltage: Unknown
    Maximum Voltage: Unknown
    Configured Voltage: 1.2 V
```

`Error Correction Type: Single-bit ECC` is what we are looking for.
`Total Width: 128 bits` and `Data Width: 64 bits` are also useful informations.

**inxi**

```
$ inxi -m -xxx
Memory:    Array-1 capacity: 64 GB devices: 4 EC: Single-bit ECC
           Device-1: ChannelA-DIMM0 size: No Module Installed type: N/A
           Device-2: ChannelA-DIMM1 size: No Module Installed type: N/A
           Device-3: ChannelB-DIMM0 size: No Module Installed type: N/A
           Device-4: ChannelB-DIMM1 size: 16 GB speed: 2133 MHz type: DDR4 (Synchronous)
           bus width: 128 bits manufacturer: Samsung part: M391A2K43BB1-CRC serial: 02231910
```

Here ECC-RAM modules are used `EC: Single-bit ECC`.
