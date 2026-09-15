# rebuildmymc
A Python script to run Minecraft Java Edition directly from the .jar file.
> [!TIP]
> This program generates two run scripts.\
> The file names will end in .cmd for Windows and .sh for Linux/macOS.\
> If the `run` script fails, this is usually because no graphics drivers are installed.\
> This can be bypassed by using the `run-nogpu` script instead.

Credit to [SchmollerLab](https://github.com/SchmollerLab/java_portable_windows) for the portable JDK/JRE environment.

## Requirements
Java Development Kit (JDK) 8 or newer must be installed.\
You will need files from LWJGL.
> [!IMPORTANT]
> The portable version has its own JDK and LWJGL files.\
> If you are using the portable version, the previous two requirements may be ignored.
You will need the .jar file for the Minecraft version of your choice.

## Compatibility
OS | Minecraft Version | Main script | Portable script
--- | --- | --- | ---
Any | 1.6 or newer | No | No
Windows 11 | 1.3.1 to 1.5.2 | Yes | Yes
Windows 11 | 1.3 or earlier | Yes | Yes
Windows XP to 10 | 1.3.1 to 1.5.2 | Limited | Limited
Windows XP to 10 | 1.3 or earlier | Yes | Yes
Ubuntu | 1.3.1 to 1.5.2 | Yes | No
Debian | 1.3.1 to 1.5.2 | Yes | No
Fedora | 1.3.1 to 1.5.2 | Yes | No
Other Linux | 1.3.1 to 1.5.2 | Limited | No
Linux (any) | 1.3 or earlier | Yes | No
macOS | 1.3.1 to 1.5.2 | Limited | No
macOS | 1.3 or earlier | Yes | No

## Download links
[Download LWJGL](https://legacy.lwjgl.org/download.php.html)

## Minecraft downloads (oldest first)
### Alpha, Beta and earlier
[Pre-classic](https://omniarchive.uk/archive/java/client/preclassic/)\
[Classic](https://omniarchive.uk/archive/java/client/classic/)\
[Indev](https://omniarchive.uk/archive/java/client/indev/)\
[Infdev](https://omniarchive.uk/archive/java/client/infdev/)\
[Alpha](https://omniarchive.uk/archive/java/client/alpha/)\
[Beta](https://omniarchive.uk/archive/java/client/beta/)

### Releases
[1.0](https://omniarchive.uk/archive/java/client/release/1.0.0/)\
[1.1](https://omniarchive.uk/archive/java/client/release/1.1/)\
[1.2](https://omniarchive.uk/archive/java/client/release/1.2/)\
[1.3](https://omniarchive.uk/archive/java/client/release/1.3/)\
[1.4](https://omniarchive.uk/archive/java/client/release/1.4/)\
[1.5](https://omniarchive.uk/archive/java/client/release/1.5/)
