from functools import partial
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
CYAN = "#00f7ff"        # HEX color cyan


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
        self.groups = []
        self.active_group_buttons = 0
        self.active_tasks = 0
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
            self.active_group_buttons = 0


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
        group_button_bar.rowconfigure(0, weight = 1)
        group_button_bar.pack(side = "top", fill = "both", padx = (2, 2), pady = (0, 2))


        # Main body of the page
        body_frame = tk.Frame(self.main_frame)
        body_frame.pack(side = "bottom", fill = "both", expand = True)
        task_canvas = tk.Canvas(body_frame, bg = LIGHT_GRAY)
        task_canvas.pack(side = "left", fill = "both", expand = True)
        
        scrollable_frame = tk.Frame(task_canvas, bg = LIGHT_GRAY)
        scrollable_frame.pack(fill = "both", expand = True)

        add_group_button = tk.Button(
            group_button_bar,
            text = "Add Group",
            command = partial(self.new_group, scrollable_frame),
            bg = DARK_GRAY,
            fg = WHITE,
            activebackground = GRAY,
            activeforeground = WHITE,
            cursor = "hand2"
        )
        add_group_button.grid(row = 0, column = 0, sticky = tk.NSEW)
        
        scroll_bar_frame = tk.Frame(body_frame)
        scroll_bar_frame.pack(side = "right", fill = "y")
        scroll_bar = tk.Scrollbar(
            scroll_bar_frame,
            orient = "vertical",
            command = task_canvas.yview
        )
        scroll_bar.pack(fill = "both", expand = True)
        canvas_window = task_canvas.create_window(
            (0, 0),
            window = scrollable_frame,
            anchor = "nw"
        )
        task_canvas.bind(
            "<Configure>",
            lambda e: task_canvas.itemconfig(
                canvas_window,
                width = e.width
            )
        )
        task_canvas.configure(yscrollcommand = scroll_bar.set)
        scrollable_frame.bind(
            "<Configure>",
            lambda e: task_canvas.configure(
                scrollregion = task_canvas.bbox("all")
            )
        )

        for grp in self.groups:
            self.add_group(grp, scrollable_frame)


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


    def new_group(self, scrollable_frame):
        """
        This method handles the logic for creating a
        new group.
        """

        num = len(self.groups)
        grp = Group(f"Group #{num + 1}")
        self.groups.append(grp)
        self.add_group(grp, scrollable_frame)


    def delete_group(self, grp):
        """
        This method handles the logic for deleting a
        given group.
        """

        self.groups.remove(grp)
        self.switch_to_task()

    def add_group(self, grp, scrollable_frame):
        """
        This method handles the logic for adding a new group
        display in the task menu.
        """

        index = self.active_group_buttons
        row = index // 3
        col = index % 3
        w_height = scrollable_frame.winfo_screenheight()
        w_width = scrollable_frame.winfo_screenwidth()
        scrollable_frame.columnconfigure(col, weight = 1)
        scrollable_frame.rowconfigure(row, weight = 1)
        self.active_group_buttons += 1

        button = ctk.CTkButton(
            scrollable_frame,
            text = grp.get_name(),
            height = w_height // 4,
            width = w_width // 4,
            corner_radius = 8,
            border_width = 3,
            cursor = "hand2",
            border_color = BLACK,
            fg_color = CYAN,
            text_color = BLACK,
            command = partial(self.switch_to_group, grp)
        )
        button.grid(
            row = row, 
            column = col, 
            sticky = tk.NSEW,
            padx = 5, 
            pady = 5
        )


    def create_group_page(self, grp):
        """
        This method handles the logic for creating the
        group page display for the GUI application.
        """
        
        if self.active_frames["group"] == True:
            return
        else:
            self.clear_active_frames()
            self.active_frames["group"] = True

        self.main_frame = tk.Frame(self.root)
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
        task_button_bar.columnconfigure(1, weight = 1)
        task_button_bar.rowconfigure(0, weight = 1)
        task_button_bar.pack(side = "top", fill = "both", padx = (2, 2), pady = (0, 2))

        # The main body for the page
        body_frame = tk.Frame(self.main_frame)
        body_frame.pack(side = "bottom", fill = "both", expand = True)

        task_canvas = tk.Canvas(body_frame, bg = LIGHT_GRAY)
        task_canvas.pack(side = "left", fill = "both", expand = True)
        scrollable_frame = tk.Frame(
            task_canvas,
            bg = BLACK
        )
        scrollable_frame.pack(fill = "both", expand = True)

        add_task_button = tk.Button(
            task_button_bar,
            text = "Add Task",
            bg = DARK_GRAY,
            fg = WHITE,
            activebackground = GRAY,
            activeforeground = WHITE,
            cursor = "hand2",
            command = partial(self.new_task, grp)
        )
        add_task_button.grid(row = 0, column = 0, sticky = tk.NSEW)
        delete_group_button = tk.Button(
            task_button_bar,
            text = "Delete Group",
            bg = DARK_GRAY,
            fg = WHITE,
            activebackground = GRAY,
            activeforeground = WHITE,
            cursor = "hand2",
            command = partial(self.delete_group, grp)
        )
        delete_group_button.grid(row = 0, column = 1, sticky = tk.NSEW)

        scroll_bar_frame = tk.Frame(body_frame)
        scroll_bar_frame.pack(side = "right", fill = "y")
        scroll_bar = tk.Scrollbar(
            scroll_bar_frame,
            orient = "vertical",
            command = task_canvas.yview
        )
        scroll_bar.pack(fill = "both", expand = True)
        
        canvas_window = task_canvas.create_window(
            (0, 0),
            window = scrollable_frame,
            anchor = "nw"
        )
        task_canvas.bind(
            "<Configure>",
            lambda e: task_canvas.itemconfig(
                canvas_window,
                width = e.width
            )
        )
        task_canvas.configure(yscrollcommand = scroll_bar.set)
        scrollable_frame.bind(
            "<Configure>",
            lambda e: task_canvas.configure(
                scrollregion = task_canvas.bbox("all")
            )
        )

        for task in grp.get_tasks():
            self.load_task(task, grp, scrollable_frame)


    def new_task(self, grp):
        """
        This method handles the logic for creating
        a new task object.
        """

        self.active_tasks += 1
        index = self.active_tasks
        task = Task(id_num = index, name = f"Task #{index}")
        grp.add_task(task)
        self.active_frames["group"] = False
        self.switch_to_group(grp)


    def load_task(self, task, grp, scrollable_frame):
        """
        This method handles the logic for creating a
        new task within a group page.
        """

        task_bar = tk.Frame(scrollable_frame, padx = 1, pady = 1)
        task_bar.columnconfigure(0, weight = 7)
        task_bar.columnconfigure(1, weight = 2)
        task_bar.columnconfigure(2, weight = 1)
        task_bar.columnconfigure(3, weight = 1)
        task_bar.rowconfigure(0, weight = 1)
        task_bar.pack(fill = "both", expand = True)

        task_name = tk.Label(
            task_bar,
            text = task.get_name(),
            bg = WHITE,
            fg = BLACK,
            bd = 1,
            relief = "solid"
        )
        task_name.grid(
            row = 0, 
            column = 0, 
            sticky = tk.NSEW, 
            padx = 1, 
            pady = 1
        )
        
        task_date = tk.Label(
            task_bar,
            text = task.get_date(),
            bg = WHITE,
            fg = BLACK,
            bd = 1,
            relief = "solid"
        )
        task_date.grid(
            row = 0, 
            column = 1, 
            sticky = tk.NSEW, 
            padx = 1, 
            pady = 1
        )

        task_completion = tk.Button(
            task_bar,
            cursor = "hand2",
            bg = WHITE,
            fg = BLACK,
            bd = 1,
            relief = "solid",
            activebackground = GRAY,
            activeforeground = WHITE
        )
        task_completion.grid(
            row = 0, 
            column = 2, 
            sticky = tk.NSEW
        )

        task_delete = tk.Button(
            task_bar,
            text = "Delete Task",
            cursor = "hand2",
            bg = WHITE,
            fg = BLACK,
            bd = 1,
            relief = "solid",
            activebackground = GRAY,
            activeforeground = WHITE,
            command = partial(self.remove_task, task, grp)
        )
        task_delete.grid(
            row = 0, 
            column = 3, 
            sticky = tk.NSEW, 
            padx = (0, 1)
        )


    def remove_task(self, task, grp):
        """
        This method handles the logic for deleting a task
        within a group.
        """
  
        grp.remove_task(task)
        self.active_tasks -= 1
        self.active_frames["group"] = False
        self.switch_to_group(grp)


    def switch_to_group(self, grp):
        """
        This method is for the use of displaying the
        "add task" button for the GUI application when
        a user is viewing a group.
        """
        
        if self.active_frames["group"] == True:
            return
        else:
            self.main_frame.destroy()
            self.create_group_page(grp)
            self.active_group_buttons = 0


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
            self.active_group_buttons = 0


    def start(self):
        """
        This method starts the main loop of 
        the GUI application.
        """
        
        self.root.mainloop()
