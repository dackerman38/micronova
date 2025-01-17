import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import button

from .. import (
    MicroNova,
    MicroNovaFunctions,
    CONF_MICRONOVA_ID,
    CONF_MEMORY_LOCATION,
    CONF_MEMORY_ADDRESS,
    MICRONOVA_LISTENER_SCHEMA,
    micronova_ns,
)

MicroNovaButton = micronova_ns.class_("MicroNovaButton", button.Button, cg.Component)

MicroNovaButton1 = micronova_ns.class_("MicroNovaButton1", button.Button, cg.Component)
MicroNovaButton2 = micronova_ns.class_("MicroNovaButton2", button.Button, cg.Component)
MicroNovaButton3 = micronova_ns.class_("MicroNovaButton3", button.Button, cg.Component)
MicroNovaButton4 = micronova_ns.class_("MicroNovaButton4", button.Button, cg.Component)
MicroNovaButton5 = micronova_ns.class_("MicroNovaButton5", button.Button, cg.Component)


CONF_CUSTOM_BUTTON = "custom_button"

CONF_CUSTOM_BUTTON1 = "1_button"
CONF_CUSTOM_BUTTON2 = "2_button"
CONF_CUSTOM_BUTTON3 = "3_button"
CONF_CUSTOM_BUTTON4 = "4_button"
CONF_CUSTOM_BUTTON5 = "5_button"

CONF_MEMORY_DATA = "memory_data"

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_MICRONOVA_ID): cv.use_id(MicroNova),
        cv.Optional(CONF_CUSTOM_BUTTON): button.button_schema(
            MicroNovaButton,
        )
        .extend(
            MICRONOVA_LISTENER_SCHEMA(
                default_memory_location=0xA0, default_memory_address=0x7D
            )
        )
        .extend({cv.Required(CONF_MEMORY_DATA): cv.hex_int_range()}),
 }


        
        cv.GenerateID(CONF_MICRONOVA_ID): cv.use_id(MicroNova),
        cv.Optional(CONF_CUSTOM_BUTTON1): button.button_schema(
            MicroNovaButton1, icon=numeric-1
        )
        .extend(
            MICRONOVA_LISTENER_SCHEMA(
                default_memory_location=0xA0, default_memory_address=0x7D
            )
        )
        .extend({cv.Required(CONF_MEMORY_DATA): cv.hex_int_range()}),


}


        
        cv.GenerateID(CONF_MICRONOVA_ID): cv.use_id(MicroNova),
        cv.Optional(CONF_CUSTOM_BUTTON2): button.button_schema(
            MicroNovaButton2, icon=numeric-2
        )
        .extend(
            MICRONOVA_LISTENER_SCHEMA(
                default_memory_location=0xA0, default_memory_address=0x7D
            )
        )
        .extend({cv.Required(CONF_MEMORY_DATA): cv.hex_int_range()}),

        cv.Optional(CONF_CUSTOM_BUTTON3): button.button_schema(
            MicroNovaButton3, icon=numeric-3
        )
        .extend(
            MICRONOVA_LISTENER_SCHEMA(
                default_memory_location=0xA0, default_memory_address=0x7D
            )
        )
        .extend({cv.Required(CONF_MEMORY_DATA): cv.hex_int_range()}),

        cv.Optional(CONF_CUSTOM_BUTTON4): button.button_schema(
            MicroNovaButton4, icon=numeric-4
        )
        .extend(
            MICRONOVA_LISTENER_SCHEMA(
                default_memory_location=0xA0, default_memory_address=0x7D
            )
        )
        .extend({cv.Required(CONF_MEMORY_DATA): cv.hex_int_range()}),

        cv.Optional(CONF_CUSTOM_BUTTON5): button.button_schema(
            MicroNovaButton5, icon=numeric-5
        )
        .extend(
            MICRONOVA_LISTENER_SCHEMA(
                default_memory_location=0xA0, default_memory_address=0x7D
            )
        )
        .extend({cv.Required(CONF_MEMORY_DATA): cv.hex_int_range()}),
    }
)


async def to_code(config):
    mv = await cg.get_variable(config[CONF_MICRONOVA_ID])

    if custom_button_config := config.get(CONF_CUSTOM_BUTTON):
        bt = await button.new_button(custom_button_config, mv)
        cg.add(bt.set_memory_location(custom_button_config.get(CONF_MEMORY_LOCATION)))
        cg.add(bt.set_memory_address(custom_button_config.get(CONF_MEMORY_ADDRESS)))
        cg.add(bt.set_memory_data(custom_button_config[CONF_MEMORY_DATA]))
        cg.add(bt.set_function(MicroNovaFunctions.STOVE_FUNCTION_CUSTOM))

 if custom_button_config1 := config.get(CONF_CUSTOM_BUTTON1):
        bt = await button.new_button(custom_button_config1, mv)
        cg.add(bt.set_memory_location(custom_button_config1.get(CONF_MEMORY_LOCATION)))
        cg.add(bt.set_memory_address(custom_button_config1.get(CONF_MEMORY_ADDRESS)))
        cg.add(bt.set_memory_data(custom_button_config1[CONF_MEMORY_DATA]))
        cg.add(bt.set_function(MicroNovaFunctions.STOVE_FUNCTION_CUSTOM))

 if custom_button_config2 := config.get(CONF_CUSTOM_BUTTON2):
        bt = await button.new_button(custom_button_config2, mv)
        cg.add(bt.set_memory_location(custom_button_config2.get(CONF_MEMORY_LOCATION)))
        cg.add(bt.set_memory_address(custom_button_config2.get(CONF_MEMORY_ADDRESS)))
        cg.add(bt.set_memory_data(custom_button_config2[CONF_MEMORY_DATA]))
        cg.add(bt.set_function(MicroNovaFunctions.STOVE_FUNCTION_CUSTOM))

 if custom_button_config3 := config.get(CONF_CUSTOM_BUTTON3):
        bt = await button.new_button(custom_button_config3, mv)
        cg.add(bt.set_memory_location(custom_button_config3.get(CONF_MEMORY_LOCATION)))
        cg.add(bt.set_memory_address(custom_button_config3.get(CONF_MEMORY_ADDRESS)))
        cg.add(bt.set_memory_data(custom_button_config3[CONF_MEMORY_DATA]))
        cg.add(bt.set_function(MicroNovaFunctions.STOVE_FUNCTION_CUSTOM))

 if custom_button_config4 := config.get(CONF_CUSTOM_BUTTON4):
        bt = await button.new_button(custom_button_config4, mv)
        cg.add(bt.set_memory_location(custom_button_config.4get(CONF_MEMORY_LOCATION)))
        cg.add(bt.set_memory_address(custom_button_config4.get(CONF_MEMORY_ADDRESS)))
        cg.add(bt.set_memory_data(custom_button_config4[CONF_MEMORY_DATA]))
        cg.add(bt.set_function(MicroNovaFunctions.STOVE_FUNCTION_CUSTOM))

 if custom_button_config5 := config.get(CONF_CUSTOM_BUTTON5):
        bt = await button.new_button(custom_button_config5, mv)
        cg.add(bt.set_memory_location(custom_button_config5.get(CONF_MEMORY_LOCATION)))
        cg.add(bt.set_memory_address(custom_button_config5.get(CONF_MEMORY_ADDRESS)))
        cg.add(bt.set_memory_data(custom_button_config5[CONF_MEMORY_DATA]))
        cg.add(bt.set_function(MicroNovaFunctions.STOVE_FUNCTION_CUSTOM))




