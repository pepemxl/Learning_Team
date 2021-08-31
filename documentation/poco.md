# POCO C++

POCO is a collection of C++ class libraries, with a similar concept to the [Java Class Library](https://en.wikipedia.org/wiki/Java_Class_Library), the [.NET Framework](https://en.wikipedia.org/wiki/.NET_Framework) or [Apple´s Cocoa](https://en.wikipedia.org/wiki/Cocoa_(API)). POCO is a open source cross-platform library focused in network applications licensed under Boost Software License.

## Features
- Cache framework
- Cryptography
- Date and Time Classes
- Events (signal/slot mechanism) and notifications framework.
- FTP client for transferring files
- Filesystem classes for platform-independent path manipulation, directory listing and globing
- HTML form handling
- HTTP server and client, C++ Server Page Compiler
- Logging framework
- Multithreading
    - basic threads
    - synchronization
- POP3 client for receivin mail
- Platform Abstraction
- Processes and IPC
- Reactor framework
- Regular Expresions
- SMTP client for sending mail
- SQL database access (SQLite, MySQL, ODBC)
- SSL/TLS support based on OpenSSL
- Shared Library and class loading
- Smart Pointers and Memory Management
- Sockets and raw sockets
- Stream classes for Base64 and HexBinary encoding/decoding, compression, line ending conversion, reading/writing to memory.
- String formattion and string utilities
- TCP server framework (multithreaded)
- Text encoding and conversions
- Tuples
- URI handling
- UTF-8 and Unicode support
- UUID handling and support
- XML parsing and XML generation
- Zip file manipulation

## Platforms
- Windows
- Linux
- Max OS X
- Solaris (requires patches)
- Embedded Linux(uClibc, glibc)
- iOS
- Windows Embedded CE
- QNX

POCO based applications, using the built-in web server run on 75 MHz ARM9-based linux systems (uClibc) with 8MB RAM and 4MB Flask.

Typical mid-range embedded platforms(64MB RAM, 64 MB Flask and 180 MHz ARM9) provide plenty or resources even for more complex applications.

## Types and Byte Order
- Fixed-Size Integer Types
- Byte Order Conversions
- AnyType
- DynamicAny Type

### Fixed-Size Integer Types
- POCO defines types of fixed-size integers
- `#include "Poco/Types.h"`
    - `Poco::Int8`
    - `Poco::Int16`
    - `Poco::Int32`
    - `Poco::Int64`
    - `Poco::UInt8`
    - `Poco::UInt16`
    - `Poco::UInt32`
    - `Poco::UInt64`
- `Poco::IntPtr` and `Poco::UIntPtr` are integer with same size as a pointer type.
- `POCO_PTR_IS_64_BIT`: this macro is defined if pointers are 64 bits.
- `POCO_LONG_IS_64_BIT`: this macro is defined if long's are 64 bits.
- `POCO_ARCH_LITTLE_ENDIAN`: macro is defined if architecture is little endian
- `POCO_ARCH_BIG_ENDIAN`: macro is defined if architecture is big endian
- `#include "Poco/ByteOrder.h"`, class `Poco::ByteOrder` provides static methods for byte order conversions.
- `IntXX flipBytes(IntXX value)` changes byte order from big order from big to little endian and viceversa.
- `IntXX toBigEndian(IntXX value)` converts from host byte order to big endian
- `IntXX toLittleEndian(IntXX value)` converts from host byte order to little endian
- `IntXX fromBigEndian(IntXX value)` converts from big endian to host byte order
- `IntXX fromLittleEndian(IntXX value)` converts from little endian to host byte order
- `IntXX toNetwork(IntXX value)` converts from host byte order to network byte order
- `IntXX fromNetwork(IntXX value)` converts from network byte order to host byte order
- **Network byte order is big endian**
- All methods are defined as inline functions.
- 


## Include files

`/usr/local/include/Poco`

Libraries `/usr/local/lib/`

```bash 
root@890e77dd83d8:/# ls /usr/local/**/libPoco*.so
/usr/local/lib/libPocoActiveRecord.so  /usr/local/lib/libPocoDataPostgreSQL.so  /usr/local/lib/libPocoJSON.so     /usr/local/lib/libPocoNetSSL.so  /usr/local/lib/libPocoZip.so
/usr/local/lib/libPocoCrypto.so        /usr/local/lib/libPocoDataSQLite.so      /usr/local/lib/libPocoJWT.so      /usr/local/lib/libPocoRedis.so
/usr/local/lib/libPocoData.so          /usr/local/lib/libPocoEncodings.so       /usr/local/lib/libPocoMongoDB.so  /usr/local/lib/libPocoUtil.so
/usr/local/lib/libPocoDataODBC.so      /usr/local/lib/libPocoFoundation.so      /usr/local/lib/libPocoNet.so      /usr/local/lib/libPocoXML.so
```

```bash
root@890e77dd83d8:/# ls /usr/local/lib/cmake/Poco
PocoActiveRecordConfig.cmake                  PocoDataPostgreSQLTargets-relwithdebinfo.cmake  PocoJSONTargets-relwithdebinfo.cmake     PocoRedisConfig.cmake
PocoActiveRecordConfigVersion.cmake           PocoDataPostgreSQLTargets.cmake                 PocoJSONTargets.cmake                    PocoRedisConfigVersion.cmake
PocoActiveRecordTargets-relwithdebinfo.cmake  PocoDataSQLiteConfig.cmake                      PocoJWTConfig.cmake                      PocoRedisTargets-relwithdebinfo.cmake
PocoActiveRecordTargets.cmake                 PocoDataSQLiteConfigVersion.cmake               PocoJWTConfigVersion.cmake               PocoRedisTargets.cmake
PocoConfig.cmake                              PocoDataSQLiteTargets-relwithdebinfo.cmake      PocoJWTTargets-relwithdebinfo.cmake      PocoUtilConfig.cmake
PocoConfigVersion.cmake                       PocoDataSQLiteTargets.cmake                     PocoJWTTargets.cmake                     PocoUtilConfigVersion.cmake
PocoCryptoConfig.cmake                        PocoDataTargets-relwithdebinfo.cmake            PocoMongoDBConfig.cmake                  PocoUtilTargets-relwithdebinfo.cmake
PocoCryptoConfigVersion.cmake                 PocoDataTargets.cmake                           PocoMongoDBConfigVersion.cmake           PocoUtilTargets.cmake
PocoCryptoTargets-relwithdebinfo.cmake        PocoEncodingsConfig.cmake                       PocoMongoDBTargets-relwithdebinfo.cmake  PocoXMLConfig.cmake
PocoCryptoTargets.cmake                       PocoEncodingsConfigVersion.cmake                PocoMongoDBTargets.cmake                 PocoXMLConfigVersion.cmake
PocoDataConfig.cmake                          PocoEncodingsTargets-relwithdebinfo.cmake       PocoNetConfig.cmake                      PocoXMLTargets-relwithdebinfo.cmake
PocoDataConfigVersion.cmake                   PocoEncodingsTargets.cmake                      PocoNetConfigVersion.cmake               PocoXMLTargets.cmake
PocoDataODBCConfig.cmake                      PocoFoundationConfig.cmake                      PocoNetSSLConfig.cmake                   PocoZipConfig.cmake
PocoDataODBCConfigVersion.cmake               PocoFoundationConfigVersion.cmake               PocoNetSSLConfigVersion.cmake            PocoZipConfigVersion.cmake
PocoDataODBCTargets-relwithdebinfo.cmake      PocoFoundationTargets-relwithdebinfo.cmake      PocoNetSSLTargets-relwithdebinfo.cmake   PocoZipTargets-relwithdebinfo.cmake
PocoDataODBCTargets.cmake                     PocoFoundationTargets.cmake                     PocoNetSSLTargets.cmake                  PocoZipTargets.cmake
PocoDataPostgreSQLConfig.cmake                PocoJSONConfig.cmake                            PocoNetTargets-relwithdebinfo.cmake
PocoDataPostgreSQLConfigVersion.cmake         PocoJSONConfigVersion.cmake                     PocoNetTargets.cmake

```