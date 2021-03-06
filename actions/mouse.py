from talon import ctrl, ui, Module, Context, actions
from talon.engine import engine
from talon_plugins import speech, eye_mouse, eye_zoom_mouse
import platform
import subprocess
import ctypes
import os
import pathlib

key = actions.key
self = actions.self

def show_cursor_helper(show):
    """Show/hide the cursor"""
    ctrl.cursor_visible(show)
    
mod = Module()
@mod.action_class
class Actions:
    def show_cursor():
        """Shows the cursor"""
        show_cursor_helper(True)
        
    def hide_cursor():
        """Hides the cursor"""
        show_cursor_helper(False) 
  
    def wake():
        """Enable control mouse, zoom mouse, and disables cursor"""
        eye_zoom_mouse.zoom_mouse.enable()
        eye_mouse.control_mouse.enable() 
        show_cursor_helper(False)
        
    def calibrate():
        """Start calibration"""
        eye_mouse.calib_start()
            
    def toggle_control_mouse():
        """Toggles control mouse"""
        eye_mouse.control_mouse.toggle()

    def toggle_zoom_mouse():
        """Toggles zoom mouse"""
        if eye_zoom_mouse.zoom_mouse.enabled:
            try:
                eye_zoom_mouse.zoom_mouse.disable()
            except:
                eye_zoom_mouse.zoom_mouse.enabled = False
        else:
            eye_zoom_mouse.zoom_mouse.enable()      
       
    def cancel_zoom_mouse():
        """Cancel zoom mouse if pending"""
        if eye_zoom_mouse.zoom_mouse.enabled and eye_zoom_mouse.zoom_mouse.state != eye_zoom_mouse.STATE_IDLE:
            eye_zoom_mouse.zoom_mouse.cancel()
        
    def sleep():
        """Disables control mouse, zoom mouse, and re-enables cursor"""
        eye_zoom_mouse.zoom_mouse.disable()
        eye_mouse.control_mouse.disable() 
        show_cursor_helper(True)
