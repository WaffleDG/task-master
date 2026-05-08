"""
   Riya Jonnala, Suraj Narra, Gregory Cohen
   May 6, 2026

   Builds the TaskMaster task entry screen.
   This screen contains the form controls used to describe a new task.
"""

from PySide6.QtCore import QDateTime
from PySide6.QtWidgets import (
    QComboBox,
    QDateTimeEdit,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QWidget,
)

from screen_helpers import build_button_row, build_page_layout


def build_enter_task_screen(show_home_screen) -> QWidget:
    """
       build_enter_task_screen() creates the task entry screen.
       inputs:
          show_home_screen: function - function that returns the app to the home screen
       returns a QWidget that contains the task form layout
    """

    # Create the main widget that will hold the task entry screen
    enter_task_screen = QWidget()

    # Use the shared page layout so this screen matches the other screens
    layout = build_page_layout("Enter Task")

    # Create the form layout that holds task input fields
    form_layout = QFormLayout()

    # Create a text input for the assignment or task name
    task_name_input = QLineEdit()

    # Add helpful placeholder text inside the empty task name input
    task_name_input.setPlaceholderText("Example: Finish math homework")

    # Create a text input for the class or category name
    category_input = QLineEdit()

    # Add helpful placeholder text inside the empty category input
    category_input.setPlaceholderText("Example: Math")

    # Create a number input for the estimated task length
    minutes_input = QSpinBox()

    # Keep the minimum at one minute so every task has a real length
    minutes_input.setMinimum(1)

    # Keep the maximum high enough for long projects
    minutes_input.setMaximum(600)

    # Start with a common homework estimate
    minutes_input.setValue(30)

    # Add a suffix so the number input is easier to understand
    minutes_input.setSuffix(" minutes")

    # Create a date and time input for the deadline
    deadline_input = QDateTimeEdit()

    # Start the deadline input at the current date and time
    deadline_input.setDateTime(QDateTime.currentDateTime())

    # Show a calendar popup to make deadline entry easier
    deadline_input.setCalendarPopup(True)

    # Create a simple priority dropdown
    priority_input = QComboBox()

    # Add priority choices the scheduler can use later
    priority_input.addItems(["Normal", "High", "Low"])

    # Add each input to the form with a clear label
    form_layout.addRow("Task name:", task_name_input)
    form_layout.addRow("Class/category:", category_input)
    form_layout.addRow("Estimated time:", minutes_input)
    form_layout.addRow("Deadline:", deadline_input)
    form_layout.addRow("Priority:", priority_input)

    # Create a disabled save button to show where task saving will happen
    add_task_button = QPushButton("Add Task")

    # Disable the button until task storage is added
    add_task_button.setEnabled(False)

    # Create a back button that returns to the home screen
    back_button = QPushButton("Back to Home")

    # Connect the back button to the home screen
    back_button.clicked.connect(show_home_screen)

    # Add the task form to the screen
    layout.addLayout(form_layout)

    # Add the screen action buttons
    layout.addLayout(build_button_row([add_task_button, back_button]))

    # Add stretchable empty space below the form
    layout.addStretch()

    # Attach the completed layout to the task entry screen
    enter_task_screen.setLayout(layout)

    # Return the finished task entry screen
    return enter_task_screen
