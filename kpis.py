def availability(planned_minutes, downtime_minutes):
    run_time = planned_minutes - downtime_minutes
    return run_time/ planned_minutes
# print(availability(450, 45))


def quality(good_units, total_units) :
    return good_units/ total_units
# print(quality(380,400))


def performance(ideal_cycle_time, total_units, run_time) :
    return (ideal_cycle_time * total_units) / run_time
# print(performance(1, 400, 420))


def oee (availability_value , performance_value , quality_value) : 
    return availability_value * performance_value * quality_value
# print (oee(0.9, 0.95, 0.95))
# print (round(oee(0.9, 0.95, 0.95), 4))


def line_oee (planned_minutes, downtime_minutes, ideal_cycle_time, total_units, good_units) :
    run_time = planned_minutes - downtime_minutes
    a = availability (planned_minutes, downtime_minutes)
    p = performance (ideal_cycle_time, total_units, run_time)
    q = quality (good_units, total_units)
    return round (oee (a, p, q), 4)
# print (line_oee(480, 60, 1, 400, 380))


planned_list = [480, 450, 600]
for minutes in planned_list :
    print (minutes)


for minutes in planned_list :
    print (availability(minutes, 60))


for minutes in planned_list :
    a= availability(minutes, 60)
    if a < 0.88 :
        print(minutes, "low availability", round(a, 3))