def availability(planned_minutes, downtime_minutes):
    run_time = planned_minutes - downtime_minutes
    return run_time/ planned_minutes
print(availability(450, 45))

