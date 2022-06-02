import tkinter as tk
import yaml
from tkinter.colorchooser import askcolor

class Menu(tk.Menu):
    # Menu method and its initializatipn from settings.yaml
    def __init__(self, *args, **kwargs):
        with open('config/settings.yaml', 'r') as settings_yaml:
            settings = yaml.load(settings_yaml, Loader=yaml.FullLoader)
        super().__init__(bg=settings["menu_bg"],
                         activeforeground=settings['menu_active_fg'],
                         activebackground=settings['menu_active_bg'],
                         foreground='#fff',
                         activeborderwidth=0,
                         bd=0,
                         *args, **kwargs)

class Menubar:
    # Initialising the menu bar of editor
    def __init__(self, parent):
        self._parent = parent
        font_specs = ('Droid Sans Fallback', 12)

        # Setting up basic features in menubar
        menubar = tk.Menu(parent.master,
                          font=font_specs,
                          fg='#75715E',
                          bg='#181816',
                          activeforeground='#fff',
                          activebackground='#38342b',
                          activeborderwidth=0,
                          bd=0)

        parent.master.config(menu=menubar)
        self._menubar = menubar
        # Adding features file dropdown in menubar
        file_dropdown = Menu(menubar, font=font_specs, tearoff=0)
        # New file creation feature
        file_dropdown.add_command(label='New File',
                                  accelerator='Ctrl+N',
                                  command=parent.new_file)
        # Open file feature
        file_dropdown.add_command(label='Open File',
                                  accelerator='Ctrl+O',
                                  command=parent.open_file)
        # Save file feature
        file_dropdown.add_command(label='Save',
                                  accelerator='Ctrl+S',
                                  command=parent.save)
        # Save as feature
        file_dropdown.add_command(label='Save As',
                                  accelerator='Ctrl+Shift+S',
                                  command=parent.save_as)
        # Run file feature
        file_dropdown.add_command(label='Run File',
                                  accelerator='Ctrl+R',
                                  command=parent.run)
        # Exit Feature
        file_dropdown.add_separator()
        file_dropdown.add_command(label='Exit', 
                                  command=parent.on_closing)

        # Adding features to about dropdown in menubar
        about_dropdown = Menu(menubar, font=font_specs, tearoff=0)
        about_dropdown.add_command(label='Release Notes',
                                   command=self.release_notes)
        # About command Added
        about_dropdown.add_command(label='About',
                                   command=self.about_message)

        # Adding features to settings dropdown in menubar
        # Edit settings feature
        settings_dropdown = Menu(menubar, font=font_specs, tearoff=0)
        settings_dropdown.add_command(label='Edit Settings',
                                      command=parent.open_settings_file)
        # Reset settings feature
        settings_dropdown.add_command(label='Reset Settings to Default',
                                      command=parent.reset_settings_file)
        
        view_dropdown = Menu(menubar, font=font_specs, tearoff=0)
        view_dropdown.add_command(label='Hide Menu Bar',
                                  command=self.hide_menu)
        view_dropdown.add_command(label='Hide Status Bar',
                                  command=parent.hide_status_bar)
        
        # Menubar add buttons
        menubar.add_cascade(label='File', menu=file_dropdown)
        menubar.add_cascade(label='Settings', menu=settings_dropdown)
        menubar.add_cascade(label='View', menu=view_dropdown)
        menubar.add_command(label='Color Menu', command=self.open_color_picker)
        menubar.add_command(label='Zen Mode', command=self.enter_quiet_mode)
        menubar.add_cascade(label='About', menu=about_dropdown)

        self.menu_fields = [field for field in (
            file_dropdown, about_dropdown, settings_dropdown)]

    # Settings reconfiguration function
    def reconfigure_settings(self):
        with open('config/settings.yaml', 'r') as settings_yaml:
            settings = yaml.load(settings_yaml, Loader=yaml.FullLoader)
        for field in self.menu_fields:
            field.configure(bg=settings['menu_bg'],
                            activeforeground=settings['menu_active_fg'],
                            activebackground=settings['menu_active_bg'],)

    # Color to different text tye can be set here
    def open_color_picker(self):
        return askcolor(title='Color Menu', initialcolor='#d5c4a1')[1]

    # Quiet mode is defined here
    def enter_quiet_mode(self):
        self._parent.enter_quiet_mode()

    # Hiding the menubar
    def hide_menu(self):
        empty_menu = tk.Menu(self._parent.master)
        self._parent.master.config(menu=empty_menu)

    # Display the menubar
    def show_menu(self):
        self._parent.master.config(menu=self._menubar)

    # What to display on clicking about feature is defined here
    def about_message(self):
        box_title = 'About ExEditor'
        box_message = 'A IDE that tries to give the user the best working environment'
        tk.messagebox.showinfo(box_title, box_message)

    def release_notes(self):
        box_title = 'Release Notes'
        box_message = 'Version 0.7 - Added new UI'
        tk.messagebox.showinfo(box_title, box_message)