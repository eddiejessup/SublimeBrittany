"""
@name     Brittany
@package  sublime_plugin
@author   Elliot Marsden

Format Haskell code with Brittany.
"""

import subprocess

import sublime
import sublime_plugin


class SetContentsCommand(sublime_plugin.TextCommand):

    def run(self, edit, text):
        r = sublime.Region(0, self.view.size())
        self.view.replace(edit, r, text)
        self.view.end_edit(edit)


class ShowPanelMessageCommand(sublime_plugin.WindowCommand):

    def run(self, message):
        v = self.window.create_output_panel('brittany_error')
        v.run_command("set_contents", {"text": message})
        self.window.run_command(
            "show_panel",
            {"panel": "output.brittany_error"},
        )


def show_panel_message(window, message):
    window.run_command("show_panel_message", {"message": message})


class BrittanyCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        # Get the document's length.
        view_size = self.view.size()

        # Get selections.
        regions = self.view.sel()
        nr_regions = len(regions)
        # Select the whole document if there is no selection.
        if nr_regions <= 1 and len(self.view.substr(regions[0])) == 0:
            regions.clear()
            regions.add(sublime.Region(0, view_size))

        # For each text selection region.
        for region in regions:
            data = self.view.substr(region)
            p = subprocess.Popen(['brittany'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            stdout_data, stderr_data = p.communicate(input=data.encode(), timeout=10)
            if p.returncode != 0:
                if p.returncode == 60:
                    explanation = "Does the selection contain valid Haskell?"
                else:
                    explanation = "Sorry, I don't know what this error code means."
                show_panel_message(self.view.window(),
                                   'Error: Got return code: {}. {}'
                                   .format(p.returncode, explanation))
            # Replace selection with output.
            else:
                self.view.replace(edit, region, stdout_data.decode())
        self.view.end_edit(edit)
