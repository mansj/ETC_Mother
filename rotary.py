#!/usr/bin/python

from gpiozero import Button, LED, PWMLED

etc = None

def init(etc_obj) :
    global etc
    etc = etc_obj

knob_counter = [0] * 5

rot0_pin_a = Button(18,pull_up=True)
rot0_pin_b = Button(17,pull_up=True)
rot1_pin_a = Button(27,pull_up=True)
rot1_pin_b = Button(22,pull_up=True)
rot2_pin_a = Button(24,pull_up=True)
rot2_pin_b = Button(23,pull_up=True)
rot3_pin_a = Button(6,pull_up=True)
rot3_pin_b = Button(5,pull_up=True)
rot4_pin_a = Button(13,pull_up=True)
rot4_pin_b = Button(12,pull_up=True)

def count_knob(i, newval):
    knob_counter[i] = knob_counter[i] + newval
    if knob_counter[i] > 50: knob_counter[i] = 50
    if knob_counter[i] < 0: knob_counter[i] = 0
    new_value = float(knob_counter[i]) / 50
    if new_value < 0: new_value = 0.000
    etc.knob_hardware[i] = new_value
    etc.knob[i] = new_value

def rot0_pin_a_rising():
    if rot0_pin_b.is_pressed: count_knob(0, -2)

def rot0_pin_b_rising():
    if rot0_pin_a.is_pressed: count_knob(0, 2)

def rot1_pin_a_rising():
    if rot1_pin_b.is_pressed: count_knob(1, -2)

def rot1_pin_b_rising():
    if rot1_pin_a.is_pressed: count_knob(1, 2)

def rot2_pin_a_rising():
    if rot2_pin_b.is_pressed: count_knob(2, -2)

def rot2_pin_b_rising():
    if rot2_pin_a.is_pressed: count_knob(2, 2)

def rot3_pin_a_rising():
    if rot3_pin_b.is_pressed: count_knob(3, -2)

def rot3_pin_b_rising():
    if rot3_pin_a.is_pressed: count_knob(3, 2)

def rot4_pin_a_rising():
    if rot4_pin_b.is_pressed: count_knob(4, -2)

def rot4_pin_b_rising():
    if rot4_pin_a.is_pressed: count_knob(4, 2)




rot0_pin_a.when_pressed = rot0_pin_a_rising      # Register the event handler for pin A
rot0_pin_b.when_pressed = rot0_pin_b_rising      # Register the event handler for pin B
rot1_pin_a.when_pressed = rot1_pin_a_rising      # Register the event handler for pin A
rot1_pin_b.when_pressed = rot1_pin_b_rising      # Register the event handler for pin B
rot2_pin_a.when_pressed = rot2_pin_a_rising      # Register the event handler for pin A
rot2_pin_b.when_pressed = rot2_pin_b_rising      # Register the event handler for pin B
rot3_pin_a.when_pressed = rot3_pin_a_rising      # Register the event handler for pin A
rot3_pin_b.when_pressed = rot3_pin_b_rising      # Register the event handler for pin B
rot4_pin_a.when_pressed = rot4_pin_a_rising      # Register the event handler for pin A
rot4_pin_b.when_pressed = rot4_pin_b_rising      # Register the event handler for pin B


#input("Turn the knob, press Enter to quit.\n")
