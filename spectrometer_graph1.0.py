import serial # import Serial Library
import numpy  # Import numpy
import matplotlib.pyplot as plt #import matplotlib library
from drawnow import *
from time import sleep
 
violet= []
dataArray = []
blue=[]
green=[]
yellow = []
orange = []
red = []
arduinoData = serial.Serial('/dev/cu.wchusbserial1420', 115200) #Creating our serial object named arduinoData
plt.ion() #Tell matplotlib you want interactive mode to plot live data
cnt=0
firstRun = 0
 
def makeFig(): #Create a function that makes our desired plot
    #plt.ylim(0,20000)                                 #Set y min and max values
    plt.title('My Live Streaming Sensor Data')      #Plot the title
    plt.grid(True)                                  #Turn the grid on
    plt.ylabel('Intensity')                            #Set ylabels
    plt.plot(violet, 'darkviolet', label='Violet')       #plot the temperature
    plt.legend(loc='upper left')                    #plot the legend
    #plt2=plt.twinx()                                #Create a second y axis
    #plt.ylim(0,20000)                           #Set limits of second y axis- adjust to readings you are getting
    #plt2.plot(pressure, 'b^-', label='Pressure (Pa)') #plot pressure data
    #plt2.set_ylabel('Pressrue (Pa)')                    #label second y axis
    #plt2.ticklabel_format(useOffset=False)           #Force matplotlib to NOT autoscale y axis
    #plt2.legend(loc='upper right')                  #plot the legend
    
    
    plt.plot(blue, 'b', label='Blue') #plot pressure data
    plt.plot(green, 'green', label='Green') #plot pressure data
    plt.plot(yellow, 'yellow', label='Yellow') #plot pressure data
    plt.plot(orange, 'orange', label='Orange') #plot pressure data
    plt.plot(red, 'red', label='Red') #plot pressure data
    
    #plt.ticklabel_format(useOffset=False)           #Force matplotlib to NOT autoscale y axis
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)   
    
 
while True: # While loop that loops forever
    while (arduinoData.inWaiting()==0): #Wait here until there is data
        pass #do nothing
    while firstRun < 5:
        discardString = arduinoData.readline()
        firstRun += 1
        print(firstRun)
    arduinoString = arduinoData.readline() #read the line of text from the serial port
    print(arduinoString)
    dataArray = arduinoString.decode().split(' , ')   #Split it into an array called dataArray
    v = float( dataArray[0])            #Convert first element to floating number and put in temp
    b = float( dataArray[1])            #Convert second element to floating number and put in P
    g = float( dataArray[2]) 
    y = float( dataArray[3]) 
    o = float( dataArray[4])
    r = float( dataArray[5])
    
    violet.append(v)                     #Build our tempF array by appending temp readings
    blue.append(b)                     #Building our pressure array by appending P readings
    green.append(g)
    yellow.append(y)
    orange.append(o)
    red.append(r)
    drawnow(makeFig)                       #Call drawnow to update our live graph
    #plt.pause(1)                     #Pause Briefly. Important to keep drawnow from crashing
    cnt=cnt+1
    if(cnt>50):                            #If you have 50 or more points, delete the first one from the array
        violet.pop(0)                       #This allows us to just see the last 50 data points
        blue.pop(0)
        green.pop(0)
        yellow.pop(0)
        orange.pop(0)
        red.pop(0)
