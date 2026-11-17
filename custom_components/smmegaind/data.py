from . import driver_adapter

FULL_NAME = "Industrial Automation"
LINK = "https://sequentmicrosystems.com/products/industrial-raspberry-pi?variant=46030010810620"
API = driver_adapter
DOMAIN = "smmegaind"
NAME_PREFIX = "smmi"
SM_MAP = {
    "button": {
        "opto_cnt_rst": {
            "chan_no": 4,
            "com": {
                "set": "rstOptoCount",
            },
        },
        "watchdog_reload": {
            "chan_no": 1,
            "optional": True,
            "com": {"set": "wdtReload"},
        },
        "owb_scan": {
            "chan_no": 1,
            "optional": True,
            "com": {"set": "owbScan"},
        },
    },
    "select": {
        "opto_edge": {
            "chan_no": 4,
            "optional": True,
            "com": {"get": "get_opto_edge", "set": "set_opto_edge"},
            "option_map": {"None": 0, "Rising": 1, "Falling": 2, "Both": 3},
        },
        "input_range": {
            "chan_no": 4,
            "optional": True,
            "com": {"get": "getUinRange", "set": "setUinRange"},
            "option_map": {"0 to 10 V": 0, "-10 to 10 V": 1},
        },
    },
    "datetime": {
        "rtc": {
            "chan_no": 1,
            "optional": True,
            "com": {"get": "rtcGet", "set": "rtcSet"},
        },
    },
    "sensor": {
        "opto_frequency": {
            "chan_no": 4,
            "optional": True,
            "uom": "Hz",
            "com": {"get": "getOptoFrequency"},
        },
        "rasp_volt": {
            "chan_no": 1,
            "optional": True,
            "uom": "V",
            "com": {"get": "getRaspVolt"},
        },
        "power_volt": {
            "chan_no": 1,
            "optional": True,
            "uom": "V",
            "com": {"get": "getPowerVolt"},
        },
        "cpu_temp": {
            "chan_no": 1,
            "optional": True,
            "uom": "°C",
            "com": {"get": "getCpuTemp"},
        },
        "watchdog_count": {
            "chan_no": 1,
            "optional": True,
            "com": {"get": "wdtGetResetCount"},
        },
        "owb_count": {
            "chan_no": 1,
            "optional": True,
            "com": {"get": "owbGetSensorNo"},
        },
        "0_10_u_in": {
            "chan_no": 4,
            "uom": "V",
            "com": {
                "get": "get0_10In",
            },
        },
        "pm10_u_in": {
            "chan_no": 4,
            "uom": "V",
            "com": {
                "get": "getpm10In",
            },
        },
        "4_20_i_in": {
            "chan_no": 4,
            "uom": "mA",
            "com": {
                "get": "get4_20In",
            },
        },
        "opto": {
            "chan_no": 4,
            "uom": "",
            "com": {
                "get": "getOptoCh",
            },
            "icon": {
                "on": "mdi:numeric-1",
            },
        },
        "opto_cnt": {
            "chan_no": 4,
            "uom": "",
            "com": {
                "get": "getOptoCount",
            },
        },
        "owb_temp": {
            "chan_no": 16,
            "uom": "°C",
            "com": {
                "get": "owbGetTemp",
            },
        },
    },
    "switch": {
        "led": {
            "chan_no": 4,
            "com": {
                "get": "getLed",
                "set": "setLed",
            },
        }
    },
    "number": {
        "watchdog_period": {
            "chan_no": 1,
            "optional": True,
            "uom": "s",
            "min_value": 10,
            "max_value": 65000,
            "step": 1,
            "com": {"get": "wdtGetPeriod", "set": "wdtSetPeriod"},
        },
        "watchdog_initial": {
            "chan_no": 1,
            "optional": True,
            "uom": "s",
            "min_value": 10,
            "max_value": 64999,
            "step": 1,
            "com": {"get": "wdtGetDefaultPeriod", "set": "wdtSetDefaultPeriod"},
        },
        "watchdog_off": {
            "chan_no": 1,
            "optional": True,
            "uom": "s",
            "min_value": 10,
            "max_value": 4147200,
            "step": 1,
            "com": {"get": "wdtGetOffInterval", "set": "wdtSetOffInterval"},
        },
        "0_10_u_out": {
            "chan_no": 4,
            "uom": "V",
            "min_value": 0.0,
            "max_value": 10.0,
            "step": 0.01,
            "com": {
                "get": "get0_10Out",
                "set": "set0_10Out",
            },
        },
        "4_20_i_out": {
            "chan_no": 4,
            "uom": "mA",
            "min_value": 4.0,
            "max_value": 20.0,
            "step": 0.01,
            "com": {
                "get": "get4_20Out",
                "set": "set4_20Out",
            },
        },
        "od": {
            "chan_no": 4,
            "uom": "%",
            "min_value": 0.0,
            "max_value": 100.0,
            "step": 0.01,
            "com": {"get": "getOdPWM", "set": "setOdPWM"},
            "icon": {"on": "mdi:percent", "off": "mdi:percent"},
        },
    },
}
