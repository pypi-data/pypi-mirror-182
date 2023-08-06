"""notify serial changes"""
# pylint: disable=wrong-import-position
from pathlib import Path
import os
import time
import gi
from serial.tools.list_ports import comports

gi.require_version("Notify", "0.7")
from gi.repository import Notify, GdkPixbuf


class PortChecker:
    """Checks serialports for changes"""

    def __init__(self):
        self.ports = set(comports())
        self.new_ports = None
        Notify.init("serial_monitor")
        self.summary = ""
        self.body = ""
        self.notification = Notify.Notification.new(self.summary, self.body)
        self.connected = GdkPixbuf.Pixbuf.new_from_file("usb_plug_connected.png")
        self.disconnected = GdkPixbuf.Pixbuf.new_from_file("usb_plug_disconnected.png")

    def check_ports(self):
        """Check the ports"""
        self.new_ports = set(comports())
        for port in self.ports - self.new_ports:
            self.notification.set_image_from_pixbuf(self.disconnected)
            self.summary = f"{port.device} disconnected"
            self.notification.update(self.summary)
            self.notification.show()

        for port in self.new_ports - self.ports:
            self.notification.set_image_from_pixbuf(self.connected)
            self.summary = f"{port.device} connected"
            self.notification.update(self.summary)
            self.notification.show()

        self.ports = self.new_ports


def main():
    """main entry"""
    os.chdir(Path(__file__).parent)
    job = PortChecker()
    while True:
        job.check_ports()
        time.sleep(1)


if __name__ == "__main__":
    main()
