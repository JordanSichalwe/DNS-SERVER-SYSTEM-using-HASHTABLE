# DNS-SERVER-SYSTEM-using-HASHTABLE
   A Domain Name System (DNS) is a system that keeps Domain names and their corresponding IP Address in a Network. It is able to resolve domain names to their IP Addresses. This is used most due to the fact that names are more convenient for humans to remember and work with, despite this computers communicate using IP address that can easily translate to binary to allow these conversations. The DNS server resolves these names into IP Addresses before sending the packets.
A Domain Name is a descriptive name given to a network device e.g. Computer based on a hierarchical decentralized naming system with structure <name>.<subdomain>.<upper domain> e.g. dns.lectures.cs
This DNS Server System uses the same approach to store domain names and their corresponding addresses to keep track of domains and their sub-domains. This also gives it the ability to resolve domain names into address. Additional Functionalities are as in a DNS Server. These include DNS Management and Creation.
### REQUIREMENTS
DNS App requires the following:

* Windows 64-bit for this build (Can be modified to work on MAC and 32-bit Windows)
* Python 3.6
  - Python Interpreter
  - Numpy module
  - Kivy modules(kivy, kivy.deps.glew, kivy.deps.sdl2)

## Insertion Diagram
![untitled](https://user-images.githubusercontent.com/36822517/42100389-573aaebc-7bc0-11e8-85fb-4d8346a5e5b5.png)

## File Management
![screenshot 114](https://user-images.githubusercontent.com/36822517/42100229-eea438c8-7bbf-11e8-821a-ee17d162f243.png)

## Rashing
Rehashing is the situation in which the Hash Table is changed, most likely in structure. This usually occurs due to Hash Table being too small to allow new entries. Therefore, Table is increased in size and entities of old table hashed to new table. This allows more entries into the table. To guarantee that every element finds a position table are of prime size. In This implementation, when table is full or entry cannot find a place the table rehashed to another table of prime size greater than double the size of original table e.g. 3 ->7-> 17. This is called Prime Double Rehashing.
![rehashing](https://user-images.githubusercontent.com/36822517/42100366-4b099aae-7bc0-11e8-8188-c1f7cd4795c3.png)

## Application

![app info](https://user-images.githubusercontent.com/36822517/42100379-4eba747a-7bc0-11e8-94c5-f09d48da4fc9.png)

![tab info](https://user-images.githubusercontent.com/36822517/42100359-47714aa4-7bc0-11e8-8da0-f8ae6e0bddbf.png)

![screenshot 78](https://user-images.githubusercontent.com/36822517/42100189-d3b215a8-7bbf-11e8-94ed-0fb0b6c43ca2.png)

![screenshot 137](https://user-images.githubusercontent.com/36822517/42100245-fab54832-7bbf-11e8-83bc-5e3d25ce9977.png)

## Implementation Example
 Simulate a web with .cs as the highest level domain. This has subdomains guests.cs, lecturers.cs and students.cs as illustrated in the diagram below. Each of these subdomains have at least 10 computers.
![dns](https://user-images.githubusercontent.com/36822517/42100976-04707d18-7bc2-11e8-8288-d546eee89843.png)
