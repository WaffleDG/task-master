"""
   Riya Jonnala, Suraj Narra, Gregory Cohen
   May 6, 2026

   Builds the TaskMaster home screen.
   This screen gives the user access to the main app sections.
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget


def build_home_screen(
    show_enter_task_screen,
    show_schedule_screen,
    show_whiteboard_screen,
) -> QWidget:
    """
       build_home_screen() creates the home screen layout.
       inputs:
          show_enter_task_screen: function - function that opens the task entry screen
          show_schedule_screen: function - function that opens the schedule screen
          show_whiteboard_screen: function - function that opens the whiteboard screen
       returns a QWidget that contains the home screen layout
    """

    # Create the main widget that will hold all home screen content
    home_screen = QWidget()

    # Use a vertical layout so the title, description, and buttons stack neatly
    layout = QVBoxLayout()

    # Keep the home screen from looking cramped against the window edges
    layout.setContentsMargins(80, 80, 80, 80)

    # Add consistent spacing between widgets
    layout.setSpacing(18)

    # Create the main app title
    title_label = QLabel("TaskMaster")

    # Center the title so it feels like the main home screen heading
    title_label.setAlignment(Qt.AlignCenter)

    # Give the title a larger font without needing a separate stylesheet file
    title_label.setStyleSheet("font-size: 36px; font-weight: 700;")

    # Create a short description of the application
    subtitle_label = QLabel("Desktop student planner")

    # Center the subtitle under the title
    subtitle_label.setAlignment(Qt.AlignCenter)

    # Make the subtitle readable but less visually important than the title
    subtitle_label.setStyleSheet("font-size: 18px; color: #555555;")

    # Create a blank visual area for a graphic from the Graphics folder
    graphic_placeholder = QLabel()

    # Give the graphic area a stable size
    graphic_placeholder.setMinimumHeight(120)

    # Style the graphic area as a simple bordered space
    graphic_placeholder.setStyleSheet("border: 1px solid #cccccc; border-radius: 6px;")

    # Create the navigation buttons for the main app sections
    enter_tasks_button = QPushButton("Enter Tasks")
    view_schedule_button = QPushButton("View Schedule")
    view_whiteboard_button = QPushButton("View Whiteboard")

    # Connect the Enter Tasks button to the task entry screen
    enter_tasks_button.clicked.connect(show_enter_task_screen)

    # Connect the View Schedule button to the schedule screen
    view_schedule_button.clicked.connect(show_schedule_screen)

    # Connect the View Whiteboard button to the whiteboard screen
    view_whiteboard_button.clicked.connect(show_whiteboard_screen)

    # Keep the buttons a consistent height for a cleaner first screen
    for button in (enter_tasks_button, view_schedule_button, view_whiteboard_button):
        # Set a readable button height for desktop use
        button.setMinimumHeight(44)

    # Add the title and subtitle to the screen
    layout.addWidget(title_label)
    layout.addWidget(subtitle_label)
    layout.addWidget(graphic_placeholder)

    # Add stretchable empty space so the buttons sit comfortably below the heading
    layout.addStretch()

    # Add the navigation buttons to the screen
    layout.addWidget(enter_tasks_button)
    layout.addWidget(view_schedule_button)
    layout.addWidget(view_whiteboard_button)

    # Add stretchable empty space below the buttons to balance the layout
    layout.addStretch()

    # Attach the completed layout to the home screen widget
    home_screen.setLayout(layout)

    # Return the finished screen so the main window can display it
    return home_screen
