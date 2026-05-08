"""
   Riya Jonnala, Suraj Narra, Gregory Cohen
   May 6, 2026

   Builds the TaskMaster schedule screen.
   This screen shows the area where the generated schedule will be displayed.
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QPushButton, QWidget

from screen_helpers import build_button_row, build_page_layout


def build_schedule_screen(show_home_screen) -> QWidget:
    """
       build_schedule_screen() creates the schedule screen.
       inputs:
          show_home_screen: function - function that returns the app to the home screen
       returns a QWidget that contains the schedule placeholder layout
    """

    # Create the main widget that will hold the schedule screen
    schedule_screen = QWidget()

    # Use the shared page layout so this screen matches the other screens
    layout = build_page_layout("Current Schedule")

    # Create a placeholder label for the schedule output area
    schedule_placeholder = QLabel("Your generated schedule will appear here")

    # Center the placeholder inside its display area
    schedule_placeholder.setAlignment(Qt.AlignCenter)

    # Give the placeholder enough space to feel like the schedule area
    schedule_placeholder.setMinimumHeight(260)

    # Style the placeholder as a simple bordered panel
    schedule_placeholder.setStyleSheet(
        "border: 1px solid #cccccc; border-radius: 6px; color: #555555;"
    )

    # Create a back button that returns to the home screen
    back_button = QPushButton("Back to Home")

    # Connect the back button to the home screen
    back_button.clicked.connect(show_home_screen)

    # Add the schedule placeholder to the screen
    layout.addWidget(schedule_placeholder)

    # Add the screen action button
    layout.addLayout(build_button_row([back_button]))

    # Add stretchable empty space below the placeholder
    layout.addStretch()

    # Attach the completed layout to the schedule screen
    schedule_screen.setLayout(layout)

    # Return the finished schedule screen
    return schedule_screen
