import tkinter as tk
import customtkinter as ctk

from task import Task, Priority
from group import Group

# Constants for the class
APPLICATION_TITLE = "KittyTask"

BLACK = "#000000"       # HEX color black
DARK_GRAY = "#2b2b2b"   # HEX color dark gray
GRAY = "#5c5c5c"        # HEX color gray
LIGHT_GRAY = "#949494"  # HEX color light gray
WHITE = "#FFFFFF"       # HEX color white


class Window:
    """ 
    A class meant to handle GUI logic.

    This class is meant to handle the core GUI logic handling
    for the application. This class should have methods that
    handle the switching between different pages of the application
    and receive user input and allocate data where it is needed.
    
    Attributes:
    --------------------
    root : tkinter.Tk
        the root frame of the GUI application.
    main_frame : tkinter.Frame
        the main body frame for the GUI application.
    active_frames : dict
        a dictionary that keeps track of the active
        main frame.

    Methods:
    --------------------
    clear_active_frames()
        loops through the possible active main frames in
        the actove_frames dictionary and sets all keys to
        False in order to "clear" each frame.
    create_menu_bar()
        initializes the top widget bar for the GUI application.
    create_home_page()
        initializes the home page frame for the GUI application.
    switch_to_home()
        switches the main body frame to the home page display.
    create_task_page()
        initializes the task management page frame for the 
        GUI application.
    switch_to_task()
        switches the main body frame to the task management
        page display.
    create_group_page()
        initializes the internal group view page frame for
        the GUI application.
    switch_to_group()
        switches the main body from to the internal group display.
    create_settings_page()
        initializes the settings page frame for the GUI application.
    switch_to_settings()
        switches the main body frame to the settings page display.
    start()
        starts the GUI application.
    """

    def __init__(self):
        """ 
        A constructor for the class
        """

        self.root = tk.Tk()
        self.root.title(APPLICATION_TITLE)
        self.main_frame = tk.Frame(self.root)
        self.active_frames = {
            "home": False,
            "task": False,
            "settings": False,
            "group": False
        }
        self.create_menu_bar()
        self.create_home_page()


    def clear_active_frames(self):
        """
        This method clears all of the active frames
        in the active_frames dictionary.
        """

        for key in self.active_frames:
            self.active_frames[key] = False


    def create_menu_bar(self):
        """
        This method handles the logic for creating the
        top widget bar for the GUI display.
        """

        w_height = self.root.winfo_screenheight()
        w_width = self.root.winfo_screenwidth()
        
        menu_bar_frame = tk.Frame(
            self.root, 
            height = w_height * 0.1, 
            width = w_width, 
            bd = 2,
            relief = "solid"
        )
        menu_bar_frame.columnconfigure(0, weight = 1)
        menu_bar_frame.columnconfigure(1, weight = 1)
        menu_bar_frame.columnconfigure(2, weight = 1)
        menu_bar_frame.rowconfigure(0, weight = 1)
        menu_bar_frame.pack(fill = "both")
        home_button = tk.Button(
            menu_bar_frame, 
            text = "Home",
            command = self.switch_to_home,
            bg = DARK_GRAY,
            fg = WHITE,
            activebackground = GRAY,
            activeforeground = WHITE,
            cursor = "hand2"
        )
        home_button.grid(row = 0, column = 0, sticky = tk.NSEW)
        task_button = tk.Button(
            menu_bar_frame,
            text = "Tasks",
            command = self.switch_to_task,
            bg = DARK_GRAY,
            fg = WHITE,
            activebackground = GRAY,
            activeforeground = WHITE,
            cursor = "hand2"
        )
        task_button.grid(row = 0, column = 1, sticky = tk.NSEW)
        settings_button = tk.Button(
            menu_bar_frame,
            text = "Settings",
            command = self.switch_to_settings,
            bg = DARK_GRAY,
            fg = WHITE,
            activebackground = GRAY,
            activeforeground = WHITE,
            cursor = "hand2"
        )
        settings_button.grid(row = 0, column = 2, sticky = tk.NSEW)


    def create_home_page(self):
        """
        This method handles the logic for creating the
        homepage display for the GUI application.
        """

        if self.active_frames["home"] == True:
            return
        else:
            self.clear_active_frames()
            self.active_frames["home"] = True

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill = "both", expand = True)
        
        w_height = self.root.winfo_screenheight()
        w_width = self.root.winfo_screenwidth()

        upper_frame = tk.Frame(
            self.main_frame, 
            height = w_height * 0.65, 
            width = w_width
        )
        upper_frame.columnconfigure(0, weight = 2)
        upper_frame.columnconfigure(1, weight = 1)
        upper_frame.rowconfigure(0, weight = 1)
        upper_frame.pack(fill = "both", expand = True)
        overview_frame = tk.Frame(
            upper_frame, 
            bg = LIGHT_GRAY,
            bd = 1,
            relief = "solid"
        )
        overview_frame.grid(row = 0, column = 0, sticky = tk.NSEW)
        hotbox_frame = tk.Frame(
            upper_frame, 
            bg = LIGHT_GRAY,
            bd = 1,
            relief = "solid"
        )
        hotbox_frame.grid(row = 0, column = 1, stick = tk.NSEW)
        
        recent_pdfs_frame = tk.Frame(
            self.main_frame, 
            height = w_height * 0.25, 
            width = w_width, 
            bg = LIGHT_GRAY,
            bd = 1,
            relief = "solid"
        )
        recent_pdfs_frame.pack(fill = "both")


    def switch_to_home(self):
        """
        This method is mainly for the use of destroying the
        current displayed main page and switching to the
        homepage view.
        """

        if self.active_frames["home"] == True:
            return
        else:
            self.main_frame.destroy()
            self.create_home_page()


    def create_task_page(self):
        """
        This method handles the logic for creating 
        the task management page display for the 
        GUI application.
        """
        
        if self.active_frames["task"] == True:
            return
        else:
            self.clear_active_frames()
            self.active_frames["task"] = True

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill = "both", expand = True)
        w_height = self.root.winfo_screenheight()
        w_width = self.root.winfo_screenwidth()

        # Another menu bar at the top of page
        button_container = tk.Frame(self.main_frame, bg = BLACK)
        button_container.pack(fill = "x")
        group_button_bar = tk.Frame(
            button_container,
            height = w_height * 0.05,
            width = w_width
        )
        group_button_bar.columnconfigure(0, weight = 1)
        group_button_bar.columnconfigure(1, weight = 10)
        group_button_bar.rowconfigure(0, weight = 1)
        group_button_bar.pack(side = "top", fill = "both", padx = (2, 2), pady = (0, 2))
        add_group_button = tk.Button(
            group_button_bar,
            text = "Add Group",
            bg = DARK_GRAY,
            fg = WHITE,
            activebackground = GRAY,
            activeforeground = WHITE,
            cursor = "hand2"
        )
        add_group_button.grid(row = 0, column = 0, sticky = tk.NSEW)
        spacer_frame = tk.Frame(group_button_bar, bg = LIGHT_GRAY)
        spacer_frame.grid(row = 0, column = 1, sticky = tk.NSEW)

        # Main body of the page
        body_frame = tk.Frame(self.main_frame)
        body_frame.pack(side = "bottom", fill = "both", expand = True)
        task_canvas = tk.Canvas(body_frame, bg = LIGHT_GRAY)
        task_canvas.pack(side = "left", fill = "both", expand = True)
        self.scrollable_task_frame = tk.Frame(task_canvas)
        self.scrollable_task_frame.pack(fill = "both", expand = True)
        scroll_bar_frame = tk.Frame(body_frame)
        scroll_bar_frame.pack(side = "right", fill = "y")
        scroll_bar = tk.Scrollbar(
            scroll_bar_frame,
            orient = "vertical",
            command = task_canvas.yview
        )
        scroll_bar.pack(fill = "both", expand = True)
        task_canvas.create_window(
            (0, 0), 
            window = self.scrollable_task_frame, 
            anchor = "nw"
        )
        task_canvas.configure(yscrollcommand = scroll_bar.set)
        task_canvas.pack()
        self.scrollable_task_frame.bind(
            "<Configure>",
            lambda e: task_canvas.configure(
                scrollregion = task_canvas.bbox("all")
            )
        )

        # Testing label
        test_label = tk.Label(
            self.scrollable_task_frame, 
            text = "This feature has yet to be implemented"
        )
        test_label.pack()


    def switch_to_task(self):
        """
        This method is mainly for the use of destroying the
        current displayed main page and switching to the
        task management page view.
        """
        
        if self.active_frames["task"] == True:
            return
        else:
            self.main_frame.destroy()
            self.create_task_page()


    def create_group_page(self):
        """
        This method handles the logic for creating the
        group page display for the GUI application.
        """
        
        if self.active_frames["group"] == True:
            return
        else:
            self.clear_active_frames()
            self.active_frames["group"] = True

        self.main_frame = tk.Frame
        self.main_frame.pack(fill = "both", expand = True)
        w_height = self.root.winfo_screenheight()
        w_width = self.root.winfo_screenwidth()

        # Another menu frame for the top of the page 
        button_container = tk.Frame(self.main_frame, bg = BLACK)
        button_container.pack(fill = "x")
        task_button_bar = tk.Frame(
            button_container,
            height = w_height * 0.05,
            width = w_width
        )
        task_button_bar.columnconfigure(0, weight = 1)
        task_button_bar.columnconfigure(1, weight = 10)
        task_button_bar.rowconfigure(0, weight = 1)
        task_button_bar.pack(side = "top", fill = "both", padx = (2, 2), pady = (0, 2))
        add_group_button = tk.Button(
            task_button_bar,
            text = "Add Task",
            bg = DARK_GRAY,
            fg = WHITE,
            activebackground = GRAY,
            activeforeground = WHITE,
            cursor = "hand2"
        )
        add_group_button.grid(row = 0, column = 0, sticky = tk.NSEW)
        spacer_frame = tk.Frame(task_button_bar, bg = LIGHT_GRAY)
        spacer_frame.grid(row = 0, column = 1, sticky = tk.NSEW)

        # The main body for the page
        body_frame = tk.Frame(self.main_frame)
        body_frame.pack(side = "bottom", fill = "both", expand = True)
        test_label = tk.Label(body_frame, text = "testing")
        test_label.pack()


    def switch_to_group(self):
        """
        This method is for the use of displaying the
        "add task" button for the GUI application when
        a user is viewing a group.
        """
        
        if self.active_frames["group"] == True:
            return
        else:
            self.main_frame.destroy()
            self.create_group_page()


    def create_settings_page(self):
        """
        This method handles the logic for creating the
        settings page display for the GUI application.
        """

        if self.active_frames["settings"] == True:
            return
        else:
            self.clear_active_frames()
            self.active_frames["settings"] = True

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill = "both", expand = True)
        w_height = self.root.winfo_screenheight()
        w_width = self.root.winfo_screenwidth()

        # Testing label
        label = tk.Label(
            self.main_frame, 
            text = "This feature has yet to be implemented"
        )
        label.pack()


    def switch_to_settings(self):
        """
        This method is mainly for the use of destroying the
        current displayed main page and switching to the
        settings page view.
        """

        if self.active_frames["settings"] == True:
            return
        else:
            self.main_frame.destroy()
            self.create_settings_page()


    def start(self):
        """
        This method starts the main loop of 
        the GUI application.
        """
        
        self.root.mainloop()
