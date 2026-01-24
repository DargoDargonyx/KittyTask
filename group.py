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
    addTask()
        Adds a given task to the _tasks list attribute.
    removeTask()
        Removes a specified task from the _tasks
        list attribute.
    getName()
        Returns the name of the group.
    getColor()
        Returns the color associated with the group.
    getDescription()
        Returns a description of the group.
    getTasks()
        Returns a list of the tasks associated with
        the group.
    setName()
        Sets the name of the group to the value given
        to the method call.
    setColor()
        Sets the color of the group to the value given
        to the method call.
    setDescription()
        Sets the description of the group to the value
        given to the method call.
    setTasks()
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
   

    def addTask(self, task):
        """
        Appends a given task to the the end of
        the _tasks list attribute.
        """

        self._tasks.append(task)


    def removeTask(self, task_id):
        """
        Searches the _tasks list attribute for
        a task object that matches the task id
        given to the method call in order to
        remove it from the list.
        """

        for task in self._tasks:
            if task.getIdNum() == task_id:
                self._tasks.remove(task)


    def getName(self):
        """
        Returns the name of the group.
        """

        return self._name
    

    def getColor(self):
        """
        Returns the color of the group as a
        HEX representation, an example would
        be the color black as "#000000".
        """

        return self._color
    

    def getDescription(self):
        """
        Returns the description of the group.
        """

        return self._description
    

    def getTasks(self):
        """
        Returns a list of tasks associated with
        the group.
        """
        return self._tasks


    def setName(self, name):
        """
        Sets the name of the group to the value
        given at the method call.
        """

        self._name = name
    

    def setColor(self, color):
        """
        Sets the color of the group to the value
        given at the method call, requires a HEX
        representation. An example would be the
        color black as "#000000".
        """
        
        self._color = color
    

    def setDescription(self, description):
        """
        Sets the description of the group to the
        value given at the method call.
        """

        self._description = description


    def setTasks(self, tasks):
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
        temp.setColor(self._color)
        temp.setDescription(self._description)
        temp.setTasks(self._tasks)
        return temp
