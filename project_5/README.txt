Project 5 ReadMe.txt
Andrew Trick
andyjtrick@gmail.com


-------
Summary
-------
The dataset used was a cleaned-up version of data obtained by scraping www.songkick.com for the show history of my band: 'The Devil Wears Prada'. TDWP is a metal band, currently based out of Chicago, IL., that has been playing shows since 2006.  I was intrigued to discover what states we have played the most and what places we may have continuously passed by, while also seeing the yearly differences. I decided a choropleth of the states was the best option to view this data in an interesting and interactive way.



------
Design
------
Several decisions of the design of the visuals were chosen with aesthetics in mind. I chose AlbersUsa because I believe it is the most appealing display of the US out of the d3 map libraries available.  The borders around the map and between the states are pointless aside from elevating to the visuals of the display.  Count split's were chosen at the specified numbers based off the overall counts of each state;  0's and 1's were of a frequency that it was appropriate to give each their own category. Colorbrewer2.org was used to find a color range that worked well together. Year buttons were chose to easily see the difference between each year.
	
Many critiques I recieved in my feedback helped me make further design decisions.  As suggested, the zoom was unnecessary and I opted to cut it.  I also edited the tooltip to leave a plainer tooltip (year and total) above the border while adding a second, state-based, popup tooltip closer to the map.  Finally,  I changed the title to be more specific, found a font family that was more appropriate, and added links to the band webpage and sonkick site.



--------
Feedback
--------	
Chris Danson
    -return to full map view if zoomed and changing year.
    -have button highlighted at load
    -change to start at 2006
	
Courtney Wachs
    -change title
    -change font
    -cut zoom (useless)

Lucas Frazier
    -BUG: double clicking state from state is wrong
    -get rid of box and color around tooltip
    -link tdwp to band page



---------
Resources
---------
Russia Choropleth Example
-http://bl.ocks.org/KoGor/5685876

Zoom Map Example
-http://bl.ocks.org/mbostock/2206590

More Examples
-https://github.com/mbostock/d3/wiki/Gallery

Color Choices
-http://colorbrewer2.org/
