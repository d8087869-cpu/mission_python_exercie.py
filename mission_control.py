# number 2 
agent_name = "david" 
mission_code = 147
distance_to_target = 5.5
mission_active_status = False 
print(f"agent name{agent_name},mission code{mission_code},distance to target{distance_to_target} , mission active status{mission_active_status}")
#number 4 
print(type(agent_name))
print(type(mission_code))
print(type(distance_to_target))
print(type(mission_active_status))
#number 5 
base_to_target_and_back = distance_to_target*2 
print(f"base to target and back {base_to_target_and_back}")
# number 6 
fuel_usage = 3
fuel_usage = int(fuel_usage)
fuel_usaeg_for_mission = base_to_target_and_back*fuel_usage
print(f"fuel usaeg for mission{fuel_usaeg_for_mission}")
#number 7 
total_fuel = 50
total_fuel = int(total_fuel)
total_fule_after_mission = total_fuel - fuel_usaeg_for_mission
print(f"total feul after mission {total_fule_after_mission}")
#number 8 
time = input("in how many minute the mission starts")
time=int(time)
print(f"the mission start in {time*60}-seconds")
print(f"the mission starts in {time}-minute")
print(f"the mission strats in {time/60}-hours")
#nymber 9 
km_into_mile = input("enter distance")
km_into_mile = int(km_into_mile)
mile = km_into_mile/1.6
print(f"distance_in_mile{mile}") 
