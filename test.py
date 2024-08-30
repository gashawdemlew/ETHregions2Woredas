from ETHregions2Woredas import (
    get_all_regions,
    get_all_zones,
    get_zones_by_region,
    get_woredas_by_zone,
    get_woredas_by_region,
    get_woredas_by_region_and_zone,
    get_region_by_woreda,
    get_region_by_zone,
    get_zone_by_woreda,
    get_all_woredas
)

# Example usage
#print(get_all_regions())
print(get_zones_by_region('Addis Ababa'))
# print(get_woredas_by_region('Addis Ababa'))
#print(get_all_zones())

#print(get_woredas_by_region_and_zone('Addis Ababa', "Arada sub-city"))

#print(get_region_by_woreda("Arat Kilo"))

# print(get_region_by_zone("Arada sub-city"))

# print(get_zone_by_woreda("Arat Kilo"))

#print(get_all_woredas())