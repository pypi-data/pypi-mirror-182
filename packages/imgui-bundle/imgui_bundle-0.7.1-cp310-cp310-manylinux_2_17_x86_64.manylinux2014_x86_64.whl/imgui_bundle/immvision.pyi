"""immvision: immediate image debugger and insights
Python bindings for https://github.com/pthom/immvision.git
"""

from typing import List
import numpy as np

import cv2
cv = cv2


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# <litgen_stub> // Autogenerated code below! Do not edit!
####################    <generated_from:immvision.h>    ####################
# THIS FILE WAS GENERATED AUTOMATICALLY. DO NOT EDIT.

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       src/immvision/immvision.h                                                              //
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       src/immvision/image.h included by src/immvision/immvision.h                            //
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////

# IMMVISION_API is a marker for public API functions. IMMVISION_STRUCT_API is a marker for public API structs (in comment lines)
# Usage of ImmVision as a shared library is not recommended. No guaranty of ABI stability is provided

class ColormapScaleFromStatsData:  # immvision.h:28
    """Scale the Colormap according to the Image  stats

    IMMVISION_API_STRUCT
    """

    # bool ActiveOnFullImage = true;    /* original C++ signature */
    # Are we using the stats on the full image?
    # If ActiveOnFullImage and ActiveOnROI are both False, then ColormapSettingsData.ColormapScaleMin/Max will be used
    active_on_full_image: bool = True  # immvision.h:32
    # bool   ActiveOnROI = false;    /* original C++ signature */
    # Are we using the stats on the ROI?
    # If ActiveOnFullImage and ActiveOnROI are both False, then ColormapSettingsData.ColormapScaleMin/Max will be used
    # Note: ActiveOnROI and ActiveOnFullImage cannot be True at the same time!
    active_on_roi: bool = False  # immvision.h:36
    # double NbSigmas = 1.5;    /* original C++ signature */
    # If active (either on ROI or on Image), how many sigmas around the mean should the Colormap be applied
    nb_sigmas: float = 1.5  # immvision.h:38
    # bool UseStatsMin = false;    /* original C++ signature */
    # If UseStatsMin is True, then ColormapScaleMin will be calculated from the matrix min value instead of a sigma based value
    use_stats_min: bool = False  # immvision.h:40
    # bool UseStatsMax = false;    /* original C++ signature */
    # If UseStatsMin is True, then ColormapScaleMax will be calculated from the matrix max value instead of a sigma based value
    use_stats_max: bool = False  # immvision.h:42
    # ColormapScaleFromStatsData(bool ActiveOnFullImage = true, bool ActiveOnROI = false, double NbSigmas = 1.5, bool UseStatsMin = false, bool UseStatsMax = false);    /* original C++ signature */
    def __init__(  # Line:3
        self,
        active_on_full_image: bool = True,
        active_on_roi: bool = False,
        nb_sigmas: float = 1.5,
        use_stats_min: bool = False,
        use_stats_max: bool = False,
    ) -> None:
        """Auto-generated default constructor with named params"""
        pass

class ColormapSettingsData:  # immvision.h:47
    """Colormap Settings (useful for matrices with one channel, in order to see colors mapping float values)

    IMMVISION_API_STRUCT
    """

    # std::string Colormap = "None";    /* original C++ signature */
    # Colormap, see available Colormaps with AvailableColormaps()
    # Work only with 1 channel matrices, i.e len(shape)==2
    colormap: str = "None"  # immvision.h:51

    # ColormapScaleMin and ColormapScaleMax indicate how the Colormap is applied:
    #     - Values in [ColormapScaleMin, ColomapScaleMax] will use the full colormap.
    #     - Values outside this interval will be clamped before coloring
    # by default, the initial values are ignored, and they will be updated automatically
    # via the options in ColormapScaleFromStats
    # double ColormapScaleMin = 0.;    /* original C++ signature */
    colormap_scale_min: float = 0.0  # immvision.h:58
    # double ColormapScaleMax = 1.;    /* original C++ signature */
    colormap_scale_max: float = 1.0  # immvision.h:59

    # ColormapScaleFromStatsData ColormapScaleFromStats = ColormapScaleFromStatsData();    /* original C++ signature */
    # If ColormapScaleFromStats.ActiveOnFullImage or ColormapScaleFromStats.ActiveOnROI,
    # then ColormapScaleMin/Max are ignored, and the scaling is done according to the image stats.
    # ColormapScaleFromStats.ActiveOnFullImage is True by default
    colormap_scale_from_stats: ColormapScaleFromStatsData = (
        ColormapScaleFromStatsData()
    )  # immvision.h:64

    # std::string internal_ColormapHovered = "";    /* original C++ signature */
    # Internal value: stores the name of the Colormap that is hovered by the mouse
    internal_colormap_hovered: str = ""  # immvision.h:68
    # ColormapSettingsData(std::string Colormap = "None", double ColormapScaleMin = 0., double ColormapScaleMax = 1., ColormapScaleFromStatsData ColormapScaleFromStats = ColormapScaleFromStatsData(), std::string internal_ColormapHovered = "");    /* original C++ signature */
    def __init__(  # Line:3
        self,
        colormap: str = "None",
        colormap_scale_min: float = 0.0,
        colormap_scale_max: float = 1.0,
        colormap_scale_from_stats: ColormapScaleFromStatsData = ColormapScaleFromStatsData(),
        internal_colormap_hovered: str = "",
    ) -> None:
        """Auto-generated default constructor with named params"""
        pass

class MouseInformation:  # immvision.h:73
    """Contains information about the mouse inside an image

    IMMVISION_API_STRUCT
    """

    # bool IsMouseHovering = false;    /* original C++ signature */
    # Is the mouse hovering the image
    is_mouse_hovering: bool = False  # immvision.h:76

    # cv::Point2d MousePosition = cv::Point2d(-1., -1.);    /* original C++ signature */
    # Mouse position in the original image/matrix
    # This position is given with float coordinates, and will be (-1., -1.) if the mouse is not hovering the image
    mouse_position: cv.Point2d = cv.Point2(-1.0, -1.0)  # immvision.h:80
    # cv::Point MousePosition_Displayed = cv::Point(-1, -1);    /* original C++ signature */
    # Mouse position in the displayed portion of the image (the original image can be zoomed,
    # and only show a subset if it may be shown).
    # This position is given with integer coordinates, and will be (-1, -1) if the mouse is not hovering the image
    mouse_position_displayed: cv.Point = cv.Point(-1, -1)  # immvision.h:84

    #
    # Note: you can query ImGui::IsMouseDown(mouse_button) (c++) or imgui.is_mouse_down(mouse_button) (Python)
    #
    # MouseInformation(bool IsMouseHovering = false, cv::Point2d MousePosition = cv::Point2d(-1., -1.), cv::Point MousePosition_Displayed = cv::Point(-1, -1));    /* original C++ signature */
    def __init__(  # Line:3
        self,
        is_mouse_hovering: bool = False,
        mouse_position: cv.Point2d = cv.Point2(-1.0, -1.0),
        mouse_position_displayed: cv.Point = cv.Point(-1, -1),
    ) -> None:
        """Auto-generated default constructor with named params"""
        pass

class ImageParams:  # immvision.h:93
    """Set of display parameters and options for an Image

    IMMVISION_API_STRUCT
    """

    #
    # ImageParams store the parameters for a displayed image
    # (as well as user selected watched pixels, selected channel, etc.)
    # Its default constructor will give them reasonable choices, which you can adapt to your needs.
    # Its values will be updated when the user pans or zooms the image, adds watched pixels, etc.
    #

    #
    # Refresh Images Textures
    #

    # bool RefreshImage = false;    /* original C++ signature */
    # Refresh Image: images textures are cached. Set to True if your image matrix/buffer has changed
    # (for example, for live video images)
    refresh_image: bool = False  # immvision.h:108

    #
    # Display size and title
    #

    # cv::Size ImageDisplaySize = cv::Size();    /* original C++ signature */
    # Size of the displayed image (can be different from the matrix size)
    # If you specify only the width or height (e.g (300, 0), then the other dimension
    # will be calculated automatically, respecting the original image w/h ratio.
    image_display_size: cv.Size = cv.Size()  # immvision.h:117

    #
    # Zoom and Pan (represented by an affine transform matrix, of size 3x3)
    #

    # cv::Matx33d ZoomPanMatrix = cv::Matx33d::eye();    /* original C++ signature */
    # ZoomPanMatrix can be created using MakeZoomPanMatrix to create a view centered around a given point
    zoom_pan_matrix: cv.Matx33d = cv.Matx33.eye()  # immvision.h:124
    # std::string ZoomKey = "";    /* original C++ signature */
    # If displaying several images, those with the same ZoomKey will zoom and pan together
    zoom_key: str = ""  # immvision.h:126

    # ColormapSettingsData ColormapSettings = ColormapSettingsData();    /* original C++ signature */
    #
    # Colormap Settings (useful for matrices with one channel, in order to see colors mapping float values)
    #
    # ColormapSettings stores all the parameter concerning the Colormap
    colormap_settings: ColormapSettingsData = ColormapSettingsData()  # immvision.h:132
    # std::string ColormapKey = "";    /* original C++ signature */
    # If displaying several images, those with the same ColormapKey will adjust together
    colormap_key: str = ""  # immvision.h:134

    #
    # Zoom and pan with the mouse
    #
    # bool PanWithMouse = true;    /* original C++ signature */
    pan_with_mouse: bool = True  # immvision.h:139
    # bool ZoomWithMouseWheel = true;    /* original C++ signature */
    zoom_with_mouse_wheel: bool = True  # immvision.h:140

    # bool IsColorOrderBGR = true;    /* original C++ signature */
    # Color Order: RGB or RGBA versus BGR or BGRA (Note: by default OpenCV uses BGR and BGRA)
    is_color_order_bgr: bool = True  # immvision.h:143

    # int  SelectedChannel = -1;    /* original C++ signature */
    #
    # Image display options
    #
    # if SelectedChannel >= 0 then only this channel is displayed
    selected_channel: int = -1  # immvision.h:149
    # bool ShowSchoolPaperBackground = true;    /* original C++ signature */
    # Show a "school paper" background grid
    show_school_paper_background: bool = True  # immvision.h:151
    # bool ShowAlphaChannelCheckerboard = true;    /* original C++ signature */
    # show a checkerboard behind transparent portions of 4 channels RGBA images
    show_alpha_channel_checkerboard: bool = True  # immvision.h:153
    # bool ShowGrid = true;    /* original C++ signature */
    # Grid displayed when the zoom is high
    show_grid: bool = True  # immvision.h:155
    # bool DrawValuesOnZoomedPixels = true;    /* original C++ signature */
    # Pixel values show when the zoom is high
    draw_values_on_zoomed_pixels: bool = True  # immvision.h:157

    # bool ShowImageInfo = true;    /* original C++ signature */
    #
    # Image display options
    #
    # Show matrix type and size
    show_image_info: bool = True  # immvision.h:163
    # bool ShowPixelInfo = true;    /* original C++ signature */
    # Show pixel values
    show_pixel_info: bool = True  # immvision.h:165
    # bool ShowZoomButtons = true;    /* original C++ signature */
    # Show buttons that enable to zoom in/out (the mouse wheel also zoom)
    show_zoom_buttons: bool = True  # immvision.h:167
    # bool ShowOptionsPanel = false;    /* original C++ signature */
    # Open the options panel
    show_options_panel: bool = False  # immvision.h:169
    # bool ShowOptionsInTooltip = false;    /* original C++ signature */
    # If set to True, then the option panel will be displayed in a transient tooltip window
    show_options_in_tooltip: bool = False  # immvision.h:171
    # bool ShowOptionsButton = true;    /* original C++ signature */
    # If set to False, then the Options button will not be displayed
    show_options_button: bool = True  # immvision.h:173

    # std::vector<cv::Point> WatchedPixels = std::vector<cv::Point>();    /* original C++ signature */
    #
    # Watched Pixels
    #
    # List of Watched Pixel coordinates
    watched_pixels: List[cv.Point] = List[cv.Point]()  # immvision.h:179
    # bool AddWatchedPixelOnDoubleClick = true;    /* original C++ signature */
    # Shall we add a watched pixel on double click
    add_watched_pixel_on_double_click: bool = True  # immvision.h:181
    # bool HighlightWatchedPixels = true;    /* original C++ signature */
    # Shall the watched pixels be drawn on the image
    highlight_watched_pixels: bool = True  # immvision.h:183

    # MouseInformation MouseInfo = MouseInformation();    /* original C++ signature */
    # Mouse position information. These values are filled after displaying an image
    mouse_info: MouseInformation = MouseInformation()  # immvision.h:186

    # ImageParams(bool RefreshImage = false, cv::Size ImageDisplaySize = cv::Size(), cv::Matx33d ZoomPanMatrix = cv::Matx33d::eye(), std::string ZoomKey = "", ColormapSettingsData ColormapSettings = ColormapSettingsData(), std::string ColormapKey = "", bool PanWithMouse = true, bool ZoomWithMouseWheel = true, bool IsColorOrderBGR = true, int SelectedChannel = -1, bool ShowSchoolPaperBackground = true, bool ShowAlphaChannelCheckerboard = true, bool ShowGrid = true, bool DrawValuesOnZoomedPixels = true, bool ShowImageInfo = true, bool ShowPixelInfo = true, bool ShowZoomButtons = true, bool ShowOptionsPanel = false, bool ShowOptionsInTooltip = false, bool ShowOptionsButton = true, std::vector<cv::Point> WatchedPixels = std::vector<cv::Point>(), bool AddWatchedPixelOnDoubleClick = true, bool HighlightWatchedPixels = true, MouseInformation MouseInfo = MouseInformation());    /* original C++ signature */
    def __init__(  # Line:3
        self,
        refresh_image: bool = False,
        image_display_size: cv.Size = cv.Size(),
        zoom_pan_matrix: cv.Matx33d = cv.Matx33.eye(),
        zoom_key: str = "",
        colormap_settings: ColormapSettingsData = ColormapSettingsData(),
        colormap_key: str = "",
        pan_with_mouse: bool = True,
        zoom_with_mouse_wheel: bool = True,
        is_color_order_bgr: bool = True,
        selected_channel: int = -1,
        show_school_paper_background: bool = True,
        show_alpha_channel_checkerboard: bool = True,
        show_grid: bool = True,
        draw_values_on_zoomed_pixels: bool = True,
        show_image_info: bool = True,
        show_pixel_info: bool = True,
        show_zoom_buttons: bool = True,
        show_options_panel: bool = False,
        show_options_in_tooltip: bool = False,
        show_options_button: bool = True,
        watched_pixels: List[cv.Point] = List[cv.Point](),
        add_watched_pixel_on_double_click: bool = True,
        highlight_watched_pixels: bool = True,
        mouse_info: MouseInformation = MouseInformation(),
    ) -> None:
        """Auto-generated default constructor with named params"""
        pass

# IMMVISION_API ImageParams FactorImageParamsDisplayOnly();    /* original C++ signature */
def factor_image_params_display_only() -> ImageParams:  # immvision.h:193
    """Create ImageParams that display the image only, with no decoration, and no user interaction"""
    pass

# IMMVISION_API cv::Matx33d MakeZoomPanMatrix(    /* original C++ signature */
#                         const cv::Point2d & zoomCenter,
#                         double zoomRatio,
#                         const cv::Size displayedImageSize
#     );
def make_zoom_pan_matrix(  # immvision.h:197
    zoom_center: cv.Point2d, zoom_ratio: float, displayed_image_size: cv.Size
) -> cv.Matx33d:
    """Create a zoom/pan matrix centered around a given point of interest"""
    pass

# IMMVISION_API cv::Matx33d MakeZoomPanMatrix_ScaleOne(    /* original C++ signature */
#         cv::Size imageSize,
#         const cv::Size displayedImageSize
#     );
def make_zoom_pan_matrix_scale_one(  # immvision.h:203
    image_size: cv.Size, displayed_image_size: cv.Size
) -> cv.Matx33d:
    pass

# IMMVISION_API cv::Matx33d MakeZoomPanMatrix_FullView(    /* original C++ signature */
#         cv::Size imageSize,
#         const cv::Size displayedImageSize
#     );
def make_zoom_pan_matrix_full_view(  # immvision.h:208
    image_size: cv.Size, displayed_image_size: cv.Size
) -> cv.Matx33d:
    pass

# IMMVISION_API void Image(const std::string& label, const cv::Mat& mat, ImageParams* params);    /* original C++ signature */
def image(label: str, mat: cv.Mat, params: ImageParams) -> None:  # immvision.h:248
    """Display an image, with full user control: zoom, pan, watch pixels, etc.

    :param label
        A legend that will be displayed.
        Important notes:
            - With ImGui and ImmVision, widgets *must* have a unique Ids.
              For this widget, the id is given by this label.
              Two widgets (for example) two images *cannot* have the same label or the same id!
              (you can use ImGui::PushID / ImGui::PopID to circumvent this, or add suffixes with ##)

              If they do, they might not refresh correctly!
              To circumvent this, you can:
                 - Call `ImGui::PushID("some_unique_string")` at the start of your function,
                   and `ImGui::PopID()` at the end.
                 - Or modify your label like this:
                     "MyLabel##some_unique_id"
                     (the part after "##" will not be displayed but will be part of the id)
           - To display an empty legend, use "##_some_unique_id"

    :param mat
        An image you want to display, under the form of an OpenCV matrix. All types of dense matrices are supported.

    :param params
        Complete options (as modifiable inputs), and outputs (mouse position, watched pixels, etc)
        @see ImageParams structure.
        The ImageParams may be modified by this function: you can extract from them
        the mouse position, watched pixels, etc.
        Important note:
            ImageParams is an input-output parameter, passed as a pointer.
            Its scope should be wide enough so that it is preserved from frame to frame.
            !! If you cannot zoom/pan in a displayed image, extend the scope of the ImageParams !!

    - This function requires that both imgui and OpenGL were initialized.
      (for example, use `imgui_runner.run`for Python,  or `HelloImGui::Run` for C++)
    """
    pass

# IMMVISION_API cv::Point2d ImageDisplay(    /* original C++ signature */
#         const std::string& label_id,
#         const cv::Mat& mat,
#         const cv::Size& imageDisplaySize = cv::Size(),
#         bool refreshImage = false,
#         bool showOptionsButton = false,
#         bool isBgrOrBgra = true
#         );
def image_display(  # immvision.h:294
    label_id: str,
    mat: cv.Mat,
    image_display_size: cv.Size = cv.Size(),
    refresh_image: bool = False,
    show_options_button: bool = False,
    is_bgr_or_bgra: bool = True,
) -> cv.Point2d:
    """Only, display the image, with no decoration, and no user interaction (by default)

    Parameters:
    :param label
        A legend that will be displayed.
        Important notes:
            - With ImGui and ImmVision, widgets must have a unique Ids. For this widget, the id is given by this label.
              Two widgets (for example) two images *cannot* have the same label or the same id!
              If they do, they might not refresh correctly!
              To circumvent this, you can modify your label like this:
                 "MyLabel##some_unique_id"    (the part after "##" will not be displayed but will be part of the id)
           - To display an empty legend, use "##_some_unique_id"

    :param Mat:
        An image you want to display, under the form of an OpenCV matrix. All types of dense matrices are supported.

    :param imageDisplaySize:
        Size of the displayed image (can be different from the mat size)
        If you specify only the width or height (e.g (300, 0), then the other dimension
        will be calculated automatically, respecting the original image w/h ratio.

    :param refreshImage:
        images textures are cached. Set to True if your image matrix/buffer has changed
        (for example, for live video images)

    :param showOptionsButton:
        If True, show an option button that opens the option panel.
        In that case, it also becomes possible to zoom & pan, add watched pixel by double-clicking, etc.

    :param isBgrOrBgra:
        set to True if the color order of the image is BGR or BGRA (as in OpenCV, by default)

    :return:
         The mouse position in `mat` original image coordinates, as double values.
         (i.e. it does not matter if imageDisplaySize is different from mat.size())
         It will return (-1., -1.) if the mouse is not hovering the image.

         Note: use ImGui::IsMouseDown(mouse_button) (C++) or imgui.is_mouse_down(mouse_button) (Python)
               to query more information about the mouse.

    Note: this function requires that both imgui and OpenGL were initialized.
          (for example, use `imgui_runner.run`for Python,  or `HelloImGui::Run` for C++)

    """
    pass

# IMMVISION_API std::vector<std::string> AvailableColormaps();    /* original C++ signature */
def available_colormaps() -> List[str]:  # immvision.h:306
    """Return the list of the available color maps
    Taken from https://github.com/yuki-koyama/tinycolormap, thanks to Yuki Koyama
    """
    pass

# IMMVISION_API void ClearTextureCache();    /* original C++ signature */
def clear_texture_cache() -> None:  # immvision.h:313
    """Clears the internal texture cache of immvision (this is done automatically at exit time)

    Note: this function requires that both imgui and OpenGL were initialized.
          (for example, use `imgui_runner.run`for Python,  or `HelloImGui::Run` for C++)
    """
    pass

# IMMVISION_API cv::Mat GetCachedRgbaImage(const std::string& label);    /* original C++ signature */
def get_cached_rgba_image(label: str) -> cv.Mat:  # immvision.h:318
    """Returns the RGBA image currently displayed by ImmVision::Image or ImmVision::ImageDisplay
    Note: this image must be currently displayed. This function will return the transformed image
    (i.e with ColorMap, Zoom, etc.)
    """
    pass

# IMMVISION_API std::string VersionInfo();    /* original C++ signature */
def version_info() -> str:  # immvision.h:321
    """Return immvision version info"""
    pass

# namespace ImmVision

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       src/immvision/immvision.h continued                                                    //
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                       src/immvision/inspector.h included by src/immvision/immvision.h                        //
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////

# IMMVISION_API is a marker for public API functions. IMMVISION_STRUCT_API is a marker for public API structs (in comment lines)
# Usage of ImmVision as a shared library is not recommended. No guaranty of ABI stability is provided

""" namespace ImmVision"""
# IMMVISION_API void Inspector_AddImage(    /* original C++ signature */
#         const cv::Mat& image,
#         const std::string& legend,
#         const std::string& zoomKey = "",
#         const std::string& colormapKey = "",
#         const cv::Point2d & zoomCenter = cv::Point2d(),
#         double zoomRatio = -1.,
#         bool isColorOrderBGR = true
#     );
def inspector_add_image(  # immvision.h:342
    image: cv.Mat,
    legend: str,
    zoom_key: str = "",
    colormap_key: str = "",
    zoom_center: cv.Point2d = cv.Point2(),
    zoom_ratio: float = -1.0,
    is_color_order_bgr: bool = True,
) -> None:
    pass

# IMMVISION_API void Inspector_Show();    /* original C++ signature */
def inspector_show() -> None:  # immvision.h:352
    pass

# IMMVISION_API void Inspector_ClearImages();    /* original C++ signature */
def inspector_clear_images() -> None:  # immvision.h:354
    pass
####################    </generated_from:immvision.h>    ####################

# </litgen_stub> // Autogenerated code end!
