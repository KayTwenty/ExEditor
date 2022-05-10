import os
import tkinter as tk
import tkinter.font as tk_font
import json
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser


class Menu(tk.Menu):
    def __init__(self, *args, **kwargs):
        with open('settings.json', 'r') as settings_json:
            settings = json.load(settings_json)
        super().__init__(bg=settings["menu_bg"],
                         activeforeground=settings['menu_active_fg'],
                         activebackground=settings['menu_active_bg'],
                         activeborderwidth=0,
                         *args, **kwargs)

class Menubar:
    def __init__(self, parent):
        self._parent = parent
        font_specs = ('Droid Sans Fallback', 12)

        menubar = tk.Menu(parent.master, font=font_specs,
                          fg='#c9bebb', bg='#3C443A',
                          activebackground='#3C443A',
                          bd=0)
        parent.master.config(menu=menubar)
        self._menubar = menubar

        file_dropdown = Menu(menubar, font=font_specs, tearoff=0)
        file_dropdown.add_command(label='New File',
                                  accelerator='Ctrl+N',
                                  command=parent.new_file)
        file_dropdown.add_command(label='Open File',
                                  accelerator='Ctrl+O',
                                  command=parent.open_file)
        file_dropdown.add_command(label='Save',
                                  accelerator='Ctrl+S',
                                  command=parent.save)
        file_dropdown.add_command(label='Save As',
                                  accelerator='Ctrl+Shift+S',
                                  command=parent.save_as)
        file_dropdown.add_command(label='Run File',
                                  accelerator='Ctrl+b',
                                  command=parent.run)
        file_dropdown.add_separator()
        file_dropdown.add_command(label='Exit',
                                  command=parent.master.destroy)

        about_dropdown = Menu(menubar, font=font_specs, tearoff=0)
        about_dropdown.add_command(label='Release Notes',
                                   command=self.release_notes)
        about_dropdown.add_command(label='About',
                                   command=self.about_message)

        settings_dropdown = Menu(menubar, font=font_specs, tearoff=0)
        settings_dropdown.add_command(label='Edit Settings',
                                      command=parent.open_settings_file)
        settings_dropdown.add_command(label='Reset Settings to Default',
                                      command=parent.reset_settings_file)

        menubar.add_cascade(label='File', menu=file_dropdown)
        menubar.add_cascade(label='Settings', menu=settings_dropdown)
        menubar.add_command(label='Color Wheel',
                            command=self.open_color_picker)
        menubar.add_command(label='Zen Mode', command=self.enter_quiet_mode)
        menubar.add_cascade(label='About', menu=about_dropdown)
        self.menu_fields = [field for field in (file_dropdown, about_dropdown, settings_dropdown)]
            
    def reconfigure_settings(self):
        with open('settings.json', 'r') as settings_json:
            settings = json.load(settings_json)
        for field in self.menu_fields:
            field.configure(bg=settings['menu_bg'],
                            activeforeground=settings['menu_active_fg'],
                            activebackground=settings['menu_active_bg'],)

    def open_color_picker(self):
        return colorchooser.askcolor()[1]

    def enter_quiet_mode(self):
        self._parent.enter_quiet_mode()

    def hide_menu(self):
        empty_menu = tk.Menu(self._parent.master)
        self._parent.master.config(menu=empty_menu)

    def show_menu(self):
        self._parent.master.config(menu=self._menubar)

    def about_message(self):
        box_title = 'About ExEditor'
        box_message = 'A powerful IDE that tries to give the user the best working environment'
        messagebox.showinfo(box_title, box_message)

    def release_notes(self):
        box_title = 'Release Notes'
        box_message = 'Version 0.2 - Added new right click menu & zen mode support'
        messagebox.showinfo(box_title, box_message)


class Statusbar:
    def __init__(self, parent):

        self._parent = parent
        font_specs = ('Droid Sans Fallback', 10)

        self.status = tk.StringVar()
        self.status.set('ExEditor (v0.2)')

        label = tk.Label(parent.textarea, textvariable=self.status, fg='#c9bebb',
                         bg='#272C26', anchor='sw', font=font_specs)
        label.pack(side=tk.BOTTOM, fill=tk.BOTH)
        self._label = label

    def update_status(self, *args):
        if args[0] == 'saved':
            self.status.set('Changes saved!')
        elif args[0] == 'no file':
            self.status.set('Cannot run! No file selected.')
        else:
            self.status.set('ExEditor (v0.2)')

    def hide_status_bar(self):
        self._label.pack_forget()

    def show_status_bar(self):
        self._label.pack(side=tk.BOTTOM, fill=tk.BOTH)


class ExEditor:
    def __init__(self, master):
        master.title('untitled - ExEditor')
        master.geometry('1200x700')
        master.tk_setPalette(background='#30362F',
                             foreground='#c9bebb',
                             activeForeground='white',
                             activeBackground='#151B24',)
        with open('settings.json') as settings_json:
            settings = json.load(settings_json)

        self.text_font = settings['text_font']
        self.bg_color = settings['bg_color']
        self.text_color = settings['text_color']
        self.tab_size = settings['tab_size']
        self.font_style = tk_font.Font(family=self.text_font, size=settings['font_size'])

        self.master = master
        self.filename = None

        self.textarea = tk.Text(master, font=self.text_font)
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview,
                                   bg='#383030', troughcolor='#2e2724',
                                   bd=0, width=8, highlightthickness=0,
                                   activebackground='#3C443A')

        self.textarea.configure(yscrollcommand=self.scroll.set,
                                bg=self.bg_color, fg=self.text_color,
                                wrap='word', spacing1=1, tabs=self.tab_size,
                                spacing3=1, selectbackground='#3d3430',
                                insertbackground='white', bd=0,
                                highlightthickness=0,
                                insertofftime=0, font=self.font_style,
                                undo=True, autoseparators=True, maxundo=-1)

        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.menubar = Menubar(self)
        self.statusbar = Statusbar(self)
        
        self.right_click_menu = tk.Menu(master, font=self.text_font,
                                        fg='#c9bebb', bg='#3C443A',
                                        activebackground='#9c8383',
                                        bd=0, tearoff=0)

        self.right_click_menu.add_command(label='Cut',
                                          accelerator='Ctrl+X')
        self.right_click_menu.add_command(label='Copy',
                                          accelerator='Ctrl+C')
        self.right_click_menu.add_command(label='Paste',
                                          accelerator='Ctrl+V')

        self.bind_shortcuts()

    def reconfigure_settings(self, settings_path, overwrite=False):
        with open(settings_path, 'r') as settings_json:
            settings = json.load(settings_json)
        text_font = settings['text_font']
        bg_color = settings['bg_color']
        text_color = settings['text_color']
        tab_size = settings['tab_size']
        font_style = tk_font.Font(family=text_font, size=settings['font_size'])
        self.textarea.configure(font=font_style, bg=bg_color,
                                fg=text_color, tabs=tab_size)
        if overwrite:
            MsgBox = tk.messagebox.askquestion('Reset Settings?',
                                               'Are you sure you want to reset the editor settings to their default value?',
                                               icon='warning')
            if MsgBox == 'yes':
                with open('settings.json', 'w') as user_settings:
                    json.dump(settings, user_settings)
            else:
                self.save('settings.json')

    def enter_quiet_mode(self, *args):
        self.statusbar.hide_status_bar()
        self.menubar.hide_menu()

    def leave_quiet_mode(self, *args):
        self.statusbar.show_status_bar()
        self.menubar.show_menu()

    def set_window_title(self, name=None):
        if name:
            self.master.title(f'{name} - ExEditor')
        else:
            self.master.title('Untitled - ExEditor')

    def new_file(self, *args):
        self.textarea.delete(1.0, tk.END)
        self.filename = None
        self.set_window_title()

    def open_file(self, *args):
        self.filename = filedialog.askopenfilename(
            defaultextension='.txt',
            filetypes=[('All Files', '*.*'),
                       ('Text Files', '*.txt'),
                       ('Python Scripts', '*.py'),
                       ('Markdown Documents', '*.md'),
                       ('Javascript Files', '*.js'),
                       ('HTML Documents', '*.html'),
                       ('CSS Documents', '*.css')])
        if self.filename:
            self.textarea.delete(1.0, tk.END)
            with open(self.filename, 'r') as f:
                self.textarea.insert(1.0, f.read())
            self.set_window_title(name=self.filename)

    def save(self, *args):
        if self.filename:
            try:
                textarea_content = self.textarea.get(1.0, tk.END)
                with open(self.filename, 'w') as f:
                    f.write(textarea_content)
                self.statusbar.update_status('saved')
                if self.filename == 'settings.json':
                    self.reconfigure_settings(self.filename)
                    self.menubar.reconfigure_settings()
            except Exception as e:
                print(e)
        else:
            self.save_as()

    def save_as(self, *args):
        try:
            new_file = filedialog.asksaveasfilename(
                initialfile='untitled.txt',
                defaultextension='.txt',
                filetypes=[('All Files', '*.*'),
                           ('Text Files', '*.txt'),
                           ('Python Scripts', '*.py'),
                           ('Markdown Documents', '*.md'),
                           ('Javascript Files', '*.js'),
                           ('HTML Documents', '*.html'),
                           ('CSS Documents', '*.css')])
            textarea_content = self.textarea.get(1.0, tk.END)
            with open(new_file, 'w') as f:
                f.write(textarea_content)
            self.filename = new_file
            self.set_window_title(self.filename)
            self.statusbar.update_status('saved')
        except Exception as e:
            print(e)

    def run(self, *args):
        if self.filename:
            os.system(
                f"cmd /k py {self.filename}")
        else:
            self.statusbar.update_status('no file')

    def open_settings_file(self):
        self.filename = 'settings.json'
        self.textarea.delete(1.0, tk.END)
        with open(self.filename, 'r') as f:
            self.textarea.insert(1.0, f.read())
        self.set_window_title(name=self.filename)

    def reset_settings_file(self):
        self.reconfigure_settings('settings-default.json', overwrite=True)

    def select_all_text(self, *args):
        self.textarea.tag_add(tk.SEL, '1.0', tk.END)
        self.textarea.mark_set(tk.INSERT, '1.0')
        self.textarea.see(tk.INSERT)
        return 'break'

    def apply_hex_color(self, key_event):
        new_color = self.menubar.open_color_picker()
        try:
            sel_start = self.textarea.index(tk.SEL_FIRST)
            sel_end = self.textarea.index(tk.SEL_LAST)
            self.textarea.delete(sel_start, sel_end)
            self.textarea.insert(sel_start, new_color)
        except tk.TclError:
            pass
    
    # Triggers the right click menu to appear
    def show_click_menu(self, key_event):
        try:
            self.right_click_menu.tk_popup(key_event.x_root, key_event.y_root)
        finally:
            self.right_click_menu.grab_release()

    # Where all the key binding are stored.
    def bind_shortcuts(self, *args):
        self.textarea.bind('<Control-n>', self.new_file)
        self.textarea.bind('<Control-o>', self.open_file)
        self.textarea.bind('<Control-s>', self.save)
        self.textarea.bind('<Control-S>', self.save_as)
        self.textarea.bind('<Control-b>', self.run)
        self.textarea.bind('<Control-a>', self.select_all_text)
        self.textarea.bind('<Control-h>', self.apply_hex_color)
        self.textarea.bind('<Control-q>', self.enter_quiet_mode)
        self.textarea.bind('<Escape>', self.leave_quiet_mode)
        self.textarea.bind('<Key>', self.statusbar.update_status)
        self.textarea.bind('<Button-3>', self.show_click_menu)

    def python_syntax_highlighting(self):
        pass


if __name__ == '__main__':
    master = tk.Tk()
    qt = ExEditor(master)
    master.mainloop()
