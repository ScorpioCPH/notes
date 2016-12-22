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


##### Network Card

- `lspci`: list all PCI devices.
- `lshw`: list all hardware.

```
$ lspci | grep -i "ethernet"
03:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (rev 0c)
```

```
$ sudo lshw -C network
  *-network               
       description: Ethernet interface
       product: RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
       vendor: Realtek Semiconductor Co., Ltd.
       physical id: 0
       bus info: pci@0000:03:00.0
       logical name: enp3s0
       version: 0c
       serial: 40:8d:5c:6b:e8:2d
       size: 1Gbit/s
       capacity: 1Gbit/s
       width: 64 bits
       clock: 33MHz
       capabilities: pm msi pciexpress msix vpd bus_master cap_list ethernet physical tp mii 10bt 10bt-fd 100bt 100bt-fd 1000bt 1000bt-fd autonegotiation
       configuration: autonegotiation=on broadcast=yes driver=r8169 driverversion=2.3LK-NAPI duplex=full firmware=rtl8168g-2_0.0.1 02/06/13 ip=192.168.1.11 latency=0 link=yes multicast=yes port=MII speed=1Gbit/s
       resources: irq:29 ioport:d000(size=256) memory:f7800000-f7800fff memory:f2100000-f2103fff
```
