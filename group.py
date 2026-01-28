from task import Task, Priority


class Group:
    """
    A class built with the intention of keeping track
    of different subjects of tasks.
    
    Attributes:
    --------------------
    _name : str
        The name of the group.
    _color : str
        The color associated with the group
        stored as a HEX representation.
    _description : str
        A quick description of the group.
    _tasks : list
        A list of tasks associated with the
        constructed group.
    Methods:
    --------------------
    add_task()
        Adds a given task to the _tasks list attribute.
    remove_task()
        Removes a specified task from the _tasks
        list attribute.
    get_name()
        Returns the name of the group.
    get_color()
        Returns the color associated with the group.
    get_description()
        Returns a description of the group.
    get_tasks()
        Returns a list of the tasks associated with
        the group.
    set_name()
        Sets the name of the group to the value given
        to the method call.
    set_color()
        Sets the color of the group to the value given
        to the method call.
    set_description()
        Sets the description of the group to the value
        given to the method call.
    set_tasks()
        Sets the list of tasks associated with the group
        to the value given to the method call.
    copy()
        Returns a copy of the group.
    """

    def __init__(self, name = "Generic Group"):
        """
        A one-argument constructor for the class
        that requires a given name and sets the
        default color to black, the default description
        to prefab sentence, and creates an empty
        list of tasks.
        """

        self._name = name
        self._color = "#000000"
        self._description = "No known description."
        self._tasks = []
   

    def add_task(self, task):
        """
        Appends a given task to the the end of
        the _tasks list attribute.
        """

        self._tasks.append(task)


    def remove_task(self, task):
        """
        Searches the _tasks list attribute for
        a task object that matches the task id
        given to the method call in order to
        remove it from the list.
        """

        if task in self._tasks:
            self._tasks.remove(task)


    def get_name(self):
        """
        Returns the name of the group.
        """

        return self._name
    

    def get_color(self):
        """
        Returns the color of the group as a
        HEX representation, an example would
        be the color black as "#000000".
        """

        return self._color
    

    def get_description(self):
        """
        Returns the description of the group.
        """

        return self._description
    

    def get_tasks(self):
        """
        Returns a list of tasks associated with
        the group.
        """
        return self._tasks


    def set_name(self, name):
        """
        Sets the name of the group to the value
        given at the method call.
        """

        self._name = name
    

    def set_color(self, color):
        """
        Sets the color of the group to the value
        given at the method call, requires a HEX
        representation. An example would be the
        color black as "#000000".
        """
        
        self._color = color
    

    def set_description(self, description):
        """
        Sets the description of the group to the
        value given at the method call.
        """

        self._description = description


    def set_tasks(self, tasks):
        """
        Sets the list of tasks associated with the
        group to the value given at the method call.
        """
        
        self._tasks = tasks


    def copy(self):
        """
        Creates a deep copy of the group and returns
        that group.
        """
        temp = Group(self._name)
        temp.set_color(self._color)
        temp.set_description(self._description)
        temp.set_tasks(self._tasks)
        return temp

    
    def __eq__(self, other):
        """
        Defines the equality comparison.
        """

        if isInstance(other, Group):
            return self._name == other.get_name()
        return NotImplemented


    def __str__(self):
        """
        Defines the toString behavior for the
        group object.
        """

        return f"Group Name: {self._name}"
