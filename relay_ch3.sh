ch=21
state=1

echo $ch › /sys/class/gpio/export
echo out > /sys/class/gpio/gpio$ch/direction
echo $state › /sys/class/gpio/gpio$ch/value