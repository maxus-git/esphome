"""Constants used by esphome."""

__version__ = "2022.3.0b1"

ALLOWED_NAME_CHARS = "abcdefghijklmnopqrstuvwxyz0123456789-_"

PLATFORM_ESP32 = "esp32"
PLATFORM_ESP8266 = "esp8266"

TARGET_PLATFORMS = [PLATFORM_ESP32, PLATFORM_ESP8266]

SOURCE_FILE_EXTENSIONS = {".cpp", ".hpp", ".h", ".c", ".tcc", ".ino"}
HEADER_FILE_EXTENSIONS = {".h", ".hpp", ".tcc"}
SECRETS_FILES = {"secrets.yaml", "secrets.yml"}


CONF_ABOVE = "above"
CONF_ACCELERATION = "acceleration"
CONF_ACCELERATION_X = "acceleration_x"
CONF_ACCELERATION_Y = "acceleration_y"
CONF_ACCELERATION_Z = "acceleration_z"
CONF_ACCURACY = "accuracy"
CONF_ACCURACY_DECIMALS = "accuracy_decimals"
CONF_ACTION_ID = "action_id"
CONF_ACTION_STATE_TOPIC = "action_state_topic"
CONF_ACTIVE_POWER = "active_power"
CONF_ADDRESS = "address"
CONF_ADDRESSABLE_LIGHT_ID = "addressable_light_id"
CONF_ADVANCED = "advanced"
CONF_AFTER = "after"
CONF_ALPHA = "alpha"
CONF_ALTITUDE = "altitude"
CONF_AND = "and"
CONF_AP = "ap"
CONF_APPARENT_POWER = "apparent_power"
CONF_ARDUINO_VERSION = "arduino_version"
CONF_ARGS = "args"
CONF_ASSUMED_STATE = "assumed_state"
CONF_AT = "at"
CONF_ATTENUATION = "attenuation"
CONF_ATTRIBUTE = "attribute"
CONF_AUTH = "auth"
CONF_AUTO_CLEAR_ENABLED = "auto_clear_enabled"
CONF_AUTO_MODE = "auto_mode"
CONF_AUTOCONF = "autoconf"
CONF_AUTOMATION_ID = "automation_id"
CONF_AVAILABILITY = "availability"
CONF_AWAY = "away"
CONF_AWAY_COMMAND_TOPIC = "away_command_topic"
CONF_AWAY_CONFIG = "away_config"
CONF_AWAY_STATE_TOPIC = "away_state_topic"
CONF_BACKLIGHT_PIN = "backlight_pin"
CONF_BASELINE = "baseline"
CONF_BATTERY_LEVEL = "battery_level"
CONF_BATTERY_VOLTAGE = "battery_voltage"
CONF_BAUD_RATE = "baud_rate"
CONF_BEEPER = "beeper"
CONF_BELOW = "below"
CONF_BINARY = "binary"
CONF_BINARY_SENSOR = "binary_sensor"
CONF_BINARY_SENSORS = "binary_sensors"
CONF_BINDKEY = "bindkey"
CONF_BIRTH_MESSAGE = "birth_message"
CONF_BIT_DEPTH = "bit_depth"
CONF_BLOCK = "block"
CONF_BLUE = "blue"
CONF_BOARD = "board"
CONF_BOARD_FLASH_MODE = "board_flash_mode"
CONF_BORDER = "border"
CONF_BRANCH = "branch"
CONF_BRIGHTNESS = "brightness"
CONF_BROKER = "broker"
CONF_BSSID = "bssid"
CONF_BUFFER_SIZE = "buffer_size"
CONF_BUILD_PATH = "build_path"
CONF_BUS_VOLTAGE = "bus_voltage"
CONF_BUSY_PIN = "busy_pin"
CONF_BYTES = "bytes"
CONF_CALCULATED_LUX = "calculated_lux"
CONF_CALIBRATE_LINEAR = "calibrate_linear"
CONF_CALIBRATION = "calibration"
CONF_CAPACITANCE = "capacitance"
CONF_CAPACITY = "capacity"
CONF_CARRIER_DUTY_PERCENT = "carrier_duty_percent"
CONF_CARRIER_FREQUENCY = "carrier_frequency"
CONF_CERTIFICATE = "certificate"
CONF_CERTIFICATE_AUTHORITY = "certificate_authority"
CONF_CHANGE_MODE_EVERY = "change_mode_every"
CONF_CHANNEL = "channel"
CONF_CHANNELS = "channels"
CONF_CHIPSET = "chipset"
CONF_CLEAR_IMPEDANCE = "clear_impedance"
CONF_CLIENT_ID = "client_id"
CONF_CLK_PIN = "clk_pin"
CONF_CLOCK_PIN = "clock_pin"
CONF_CLOSE_ACTION = "close_action"
CONF_CLOSE_DURATION = "close_duration"
CONF_CLOSE_ENDSTOP = "close_endstop"
CONF_CO2 = "co2"
CONF_CODE = "code"
CONF_COLD_WHITE = "cold_white"
CONF_COLD_WHITE_COLOR_TEMPERATURE = "cold_white_color_temperature"
CONF_COLOR = "color"
CONF_COLOR_BRIGHTNESS = "color_brightness"
CONF_COLOR_CORRECT = "color_correct"
CONF_COLOR_INTERLOCK = "color_interlock"
CONF_COLOR_MODE = "color_mode"
CONF_COLOR_TEMPERATURE = "color_temperature"
CONF_COLORS = "colors"
CONF_COMMAND = "command"
CONF_COMMAND_RETAIN = "command_retain"
CONF_COMMAND_TOPIC = "command_topic"
CONF_COMMENT = "comment"
CONF_COMMIT = "commit"
CONF_COMPONENT_ID = "component_id"
CONF_COMPONENTS = "components"
CONF_CONDITION = "condition"
CONF_CONDITION_ID = "condition_id"
CONF_CONDUCTIVITY = "conductivity"
CONF_CONSTANT_BRIGHTNESS = "constant_brightness"
CONF_CONTRAST = "contrast"
CONF_COOL_ACTION = "cool_action"
CONF_COOL_DEADBAND = "cool_deadband"
CONF_COOL_MODE = "cool_mode"
CONF_COOL_OVERRUN = "cool_overrun"
CONF_COUNT = "count"
CONF_COUNT_MODE = "count_mode"
CONF_COURSE = "course"
CONF_CRON = "cron"
CONF_CS_PIN = "cs_pin"
CONF_CSS_INCLUDE = "css_include"
CONF_CSS_URL = "css_url"
CONF_CURRENT = "current"
CONF_CURRENT_OPERATION = "current_operation"
CONF_CURRENT_RESISTOR = "current_resistor"
CONF_CURRENT_TEMPERATURE_STATE_TOPIC = "current_temperature_state_topic"
CONF_CUSTOM_FAN_MODE = "custom_fan_mode"
CONF_CUSTOM_FAN_MODES = "custom_fan_modes"
CONF_CUSTOM_PRESET = "custom_preset"
CONF_CUSTOM_PRESETS = "custom_presets"
CONF_DALLAS_ID = "dallas_id"
CONF_DATA = "data"
CONF_DATA_PIN = "data_pin"
CONF_DATA_PINS = "data_pins"
CONF_DATA_RATE = "data_rate"
CONF_DATA_TEMPLATE = "data_template"
CONF_DAYS_OF_MONTH = "days_of_month"
CONF_DAYS_OF_WEEK = "days_of_week"
CONF_DC_PIN = "dc_pin"
CONF_DEASSERT_RTS_DTR = "deassert_rts_dtr"
CONF_DEBOUNCE = "debounce"
CONF_DEBUG = "debug"
CONF_DECAY_MODE = "decay_mode"
CONF_DECELERATION = "deceleration"
CONF_DEFAULT_MODE = "default_mode"
CONF_DEFAULT_TARGET_TEMPERATURE_HIGH = "default_target_temperature_high"
CONF_DEFAULT_TARGET_TEMPERATURE_LOW = "default_target_temperature_low"
CONF_DEFAULT_TRANSITION_LENGTH = "default_transition_length"
CONF_DELAY = "delay"
CONF_DELIMITER = "delimiter"
CONF_DELTA = "delta"
CONF_DEVICE = "device"
CONF_DEVICE_CLASS = "device_class"
CONF_DEVICE_FACTOR = "device_factor"
CONF_DIMENSIONS = "dimensions"
CONF_DIO_PIN = "dio_pin"
CONF_DIR_PIN = "dir_pin"
CONF_DIRECTION = "direction"
CONF_DIRECTION_OUTPUT = "direction_output"
CONF_DISABLED_BY_DEFAULT = "disabled_by_default"
CONF_DISCOVERY = "discovery"
CONF_DISCOVERY_OBJECT_ID_GENERATOR = "discovery_object_id_generator"
CONF_DISCOVERY_PREFIX = "discovery_prefix"
CONF_DISCOVERY_RETAIN = "discovery_retain"
CONF_DISCOVERY_UNIQUE_ID_GENERATOR = "discovery_unique_id_generator"
CONF_DISTANCE = "distance"
CONF_DITHER = "dither"
CONF_DIV_RATIO = "div_ratio"
CONF_DNS1 = "dns1"
CONF_DNS2 = "dns2"
CONF_DOMAIN = "domain"
CONF_DRY_ACTION = "dry_action"
CONF_DRY_MODE = "dry_mode"
CONF_DUMMY_RECEIVER = "dummy_receiver"
CONF_DUMMY_RECEIVER_ID = "dummy_receiver_id"
CONF_DUMP = "dump"
CONF_DURATION = "duration"
CONF_EAP = "eap"
CONF_ECHO_PIN = "echo_pin"
CONF_ECO2 = "eco2"
CONF_EFFECT = "effect"
CONF_EFFECTS = "effects"
CONF_ELSE = "else"
CONF_ENABLE_IPV6 = "enable_ipv6"
CONF_ENABLE_PIN = "enable_pin"
CONF_ENABLE_TIME = "enable_time"
CONF_ENERGY = "energy"
CONF_ENTITY_CATEGORY = "entity_category"
CONF_ENTITY_ID = "entity_id"
CONF_ESP8266_DISABLE_SSL_SUPPORT = "esp8266_disable_ssl_support"
CONF_ESPHOME = "esphome"
CONF_ETHERNET = "ethernet"
CONF_EVENT = "event"
CONF_EXPIRE_AFTER = "expire_after"
CONF_EXPORT_ACTIVE_ENERGY = "export_active_energy"
CONF_EXPORT_REACTIVE_ENERGY = "export_reactive_energy"
CONF_EXTERNAL_COMPONENTS = "external_components"
CONF_EXTERNAL_VCC = "external_vcc"
CONF_FALLING_EDGE = "falling_edge"
CONF_FAMILY = "family"
CONF_FAN_MODE = "fan_mode"
CONF_FAN_MODE_AUTO_ACTION = "fan_mode_auto_action"
CONF_FAN_MODE_COMMAND_TOPIC = "fan_mode_command_topic"
CONF_FAN_MODE_DIFFUSE_ACTION = "fan_mode_diffuse_action"
CONF_FAN_MODE_FOCUS_ACTION = "fan_mode_focus_action"
CONF_FAN_MODE_HIGH_ACTION = "fan_mode_high_action"
CONF_FAN_MODE_LOW_ACTION = "fan_mode_low_action"
CONF_FAN_MODE_MEDIUM_ACTION = "fan_mode_medium_action"
CONF_FAN_MODE_MIDDLE_ACTION = "fan_mode_middle_action"
CONF_FAN_MODE_OFF_ACTION = "fan_mode_off_action"
CONF_FAN_MODE_ON_ACTION = "fan_mode_on_action"
CONF_FAN_MODE_STATE_TOPIC = "fan_mode_state_topic"
CONF_FAN_ONLY_ACTION = "fan_only_action"
CONF_FAN_ONLY_ACTION_USES_FAN_MODE_TIMER = "fan_only_action_uses_fan_mode_timer"
CONF_FAN_ONLY_COOLING = "fan_only_cooling"
CONF_FAN_ONLY_MODE = "fan_only_mode"
CONF_FAN_WITH_COOLING = "fan_with_cooling"
CONF_FAN_WITH_HEATING = "fan_with_heating"
CONF_FAST_CONNECT = "fast_connect"
CONF_FILE = "file"
CONF_FILES = "files"
CONF_FILTER = "filter"
CONF_FILTER_OUT = "filter_out"
CONF_FILTERS = "filters"
CONF_FINGER_ID = "finger_id"
CONF_FINGERPRINT_COUNT = "fingerprint_count"
CONF_FLASH_LENGTH = "flash_length"
CONF_FLASH_TRANSITION_LENGTH = "flash_transition_length"
CONF_FLOW_CONTROL_PIN = "flow_control_pin"
CONF_FOR = "for"
CONF_FORCE_UPDATE = "force_update"
CONF_FORMALDEHYDE = "formaldehyde"
CONF_FORMAT = "format"
CONF_FORWARD_ACTIVE_ENERGY = "forward_active_energy"
CONF_FRAGMENTATION = "fragmentation"
CONF_FRAMEWORK = "framework"
CONF_FREE = "free"
CONF_FREQUENCY = "frequency"
CONF_FROM = "from"
CONF_FULL_SPECTRUM = "full_spectrum"
CONF_FULL_UPDATE_EVERY = "full_update_every"
CONF_GAIN = "gain"
CONF_GAMMA_CORRECT = "gamma_correct"
CONF_GAS_RESISTANCE = "gas_resistance"
CONF_GATEWAY = "gateway"
CONF_GLASS_ATTENUATION_FACTOR = "glass_attenuation_factor"
CONF_GLYPHS = "glyphs"
CONF_GPIO = "gpio"
CONF_GREEN = "green"
CONF_GROUP = "group"
CONF_HARDWARE_UART = "hardware_uart"
CONF_HEARTBEAT = "heartbeat"
CONF_HEAT_ACTION = "heat_action"
CONF_HEAT_DEADBAND = "heat_deadband"
CONF_HEAT_MODE = "heat_mode"
CONF_HEAT_OVERRUN = "heat_overrun"
CONF_HEATER = "heater"
CONF_HEIGHT = "height"
CONF_HIDDEN = "hidden"
CONF_HIDE_TIMESTAMP = "hide_timestamp"
CONF_HIGH = "high"
CONF_HIGH_VOLTAGE_REFERENCE = "high_voltage_reference"
CONF_HOUR = "hour"
CONF_HOURS = "hours"
CONF_HUMIDITY = "humidity"
CONF_HYSTERESIS = "hysteresis"
CONF_I2C = "i2c"
CONF_I2C_ID = "i2c_id"
CONF_IBEACON_MAJOR = "ibeacon_major"
CONF_IBEACON_MINOR = "ibeacon_minor"
CONF_IBEACON_UUID = "ibeacon_uuid"
CONF_ICON = "icon"
CONF_ID = "id"
CONF_IDENTITY = "identity"
CONF_IDLE = "idle"
CONF_IDLE_ACTION = "idle_action"
CONF_IDLE_LEVEL = "idle_level"
CONF_IDLE_TIME = "idle_time"
CONF_IF = "if"
CONF_IGNORE_EFUSE_MAC_CRC = "ignore_efuse_mac_crc"
CONF_IIR_FILTER = "iir_filter"
CONF_ILLUMINANCE = "illuminance"
CONF_IMPEDANCE = "impedance"
CONF_IMPORT_ACTIVE_ENERGY = "import_active_energy"
CONF_IMPORT_REACTIVE_ENERGY = "import_reactive_energy"
CONF_INCLUDE_INTERNAL = "include_internal"
CONF_INCLUDES = "includes"
CONF_INDEX = "index"
CONF_INDOOR = "indoor"
CONF_INFRARED = "infrared"
CONF_INITIAL_MODE = "initial_mode"
CONF_INITIAL_OPTION = "initial_option"
CONF_INITIAL_VALUE = "initial_value"
CONF_INPUT = "input"
CONF_INTEGRATION_TIME = "integration_time"
CONF_INTENSITY = "intensity"
CONF_INTERLOCK = "interlock"
CONF_INTERNAL = "internal"
CONF_INTERNAL_FILTER = "internal_filter"
CONF_INTERNAL_FILTER_MODE = "internal_filter_mode"
CONF_INTERRUPT = "interrupt"
CONF_INTERVAL = "interval"
CONF_INVALID_COOLDOWN = "invalid_cooldown"
CONF_INVERT = "invert"
CONF_INVERTED = "inverted"
CONF_IP_ADDRESS = "ip_address"
CONF_JS_INCLUDE = "js_include"
CONF_JS_URL = "js_url"
CONF_JVC = "jvc"
CONF_KEEP_ON_TIME = "keep_on_time"
CONF_KEEPALIVE = "keepalive"
CONF_KEY = "key"
CONF_LAMBDA = "lambda"
CONF_LAST_CONFIDENCE = "last_confidence"
CONF_LAST_FINGER_ID = "last_finger_id"
CONF_LATITUDE = "latitude"
CONF_LEGEND = "legend"
CONF_LENGTH = "length"
CONF_LEVEL = "level"
CONF_LG = "lg"
CONF_LIBRARIES = "libraries"
CONF_LIGHT = "light"
CONF_LIGHT_ID = "light_id"
CONF_LIGHTNING_ENERGY = "lightning_energy"
CONF_LIGHTNING_THRESHOLD = "lightning_threshold"
CONF_LINE_THICKNESS = "line_thickness"
CONF_LINE_TYPE = "line_type"
CONF_LOADED_INTEGRATIONS = "loaded_integrations"
CONF_LOCAL = "local"
CONF_LOCK_ACTION = "lock_action"
CONF_LOG_TOPIC = "log_topic"
CONF_LOGGER = "logger"
CONF_LOGS = "logs"
CONF_LONGITUDE = "longitude"
CONF_LOOP_TIME = "loop_time"
CONF_LOW = "low"
CONF_LOW_VOLTAGE_REFERENCE = "low_voltage_reference"
CONF_MAC_ADDRESS = "mac_address"
CONF_MAGNITUDE = "magnitude"
CONF_MAINS_FILTER = "mains_filter"
CONF_MAKE_ID = "make_id"
CONF_MANUAL_IP = "manual_ip"
CONF_MANUFACTURER_ID = "manufacturer_id"
CONF_MASK_DISTURBER = "mask_disturber"
CONF_MAX_COOLING_RUN_TIME = "max_cooling_run_time"
CONF_MAX_CURRENT = "max_current"
CONF_MAX_DURATION = "max_duration"
CONF_MAX_HEATING_RUN_TIME = "max_heating_run_time"
CONF_MAX_LENGTH = "max_length"
CONF_MAX_LEVEL = "max_level"
CONF_MAX_POWER = "max_power"
CONF_MAX_RANGE = "max_range"
CONF_MAX_REFRESH_RATE = "max_refresh_rate"
CONF_MAX_SPEED = "max_speed"
CONF_MAX_TEMPERATURE = "max_temperature"
CONF_MAX_VALUE = "max_value"
CONF_MAX_VOLTAGE = "max_voltage"
CONF_MEASUREMENT_DURATION = "measurement_duration"
CONF_MEASUREMENT_SEQUENCE_NUMBER = "measurement_sequence_number"
CONF_MEDIUM = "medium"
CONF_MEMORY_BLOCKS = "memory_blocks"
CONF_METHOD = "method"
CONF_MIN_COOLING_OFF_TIME = "min_cooling_off_time"
CONF_MIN_COOLING_RUN_TIME = "min_cooling_run_time"
CONF_MIN_FAN_MODE_SWITCHING_TIME = "min_fan_mode_switching_time"
CONF_MIN_FANNING_OFF_TIME = "min_fanning_off_time"
CONF_MIN_FANNING_RUN_TIME = "min_fanning_run_time"
CONF_MIN_HEATING_OFF_TIME = "min_heating_off_time"
CONF_MIN_HEATING_RUN_TIME = "min_heating_run_time"
CONF_MIN_IDLE_TIME = "min_idle_time"
CONF_MIN_LENGTH = "min_length"
CONF_MIN_LEVEL = "min_level"
CONF_MIN_POWER = "min_power"
CONF_MIN_RANGE = "min_range"
CONF_MIN_TEMPERATURE = "min_temperature"
CONF_MIN_VALUE = "min_value"
CONF_MINUTE = "minute"
CONF_MINUTES = "minutes"
CONF_MISO_PIN = "miso_pin"
CONF_MODE = "mode"
CONF_MODE_COMMAND_TOPIC = "mode_command_topic"
CONF_MODE_STATE_TOPIC = "mode_state_topic"
CONF_MODEL = "model"
CONF_MOISTURE = "moisture"
CONF_MONTHS = "months"
CONF_MOSI_PIN = "mosi_pin"
CONF_MOTION = "motion"
CONF_MOVEMENT_COUNTER = "movement_counter"
CONF_MQTT = "mqtt"
CONF_MQTT_ID = "mqtt_id"
CONF_MULTIPLEXER = "multiplexer"
CONF_MULTIPLY = "multiply"
CONF_NAME = "name"
CONF_NAME_FONT = "name_font"
CONF_NBITS = "nbits"
CONF_NEC = "nec"
CONF_NETWORKS = "networks"
CONF_NEW_PASSWORD = "new_password"
CONF_NOISE_LEVEL = "noise_level"
CONF_NUM_ATTEMPTS = "num_attempts"
CONF_NUM_CHANNELS = "num_channels"
CONF_NUM_CHIPS = "num_chips"
CONF_NUM_LEDS = "num_leds"
CONF_NUM_SCANS = "num_scans"
CONF_NUMBER = "number"
CONF_NUMBER_DATAPOINT = "number_datapoint"
CONF_OFF_MODE = "off_mode"
CONF_OFFSET = "offset"
CONF_ON = "on"
CONF_ON_BLE_ADVERTISE = "on_ble_advertise"
CONF_ON_BLE_MANUFACTURER_DATA_ADVERTISE = "on_ble_manufacturer_data_advertise"
CONF_ON_BLE_SERVICE_DATA_ADVERTISE = "on_ble_service_data_advertise"
CONF_ON_BOOT = "on_boot"
CONF_ON_CLICK = "on_click"
CONF_ON_CONNECT = "on_connect"
CONF_ON_DISCONNECT = "on_disconnect"
CONF_ON_DOUBLE_CLICK = "on_double_click"
CONF_ON_ENROLLMENT_DONE = "on_enrollment_done"
CONF_ON_ENROLLMENT_FAILED = "on_enrollment_failed"
CONF_ON_ENROLLMENT_SCAN = "on_enrollment_scan"
CONF_ON_FINGER_SCAN_MATCHED = "on_finger_scan_matched"
CONF_ON_FINGER_SCAN_UNMATCHED = "on_finger_scan_unmatched"
CONF_ON_JSON_MESSAGE = "on_json_message"
CONF_ON_LOCK = "on_lock"
CONF_ON_LOOP = "on_loop"
CONF_ON_MESSAGE = "on_message"
CONF_ON_MULTI_CLICK = "on_multi_click"
CONF_ON_OPEN = "on_open"
CONF_ON_PRESS = "on_press"
CONF_ON_RAW_VALUE = "on_raw_value"
CONF_ON_RELEASE = "on_release"
CONF_ON_SHUTDOWN = "on_shutdown"
CONF_ON_SPEED_SET = "on_speed_set"
CONF_ON_STATE = "on_state"
CONF_ON_TAG = "on_tag"
CONF_ON_TAG_REMOVED = "on_tag_removed"
CONF_ON_TIME = "on_time"
CONF_ON_TIME_SYNC = "on_time_sync"
CONF_ON_TOUCH = "on_touch"
CONF_ON_TURN_OFF = "on_turn_off"
CONF_ON_TURN_ON = "on_turn_on"
CONF_ON_UNLOCK = "on_unlock"
CONF_ON_VALUE = "on_value"
CONF_ON_VALUE_RANGE = "on_value_range"
CONF_ONE = "one"
CONF_OPEN_ACTION = "open_action"
CONF_OPEN_DRAIN = "open_drain"
CONF_OPEN_DRAIN_INTERRUPT = "open_drain_interrupt"
CONF_OPEN_DURATION = "open_duration"
CONF_OPEN_ENDSTOP = "open_endstop"
CONF_OPTIMISTIC = "optimistic"
CONF_OPTION = "option"
CONF_OPTIONS = "options"
CONF_OR = "or"
CONF_OSCILLATING = "oscillating"
CONF_OSCILLATION_COMMAND_TOPIC = "oscillation_command_topic"
CONF_OSCILLATION_OUTPUT = "oscillation_output"
CONF_OSCILLATION_STATE_TOPIC = "oscillation_state_topic"
CONF_OTA = "ota"
CONF_OUTPUT = "output"
CONF_OUTPUT_ID = "output_id"
CONF_OUTPUTS = "outputs"
CONF_OVERSAMPLING = "oversampling"
CONF_PACKAGES = "packages"
CONF_PAGE_ID = "page_id"
CONF_PAGES = "pages"
CONF_PANASONIC = "panasonic"
CONF_PASSWORD = "password"
CONF_PATH = "path"
CONF_PAYLOAD = "payload"
CONF_PAYLOAD_AVAILABLE = "payload_available"
CONF_PAYLOAD_NOT_AVAILABLE = "payload_not_available"
CONF_PERIOD = "period"
CONF_PHASE_ANGLE = "phase_angle"
CONF_PHASE_BALANCER = "phase_balancer"
CONF_PIN = "pin"
CONF_PIN_A = "pin_a"
CONF_PIN_B = "pin_b"
CONF_PIN_C = "pin_c"
CONF_PIN_D = "pin_d"
CONF_PINS = "pins"
CONF_PIXEL_MAPPER = "pixel_mapper"
CONF_PLATFORM = "platform"
CONF_PLATFORMIO_OPTIONS = "platformio_options"
CONF_PM_0_3UM = "pm_0_3um"
CONF_PM_0_5UM = "pm_0_5um"
CONF_PM_1_0 = "pm_1_0"
CONF_PM_1_0_STD = "pm_1_0_std"
CONF_PM_1_0UM = "pm_1_0um"
CONF_PM_10_0 = "pm_10_0"
CONF_PM_10_0_STD = "pm_10_0_std"
CONF_PM_10_0UM = "pm_10_0um"
CONF_PM_2_5 = "pm_2_5"
CONF_PM_2_5_STD = "pm_2_5_std"
CONF_PM_2_5UM = "pm_2_5um"
CONF_PM_4_0 = "pm_4_0"
CONF_PM_5_0UM = "pm_5_0um"
CONF_PM_SIZE = "pm_size"
CONF_PMC_0_5 = "pmc_0_5"
CONF_PMC_1_0 = "pmc_1_0"
CONF_PMC_10_0 = "pmc_10_0"
CONF_PMC_2_5 = "pmc_2_5"
CONF_PMC_4_0 = "pmc_4_0"
CONF_PORT = "port"
CONF_POSITION = "position"
CONF_POSITION_ACTION = "position_action"
CONF_POSITION_COMMAND_TOPIC = "position_command_topic"
CONF_POSITION_STATE_TOPIC = "position_state_topic"
CONF_POWER = "power"
CONF_POWER_FACTOR = "power_factor"
CONF_POWER_ON_VALUE = "power_on_value"
CONF_POWER_SAVE_MODE = "power_save_mode"
CONF_POWER_SUPPLY = "power_supply"
CONF_PRESET = "preset"
CONF_PRESET_BOOST = "preset_boost"
CONF_PRESET_ECO = "preset_eco"
CONF_PRESET_SLEEP = "preset_sleep"
CONF_PRESSURE = "pressure"
CONF_PRIORITY = "priority"
CONF_PROJECT = "project"
CONF_PROTOCOL = "protocol"
CONF_PULL_MODE = "pull_mode"
CONF_PULLDOWN = "pulldown"
CONF_PULLUP = "pullup"
CONF_PULSE_LENGTH = "pulse_length"
CONF_QOS = "qos"
CONF_QUANTILE = "quantile"
CONF_RADON = "radon"
CONF_RADON_LONG_TERM = "radon_long_term"
CONF_RANDOM = "random"
CONF_RANGE = "range"
CONF_RANGE_FROM = "range_from"
CONF_RANGE_TO = "range_to"
CONF_RATE = "rate"
CONF_RAW = "raw"
CONF_RAW_DATA_ID = "raw_data_id"
CONF_RC_CODE_1 = "rc_code_1"
CONF_RC_CODE_2 = "rc_code_2"
CONF_REACTIVE_POWER = "reactive_power"
CONF_REBOOT_TIMEOUT = "reboot_timeout"
CONF_RECEIVE_TIMEOUT = "receive_timeout"
CONF_RED = "red"
CONF_REF = "ref"
CONF_REFERENCE_RESISTANCE = "reference_resistance"
CONF_REFERENCE_TEMPERATURE = "reference_temperature"
CONF_REFRESH = "refresh"
CONF_REPEAT = "repeat"
CONF_REPOSITORY = "repository"
CONF_RESET_DURATION = "reset_duration"
CONF_RESET_PIN = "reset_pin"
CONF_RESIZE = "resize"
CONF_RESOLUTION = "resolution"
CONF_RESTORE = "restore"
CONF_RESTORE_MODE = "restore_mode"
CONF_RESTORE_STATE = "restore_state"
CONF_RESTORE_VALUE = "restore_value"
CONF_RETAIN = "retain"
CONF_REVERSE_ACTIVE_ENERGY = "reverse_active_energy"
CONF_REVERSED = "reversed"
CONF_RGB_ORDER = "rgb_order"
CONF_RGBW = "rgbw"
CONF_RISING_EDGE = "rising_edge"
CONF_ROTATION = "rotation"
CONF_RS_PIN = "rs_pin"
CONF_RTD_NOMINAL_RESISTANCE = "rtd_nominal_resistance"
CONF_RTD_WIRES = "rtd_wires"
CONF_RUN_DURATION = "run_duration"
CONF_RW_PIN = "rw_pin"
CONF_RX_BUFFER_SIZE = "rx_buffer_size"
CONF_RX_ONLY = "rx_only"
CONF_RX_PIN = "rx_pin"
CONF_SAFE_MODE = "safe_mode"
CONF_SAMSUNG = "samsung"
CONF_SATELLITES = "satellites"
CONF_SCAN = "scan"
CONF_SCAN_RESULTS = "scan_results"
CONF_SCL = "scl"
CONF_SCL_PIN = "scl_pin"
CONF_SDA = "sda"
CONF_SDO_PIN = "sdo_pin"
CONF_SECOND = "second"
CONF_SECONDS = "seconds"
CONF_SECURITY_LEVEL = "security_level"
CONF_SEGMENTS = "segments"
CONF_SEL_PIN = "sel_pin"
CONF_SEND_EVERY = "send_every"
CONF_SEND_FIRST_AT = "send_first_at"
CONF_SENSING_PIN = "sensing_pin"
CONF_SENSOR = "sensor"
CONF_SENSOR_DATAPOINT = "sensor_datapoint"
CONF_SENSOR_ID = "sensor_id"
CONF_SENSORS = "sensors"
CONF_SEQUENCE = "sequence"
CONF_SERVERS = "servers"
CONF_SERVICE = "service"
CONF_SERVICE_UUID = "service_uuid"
CONF_SERVICES = "services"
CONF_SET_POINT_MINIMUM_DIFFERENTIAL = "set_point_minimum_differential"
CONF_SETUP_MODE = "setup_mode"
CONF_SETUP_PRIORITY = "setup_priority"
CONF_SHOW_LINES = "show_lines"
CONF_SHOW_UNITS = "show_units"
CONF_SHOW_VALUES = "show_values"
CONF_SHUNT_RESISTANCE = "shunt_resistance"
CONF_SHUNT_VOLTAGE = "shunt_voltage"
CONF_SHUTDOWN_MESSAGE = "shutdown_message"
CONF_SIGNAL_STRENGTH = "signal_strength"
CONF_SINGLE_LIGHT_ID = "single_light_id"
CONF_SIZE = "size"
CONF_SLEEP_DURATION = "sleep_duration"
CONF_SLEEP_PIN = "sleep_pin"
CONF_SLEEP_WHEN_DONE = "sleep_when_done"
CONF_SONY = "sony"
CONF_SOURCE = "source"
CONF_SOURCE_ID = "source_id"
CONF_SPEED = "speed"
CONF_SPEED_COMMAND_TOPIC = "speed_command_topic"
CONF_SPEED_COUNT = "speed_count"
CONF_SPEED_LEVEL_COMMAND_TOPIC = "speed_level_command_topic"
CONF_SPEED_LEVEL_STATE_TOPIC = "speed_level_state_topic"
CONF_SPEED_STATE_TOPIC = "speed_state_topic"
CONF_SPI_ID = "spi_id"
CONF_SPIKE_REJECTION = "spike_rejection"
CONF_SSID = "ssid"
CONF_SSL_FINGERPRINTS = "ssl_fingerprints"
CONF_STARTUP_DELAY = "startup_delay"
CONF_STATE = "state"
CONF_STATE_CLASS = "state_class"
CONF_STATE_TOPIC = "state_topic"
CONF_STATIC_IP = "static_ip"
CONF_STATUS = "status"
CONF_STEP = "step"
CONF_STEP_MODE = "step_mode"
CONF_STEP_PIN = "step_pin"
CONF_STOP = "stop"
CONF_STOP_ACTION = "stop_action"
CONF_SUBNET = "subnet"
CONF_SUBSTITUTIONS = "substitutions"
CONF_SUPPLEMENTAL_COOLING_ACTION = "supplemental_cooling_action"
CONF_SUPPLEMENTAL_COOLING_DELTA = "supplemental_cooling_delta"
CONF_SUPPLEMENTAL_HEATING_ACTION = "supplemental_heating_action"
CONF_SUPPLEMENTAL_HEATING_DELTA = "supplemental_heating_delta"
CONF_SUPPORTED_FAN_MODES = "supported_fan_modes"
CONF_SUPPORTED_MODES = "supported_modes"
CONF_SUPPORTED_PRESETS = "supported_presets"
CONF_SUPPORTED_SWING_MODES = "supported_swing_modes"
CONF_SUPPORTS_COOL = "supports_cool"
CONF_SUPPORTS_HEAT = "supports_heat"
CONF_SWING_BOTH_ACTION = "swing_both_action"
CONF_SWING_HORIZONTAL_ACTION = "swing_horizontal_action"
CONF_SWING_MODE = "swing_mode"
CONF_SWING_MODE_COMMAND_TOPIC = "swing_mode_command_topic"
CONF_SWING_MODE_STATE_TOPIC = "swing_mode_state_topic"
CONF_SWING_OFF_ACTION = "swing_off_action"
CONF_SWING_VERTICAL_ACTION = "swing_vertical_action"
CONF_SWITCH_DATAPOINT = "switch_datapoint"
CONF_SWITCHES = "switches"
CONF_SYNC = "sync"
CONF_TABLET = "tablet"
CONF_TAG = "tag"
CONF_TARGET = "target"
CONF_TARGET_TEMPERATURE = "target_temperature"
CONF_TARGET_TEMPERATURE_CHANGE_ACTION = "target_temperature_change_action"
CONF_TARGET_TEMPERATURE_COMMAND_TOPIC = "target_temperature_command_topic"
CONF_TARGET_TEMPERATURE_HIGH = "target_temperature_high"
CONF_TARGET_TEMPERATURE_HIGH_COMMAND_TOPIC = "target_temperature_high_command_topic"
CONF_TARGET_TEMPERATURE_HIGH_STATE_TOPIC = "target_temperature_high_state_topic"
CONF_TARGET_TEMPERATURE_LOW = "target_temperature_low"
CONF_TARGET_TEMPERATURE_LOW_COMMAND_TOPIC = "target_temperature_low_command_topic"
CONF_TARGET_TEMPERATURE_LOW_STATE_TOPIC = "target_temperature_low_state_topic"
CONF_TARGET_TEMPERATURE_STATE_TOPIC = "target_temperature_state_topic"
CONF_TEMPERATURE = "temperature"
CONF_TEMPERATURE_STEP = "temperature_step"
CONF_TEXT_SENSORS = "text_sensors"
CONF_THEN = "then"
CONF_THRESHOLD = "threshold"
CONF_THROTTLE = "throttle"
CONF_TILT = "tilt"
CONF_TILT_ACTION = "tilt_action"
CONF_TILT_COMMAND_TOPIC = "tilt_command_topic"
CONF_TILT_LAMBDA = "tilt_lambda"
CONF_TILT_STATE_TOPIC = "tilt_state_topic"
CONF_TIME = "time"
CONF_TIME_ID = "time_id"
CONF_TIMEOUT = "timeout"
CONF_TIMES = "times"
CONF_TIMEZONE = "timezone"
CONF_TIMING = "timing"
CONF_TO = "to"
CONF_TOLERANCE = "tolerance"
CONF_TOPIC = "topic"
CONF_TOPIC_PREFIX = "topic_prefix"
CONF_TOTAL = "total"
CONF_TOTAL_POWER = "total_power"
CONF_TRACES = "traces"
CONF_TRANSITION_LENGTH = "transition_length"
CONF_TRIGGER_ID = "trigger_id"
CONF_TRIGGER_PIN = "trigger_pin"
CONF_TURN_OFF_ACTION = "turn_off_action"
CONF_TURN_ON_ACTION = "turn_on_action"
CONF_TVOC = "tvoc"
CONF_TX_BUFFER_SIZE = "tx_buffer_size"
CONF_TX_PIN = "tx_pin"
CONF_TX_POWER = "tx_power"
CONF_TYPE = "type"
CONF_TYPE_ID = "type_id"
CONF_UART_ID = "uart_id"
CONF_UID = "uid"
CONF_UNIQUE = "unique"
CONF_UNIT_OF_MEASUREMENT = "unit_of_measurement"
CONF_UNLOCK_ACTION = "unlock_action"
CONF_UPDATE_INTERVAL = "update_interval"
CONF_UPDATE_ON_BOOT = "update_on_boot"
CONF_URL = "url"
CONF_USE_ABBREVIATIONS = "use_abbreviations"
CONF_USE_ADDRESS = "use_address"
CONF_USERNAME = "username"
CONF_UUID = "uuid"
CONF_VALUE = "value"
CONF_VALUE_FONT = "value_font"
CONF_VARIABLES = "variables"
CONF_VARIANT = "variant"
CONF_VERSION = "version"
CONF_VISIBLE = "visible"
CONF_VISUAL = "visual"
CONF_VOLTAGE = "voltage"
CONF_VOLTAGE_ATTENUATION = "voltage_attenuation"
CONF_VOLTAGE_DIVIDER = "voltage_divider"
CONF_WAIT_TIME = "wait_time"
CONF_WAIT_UNTIL = "wait_until"
CONF_WAKEUP_PIN = "wakeup_pin"
CONF_WAND_ID = "wand_id"
CONF_WARM_WHITE = "warm_white"
CONF_WARM_WHITE_COLOR_TEMPERATURE = "warm_white_color_temperature"
CONF_WATCHDOG_THRESHOLD = "watchdog_threshold"
CONF_WEIGHT = "weight"
CONF_WHILE = "while"
CONF_WHITE = "white"
CONF_WIDTH = "width"
CONF_WIFI = "wifi"
CONF_WILL_MESSAGE = "will_message"
CONF_WIND_DIRECTION_DEGREES = "wind_direction_degrees"
CONF_WIND_SPEED = "wind_speed"
CONF_WINDOW_SIZE = "window_size"
CONF_X_GRID = "x_grid"
CONF_Y_GRID = "y_grid"
CONF_ZERO = "zero"

ENV_NOGITIGNORE = "ESPHOME_NOGITIGNORE"
ENV_QUICKWIZARD = "ESPHOME_QUICKWIZARD"

ICON_ACCELERATION = "mdi:axis-arrow"
ICON_ACCELERATION_X = "mdi:axis-x-arrow"
ICON_ACCELERATION_Y = "mdi:axis-y-arrow"
ICON_ACCELERATION_Z = "mdi:axis-z-arrow"
ICON_ACCOUNT = "mdi:account"
ICON_ACCOUNT_CHECK = "mdi:account-check"
ICON_ARROW_EXPAND_VERTICAL = "mdi:arrow-expand-vertical"
ICON_BATTERY = "mdi:battery"
ICON_BLUETOOTH = "mdi:bluetooth"
ICON_BLUR = "mdi:blur"
ICON_BRIEFCASE_DOWNLOAD = "mdi:briefcase-download"
ICON_BRIGHTNESS_5 = "mdi:brightness-5"
ICON_BRIGHTNESS_6 = "mdi:brightness-6"
ICON_BUG = "mdi:bug"
ICON_CHECK_CIRCLE_OUTLINE = "mdi:check-circle-outline"
ICON_CHEMICAL_WEAPON = "mdi:chemical-weapon"
ICON_COUNTER = "mdi:counter"
ICON_CURRENT_AC = "mdi:current-ac"
ICON_DATABASE = "mdi:database"
ICON_EMPTY = ""
ICON_FINGERPRINT = "mdi:fingerprint"
ICON_FLASH = "mdi:flash"
ICON_FLASK = "mdi:flask"
ICON_FLASK_OUTLINE = "mdi:flask-outline"
ICON_FLOWER = "mdi:flower"
ICON_GAS_CYLINDER = "mdi:gas-cylinder"
ICON_GAUGE = "mdi:gauge"
ICON_GRAIN = "mdi:grain"
ICON_KEY_PLUS = "mdi:key-plus"
ICON_LIGHTBULB = "mdi:lightbulb"
ICON_MAGNET = "mdi:magnet"
ICON_MOLECULE_CO2 = "mdi:molecule-co2"
ICON_MOTION_SENSOR = "mdi:motion-sensor"
ICON_NEW_BOX = "mdi:new-box"
ICON_OMEGA = "mdi:omega"
ICON_PERCENT = "mdi:percent"
ICON_POWER = "mdi:power"
ICON_PULSE = "mdi:pulse"
ICON_RADIATOR = "mdi:radiator"
ICON_RADIOACTIVE = "mdi:radioactive"
ICON_RESTART = "mdi:restart"
ICON_RESTART_ALERT = "mdi:restart-alert"
ICON_ROTATE_RIGHT = "mdi:rotate-right"
ICON_RULER = "mdi:ruler"
ICON_SCALE = "mdi:scale"
ICON_SCALE_BATHROOM = "mdi:scale-bathroom"
ICON_SCREEN_ROTATION = "mdi:screen-rotation"
ICON_SECURITY = "mdi:security"
ICON_SIGN_DIRECTION = "mdi:sign-direction"
ICON_SIGNAL = "mdi:signal-distance-variant"
ICON_SIGNAL_DISTANCE_VARIANT = "mdi:signal"
ICON_THERMOMETER = "mdi:thermometer"
ICON_TIMELAPSE = "mdi:timelapse"
ICON_TIMER = "mdi:timer-outline"
ICON_WATER_PERCENT = "mdi:water-percent"
ICON_WEATHER_SUNSET = "mdi:weather-sunset"
ICON_WEATHER_SUNSET_DOWN = "mdi:weather-sunset-down"
ICON_WEATHER_SUNSET_UP = "mdi:weather-sunset-up"
ICON_WEATHER_WINDY = "mdi:weather-windy"
ICON_WIFI = "mdi:wifi"

UNIT_AMPERE = "A"
UNIT_BECQUEREL_PER_CUBIC_METER = "Bq/m³"
UNIT_BYTES = "B"
UNIT_CELSIUS = "°C"
UNIT_COUNT_DECILITRE = "/dL"
UNIT_COUNTS_PER_CUBIC_METER = "#/m³"
UNIT_CUBIC_METER = "m³"
UNIT_DECIBEL = "dB"
UNIT_DECIBEL_MILLIWATT = "dBm"
UNIT_DEGREE_PER_SECOND = "°/s"
UNIT_DEGREES = "°"
UNIT_EMPTY = ""
UNIT_G = "G"
UNIT_HECTOPASCAL = "hPa"
UNIT_HERTZ = "Hz"
UNIT_KELVIN = "K"
UNIT_KILOGRAM = "kg"
UNIT_KILOMETER = "km"
UNIT_KILOMETER_PER_HOUR = "km/h"
UNIT_KILOVOLT_AMPS_REACTIVE = "kVAr"
UNIT_KILOVOLT_AMPS_REACTIVE_HOURS = "kVArh"
UNIT_KILOWATT = "kW"
UNIT_KILOWATT_HOURS = "kWh"
UNIT_LUX = "lx"
UNIT_METER = "m"
UNIT_METER_PER_SECOND_SQUARED = "m/s²"
UNIT_MICROGRAMS_PER_CUBIC_METER = "µg/m³"
UNIT_MICROMETER = "µm"
UNIT_MICROSIEMENS_PER_CENTIMETER = "µS/cm"
UNIT_MICROTESLA = "µT"
UNIT_MILLIGRAMS_PER_CUBIC_METER = "mg/m³"
UNIT_MILLISECOND = "ms"
UNIT_MINUTE = "min"
UNIT_OHM = "Ω"
UNIT_PARTS_PER_BILLION = "ppb"
UNIT_PARTS_PER_MILLION = "ppm"
UNIT_PASCAL = "Pa"
UNIT_PERCENT = "%"
UNIT_PULSES = "pulses"
UNIT_PULSES_PER_MINUTE = "pulses/min"
UNIT_SECOND = "s"
UNIT_STEPS = "steps"
UNIT_VOLT = "V"
UNIT_VOLT_AMPS = "VA"
UNIT_VOLT_AMPS_REACTIVE = "VAR"
UNIT_VOLT_AMPS_REACTIVE_HOURS = "VARh"
UNIT_WATT = "W"
UNIT_WATT_HOURS = "Wh"

# device classes of binary_sensor component
DEVICE_CLASS_BATTERY_CHARGING = "battery_charging"
DEVICE_CLASS_COLD = "cold"
DEVICE_CLASS_CONNECTIVITY = "connectivity"
DEVICE_CLASS_DOOR = "door"
DEVICE_CLASS_GARAGE_DOOR = "garage_door"
DEVICE_CLASS_HEAT = "heat"
DEVICE_CLASS_LIGHT = "light"
DEVICE_CLASS_LOCK = "lock"
DEVICE_CLASS_MOISTURE = "moisture"
DEVICE_CLASS_MOTION = "motion"
DEVICE_CLASS_MOVING = "moving"
DEVICE_CLASS_OCCUPANCY = "occupancy"
DEVICE_CLASS_OPENING = "opening"
DEVICE_CLASS_PLUG = "plug"
DEVICE_CLASS_PRESENCE = "presence"
DEVICE_CLASS_PROBLEM = "problem"
DEVICE_CLASS_RUNNING = "running"
DEVICE_CLASS_SAFETY = "safety"
DEVICE_CLASS_SMOKE = "smoke"
DEVICE_CLASS_SOUND = "sound"
DEVICE_CLASS_TAMPER = "tamper"
DEVICE_CLASS_VIBRATION = "vibration"
DEVICE_CLASS_WINDOW = "window"
# device classes of both binary_sensor and sensor component
DEVICE_CLASS_EMPTY = ""
DEVICE_CLASS_BATTERY = "battery"
DEVICE_CLASS_GAS = "gas"
DEVICE_CLASS_POWER = "power"
# device classes of sensor component
DEVICE_CLASS_AQI = "aqi"
DEVICE_CLASS_CARBON_DIOXIDE = "carbon_dioxide"
DEVICE_CLASS_CARBON_MONOXIDE = "carbon_monoxide"
DEVICE_CLASS_CURRENT = "current"
DEVICE_CLASS_ENERGY = "energy"
DEVICE_CLASS_HUMIDITY = "humidity"
DEVICE_CLASS_ILLUMINANCE = "illuminance"
DEVICE_CLASS_MONETARY = "monetary"
DEVICE_CLASS_NITROGEN_DIOXIDE = "nitrogen_dioxide"
DEVICE_CLASS_NITROGEN_MONOXIDE = "nitrogen_monoxide"
DEVICE_CLASS_NITROUS_OXIDE = "nitrous_oxide"
DEVICE_CLASS_OZONE = "ozone"
DEVICE_CLASS_PM1 = "pm1"
DEVICE_CLASS_PM10 = "pm10"
DEVICE_CLASS_PM25 = "pm25"
DEVICE_CLASS_POWER_FACTOR = "power_factor"
DEVICE_CLASS_PRESSURE = "pressure"
DEVICE_CLASS_SIGNAL_STRENGTH = "signal_strength"
DEVICE_CLASS_SULPHUR_DIOXIDE = "sulphur_dioxide"
DEVICE_CLASS_TEMPERATURE = "temperature"
DEVICE_CLASS_TIMESTAMP = "timestamp"
DEVICE_CLASS_VOLATILE_ORGANIC_COMPOUNDS = "volatile_organic_compounds"
DEVICE_CLASS_VOLTAGE = "voltage"
# device classes of both binary_sensor and button component
DEVICE_CLASS_UPDATE = "update"
# device classes of button component
DEVICE_CLASS_RESTART = "restart"
# device classes of switch component
DEVICE_CLASS_OUTLET = "outlet"
DEVICE_CLASS_SWITCH = "switch"


# state classes
STATE_CLASS_NONE = ""

# The state represents a measurement in present time
STATE_CLASS_MEASUREMENT = "measurement"

# The state represents a total that only increases, a decrease is considered a reset.
STATE_CLASS_TOTAL_INCREASING = "total_increasing"

KEY_CORE = "core"
KEY_TARGET_PLATFORM = "target_platform"
KEY_TARGET_FRAMEWORK = "target_framework"
KEY_FRAMEWORK_VERSION = "framework_version"

# Entity categories
ENTITY_CATEGORY_NONE = ""

# The entity category for configuration values/controls
ENTITY_CATEGORY_CONFIG = "config"

# The entity category for read only diagnostic values, for example RSSI, uptime or MAC Address
ENTITY_CATEGORY_DIAGNOSTIC = "diagnostic"
