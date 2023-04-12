# Kasa Light Controls
<h2>This repo is a work in progress.</h2>
<h2>Changes are needed to bring it up to repo standards. See Issues.</h2>
<p>These scripts are using the briandorey/tp-link-LB130-Smart-Wi-Fi-Bulb repo to create unique home lighting patterns.</p>
<p>Other brand smart lights included a 'disco' mode which would switch light colors quickly. Since this function was not available
with Kasa lights I was able to create the necessary code to add the functionality.</p>
<p>Some of the additional modes I added were:</p>
<ul>
<li>Breathing mode: Lights stay on a specific color and the brightness is slowly raised and lowered.</li>
<li>Random cycle mode: All the lights change colors randomly.</li>
<li>Chase mode: Uses two colors. One light is one color, the rest are the other color. The single color moves positions based on location, such as in a circle around the perimerer.</li>
<li>Crypto price indicator: Red Green and Neutral colors based on candlesticks.</li>
<li>Panic mode: Red/Blue flashing lights.</li>
</ul>
<h3>Installation:</h3>
<ul>
  <li>Clone briandorey/tp-link-LB130-Smart-Wi-Fi-Bulb</li>
  <li>Clone this repo into the same directory</li>
  <li>Run setup.py and set the LAN ip addresses of your lights.</li>
  <li>Run the Lights.py file which selects the group of lights you want to control.</li>
  <p>This will run the List.py file for your selection.</p>
</ul>
<p>Some files are not include here as they are duplicates used to control different groups of lights. A better method should be developed and implimented for general use.</p>
