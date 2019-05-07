#!/usr/bin/python

from gpiozero import Button, LED, PWMLED

etc = None

def init(etc_obj) :
    global etc
    etc = etc_obj

knoba_counter = 0

pin_a = Button(18,pull_up=True)         # Rotary encoder pin A connected to GPIO2
pin_b = Button(17,pull_up=True)         # Rotary encoder pin B connected to GPIO3

def pin_a_rising():                    # Pin A event handler
    global knoba_counter
    if pin_b.is_pressed:
    	knoba_counter = knoba_counter - 2
        if knoba_counter < 0: knoba_counter = 0

        new_value = float(knoba_counter) / 50
        if new_value < 0: new_value = 0.000

        etc.knob_hardware[1] = new_value
        etc.knob[1] = new_value
        etc.knob1 = new_value


def pin_b_rising():                    # Pin B event handler
    global knoba_counter
    if pin_a.is_pressed:
    	knoba_counter = knoba_counter + 2
        if knoba_counter > 50: knoba_counter = 50

        new_value = float(knoba_counter) / 50
        if new_value > 1: new_value = 1.000

        etc.knob_hardware[1] = new_value
        etc.knob[1] = new_value
        etc.knob1 = new_value


pin_a.when_pressed = pin_a_rising      # Register the event handler for pin A
pin_b.when_pressed = pin_b_rising      # Register the event handler for pin B


#input("Turn the knob, press Enter to quit.\n")
