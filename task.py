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
    get_id_num()
        Returns the identification number of the task.
    get_name()
        Returns the name of the task.
    get_date()
        Returns the date that the task needs to be
        completed by.
    get_priority()
        Returns an Enum that represents how important
        the task is.
    get_description()
        Returns the description of the task.
    get_completion()
        Returns the completion status of the task.
    set_id_num()
        Sets the identification number of the task
        to the value given to the method call.
    set_name()
        Sets the name of the task to the value
        given to the method call.
    set_date()
        Sets the date that the task needs to be completed
        by to the value given to the method call.
    set_priority()
        Sets the priority of the task to the value given
        to the method call.
    set_description()
        Sets the description of the task to the value
        given to the method call.
    set_completion()
        Sets the completion status of the task to the
        value given to the method call.
    """

    def __init__(self, id_num, name = "Generic Task", date = "N/A", priority = Priority.LOW, complete = False):
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
        self._complete = complete


    def get_id_num(self):
        """
        Returns the identification number of 
        the task.
        """
        
        return self._id_num


    def get_name(self):
        """
        Returns the name of the task.
        """

        return self._name


    def get_date(self):
        """
        Returns the date that the task needs to be
        completed by in the format of MM-DD-YYYY.
        """
        
        return self._date


    def get_priority(self):
        """
        Returns the priority of the task as an
        Enum object.
        """
        
        return self._priority


    def get_description(self):
        """
        Returns the description of the task.
        """
        
        return self._description

    
    def get_completion(self):
        """
        Returns the completion status of the task.
        """

        return self._complete


    def set_id_num(self, id_num):
        """
        Sets the identification number of the task
        to the value given at the method call.
        """
        
        self._id_num = id_num


    def set_name(self, name):
        """
        Sets the name of the task to the value
        given at the method call.
        """
        
        self._name = name


    def set_date(self, date):
        """
        Sets the date that the task needs to be completed 
        by to the value given at the method call, but 
        requires a format of MM-DD-YYYY.
        """

        self._date = date


    def set_priority(self, priority):
        """
        Sets the priority of the task to the value
        given at the method call, requires an Enum
        object representaion.
        """
        
        self._priority = priority


    def set_description(self, description):
        """
        Sets the description of the task to the value
        given at the method call.
        """
        
        self._description = description


    def set_completion(self, complete):
        """
        Sets the completion status of the task to the
        value given at the method call.
        """

        self._complete = complete


    def __eq__(self, other):
        """
        Defines the equality comparison.
        """

        if isinstance(other, Task):
            return self._id_num == other.get_name()
        return NotImplemented

    
    def __str__(self):
        """
        Defines the toString behaviour of the
        task object.
        """

        return f"Task Name: {self._name}\n Task ID: {self._id_num}\n Completed{self._complete}"
