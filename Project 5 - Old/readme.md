Project 5 ReadMe.txt  
Andrew Trick  
andyjtrick@gmail.com  


--------
Summary
--------
The dataset used was a cleaned-up version of data obtained by scraping www.songkick.com for the show history of my band: 'The Devil Wears Prada'. TDWP is a metal band currently based out of Chicago, IL that has been playing shows since 2006.  It was exciting to discover that we have played California and Texas far more than any other state while also learning that we continuously pass by other states such as Maine and the Dakota's. I decided a choropleth of the states was the best option to view this data in an interesting and interactive way, but also plotted a line graph of the totals per year.  This minor addition of the line plot allowed me to easily discern the difference in shows yearly and discover that 2010 and 2011 saw more shows than the norm.



-------
Design
-------
Several decisions of the design of the visuals were chosen with aesthetics in mind. While I could have displayed this data in a large bar chart or even a simple table,  I believe a choropleth is the most interesting way to view the data.  It allows a viewer to quickly look at the map and distinguish which states were frequently visited and which were not.I chose AlbersUsa because I believe it is the most appealing display of the US out of the d3 map libraries available. The borders around the map and between the states are pointless aside from elevating to the visuals of the display.  Count split's were chosen at the specified numbers based off the overall counts of each state;  0's and 1's were of a frequency that it was appropriate to give each their own category. Colorbrewer2.org was used to find a color range that worked well together. 

Year buttons were chosen to easily see the difference between each year. I thought a button interaction would be a good choice so as to give the viewer the ability to move throughout the years as they wished while also being able to provide the particular story of our travels as the band progressed through the years.  Althought there is a legend provided,  I felt this did not provide as descriptive of information as I initially wanted; I therefore added a hover tooltip on the map to inform the viewer what the exact number for that state was. 
	
Many critiques I recieved in my feedback helped me make further design decisions.  As suggested, the zoom was unnecessary and I opted to cut it.  I also edited the tooltip to leave a plainer tooltip (year and total) above the border while adding a second, state-based, popup tooltip closer to the map.  Finally,  I changed the title to be more specific, found a font family that was more appropriate, and added links to the band webpage and sonkick site.

After my initial submission I made more edits based on the coach feedback. I changed the colors to give an easier difference by view.  Minor tweaks to the code were made to help effectiveness: Primarily adding html tags and replacement of my meta tag. Adding opacity to the states when hovering was making it difficult to connect legend and state.  I alleviated this by cutting the opacity and applying a stroke color when hovering that provides the highlight needed.  Along with adding a 'total' button and choropleth view, I also attatched a line graph of the total shows per year onto the page.  This line plot give a quick reference to the band's show frequency throughout the years.



---------
Feedback
---------	
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
  


-------------------
Feedback - round 2
-------------------  
Jeremy DePoyster  
    -change color away from browns  
  
First Submission Review  
    -fix meta placement  
    -separate css into separate file  
    -needs html tags  
    -shading of state on hover may misrepresent color and legend  
    -add total button for all years  
    -represent total with bar or line chart  
    -plot cities or venues  
    -consider separating view and content (MVC)  
    -use final suffix for latest version  
    -readme to be a .md not .txt  
  
  
  
-------------------
Feedback - round 3
-------------------    
Second Submission Review  
    -You're essentially plotting all of the data and letting the user play around with it.  
	-if you had included the 'Summary' section of the README.md file as part of your html file, it would make the chart closer to being explanatory.  
	-If you had included this paragraph above your charts, at least then I would know that you're trying to point out that you're more popular in California and Texas than in Maine.  
  
    
	  
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

line graph  
-https://gist.github.com/d3noob/4414436