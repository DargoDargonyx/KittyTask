from enum import Enum


class Priority(Enum):
    """
    Enum class built to keep track of Task priorities.
    """

    LOW = 1
    MED = 2
    HIGH = 3
    LATE = 4


class Task:
    """
    A class built to keep track of different possible
    tasks or activities to keep track of in the application.

    Attributes:
    --------------------
    _id_num : int
        An indentification number associated with the task.
    _name : str
        The name of the task.
    _date : str
        The date the task needs to be completed by.
    _priority : Priority
        A representation of how important the task is
        using a custom built Enum.
    _description : 
        A description of the task.

    Methods:
    --------------------
    getIdNum()
        Returns the identification number of the task.
    getName()
        Returns the name of the task.
    getDate()
        Returns the date that the task needs to be
        completed by.
    getPriority()
        Returns an Enum that represents how important
        the task is.
    getDescription()
        Returns the description of the task.
    setIdNum()
        Sets the identification number of the task
        to the value given to the method call.
    setName()
        Sets the name of the task to the value
        given to the method call.
    setDate()
        Sets the date that the task needs to be completed
        by to the value given to the method call.
    setPriority()
        Sets the priority of the task to the value given
        to the method call.
    setDescription()
        Sets the description of the task to the value
        given to the method call.
    """

    def __init__(self, id_num, name = "Generic Task", date = "", priority = Priority.LOW):
        """
        A four-argument constructor for the class that
        requires an identification number to be provided
        and accepts optional inputs for the name, date,
        and priority. A prefab description is set to the
        _description attribute.
        """

        self._id_num = id_num
        self._name = name
        self._date = date
        self._priority = priority
        self._description = "No known description."


    def getIdNum(self):
        """
        Returns the identification number of 
        the task.
        """
        
        return self._id_num


    def getName(self):
        """
        Returns the name of the task.
        """

        return self._name


    def getDate(self):
        """
        Returns the date that the task needs to be
        completed by in the format of MM-DD-YYYY.
        """
        
        return self._date


    def getPriority(self):
        """
        Returns the priority of the task as an
        Enum object.
        """
        
        return self._priority


    def getDescription(self):
        """
        Returns the description of the task.
        """
        return self._description


    def setIdNum(self, id_num):
        """
        Sets the identification number of the task
        to the value given at the method call.
        """
        
        self._id_num = id_num


    def setName(self, name):
        """
        Sets the name of the task to the value
        given at the method call.
        """
        
        self._name = name


    def setDate(self, date):
        """
        Sets the date that the task needs to be completed 
        by to the value given at the method call, but 
        requires a format of MM-DD-YYYY.
        """

        self._date = date


    def setPriority(self, priority):
        """
        Sets the priority of the task to the value
        given at the method call, requires an Enum
        object representaion.
        """
        
        self._priority = priority


    def setDescription(self, description):
        """
        Sets the description of the task to the value
        given at the method call.
        """
        
        self.description = description
