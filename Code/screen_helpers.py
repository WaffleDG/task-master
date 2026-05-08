"""
   Riya Jonnala, Suraj Narra, Gregory Cohen
   May 6, 2026

   Provides shared PySide6 layout helpers used by multiple TaskMaster screens.
   This file keeps repeated screen layout code in one place.
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QPushButton, QHBoxLayout, QVBoxLayout


def build_page_layout(title: str) -> QVBoxLayout:
    """
       build_page_layout() creates a shared screen layout.
       inputs:
          title: str - title text shown at the top of the screen
       returns a QVBoxLayout that contains a standard page heading
    """

    # Create the shared vertical layout for a screen
    layout = QVBoxLayout()

    # Keep every screen aligned with the same page margins
    layout.setContentsMargins(80, 60, 80, 60)

    # Add consistent spacing between screen widgets
    layout.setSpacing(16)

    # Create the screen title label
    title_label = QLabel(title)

    # Center the screen title
    title_label.setAlignment(Qt.AlignCenter)

    # Style the screen title
    title_label.setStyleSheet("font-size: 28px; font-weight: 700;")

    # Add the title to the top of the page
    layout.addWidget(title_label)

    # Return the shared layout so each screen can add its own content
    return layout


def build_button_row(buttons: list[QPushButton]) -> QHBoxLayout:
    """
       build_button_row() creates a row of buttons.
       inputs:
          buttons: list[QPushButton] - buttons that should appear in the row
       returns a QHBoxLayout that contains the provided buttons
    """

    # Create a horizontal layout for screen action buttons
    button_row = QHBoxLayout()

    # Add stretchable empty space before the buttons
    button_row.addStretch()

    # Add each button to the row
    for button in buttons:
        # Keep each action button readable and consistent
        button.setMinimumHeight(40)

        # Add the button to the button row
        button_row.addWidget(button)

    # Add stretchable empty space after the buttons
    button_row.addStretch()

    # Return the completed button row
    return button_row
