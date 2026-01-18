import tkinter as tk



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

    Methods:
    --------------------
    create_homepage()
        initializes the homepage frame for the application.

    create_settingpage()
        initializes the settings-page frame for the application.
    """

    def __init__(self, width, height):
        """ 
        A constructor for the class

        width : int
            the width of the initial root frame.
        height : int
            the hieght of the initial root frame.
        """

        self.root = tk.Tk()
        self.root.title("KittyTask")
        dimensions = str(width) + "x" + str(height)
        self.root.geometry(dimensions)

    def create_homepage(self):
        home_frame = tk.Frame(self.root)
        top_bar_frame = tk.Frame(home_frame)
        overview_frame = tk.Frame(home_frame)
        hotbox_frame = tk.Frame(home_frame)
        recent_pdfs_frame = tk.Frame(home_frame)

    def create_settingpage(self):
        settings_frame = tk.Frame(self.root) 
