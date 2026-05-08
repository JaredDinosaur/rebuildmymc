# rebuildmymc

A Python script to run Minecraft Java Edition directly from the .jar file.

This program generates two run scripts (.cmd for Windows and .sh for Linux/macOS). If `run` fails (usually because no graphics drivers are installed), try `run-nogpu`.

Credit to [SchmollerLab](https://github.com/SchmollerLab/java_portable_windows) for the portable JDK/JRE environment.

## Requirements

Java JDK and JRE must be fully installed.

If your OS does not allow you to install both, only install JDK.

You will need files from LWJGL.

* The portable version does not need these as it has its own JDK folder and LWJGL files.

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

[Pre-classic](https://omniarchive.uk/archive/java/client/preclassic/)

[Classic](https://omniarchive.uk/archive/java/client/classic/)

[Indev](https://omniarchive.uk/archive/java/client/indev/)

[Infdev](https://omniarchive.uk/archive/java/client/infdev/)

[Alpha](https://omniarchive.uk/archive/java/client/alpha/)

[Beta](https://omniarchive.uk/archive/java/client/beta/)

### Releases

[1.0](https://omniarchive.uk/archive/java/client/release/1.0.0/)

[1.1](https://omniarchive.uk/archive/java/client/release/1.1/)

[1.2](https://omniarchive.uk/archive/java/client/release/1.2/)

[1.3](https://omniarchive.uk/archive/java/client/release/1.3/)

[1.4](https://omniarchive.uk/archive/java/client/release/1.4/)

[1.5](https://omniarchive.uk/archive/java/client/release/1.5/)
