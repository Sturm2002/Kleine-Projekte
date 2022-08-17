import serial,os,json


oldSerialString = ""
serialString = ""  # Used to hold data coming over UART
running = True

jsonpath = os.path.dirname(os.path.abspath(__file__)) + '\conf.json'
jsonfile = open(jsonpath)
jsonvals = json.load(jsonfile)

ComPort = jsonvals["NFCReader"]["Settings"]["ComPort"]
#ComPort = "COM3"

def StopReader():
    global running
    running = False

def StartReader():
    global running
    running = True
    Main()
        

def GetData():
    global oldSerialString,serialString,running
    if running:
        while oldSerialString != serialString or serialString == "":
            pass
        oldSerialString = ""
        return (serialString.replace("\n","")).replace("\r","")

    else:
        return None

def Main():
    global serialPort,serialString,running,oldSerialString,ComPort
    try:
        serialPort = serial.Serial(port=ComPort, baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
    except serial.SerialException:
        running = False
        print("\n" + ComPort+ " Not Connected")
        input()
        return 

    while running:
        # Wait until there is data waiting in the serial buffer
        if serialPort.in_waiting > 0:

            # Read data out of the buffer until a carraige return / new line is found
            serialString = serialPort.readline()

            # Print the contents of the serial data
            try:
                serialString = serialString.decode("Ascii")
                oldSerialString = serialString
            except:
                pass
if __name__ == "__main__":
    Main()
