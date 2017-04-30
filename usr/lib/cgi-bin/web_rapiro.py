#!/usr/bin/env python

import time, serial, subprocess
from curses import ascii
import cgi
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

print "Content-type: text/html\n\n"


if "Submit6" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#M5")
elif "Submit3" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#M0")
elif "Submit1" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#M1")
elif "Submit2" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#M3")
elif "Submit4" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#M4")
elif "Submit5" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#M2")
elif "Submit7" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#M6")
elif "Submit8" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#M7")
elif "Submit9" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#M8")
elif "Submit10" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#M9")
elif "Submit11" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#H")
elif "Submit16" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#PS07A110T010")
elif "Submit12" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#PS05A000T010")
elif "Submit14" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#PS05A090T010")
elif "Submit13" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#PS02A180T010")
elif "Submit15" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#PS02A090T010")
elif "Submit18" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#PS07A090T010")
elif "Submit17" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#PS04A070T010")
elif "Submit19" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#PS04A090T010")
elif "Submit20" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#PS00A135T010")
elif "Submit21" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#PS00A045T010")
elif "Submit22" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#PR000G000B000T001")
elif "Submit23" in form:
    #subprocess.call("mpg321 MrRoboto_loop.mp3", shell=True)
    process = subprocess.Popen(['mpg321', 'MrRoboto_loop.mp3'])
    subprocess.call("python roboto.py", shell=True)
    #subprocess.call("python roboto.py", shell=True)
elif "Submit24" in form:
    subprocess.call('python gmail-cron.py', shell=True)
elif "TTS" in form:
    rate = form.getvalue('rate')
    lang = form.getvalue('language')
    sms = form.getvalue('txtText')
    subprocess.call('python rsstts.py %s %s "%s"' % (rate, lang, sms), shell=True)
#	print form.getvalue('ddlLanguage')
else:
    print "Error"

print """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
 	<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<link rel="stylesheet" type="text/css" href="/css/control.css">
        <link rel="stylesheet" href="/css/style_minified.css" />
        <link rel="stylesheet" href="/css/es_Default.css" />
        <script src="/js/style_minified.js"></script>
        <script src="/js/script.js"></script>
        <script src="/js/pipan.js"></script>
	</head>
   <body onload="setTimeout('init();', 100);">
    <center>
         <h1>RaPiRo Cam</h1>
         <div><img id="mjpeg_dest"  onclick="toggle_fullscreen(this);" src="/loading.jpg"></div>
         <div id="main-buttons" style="display:block;" >
            <input id="video_button" type="button" class="btn btn-primary">
            <input id="image_button" type="button" class="btn btn-primary">
            <input id="timelapse_button" type="button" class="btn btn-primary">
            <input id="md_button" type="button" class="btn btn-primary">
            <input id="halt_button" type="button" class="btn btn-danger">
         </div>

       <div id="secondary-buttons" class="container-fluid text-center" style="display:block;" >
         <a href="/preview.php" class="btn btn-default">Download Videos and Images</a>
         <a href="/motion.php" class="btn btn-default">Edit motion settings</a>
         <a href="/schedule.php" class="btn btn-default">Edit schedule settings</a>
       </div>

       <form action="/cgi-bin/web_rapiro.py" method="post">
	<table width="100%" border="1">
  	<tr>
	    <td><div class="submit23"> <INPUT type="submit" value=" " name="Submit23" /></div></td>
  	    <td><div class="submit20"><INPUT type="submit" value=" " name="Submit20" /></div></td>
	    <td><div class="submit1"><INPUT type="submit" value=" " name="Submit1" /></div></td>
	    <td><div class="submit21"><INPUT type="submit" value=" " name="Submit21" /></div></td>
	    <td><div class="submit24"> <INPUT type="submit" value=" " name="Submit24" /></div></td>
 	</tr>
 	<tr>
 	  <td>&nbsp;</td>
            <td><div class="submit2"><INPUT type="submit" value=" " name="Submit2" /></div></td>
   	    <td><div class="submit3"><INPUT type="submit" value=" " name="Submit3" /></div></td>
            <td><div class="submit4"><INPUT type="submit" value=" " name="Submit4" /></div></td>
            <td>&nbsp;</td>
  	</tr>
  	<tr>
  	  <td>&nbsp;</td>
   	    <td>&nbsp;</td>
    	    <td><div class="submit5"><INPUT type="submit" value=" " name="Submit5" /></div></td>
 	    <td>&nbsp;</td>
 	    <td>&nbsp;</td>
	</tr>
	<tr>
	  <td><div class="submit6"><INPUT type="submit" name="Submit6" value=" "/></div></td>
	    <td><div class="submit7"><INPUT type="submit" name="Submit7" value=" "/></div></td>
	    <td><div class="submit8"><INPUT type="submit" name="Submit8" value=" "/></div></td>
	    <td><div class="submit9"><INPUT type="submit" name="Submit9" value=" "/></div></td>
	    <td><div class="submit10"><INPUT type="submit" name="Submit10" value=" "/></div></td>
	</tr>
	<tr>
	  <td><div class="submit12"><INPUT type="submit" name="Submit12" value=" "/></div></td>
	  <td><div class="submit14"><INPUT type="submit" name="Submit14" value=" "/></div></td>
	  <td><div class="submit22"><INPUT type="submit" name="Submit22" value=" "/></div></td>
	  <td><div class="submit13"><INPUT type="submit" name="Submit13" value=" "/></div></td>
	  <td><div class="submit15"><INPUT type="submit" name="Submit15" value=" "/></div></td>
	  </tr>
	<tr>
	  <td><div class="submit16"><INPUT type="submit" name="Submit16" value=" "/></div></td>
	  <td><div class="submit18"><INPUT type="submit" name="Submit18" value=" "/></div></td>
	  <td><div class="submit11"><INPUT type="submit" name="Submit11" value=" "/></div></td>
	  <td><div class="submit17"><INPUT type="submit" name="Submit17" value=" "/></div></td>
	  <td><div class="submit19"><INPUT type="submit" name="Submit19" value=" "/></div></td>
	  </tr>
	</table>


	<table width="100%">
	<tr>
	  <td align="center">
	  	<textarea name="txtText" rows="7" style="width:60%" class="text_box">text to speech</textarea>
		<br>
	  	<select name="rate" style="vertical-align: top; "width: 10px" class="text_box">
	  		<option value="">- Select Speed -</option>
                	<option value="-10">-10</option>
                	<option value="-9">-9</option>
                	<option value="-8">-8</option>
                	<option value="-7">-7</option>
                	<option value="-6">-6</option>
                	<option value="-5">-5</option>
                	<option value="-4">-4</option>
                	<option value="-3">-3</option>
                	<option value="-2">-2</option>
                	<option value="-1">-1</option>
                	<option selected="selected" value="0">0</option>
                	<option value="1">1</option>
                	<option value="2">2</option>
                	<option value="3">3</option>
                	<option value="4">4</option>
                	<option value="5">5</option>
                	<option value="6">6</option>
                	<option value="7">7</option>
                	<option value="8">8</option>
                	<option value="9">9</option>
                	<option value="10">10</option>
		</select>
	  	<select name="language" style="vertical-align: top; "width: 200px" class="text_box">
	  		<option value="">------- Select language -------</option>
                	<option value="ca-es">Catalan</option>
                	<option value="zh-cn">Chinese (China)</option>
	                <option value="zh-hk">Chinese (Hong Kong)</option>
        	        <option value="zh-tw">Chinese (Taiwan)</option>
                	<option value="da-dk">Danish</option>
	                <option value="nl-nl">Dutch</option>
        	        <option value="en-au">English (Australia)</option>
                	<option value="en-ca">English (Canada)</option>
	                <option value="en-gb">English (Great Britain)</option>
        	        <option value="en-in">English (India)</option>
                	<option selected="selected" value="en-us">English (United States)</option>
	                <option value="fi-fi">Finnish</option>
        	        <option value="fr-ca">French (Canada)</option>
                	<option value="fr-fr">French (France)</option>
	                <option value="de-de">German</option>
        	        <option value="it-it">Italian</option>
                	<option value="ja-jp">Japanese</option>
	                <option value="ko-kr">Korean</option>
        	        <option value="nb-no">Norwegian</option>
                	<option value="pl-pl">Polish</option>
	                <option value="pt-br">Portuguese (Brazil)</option>
        	        <option value="pt-pt">Portuguese (Portugal)</option>
                	<option value="ru-ru">Russian</option>
	                <option value="es-mx">Spanish (Mexico)</option>
        	        <option value="es-es">Spanish (Spain)</option>
                	<option value="sv-se">Swedish (Sweden)</option>
                </select>
	  	<input type="submit" name="TTS" value="Speech Text"/>
	  </td>
	  </tr>
	</table>
        </form>
	</body>
	</html>"""
