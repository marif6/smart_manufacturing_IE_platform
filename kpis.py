def availability(planned_minutes, downtime_minutes):
    run_time = planned_minutes - downtime_minutes
    return run_time/ planned_minutes
print(availability(450, 45))


def quality(good_units, total_units) :
    return good_units/ total_units
print(quality(380,400))


def performance(ideal_cycle_time, total_units, run_time) :
    return (ideal_cycle_time * total_units) / run_time
print(performance(1, 400, 420))


def oee (availability_value , performance_value , quality_value) : 
    return availability_value * performance_value * quality_value
print (oee(0.9, 0.95, 0.95))