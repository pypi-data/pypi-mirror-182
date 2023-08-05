"""A more complex app demo,

It demonstrates:
- How to use a specific application state (instead of using static variables)
- How to set up a complex layout:
    - dockable windows that can be moved, and even be detached from the main window
    - status bar
- A default menu, with default
- log window
- How to load assets and fonts
"""
import os
from enum import Enum

from imgui_bundle import hello_imgui, icons_fontawesome, imgui, imgui_md, ImVec2, immapp


# Struct that holds the application's state
class AppState:
    f: float = 0.0
    counter: int = 0
    rocket_progress: float = 0.0

    class RocketState(Enum):
        Init = 0
        Preparing = 1
        Launched = 2

    rocket_state: RocketState = RocketState.Init


"""
Font loading:

We have two options: either we use hello imgui, or we load manually 
(see my_load_fonts_via_hello_imgui() and my_load_fonts_manually() below).
"""

gAkronimFont: imgui.ImFont


def my_load_fonts_via_hello_imgui():
    # hello_imgui can load font and merge them with font awesome automatically.
    # It will load them from the assets/ folder.

    global gAkronimFont

    # First, we load the default fonts (the font that was loaded first is the default font)
    hello_imgui.imgui_default_settings.load_default_font_with_font_awesome_icons()
    font_filename = "fonts/Akronim-Regular.ttf"
    gAkronimFont = hello_imgui.load_font_ttf_with_font_awesome_icons(font_filename, 40.0)


def my_load_fonts_manually():
    # Load font manually.
    # We need to use font_atlas_add_font_from_file_ttf instead of ImFont.add_font_from_file_ttf
    global gAkronimFont

    # first, we load the default font (it will not include icons)
    imgui.get_io().fonts.add_font_default()

    # Load a font and merge icons into it
    # i. load the font...
    this_dir = os.path.dirname(__file__)
    font_atlas = imgui.get_io().fonts
    # We need to take into account the global font scale!
    font_size_pixel = 40 / imgui.get_io().font_global_scale
    font_filename = this_dir + "/../assets/fonts/Akronim-Regular.ttf"
    font_atlas = imgui.get_io().fonts
    glyph_range = font_atlas.get_glyph_ranges_default()
    gAkronimFont = font_atlas.add_font_from_file_ttf(
        filename=font_filename,
        size_pixels=font_size_pixel,
        glyph_ranges_as_int_list=glyph_range,
    )
    # ii. ... Aad merge icons into the previous font
    from imgui_bundle import icons_fontawesome

    font_filename = this_dir + "/../assets/fonts/fontawesome-webfont.ttf"
    font_config = imgui.ImFontConfig()
    font_config.merge_mode = True
    icons_range = [icons_fontawesome.ICON_MIN_FA, icons_fontawesome.ICON_MAX_FA, 0]
    gAkronimFont = font_atlas.add_font_from_file_ttf(
        filename=font_filename,
        size_pixels=font_size_pixel,
        glyph_ranges_as_int_list=icons_range,
        font_cfg=font_config,
    )


def my_load_fonts():
    my_load_fonts_manually()
    # my_load_fonts_via_hello_imgui()


# CommandGui: the widgets on the left panel
def command_gui(state: AppState):
    # Note, you can also show the tweak theme widgets via:
    # hello_imgui.show_theme_tweak_gui(hello_imgui.get_runner_params().imgui_window_params.tweaked_theme)
    imgui_md.render(
        """
# Tweak the theme!

Select the menu "View/Theme/Theme tweak window" in order to browse the available themes (more than 15). 
You can even easily tweak their colors.
    """[
            1:
        ]
    )

    imgui.separator()

    imgui.push_font(gAkronimFont)
    imgui.text("Hello  " + icons_fontawesome.ICON_FA_SMILE)
    hello_imgui.image_from_asset("world.jpg", ImVec2(100, 100))  # type: ignore
    imgui.pop_font()
    if imgui.is_item_hovered():
        imgui.set_tooltip(
            """
        The custom font and the globe image below were loaded
        from the application assets folder
        (those files are embedded automatically).
        """
        )

    imgui.separator()

    # Edit 1 float using a slider from 0.0f to 1.0f
    changed, state.f = imgui.slider_float("float", state.f, 0.0, 1.0)
    if changed:
        hello_imgui.log(hello_imgui.LogLevel.warning, f"state.f was changed to {state.f}")

    # Buttons return true when clicked (most widgets return true when edited/activated)
    if imgui.button("Button"):
        state.counter += 1
        hello_imgui.log(hello_imgui.LogLevel.info, "Button was pressed")

    imgui.same_line()
    imgui.text(f"counter = {state.counter}")

    if state.rocket_state == AppState.RocketState.Init:
        if imgui.button(icons_fontawesome.ICON_FA_ROCKET + " Launch rocket"):
            state.rocket_state = AppState.RocketState.Preparing
            hello_imgui.log(hello_imgui.LogLevel.warning, "Rocket is being prepared")
    elif state.rocket_state == AppState.RocketState.Preparing:
        imgui.text("Please Wait")
        state.rocket_progress += 0.003
        if state.rocket_progress >= 1.0:
            state.rocket_state = AppState.RocketState.Launched
            print("Rocket was launched!")
            hello_imgui.log(hello_imgui.LogLevel.warning, "Rocker was launched")
    elif state.rocket_state == AppState.RocketState.Launched:
        imgui.text(icons_fontawesome.ICON_FA_ROCKET + " Rocket Launched")
        if imgui.button("Reset Rocket"):
            state.rocket_state = AppState.RocketState.Init
            state.rocket_progress = 0.0

    imgui_md.render(
        """
    --- 
# Markdown Test

## Title Level 2

### Title level 3

* _underline_
* *italic*
* **bold**
---
    """
    )


# Our Gui in the status bar
def status_bar_gui(app_state: AppState):
    if app_state.rocket_state == AppState.RocketState.Preparing:
        imgui.text("Rocket completion: ")
        imgui.same_line()
        imgui.progress_bar(app_state.rocket_progress, imgui.ImVec2(100.0, 15.0))  # type: ignore


def main():

    # Important: HelloImGui uses an assets dir where it can find assets (fonts, images, etc.)
    #
    # By default an assets folder is installed via pip inside site-packages/lg_imgui_bundle/assets
    # and provides two fonts (fonts/DroidSans.ttf and fonts/fontawesome-webfont.ttf)
    # If you need to add more assets, make a copy of this assets folder and add your own files, and call set_assets_folder
    this_dir = os.path.dirname(os.path.realpath(__file__))
    hello_imgui.set_assets_folder(this_dir + "/../assets")

    ################################################################################################
    # Part 1: Define the application state, fill the status and menu bars, and load additional font
    ################################################################################################

    # Our application state
    app_state = AppState()

    # Hello ImGui params (they hold the settings as well as the Gui callbacks)
    runner_params = hello_imgui.RunnerParams()

    runner_params.app_window_params.window_title = "Docking demo"
    runner_params.app_window_params.window_geometry.size = (1000, 800)
    runner_params.app_window_params.restore_previous_geometry = True

    #
    # Status bar
    #
    # We use the default status bar of Hello ImGui
    runner_params.imgui_window_params.show_status_bar = True
    # uncomment next line in order to hide the FPS in the status bar
    # runner_params.im_gui_window_params.show_status_fps = False
    runner_params.callbacks.show_status = lambda: status_bar_gui(app_state)

    #
    # Menu bar
    #
    # We use the default menu of Hello ImGui, to which we add some more items
    runner_params.imgui_window_params.show_menu_bar = True

    def show_menu_gui():
        if imgui.begin_menu("My Menu"):
            clicked, _ = imgui.menu_item("Test me", "", False)
            if clicked:
                hello_imgui.log(hello_imgui.LogLevel.warning, "It works")
            imgui.end_menu()

    runner_params.callbacks.show_menus = show_menu_gui

    # Custom load fonts
    runner_params.callbacks.load_additional_fonts = my_load_fonts

    # optional native events handling
    # runner_params.callbacks.any_backend_event_callback = ...

    ################################################################################################
    # Part 2: Define the application layout and windows
    ################################################################################################

    #
    #    2.1 Define the docking splits,
    #    i.e. the way the screen space is split in different target zones for the dockable windows
    #     We want to split "MainDockSpace" (which is provided automatically) into three zones, like this:
    #
    #    ___________________________________________
    #    |        |                                |
    #    | Left   |                                |
    #    | Space  |    MainDockSpace               |
    #    |        |                                |
    #    |        |                                |
    #    |        |                                |
    #    -------------------------------------------
    #    |     BottomSpace                         |
    #    -------------------------------------------
    #

    # First, tell HelloImGui that we want full screen dock space (this will create "MainDockSpace")
    runner_params.imgui_window_params.default_imgui_window_type = (
        hello_imgui.DefaultImGuiWindowType.provide_full_screen_dock_space
    )
    # In this demo, we also demonstrate multiple viewports.
    # you can drag windows outside out the main window in order to put their content into new native windows
    runner_params.imgui_window_params.enable_viewports = True

    # Then, add a space named "BottomSpace" whose height is 25% of the app height.
    # This will split the preexisting default dockspace "MainDockSpace" in two parts.
    split_main_bottom = hello_imgui.DockingSplit()
    split_main_bottom.initial_dock = "MainDockSpace"
    split_main_bottom.new_dock = "BottomSpace"
    split_main_bottom.direction = imgui.Dir_.down
    split_main_bottom.ratio = 0.25

    # Then, add a space to the left which occupies a column whose width is 25% of the app width
    split_main_left = hello_imgui.DockingSplit()
    split_main_left.initial_dock = "MainDockSpace"
    split_main_left.new_dock = "LeftSpace"
    split_main_left.direction = imgui.Dir_.left
    split_main_left.ratio = 0.25

    # Finally, transmit these splits to HelloImGui
    runner_params.docking_params.docking_splits = [split_main_bottom, split_main_left]

    #
    # 2.1 Define our dockable windows : each window provide a Gui callback, and will be displayed
    #     in a docking split.
    #

    # A Command panel named "Commands" will be placed in "LeftSpace". Its Gui is provided calls "CommandGui"
    commands_window = hello_imgui.DockableWindow()
    commands_window.label = "Commands"
    commands_window.dock_space_name = "LeftSpace"
    commands_window.gui_function = lambda: command_gui(app_state)
    # A Log  window named "Logs" will be placed in "BottomSpace". It uses the HelloImGui logger gui
    logs_window = hello_imgui.DockableWindow()
    logs_window.label = "Logs"
    logs_window.dock_space_name = "BottomSpace"
    logs_window.gui_function = hello_imgui.log_gui
    # A Window named "Dear ImGui Demo" will be placed in "MainDockSpace"
    dear_imgui_demo_window = hello_imgui.DockableWindow()
    dear_imgui_demo_window.label = "Dear ImGui Demo"
    dear_imgui_demo_window.dock_space_name = "MainDockSpace"
    dear_imgui_demo_window.gui_function = imgui.show_demo_window

    # Finally, transmit these windows to HelloImGui
    runner_params.docking_params.dockable_windows = [
        commands_window,
        logs_window,
        dear_imgui_demo_window,
    ]

    ################################################################################################
    # Part 3: Run the app
    ################################################################################################
    import imgui_bundle

    addons_params = immapp.AddOnsParams()
    addons_params.with_markdown = True
    immapp.run(runner_params, addons_params)


if __name__ == "__main__":
    main()
