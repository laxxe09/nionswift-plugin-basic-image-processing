#With opening of edit computation 
from __future__ import annotations

import gettext
import typing

from nion.swift import DocumentController
from nion.swift import Panel
from nion.swift import Workspace

_ = gettext.gettext


class BasicImageProcessingPanel(Panel.Panel):
    """
    A panel providing basic image processing controls with checkboxes
    and a compile button that calls Nion Swift's built-in actions
    via their action_id.
    """

    def __init__(
        self,
        document_controller: DocumentController.DocumentController,
        panel_id: str,
        properties: typing.Mapping[str, typing.Any],
    ) -> None:
        super().__init__(document_controller, panel_id, "Basic Image Processing")

        ui = document_controller.ui
        self.widget = ui.create_column_widget(properties={"margin": 6, "spacing": 4})

        # Create sections
        align_section = ui.create_column_widget(properties={"margin": 4, "spacing": 4})
        align_section.add(ui.create_label_widget("Alignment", properties={"stylesheet": "font-weight: bold"}))
        self.align_spline_cb = ui.create_check_box_widget("Spline First Order")
        self.align_fourier_cb = ui.create_check_box_widget("Fourier")
        align_section.add(self.align_spline_cb)
        align_section.add(self.align_fourier_cb)

        integrate_section = ui.create_column_widget(properties={"margin": 4, "spacing": 4})
        integrate_section.add(ui.create_label_widget("Integration", properties={"stylesheet": "font-weight: bold"}))
        self.integrate_cb = ui.create_check_box_widget("Sequence Integration")
        integrate_section.add(self.integrate_cb)

        filter_section = ui.create_column_widget(properties={"margin": 4, "spacing": 4})
        filter_section.add(ui.create_label_widget("Filters", properties={"stylesheet": "font-weight: bold"}))
        self.gaussian_cb = ui.create_check_box_widget("Gaussian")
        self.median_cb = ui.create_check_box_widget("Median")
        filter_section.add(self.gaussian_cb)
        filter_section.add(self.median_cb)

        # Add sections to main widget
        self.widget.add(align_section)
        self.widget.add_spacing(8)
        self.widget.add(integrate_section)
        self.widget.add_spacing(8)
        self.widget.add(filter_section)
        self.widget.add_spacing(8)

        # Compile button
        compile_button = ui.create_push_button_widget("Compile")
        compile_button.on_clicked = self._compile_processing
        self.widget.add(compile_button)

        self.widget.add_stretch()

    def _do_action(self, action_id: str) -> None:
        """Helper to trigger an action by its ID on the current selection."""
        try:
            self.document_controller.perform_action(action_id)
            print(f" ✓ {action_id} ran")
        except Exception as e:
            print(f" ✗ {action_id}: {e} Failed")


    def _compile_processing(self) -> None:
        """Run the selected processing steps in order."""
        selected = self.document_controller.selected_display_items
        if not selected:
            print(" No data item selected :()")
            return

        # Call window.edit_computation for each selected operation
        if self.align_spline_cb.checked:
            self._do_action("processing.sequence_align_spline_1")

        if self.align_fourier_cb.checked:
            self._do_action("processing.sequence_align_fourier")

        if self.integrate_cb.checked:
            self._do_action("processing.sequence_integrate")

        if self.gaussian_cb.checked:
            self._do_action("window.edit_computation")

        if self.median_cb.checked:
            self._do_action("window.edit_computation")


def run() -> None:
    """Register the panel with Swift."""
    Workspace.WorkspaceManager().register_panel(
        BasicImageProcessingPanel,
        "basic-image-processing-panel",
        _("Basic Image Processing"),
        ["left", "right"],
        "right",
        {},
    )

    

