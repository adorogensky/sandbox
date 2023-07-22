# Android Sandbox

Parameter | Value | Command
--- | --- | ---
OS | 6.3.6-200.fc38.x86_64 | ``uname -a``
Phone | Google Pixel 7 Pro<p>Screen: 6.7"<p>Resolution: 3120x1440<p>Density: 512 ppi| 
Phone OS | Android 13<p>Build Number: TQ3A.230605.012
Android Studio | Flamingo 2022.2.1 Patch 2 <p> Build #AI-222.4459.24.2221.10121639| https://developer.android.com <p> Linux (64 bit)<p> ``dnf install android-sdk-platform-tools-common``

# How To
What | How
--- | ---
enable dev mode | pixel: system -> about phone -> build number -- tap 7 times
keep dev mode enabled after restart/update | todo
run pixel app over wifi | pixel: enable dev mode <p>pixel: settings -> system -> developer options -> wireless debugging -- turn on<p>android studio: pair devices using wifi -> pair using qr/pairing code<p>pixel: settings -> system -> developer options -> wirless debuggging -> pair device with qr/pairing code<p>``connecting to device. this takes up to 2 minutes``<p>``google pixel 7 pro connected``
run pixel app over usb  | ``dnf install android-tools -y``<p>``systemctl enable --now adb.service``<p>``systemctl reboot -i``<p>pixel: settings -> system -> developer options -> select debug app -- tap 'no debug application set'
run app on emulators | todo

# Troubleshooting
Problem | Solution
--- | ---
pixel wont pair over wifi | 1. android studio: file -> settings -> build, execution, deployment -> debugger -> enable adb mdns for wireless debugging -- turn off and back on <p>2. pixel: system -> developer options -> wireless debugging -- turn off and back on
pixel loses wifi connection after sitting idle for some time | no solution ye

android: disconnect phone<p>
adb kill-server<p>
sudo adb start-server<p>
pixel: turn off and on usb debugging on phone
pixel: revoke usb debugging authorizations
android studio: settings -> build, execution, deployment -> debugger -> turn on and off use libusb backend
android studio: settings -> build, execution, deployment -> debugger -> turn on and off automatically start and manage server

problem 1: phone wont get detected by android studio

problem 2: changes wont get detected


