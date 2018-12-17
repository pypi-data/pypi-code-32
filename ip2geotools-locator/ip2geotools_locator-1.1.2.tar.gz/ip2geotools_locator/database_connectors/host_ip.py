from ip2geotools.databases.noncommercial import HostIP
from ip2geotools.errors import LocationError, IpAddressNotFoundError, PermissionRequiredError, InvalidRequestError, InvalidResponseError, ServiceError, LimitExceededError

from ip2geotools_locator.folium_map import FoliumMap
from ip2geotools_locator.utils import *



class HostIpDB:
    """
    Class for handling DB connection into HostIP Database
    """
    # Instance of map for placing markers
    m = FoliumMap()
    __db_data = None
    
    def __init__(self):
        # Special config
        pass        

    def get_location(self, ip):
        """
        Rethrieves location for given IP address from HostIP database
        Validation and exception handling included.
        """
        try:
            # Try to get and return location
            self.__db_data = HostIP.get(ip)
            logger.info("%s: DB returned location %.3f N, %.3f E" % (__name__, self.__db_data.latitude, self.__db_data.longitude))
            return Location(self.__db_data.latitude, self.__db_data.longitude)
       
        except IpAddressNotFoundError as e:
            # Handling for IpAddressNotFoundError exception
            logger.warning("%s: Database could not find IP address. IpAddressNotFoundError: %s " % (__name__, str(e))) 
        
        except PermissionRequiredError as e:
            # Handling for PermissionRequiredError exception
            logger.critical("%s: Additional setings required for DB. PermissionRequiredError: %s " % (__name__, str(e)))

        except ServiceError as e:
            # Handling for ServiceError exception
            logger.error("%s: Service is unavailable. ServiceError: %s " % (__name__, str(e))) 
        
        except LimitExceededError as e:
            # Handling for LimitExceededError exception
            logger.warning("%s: LimitExceededError: %s " % (__name__, str(e)))     

        except (LocationError, InvalidRequestError, InvalidResponseError) as e:
            # Handling for invalid data, request and response exception
            logger.error("%s: returned %s " % (__name__, str(e.__class__))) 

        except TypeError as e:
            # Handling for TypeError exception (in case of database returning None values)
            logger.warning("%s: DB returned invalid values. TypeError: %s " % (__name__, str(e)))     
        
    def add_to_map(self):
        """
        Add Folium Marker to map
        Call get_location(ip) method before adding any markers to map
        """
        try:
            logger.debug("%s: Calling add_marker method for %s DB" % (__name__, HostIP.__name__))
            self.m.add_marker_noncommercial(HostIP.__name__, 
                self.__db_data.ip_address, 
                self.__db_data.country, 
                self.__db_data.city, 
                self.__db_data.latitude, 
                self.__db_data.longitude)
        except AttributeError as e:
            # Handling for AttributeError exception (in case of database returning None values)
            logger.warning("%s: Cannot add empty marker %s " % (__name__, str(e)))