import folium
from geopy import distance

from ip2geotools_locator.utils import logger

class FoliumMap:
    """
    Class for creating Folium maps.
    """
    markers = []
    poly_lines = []
    FORMATTED_STRING= "<b>IP: %s</b><p>Country: %s</p><p>City: %s</p><p>Location: %.3f N, %.3f E</p>"

    @classmethod
    def add_marker_noncommercial(cls, name, ip_address, country, city, latitude, longitude):
        """This method creates marker for noncommercial database"""
        
        try:
            # Adding debug record
            logger.info("%s: Adding Marker for noncommercial DB %s" % (__name__, name))
            # append Folium Marker into class variable
            cls.markers.append(folium.Marker([latitude, longitude], popup=cls.FORMATTED_STRING % (ip_address, country, city, latitude, longitude), 
            icon=folium.Icon(color='green'), tooltip=name))

        except TypeError as e:
            # Invalid values are skipped
            logger.warning("%s: TypeError: %s. Marker from %s DB skipped." % (__name__, str(e), name))
            pass
    
    @classmethod
    def add_marker_commercial(cls, name, ip_address, country, city, latitude, longitude):
        """This method creates marker for commercial database"""
        
        try:
            # Adding debug record
            logger.info("%s: Adding Marker for commercial DB %s" % (__name__, name))
            # append Folium Marker into class variable
            cls.markers.append(folium.Marker([latitude, longitude], popup=cls.FORMATTED_STRING % (ip_address, country, city, latitude, longitude), 
            icon=folium.Icon(color='red'), tooltip=name))
        except TypeError as e:
            # Invalid values are skipped
            logger.warning("%s: TypeError: %s. Marker from %s DB skipped." % (__name__, str(e), name))
            pass
    
    @classmethod
    def add_calculated_marker(cls, name, ip_address, latitude, longitude):
        """This method creates marker for calculated location"""

        try:
            # Adding debug record
            logger.info("%s: Adding Marker for %s calculation method" % (__name__, name))
            # append Folium Marker into class variable
            cls.markers.append(folium.Marker([latitude, longitude], popup="<p><b>%s</b> location of IP: %s is:</p><p>%f N %f E</p>" % (name, ip_address, latitude, longitude), 
            icon=folium.Icon(color='blue', icon='screenshot'), tooltip=name))
        except TypeError as e:
            # Invalid values are skipped
            logger.warning("%s: TypeError: %s. Marker from %s method skipped." % (__name__, str(e), name))
            pass

    @classmethod
    def add_poly_lines(cls, locations, calculated_locations):
        """Method for creating Folium PolyLines"""
        
        # Add polylines from each calculated location
        for calculated_loc in calculated_locations:
            logger.info("%s: Creating Folium PolyLines for %s" % (__name__, str(calculated_loc)))
            # For each DB location
            for loc in locations:
                try:
                    # Calculate distance between coordinates
                    dist = distance.distance(loc, calculated_loc).km
                    # Add Folium PolyLine
                    cls.poly_lines.append(folium.PolyLine([loc, calculated_loc], tooltip = "Distance: %.3f km" % dist, weight=3, opacity=1))
                
                except TypeError as e:
                    #Invalid values are skipped
                    logger.warning("%s: TypeError: %s. PolyLine skipped." % (__name__, str(e)))
                    pass

    @classmethod  
    def generate_map(cls, center_location=[], file_name="locations"):
        """Method for generating map file."""
        try:
            # Create Folium map object
            map = folium.Map([center_location.latitude, center_location.longitude])
            
            # Add all markers to map
            logger.debug("%s: Adding Markers into map." % (__name__))
            for marker in cls.markers:
                marker.add_to(map)

            # Add all PolyLines to map
            logger.debug("%s: Adding PolyLines into map." % (__name__))
            for line in cls.poly_lines:
                line.add_to(map)
            
            # Save map in html format
            logger.info("%s: Generating map file %s.html" % (__name__, file_name))
            map.save(str(file_name)+".html")
        except TypeError as e:
            logger.error("%s: Error when creating map file! TypeError: %s" % (__name__, str(e)))
            pass