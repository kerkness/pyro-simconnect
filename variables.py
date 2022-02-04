# Create request holders
# These are groups of datapoints which it is convenient to call as a group because they fulfill a specific function
request_location = [
	'ALTITUDE',
	'LATITUDE',
	'LONGITUDE',
	'KOHLSMAN',
]

request_airspeed = [
	'AIRSPEED_TRUE',
	'AIRSPEED_INDICATE',
	'AIRSPEED_TRUE CALIBRATE',
	'AIRSPEED_BARBER POLE',
	'AIRSPEED_MACH',
]

request_compass = [
	'WISKEY_COMPASS_INDICATION_DEGREES',
	'PARTIAL_PANEL_COMPASS',
	'ADF_CARD',  # ADF compass rose setting
	'MAGNETIC_COMPASS',  # Compass reading
	'INDUCTOR_COMPASS_PERCENT_DEVIATION',  # Inductor compass deviation reading
	'INDUCTOR_COMPASS_HEADING_REF',  # Inductor compass heading
]

request_vertical_speed = [
	'VELOCITY_BODY_Y',  # True vertical speed, relative to aircraft axis
	'RELATIVE_WIND_VELOCITY_BODY_Y',  # Vertical speed relative to wind
	'VERTICAL_SPEED',  # Vertical speed indication
	'GPS_WP_VERTICAL_SPEED',  # Vertical speed to waypoint
]

request_fuel = [
	'FUEL_TANK_CENTER_LEVEL',  # Percent of maximum capacity
	'FUEL_TANK_CENTER2_LEVEL',  # Percent of maximum capacity
	'FUEL_TANK_CENTER3_LEVEL',  # Percent of maximum capacity
	'FUEL_TANK_LEFT_MAIN_LEVEL',  # Percent of maximum capacity
	'FUEL_TANK_LEFT_AUX_LEVEL',  # Percent of maximum capacity
	'FUEL_TANK_LEFT_TIP_LEVEL',  # Percent of maximum capacity
	'FUEL_TANK_RIGHT_MAIN_LEVEL',  # Percent of maximum capacity
	'FUEL_TANK_RIGHT_AUX_LEVEL',  # Percent of maximum capacity
	'FUEL_TANK_RIGHT_TIP_LEVEL',  # Percent of maximum capacity
	'FUEL_TANK_EXTERNAL1_LEVEL',  # Percent of maximum capacity
	'FUEL_TANK_EXTERNAL2_LEVEL',  # Percent of maximum capacity
	'FUEL_TANK_CENTER_CAPACITY',  # Maximum capacity in volume
	'FUEL_TANK_CENTER2_CAPACITY',  # Maximum capacity in volume
	'FUEL_TANK_CENTER3_CAPACITY',  # Maximum capacity in volume
	'FUEL_TANK_LEFT_MAIN_CAPACITY',  # Maximum capacity in volume
	'FUEL_TANK_LEFT_AUX_CAPACITY',  # Maximum capacity in volume
	'FUEL_TANK_LEFT_TIP_CAPACITY',  # Maximum capacity in volume
	'FUEL_TANK_RIGHT_MAIN_CAPACITY',  # Maximum capacity in volume
	'FUEL_TANK_RIGHT_AUX_CAPACITY',  # Maximum capacity in volume
	'FUEL_TANK_RIGHT_TIP_CAPACITY',  # Maximum capacity in volume
	'FUEL_TANK_EXTERNAL1_CAPACITY',  # Maximum capacity in volume
	'FUEL_TANK_EXTERNAL2_CAPACITY',  # Maximum capacity in volume
	'FUEL_LEFT_CAPACITY',  # Maximum capacity in volume
	'FUEL_RIGHT_CAPACITY',  # Maximum capacity in volume
	'FUEL_TANK_CENTER_QUANTITY',  # Current quantity in volume
	'FUEL_TANK_CENTER2_QUANTITY',  # Current quantity in volume
	'FUEL_TANK_CENTER3_QUANTITY',  # Current quantity in volume
	'FUEL_TANK_LEFT_MAIN_QUANTITY',  # Current quantity in volume
	'FUEL_TANK_LEFT_AUX_QUANTITY',  # Current quantity in volume
	'FUEL_TANK_LEFT_TIP_QUANTITY',  # Current quantity in volume
	'FUEL_TANK_RIGHT_MAIN_QUANTITY',  # Current quantity in volume
	'FUEL_TANK_RIGHT_AUX_QUANTITY',  # Current quantity in volume
	'FUEL_TANK_RIGHT_TIP_QUANTITY',  # Current quantity in volume
	'FUEL_TANK_EXTERNAL1_QUANTITY',  # Current quantity in volume
	'FUEL_TANK_EXTERNAL2_QUANTITY',  # Current quantity in volume
	'FUEL_LEFT_QUANTITY',  # Current quantity in volume
	'FUEL_RIGHT_QUANTITY',  # Current quantity in volume
	'FUEL_TOTAL_QUANTITY',  # Current quantity in volume
	'FUEL_WEIGHT_PER_GALLON',  # Fuel weight per gallon
	'FUEL_TOTAL_CAPACITY',  # Total capacity of the aircraft
	'FUEL_SELECTED_QUANTITY_PERCENT',  # Percent or capacity for selected tank
	'FUEL_SELECTED_QUANTITY',  # Quantity of selected tank
	'FUEL_TOTAL_QUANTITY_WEIGHT',  # Current total fuel weight of the aircraft
	'NUM_FUEL_SELECTORS',  # Number of selectors on the aircraft
	'UNLIMITED_FUEL',  # Unlimited fuel flag
	'ESTIMATED_FUEL_FLOW',  # Estimated fuel flow at cruise
]

request_flaps = [
	'FLAPS_HANDLE_PERCENT',  # Percent flap handle extended
	'FLAPS_HANDLE_INDEX',  # Index of current flap position
	'FLAPS_NUM_HANDLE_POSITIONS',  # Number of flap positions
	'TRAILING_EDGE_FLAPS_LEFT_PERCENT',  # Percent left trailing edge flap extended
	'TRAILING_EDGE_FLAPS_RIGHT_PERCENT',  # Percent right trailing edge flap extended
	'TRAILING_EDGE_FLAPS_LEFT_ANGLE',  # Angle left trailing edge flap extended. Use TRAILING EDGE FLAPS LEFT PERCENT to set a value.
	'TRAILING_EDGE_FLAPS_RIGHT_ANGLE',  # Angle right trailing edge flap extended. Use TRAILING EDGE FLAPS RIGHT PERCENT to set a value.
	'LEADING_EDGE_FLAPS_LEFT_PERCENT',  # Percent left leading edge flap extended
	'LEADING_EDGE_FLAPS_RIGHT_PERCENT',  # Percent right leading edge flap extended
	'LEADING_EDGE_FLAPS_LEFT_ANGLE',  # Angle left leading edge flap extended. Use LEADING EDGE FLAPS LEFT PERCENT to set a value.
	'LEADING_EDGE_FLAPS_RIGHT_ANGLE',  # Angle right leading edge flap extended. Use LEADING EDGE FLAPS RIGHT PERCENT to set a value.
	'FLAPS_AVAILABLE',  # True if flaps available
	'FLAP_DAMAGE_BY_SPEED',  # True if flagps are damaged by excessive speed
	'FLAP_SPEED_EXCEEDED',  # True if safe speed limit for flaps exceeded
]

request_throttle = [
	'AUTOPILOT_THROTTLE_ARM',  # Autothrottle armed
	'AUTOPILOT_TAKEOFF_POWER_ACTIVE',  # Takeoff / Go Around power mode active
	'AUTOTHROTTLE_ACTIVE',  # Auto-throttle active
	'FULL_THROTTLE_THRUST_TO_WEIGHT_RATIO',  # Full throttle thrust to weight ratio
	'THROTTLE_LOWER_LIMIT',
	'GENERAL_ENG_THROTTLE_LEVER_POSITION:index',  # Percent of max throttle position
	'AUTOPILOT_THROTTLE_ARM',  # Autothrottle armed
	'AUTOTHROTTLE_ACTIVE',  # Auto-throttle active
	'FULL_THROTTLE_THRUST_TO_WEIGHT_RATIO',  # Full throttle thrust to weight ratio
]

request_gear = [
	'IS_GEAR_RETRACTABLE',  # True if gear can be retracted
	'IS_GEAR_SKIS',  # True if landing gear is skis
	'IS_GEAR_FLOATS',  # True if landing gear is floats
	'IS_GEAR_SKIDS',  # True if landing gear is skids
	'IS_GEAR_WHEELS',  # True if landing gear is wheels
	'GEAR_HANDLE_POSITION',  # True if gear handle is applied
	'GEAR_HYDRAULIC_PRESSURE',  # Gear hydraulic pressure
	'TAILWHEEL_LOCK_ON',  # True if tailwheel lock applied
	'GEAR_CENTER_POSITION',  # Percent center gear extended
	'GEAR_LEFT_POSITION',  # Percent left gear extended
	'GEAR_RIGHT_POSITION',  # Percent right gear extended
	'GEAR_TAIL_POSITION',  # Percent tail gear extended
	'GEAR_AUX_POSITION',  # Percent auxiliary gear extended
	'GEAR_TOTAL_PCT_EXTENDED',  # Percent total gear extended
	'AUTO_BRAKE_SWITCH_CB',  # Auto brake switch position
	'WATER_RUDDER_HANDLE_POSITION',
	'WATER_LEFT_RUDDER_EXTENDED',  # Percent extended
	'WATER_RIGHT_RUDDER_EXTENDED',  # Percent extended
	'GEAR_CENTER_STEER_ANGLE',  # Center wheel angle, negative to the left, positive to the right.
	'GEAR_LEFT_STEER_ANGLE',  # Left wheel angle, negative to the left, positive to the right.
	'GEAR_RIGHT_STEER_ANGLE',  # Right wheel angle, negative to the left, positive to the right.
	'GEAR_AUX_STEER_ANGLE',  # Aux wheel angle, negative to the left, positive to the right. The aux wheel is the fourth set of gear, sometimes used on helicopters.
	'WATER_LEFT_RUDDER_STEER_ANGLE',  # Water left rudder angle, negative to the left, positive to the right.
	'WATER_RIGHT_RUDDER_STEER_ANGLE',  # Water right rudder angle, negative to the left, positive to the right.
	'GEAR_CENTER_STEER_ANGLE_PCT',  # Center steer angle as a percentage
	'GEAR_LEFT_STEER_ANGLE_PCT',  # Left steer angle as a percentage
	'GEAR_RIGHT_STEER_ANGLE_PCT',  # Right steer angle as a percentage
	'GEAR_AUX_STEER_ANGLE_PCT',  # Aux steer angle as a percentage
	'WATER_LEFT_RUDDER_STEER_ANGLE_PCT',  # Water left rudder angle as a percentage
	'WATER_RIGHT_RUDDER_STEER_ANGLE_PCT',  # Water right rudder as a percentage
	'CENTER_WHEEL_RPM',  # Center landing gear rpm
	'LEFT_WHEEL_RPM',  # Left landing gear rpm
	'RIGHT_WHEEL_RPM',  # Right landing gear rpm
	'AUX_WHEEL_RPM',  # Rpm of fourth set of gear wheels.
	'CENTER_WHEEL_ROTATION_ANGLE',  # Center wheel rotation angle
	'LEFT_WHEEL_ROTATION_ANGLE',  # Left wheel rotation angle
	'RIGHT_WHEEL_ROTATION_ANGLE',  # Right wheel rotation angle
	'AUX_WHEEL_ROTATION_ANGLE',  # Aux wheel rotation angle
	'GEAR_EMERGENCY_HANDLE_POSITION',  # True if gear emergency handle applied
	'ANTISKID_BRAKES_ACTIVE',  # True if antiskid brakes active
	'RETRACT_FLOAT_SWITCH',  # True if retract float switch on
	'RETRACT_LEFT_FLOAT_EXTENDED',  # If aircraft has retractable floats.
	'RETRACT_RIGHT_FLOAT_EXTENDED',  # If aircraft has retractable floats.
	'STEER_INPUT_CONTROL',  # Position of steering tiller
	'GEAR_DAMAGE_BY_SPEED',  # True if gear has been damaged by excessive speed
	'GEAR_SPEED_EXCEEDED',  # True if safe speed limit for gear exceeded
	'NOSEWHEEL_LOCK_ON',  # True if the nosewheel lock is engaged.
]

request_trim = [
	'ROTOR_LATERAL_TRIM_PCT',  # Trim percent
	'ELEVATOR_TRIM_POSITION',  # Elevator trim deflection
	'ELEVATOR_TRIM_INDICATOR',
	'ELEVATOR_TRIM_PCT',  # Percent elevator trim
	'AILERON_TRIM',  # Angle deflection
	'AILERON_TRIM_PCT',  # The trim position of the ailerons. Zero is fully retracted.
	'RUDDER_TRIM_PCT',  # The trim position of the rudder. Zero is no trim.
	'RUDDER_TRIM',  # Angle deflection
]

request_autopilot = [
	'AUTOPILOT_MASTER',
	'AUTOPILOT_AVAILABLE',
	'AUTOPILOT_NAV_SELECTED',
	'AUTOPILOT_WING_LEVELER',
	'AUTOPILOT_NAV1_LOCK',
	'AUTOPILOT_HEADING_LOCK',
	'AUTOPILOT_HEADING_LOCK_DIR',
	'AUTOPILOT_ALTITUDE_LOCK',
	'AUTOPILOT_ALTITUDE_LOCK_VAR',
	'AUTOPILOT_ATTITUDE_HOLD',
	'AUTOPILOT_GLIDESLOPE_HOLD',
	'AUTOPILOT_PITCH_HOLD_REF',
	'AUTOPILOT_APPROACH_HOLD',
	'AUTOPILOT_BACKCOURSE_HOLD',
	'AUTOPILOT_VERTICAL_HOLD_VAR',
	'AUTOPILOT_PITCH_HOLD',
	'AUTOPILOT_FLIGHT_DIRECTOR_ACTIVE',
	'AUTOPILOT_FLIGHT_DIRECTOR_PITCH',
	'AUTOPILOT_FLIGHT_DIRECTOR_BANK',
	'AUTOPILOT_AIRSPEED_HOLD',
	'AUTOPILOT_AIRSPEED_HOLD_VAR',
	'AUTOPILOT_MACH_HOLD',
	'AUTOPILOT_MACH_HOLD_VAR',
	'AUTOPILOT_YAW_DAMPER',
	'AUTOPILOT_RPM_HOLD_VAR',
	'AUTOPILOT_THROTTLE_ARM',
	'AUTOPILOT_TAKEOFF_POWER ACTIVE',
	'AUTOTHROTTLE_ACTIVE',
	'AUTOPILOT_VERTICAL_HOLD',
	'AUTOPILOT_RPM_HOLD',
	'AUTOPILOT_MAX_BANK',
	'FLY_BY_WIRE_ELAC_SWITCH',
	'FLY_BY_WIRE_FAC_SWITCH',
	'FLY_BY_WIRE_SEC_SWITCH',
	'FLY_BY_WIRE_ELAC_FAILED',
	'FLY_BY_WIRE_FAC_FAILED',
	'FLY_BY_WIRE_SEC_FAILED'
]

request_cabin = [
	'CABIN_SEATBELTS_ALERT_SWITCH',
	'CABIN_NO_SMOKING_ALERT_SWITCH'
]