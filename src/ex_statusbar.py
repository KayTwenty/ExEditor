import tkinter as tk


class Statusbar:
    def __init__(self, parent):
        self._parent = parent

        # Setting up the status bar
        font_specs = ('Droid Sans Fallback', 10)

        self.status = tk.StringVar()
        self.status.set('ExEditor (v0.5)')

        label = tk.Label(parent.textarea,
                         textvariable=self.status,
                         fg='#fbf1c7',
                         bg='#272822',
                         anchor='se',
                         font=font_specs)
        label.pack(side=tk.BOTTOM)
        self._label = label

    # Status update of the status bar
    def update_status(self, event):
        if event == 'saved':
            self.display_status_message('changes saved!', msg_type='save')
        elif event == 'no file run':
            self.display_status_message('Cannot run! No Python file selected.')
        elif event == 'no file':
            self.display_status_message('No file detected. Create or open a file.')
        elif event == 'no python':
            self.display_status_message('You can only run Python files.')
        elif event == 'no txt bold':
            self.display_status_message('You can only bold text in text files.')
        elif event == 'no txt high':
            self.display_status_message('You can only highlight text in text files.')
        elif event == 'quiet':
            self.display_status_message('You can leave quiet mode by pressing "escape"', msg_type='hint')
        else:
            self.hide_status_bar()
        
    def display_status_message(self, message, msg_type='error'):
        self.show_status_bar()
        self.status.set(message)
        if msg_type == 'save':
            self.save_color()
        elif msg_type == 'hint':
            self.hint_color()
        else:
            self.error_color()

    def error_color(self):
        self._label.config(bg='#522628')

    def save_color(self):
        self._label.config(bg='#47632b')

    def hint_color(self):
        self._label.config(bg='#38342b', fg='#d5c4a1')

    # Hiding the status bar while in quiet mode
    def hide_status_bar(self):
        self._label.pack_forget()

    # Display of the status bar
    def show_status_bar(self):
        self._label.pack(side=tk.BOTTOM)