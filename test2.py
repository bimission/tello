import hid

from easytello import tello


for device in hid.enumerate():
    print(device)
    print(f"0x{device['vendor_id']:04x}:0x{device['product_id']:04x} {device['product_string']}")

gamepad = hid.device()
gamepad.open(0x054c, 0x09cc)
gamepad.set_nonblocking(True)

#5th bit
##https://web.archive.org/web/20210301230721/https://www.psdevwiki.com/ps4/DS4-USB

ps4_nothing=8
ps4_triangle=136
ps4_x=40
ps4_rectangle=24
ps4_circle=72

ps4_arrow_up=0
ps4_arrow_down=4
ps4_arrow_left=6
ps4_arrow_right=2

my_drone = tello.Tello()

while True:
    report = gamepad.read(64)
    if(len(report)>0):
     if report[5]==ps4_arrow_up:
        print("up")
        my_drone.up(100)
     elif report[5]==ps4_arrow_down:
        print("down")
        my_drone.down(100)
     elif report[5]==ps4_arrow_left:
        print("left")
        my_drone.right(100)
     elif report[5]==ps4_arrow_right:
        print("right")
        my_drone.left(100)
     elif report[5]==ps4_nothing:
        print("nothing")
     elif report[5]==ps4_x:
        print("x")
        my_drone.land()
     elif report[5]==ps4_triangle:
        print("triangle")
        my_drone.takeoff()
     elif report[5]==ps4_circle:
        print("circle")
     elif report[5]==ps4_rectangle:
        print("rectangle")

##{'path': b'DevSrvsID:4295030046', 'vendor_id': 1356, 'product_id': 2508, 'serial_number': '', 'release_number': 256, 'manufacturer_string': 'Sony Interactive Entertainment', 'product_string': 'Wireless Controller', 'usage_page': 1, 'usage': 5, 'interface_number': 3}