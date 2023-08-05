/*
  Simple DirectMedia Layer
  Copyright (C) 2021 Valve Corporation

  This software is provided 'as-is', without any express or implied
  warranty.  In no event will the authors be held liable for any damages
  arising from the use of this software.

  Permission is granted to anyone to use this software for any purpose,
  including commercial applications, and to alter it and redistribute it
  freely, subject to the following restrictions:

  1. The origin of this software must not be misrepresented; you must not
     claim that you wrote the original software. If you use this software
     in a product, an acknowledgment in the product documentation would be
     appreciated but is not required.
  2. Altered source versions must be plainly marked as such, and must not be
     misrepresented as being the original software.
  3. This notice may not be removed or altered from any source distribution.
*/

#ifndef _CONTROLLER_CONSTANTS_
#define _CONTROLLER_CONSTANTS_

#include "controller_structs.h"

#ifdef __cplusplus
extern "C" {
#endif

#define FEATURE_REPORT_SIZE	64

#define VALVE_USB_VID		0x28DE

// Frame update rate (in ms).
#define FAST_SCAN_INTERVAL  6
#define SLOW_SCAN_INTERVAL  9

// Contains each of the USB PIDs for Valve controllers (only add to this enum and never change the order)
enum ValveControllerPID
{
	BASTILLE_PID              = 0x2202,
	CHELL_PID                 = 0x1101,
	D0G_PID                   = 0x1102,
	ELI_PID                   = 0x1103,
	FREEMAN_PID               = 0x1104,
	D0G_BLE_PID				  = 0x1105,
	D0G_BLE2_PID			  = 0x1106,
	D0GGLE_PID                = 0x1142,
};

// This enum contains all of the messages exchanged between the host and the target (only add to this enum and never change the order)
enum FeatureReportMessageIDs
{
	ID_SET_DIGITAL_MAPPINGS              = 0x80,
	ID_CLEAR_DIGITAL_MAPPINGS            = 0x81,
	ID_GET_DIGITAL_MAPPINGS              = 0x82,
	ID_GET_ATTRIBUTES_VALUES             = 0x83,
	ID_GET_ATTRIBUTE_LABEL               = 0x84,
	ID_SET_DEFAULT_DIGITAL_MAPPINGS      = 0x85,
	ID_FACTORY_RESET                     = 0x86,
	ID_SET_SETTINGS_VALUES               = 0x87,
	ID_CLEAR_SETTINGS_VALUES             = 0x88,
	ID_GET_SETTINGS_VALUES               = 0x89,
	ID_GET_SETTING_LABEL                 = 0x8A,
	ID_GET_SETTINGS_MAXS                 = 0x8B,
	ID_GET_SETTINGS_DEFAULTS             = 0x8C,
	ID_SET_CONTROLLER_MODE               = 0x8D,
	ID_LOAD_DEFAULT_SETTINGS             = 0x8E,
	ID_TRIGGER_HAPTIC_PULSE              = 0x8F,
	ID_TURN_OFF_CONTROLLER               = 0x9F,

	ID_GET_DEVICE_INFO                   = 0xA1,
	
	ID_CALIBRATE_TRACKPADS               = 0xA7,
	ID_RESERVED_0                        = 0xA8,
	ID_SET_SERIAL_NUMBER                 = 0xA9,
	ID_GET_TRACKPAD_CALIBRATION          = 0xAA,
	ID_GET_TRACKPAD_FACTORY_CALIBRATION  = 0xAB,
	ID_GET_TRACKPAD_RAW_DATA             = 0xAC,
	ID_ENABLE_PAIRING                    = 0xAD,
	ID_GET_STRING_ATTRIBUTE              = 0xAE,
	ID_RADIO_ERASE_RECORDS               = 0xAF,
	ID_RADIO_WRITE_RECORD                = 0xB0,
	ID_SET_DONGLE_SETTING                = 0xB1,
	ID_DONGLE_DISCONNECT_DEVICE          = 0xB2,
	ID_DONGLE_COMMIT_DEVICE              = 0xB3,
	ID_DONGLE_GET_WIRELESS_STATE         = 0xB4,
	ID_CALIBRATE_GYRO                    = 0xB5,
	ID_PLAY_AUDIO                        = 0xB6,
	ID_AUDIO_UPDATE_START                = 0xB7,
	ID_AUDIO_UPDATE_DATA                 = 0xB8,
	ID_AUDIO_UPDATE_COMPLETE             = 0xB9,
	ID_GET_CHIPID                        = 0xBA,

	ID_CALIBRATE_JOYSTICK                = 0xBF,
	ID_CALIBRATE_ANALOG_TRIGGERS         = 0xC0,
	ID_SET_AUDIO_MAPPING                 = 0xC1,
	ID_CHECK_GYRO_FW_LOAD                = 0xC2,
	ID_CALIBRATE_ANALOG                  = 0xC3,
	ID_DONGLE_GET_CONNECTED_SLOTS        = 0xC4,
};


// Enumeration of all wireless dongle events
typedef enum WirelessEventTypes
{
	WIRELESS_EVENT_DISCONNECT	= 1,
	WIRELESS_EVENT_CONNECT		= 2,
	WIRELESS_EVENT_PAIR			= 3,
} EWirelessEventType;


// Enumeration of generic digital inputs - not all of these will be supported on all controllers (only add to this enum and never change the order)
typedef enum
{
	IO_DIGITAL_BUTTON_NONE = -1,
	IO_DIGITAL_BUTTON_RIGHT_TRIGGER,
	IO_DIGITAL_BUTTON_LEFT_TRIGGER,
	IO_DIGITAL_BUTTON_1,
	IO_DIGITAL_BUTTON_Y=IO_DIGITAL_BUTTON_1,
	IO_DIGITAL_BUTTON_2,
	IO_DIGITAL_BUTTON_B=IO_DIGITAL_BUTTON_2,
	IO_DIGITAL_BUTTON_3,
	IO_DIGITAL_BUTTON_X=IO_DIGITAL_BUTTON_3,
	IO_DIGITAL_BUTTON_4,
	IO_DIGITAL_BUTTON_A=IO_DIGITAL_BUTTON_4,
	IO_DIGITAL_BUTTON_RIGHT_BUMPER,
	IO_DIGITAL_BUTTON_LEFT_BUMPER,
	IO_DIGITAL_BUTTON_LEFT_JOYSTICK_CLICK,
	IO_DIGITAL_BUTTON_ESCAPE,
	IO_DIGITAL_BUTTON_STEAM,
	IO_DIGITAL_BUTTON_MENU,
	IO_DIGITAL_STICK_UP,
	IO_DIGITAL_STICK_DOWN,
	IO_DIGITAL_STICK_LEFT,
	IO_DIGITAL_STICK_RIGHT,
	IO_DIGITAL_TOUCH_1,
	IO_DIGITAL_BUTTON_UP=IO_DIGITAL_TOUCH_1,
	IO_DIGITAL_TOUCH_2,
	IO_DIGITAL_BUTTON_RIGHT=IO_DIGITAL_TOUCH_2,
	IO_DIGITAL_TOUCH_3,
	IO_DIGITAL_BUTTON_LEFT=IO_DIGITAL_TOUCH_3,
	IO_DIGITAL_TOUCH_4,
	IO_DIGITAL_BUTTON_DOWN=IO_DIGITAL_TOUCH_4,
	IO_DIGITAL_BUTTON_BACK_LEFT,
	IO_DIGITAL_BUTTON_BACK_RIGHT,
	IO_DIGITAL_LEFT_TRACKPAD_N,
	IO_DIGITAL_LEFT_TRACKPAD_NE,
	IO_DIGITAL_LEFT_TRACKPAD_E,
	IO_DIGITAL_LEFT_TRACKPAD_SE,
	IO_DIGITAL_LEFT_TRACKPAD_S,
	IO_DIGITAL_LEFT_TRACKPAD_SW,
	IO_DIGITAL_LEFT_TRACKPAD_W,
	IO_DIGITAL_LEFT_TRACKPAD_NW,
	IO_DIGITAL_RIGHT_TRACKPAD_N,
	IO_DIGITAL_RIGHT_TRACKPAD_NE,
	IO_DIGITAL_RIGHT_TRACKPAD_E,
	IO_DIGITAL_RIGHT_TRACKPAD_SE,
	IO_DIGITAL_RIGHT_TRACKPAD_S,
	IO_DIGITAL_RIGHT_TRACKPAD_SW,
	IO_DIGITAL_RIGHT_TRACKPAD_W,
	IO_DIGITAL_RIGHT_TRACKPAD_NW,
	IO_DIGITAL_LEFT_TRACKPAD_DOUBLE_TAP,
	IO_DIGITAL_RIGHT_TRACKPAD_DOUBLE_TAP,
	IO_DIGITAL_LEFT_TRACKPAD_OUTER_RADIUS,
	IO_DIGITAL_RIGHT_TRACKPAD_OUTER_RADIUS,
	IO_DIGITAL_LEFT_TRACKPAD_CLICK,
	IO_DIGITAL_RIGHT_TRACKPAD_CLICK,
	IO_DIGITAL_BATTERY_LOW,
	IO_DIGITAL_LEFT_TRIGGER_THRESHOLD,
	IO_DIGITAL_RIGHT_TRIGGER_THRESHOLD,
	IO_DIGITAL_BUTTON_BACK_LEFT2,
	IO_DIGITAL_BUTTON_BACK_RIGHT2,
	IO_DIGITAL_BUTTON_ALWAYS_ON,
	IO_DIGITAL_BUTTON_ANCILLARY_1,
	IO_DIGITAL_BUTTON_MACRO_0,
	IO_DIGITAL_BUTTON_MACRO_1,
	IO_DIGITAL_BUTTON_MACRO_2,
	IO_DIGITAL_BUTTON_MACRO_3,
	IO_DIGITAL_BUTTON_MACRO_4,
	IO_DIGITAL_BUTTON_MACRO_5,
	IO_DIGITAL_BUTTON_MACRO_6,
	IO_DIGITAL_BUTTON_MACRO_7,
	IO_DIGITAL_BUTTON_MACRO_1FINGER,
	IO_DIGITAL_BUTTON_MACRO_2FINGER,
	IO_DIGITAL_COUNT
} DigitalIO ;

// Enumeration of generic analog inputs - not all of these will be supported on all controllers (only add to this enum and never change the order)
typedef enum 
{
	IO_ANALOG_LEFT_STICK_X,
	IO_ANALOG_LEFT_STICK_Y,
	IO_ANALOG_RIGHT_STICK_X,
	IO_ANALOG_RIGHT_STICK_Y,
	IO_ANALOG_LEFT_TRIGGER,
	IO_ANALOG_RIGHT_TRIGGER,
	IO_MOUSE1_X,
	IO_MOUSE1_Y,
	IO_MOUSE1_Z,
	IO_ACCEL_X,
	IO_ACCEL_Y,
	IO_ACCEL_Z,
	IO_GYRO_X,
	IO_GYRO_Y,
	IO_GYRO_Z,
	IO_GYRO_QUAT_W,
	IO_GYRO_QUAT_X,
	IO_GYRO_QUAT_Y,
	IO_GYRO_QUAT_Z,
	IO_GYRO_STEERING_VEC,
	IO_RAW_TRIGGER_LEFT,
	IO_RAW_TRIGGER_RIGHT,
	IO_RAW_JOYSTICK_X,
	IO_RAW_JOYSTICK_Y,
	IO_GYRO_TILT_VEC,
	IO_ANALOG_COUNT
} AnalogIO;


// Contains list of all types of devices that the controller emulates (only add to this enum and never change the order)
enum DeviceTypes
{
	DEVICE_KEYBOARD,
	DEVICE_MOUSE,
	DEVICE_GAMEPAD,
	DEVICE_MODE_ADJUST,
	DEVICE_COUNT
};

// Scan codes for HID keyboards 
enum HIDKeyboardKeys
{
	KEY_INVALID,
	KEY_FIRST = 0x04,
	KEY_A = KEY_FIRST, KEY_B, KEY_C, KEY_D, KEY_E, KEY_F, KEY_G, KEY_H, KEY_I, KEY_J, KEY_K, KEY_L, 
	KEY_M, KEY_N, KEY_O, KEY_P, KEY_Q, KEY_R, KEY_S, KEY_T, KEY_U, KEY_V, KEY_W, KEY_X, KEY_Y, KEY_Z, KEY_1, KEY_2, 
	KEY_3, KEY_4, KEY_5, KEY_6, KEY_7, KEY_8, KEY_9, KEY_0, KEY_RETURN, KEY_ESCAPE, KEY_BACKSPACE, KEY_TAB, KEY_SPACE, KEY_DASH, KEY_EQUALS, KEY_LEFT_BRACKET,
	KEY_RIGHT_BRACKET, KEY_BACKSLASH, KEY_UNUSED1, KEY_SEMICOLON, KEY_SINGLE_QUOTE, KEY_BACK_TICK, KEY_COMMA, KEY_PERIOD, KEY_FORWARD_SLASH, KEY_CAPSLOCK, KEY_F1, KEY_F2, KEY_F3, KEY_F4, KEY_F5, KEY_F6,
	KEY_F7, KEY_F8, KEY_F9, KEY_F10, KEY_F11, KEY_F12, KEY_PRINT_SCREEN, KEY_SCROLL_LOCK, KEY_BREAK, KEY_INSERT, KEY_HOME, KEY_PAGE_UP, KEY_DELETE, KEY_END, KEY_PAGE_DOWN, KEY_RIGHT_ARROW,
	KEY_LEFT_ARROW, KEY_DOWN_ARROW, KEY_UP_ARROW, KEY_NUM_LOCK, KEY_KEYPAD_FORWARD_SLASH, KEY_KEYPAD_ASTERISK, KEY_KEYPAD_DASH, KEY_KEYPAD_PLUS, KEY_KEYPAD_ENTER, KEY_KEYPAD_1, KEY_KEYPAD_2, KEY_KEYPAD_3, KEY_KEYPAD_4, KEY_KEYPAD_5, KEY_KEYPAD_6, KEY_KEYPAD_7,
	KEY_KEYPAD_8, KEY_KEYPAD_9, KEY_KEYPAD_0, KEY_KEYPAD_PERIOD,
	KEY_LALT,
    KEY_LSHIFT,
    KEY_LWIN,
    KEY_LCONTROL,
    KEY_RALT,
    KEY_RSHIFT,
    KEY_RWIN,
    KEY_RCONTROL,
	KEY_VOLUP,
	KEY_VOLDOWN,
	KEY_MUTE,
	KEY_PLAY,
	KEY_STOP,
	KEY_NEXT,
	KEY_PREV,
    KEY_LAST = KEY_PREV
};

enum ModifierMasks
{
  KEY_LCONTROL_MASK = (1<<0),
  KEY_LSHIFT_MASK = (1<<1),
  KEY_LALT_MASK = (1<<2),
  KEY_LWIN_MASK = (1<<3),
  KEY_RCONTROL_MASK = (1<<4),
  KEY_RSHIFT_MASK = (1<<5),
  KEY_RALT_MASK = (1<<6),
  KEY_RWIN_MASK = (1<<7)
};

// Standard mouse buttons as specified in the HID mouse spec
enum MouseButtons
{
	MOUSE_BTN_LEFT,
	MOUSE_BTN_RIGHT,
	MOUSE_BTN_MIDDLE,
	MOUSE_BTN_BACK,
	MOUSE_BTN_FORWARD,
	MOUSE_SCROLL_UP,
	MOUSE_SCROLL_DOWN,
	MOUSE_BTN_COUNT
};

// Gamepad buttons
enum GamepadButtons
{
	GAMEPAD_BTN_TRIGGER_LEFT=1, 
	GAMEPAD_BTN_TRIGGER_RIGHT,
	GAMEPAD_BTN_A,
	GAMEPAD_BTN_B,
	GAMEPAD_BTN_Y,
	GAMEPAD_BTN_X,
	GAMEPAD_BTN_SHOULDER_LEFT,
	GAMEPAD_BTN_SHOULDER_RIGHT,
	GAMEPAD_BTN_LEFT_JOYSTICK,
	GAMEPAD_BTN_RIGHT_JOYSTICK,
	GAMEPAD_BTN_START,
	GAMEPAD_BTN_SELECT,
	GAMEPAD_BTN_STEAM,
	GAMEPAD_BTN_DPAD_UP,
	GAMEPAD_BTN_DPAD_DOWN,
	GAMEPAD_BTN_DPAD_LEFT,
	GAMEPAD_BTN_DPAD_RIGHT,
	GAMEPAD_BTN_LSTICK_UP,
	GAMEPAD_BTN_LSTICK_DOWN,
	GAMEPAD_BTN_LSTICK_LEFT,
	GAMEPAD_BTN_LSTICK_RIGHT,
	GAMEPAD_BTN_RSTICK_UP,
	GAMEPAD_BTN_RSTICK_DOWN,
	GAMEPAD_BTN_RSTICK_LEFT,
	GAMEPAD_BTN_RSTICK_RIGHT,
	GAMEPAD_BTN_COUNT
};

// Mode adjust
enum ModeAdjustModes
{
	MODE_ADJUST_SENSITITY=1,
	MODE_ADJUST_LEFT_PAD_SECONDARY_MODE,
	MODE_ADJUST_RIGHT_PAD_SECONDARY_MODE,
	MODE_ADJUST_COUNT
};

// Read-only attributes of controllers (only add to this enum and never change the order)
typedef enum
{
	ATTRIB_UNIQUE_ID,
	ATTRIB_PRODUCT_ID,
	ATTRIB_PRODUCT_REVISON,											// deprecated
	ATTRIB_CAPABILITIES = ATTRIB_PRODUCT_REVISON,	// intentional aliasing
	ATTRIB_FIRMWARE_VERSION,										// deprecated
	ATTRIB_FIRMWARE_BUILD_TIME,
	ATTRIB_RADIO_FIRMWARE_BUILD_TIME,
	ATTRIB_RADIO_DEVICE_ID0,
	ATTRIB_RADIO_DEVICE_ID1,
	ATTRIB_DONGLE_FIRMWARE_BUILD_TIME,
	ATTRIB_BOARD_REVISION,
	ATTRIB_BOOTLOADER_BUILD_TIME,
	ATTRIB_CONNECTION_INTERVAL_IN_US,
	ATTRIB_COUNT
} ControllerAttributes;

// Read-only string attributes of controllers (only add to this enum and never change the order)
typedef enum
{
	ATTRIB_STR_BOARD_SERIAL,
	ATTRIB_STR_UNIT_SERIAL,
	ATTRIB_STR_COUNT
} ControllerStringAttributes;

typedef enum
{
	STATUS_CODE_NORMAL,
	STATUS_CODE_CRITICAL_BATTERY,
	STATUS_CODE_GYRO_INIT_ERROR,
} ControllerStatusEventCodes;

typedef enum
{
	STATUS_STATE_LOW_BATTERY=0,
} ControllerStatusStateFlags;

typedef enum {
	TRACKPAD_ABSOLUTE_MOUSE,
	TRACKPAD_RELATIVE_MOUSE,
	TRACKPAD_DPAD_FOUR_WAY_DISCRETE,
	TRACKPAD_DPAD_FOUR_WAY_OVERLAP,
	TRACKPAD_DPAD_EIGHT_WAY,
	TRACKPAD_RADIAL_MODE,
	TRACKPAD_ABSOLUTE_DPAD,
	TRACKPAD_NONE,
	TRACKPAD_GESTURE_KEYBOARD,
	TRACKPAD_NUM_MODES
} TrackpadDPadMode;

// Read-write controller settings (only add to this enum and never change the order)
typedef enum 
{
	SETTING_MOUSE_SENSITIVITY,
	SETTING_MOUSE_ACCELERATION,
	SETTING_TRACKBALL_ROTATION_ANGLE,
	SETTING_HAPTIC_INTENSITY,
	SETTING_LEFT_GAMEPAD_STICK_ENABLED,
	SETTING_RIGHT_GAMEPAD_STICK_ENABLED,
	SETTING_USB_DEBUG_MODE,
	SETTING_LEFT_TRACKPAD_MODE,
	SETTING_RIGHT_TRACKPAD_MODE,
	SETTING_MOUSE_POINTER_ENABLED,
	SETTING_DPAD_DEADZONE,
	SETTING_MINIMUM_MOMENTUM_VEL,
	SETTING_MOMENTUM_DECAY_AMMOUNT,
	SETTING_TRACKPAD_RELATIVE_MODE_TICKS_PER_PIXEL,
	SETTING_HAPTIC_INCREMENT,
	SETTING_DPAD_ANGLE_SIN,
	SETTING_DPAD_ANGLE_COS,
	SETTING_MOMENTUM_VERTICAL_DIVISOR,
	SETTING_MOMENTUM_MAXIMUM_VELOCITY,
	SETTING_TRACKPAD_Z_ON,
	SETTING_TRACKPAD_Z_OFF,
	SETTING_SENSITIVY_SCALE_AMMOUNT,
	SETTING_LEFT_TRACKPAD_SECONDARY_MODE,
	SETTING_RIGHT_TRACKPAD_SECONDARY_MODE,
	SETTING_SMOOTH_ABSOLUTE_MOUSE,
	SETTING_STEAMBUTTON_POWEROFF_TIME,
	SETTING_UNUSED_1,
	SETTING_TRACKPAD_OUTER_RADIUS,
	SETTING_TRACKPAD_Z_ON_LEFT,
	SETTING_TRACKPAD_Z_OFF_LEFT,
	SETTING_TRACKPAD_OUTER_SPIN_VEL,
	SETTING_TRACKPAD_OUTER_SPIN_RADIUS,
	SETTING_TRACKPAD_OUTER_SPIN_HORIZONTAL_ONLY,
	SETTING_TRACKPAD_RELATIVE_MODE_DEADZONE,
	SETTING_TRACKPAD_RELATIVE_MODE_MAX_VEL,
	SETTING_TRACKPAD_RELATIVE_MODE_INVERT_Y,
	SETTING_TRACKPAD_DOUBLE_TAP_BEEP_ENABLED,
	SETTING_TRACKPAD_DOUBLE_TAP_BEEP_PERIOD,
	SETTING_TRACKPAD_DOUBLE_TAP_BEEP_COUNT,
	SETTING_TRACKPAD_OUTER_RADIUS_RELEASE_ON_TRANSITION,
	SETTING_RADIAL_MODE_ANGLE,
	SETTING_HAPTIC_INTENSITY_MOUSE_MODE,
	SETTING_LEFT_DPAD_REQUIRES_CLICK,
	SETTING_RIGHT_DPAD_REQUIRES_CLICK,
	SETTING_LED_BASELINE_BRIGHTNESS,
	SETTING_LED_USER_BRIGHTNESS,
	SETTING_ENABLE_RAW_JOYSTICK,
	SETTING_ENABLE_FAST_SCAN,
	SETTING_GYRO_MODE,
	SETTING_WIRELESS_PACKET_VERSION,
	SETTING_SLEEP_INACTIVITY_TIMEOUT,
	SETTING_COUNT,
	
	// This is a special setting value use for callbacks and should not be set/get explicitly.
	SETTING_ALL=0xFF
} ControllerSettings;

typedef enum
{
	SETTING_DEFAULT,
	SETTING_MIN,
	SETTING_MAX,
	SETTING_DEFAULTMINMAXCOUNT
} SettingDefaultMinMax;

// Bitmask that define which IMU features to enable.
typedef enum
{
	SETTING_GYRO_MODE_OFF				= 0x0000,
	SETTING_GYRO_MODE_STEERING			= 0x0001,
	SETTING_GYRO_MODE_TILT				= 0x0002,
	SETTING_GYRO_MODE_SEND_ORIENTATION	= 0x0004,
	SETTING_GYRO_MODE_SEND_RAW_ACCEL	= 0x0008,
	SETTING_GYRO_MODE_SEND_RAW_GYRO		= 0x0010,
} SettingGyroMode;

// Bitmask for haptic pulse flags
typedef enum
{
	HAPTIC_PULSE_NORMAL					= 0x0000,
	HAPTIC_PULSE_HIGH_PRIORITY			= 0x0001,
	HAPTIC_PULSE_VERY_HIGH_PRIORITY		= 0x0002,
} SettingHapticPulseFlags;

typedef struct
{
	// default,min,max in this array in that order
	short defaultminmax[SETTING_DEFAULTMINMAXCOUNT]; 
} SettingValueRange_t;

// below is from controller_constants.c which should be compiled into any code that uses this
extern const SettingValueRange_t g_DefaultSettingValues[SETTING_COUNT];

// Read-write settings for dongle (only add to this enum and never change the order)
typedef enum 
{
	DONGLE_SETTING_MOUSE_KEYBOARD_ENABLED,
	DONGLE_SETTING_COUNT,
} DongleSettings;

typedef enum
{
	AUDIO_STARTUP		= 0,
	AUDIO_SHUTDOWN		= 1,
	AUDIO_PAIR			= 2,
	AUDIO_PAIR_SUCCESS	= 3,
	AUDIO_IDENTIFY		= 4,
	AUDIO_LIZARDMODE	= 5,
	AUDIO_NORMALMODE	= 6,

	AUDIO_MAX_SLOT      = 15
} ControllerAudio;

#ifdef __cplusplus
}
#endif

#endif // _CONTROLLER_CONSTANTS_H
